from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, ToolMessage
import json
from typing import Dict, Any, List

# Use absolute imports instead of relative
from src.state import TravelState
from src.tools.destination_research import research_destination
from src.tools.itinerary_builder import build_daily_itinerary
from src.tools.budget_calculator import calculate_budget_breakdown, generate_budget_chart
from src.tools.weather_checker import get_seasonal_weather
from src.tools.map_visualizer import generate_itinerary_map

class TravelPlannerAgent:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.llm = ChatOpenAI(model=model, temperature=0.7)
        self.setup_tools()
        self.build_graph()
    
    def setup_tools(self):
        """Setup all our travel planning tools"""
        self.tools = [
            research_destination,
            build_daily_itinerary,
            calculate_budget_breakdown, 
            get_seasonal_weather,
            generate_itinerary_map,
            generate_budget_chart
        ]
        
        # Bind tools to LLM
        self.llm_with_tools = self.llm.bind_tools(self.tools)
    
    def planner_node(self, state: TravelState) -> Dict[str, Any]:
        """Main planning node - decides which tools to use"""
        print(f"🔍 Planning trip to {state['destination']}...")
        
        # Create planning prompt
        prompt = f"""
        Plan a {state['trip_duration']}-day trip to {state['destination']} for {state['traveler_count']} travelers.
        Budget: ${state['budget']}, Style: {state['travel_style']}
        Interests: {', '.join(state['interests'])}
        Travel Month: {state['travel_month']}
        
        Please use the available tools to:
        1. Research the destination and attractions
        2. Build a daily itinerary
        3. Calculate budget breakdown
        4. Check weather conditions
        5. Generate visualizations
        
        Return a complete travel plan.
        """
        
        messages = [HumanMessage(content=prompt)]
        response = self.llm_with_tools.invoke(messages)
        
        return {"messages": [response], "status": "planning_started"}
    
    def tools_node(self, state: TravelState) -> Dict[str, Any]:
        """Execute tools based on LLM decisions"""
        print("🛠️ Executing tools...")
        
        last_message = state["messages"][-1]
        
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            tool_calls = last_message.tool_calls
            tool_messages = []
            
            for tool_call in tool_calls:
                tool_name = tool_call['name']
                tool_args = tool_call['args']
                
                print(f"  🔧 Calling tool: {tool_name}")
                
                # Find and execute the tool
                for tool in self.tools:
                    if tool.__name__ == tool_name:
                        try:
                            result = tool(**tool_args)
                            
                            # Store results in state based on tool type
                            if tool_name == "research_destination":
                                state["researched_destinations"] = result
                                state["attractions"] = result.get("attractions", [])
                            elif tool_name == "build_daily_itinerary":
                                state["daily_itinerary"] = result
                            elif tool_name == "calculate_budget_breakdown":
                                state["budget_breakdown"] = result
                            elif tool_name == "get_seasonal_weather":
                                state["weather_info"] = result
                            elif tool_name == "generate_itinerary_map":
                                state["itinerary_map"] = result
                            elif tool_name == "generate_budget_chart":
                                state["budget_chart"] = result
                                
                            tool_messages.append(ToolMessage(
                                content=json.dumps(result) if isinstance(result, (dict, list)) else str(result),
                                tool_call_id=tool_call['id']
                            ))
                            
                        except Exception as e:
                            tool_messages.append(ToolMessage(
                                content=f"Error: {str(e)}",
                                tool_call_id=tool_call['id']
                            ))
                        break
            
            return {"messages": tool_messages, "status": "tools_executed"}
        
        return {"status": "no_tools_called"}
    
    def synthesizer_node(self, state: TravelState) -> Dict[str, Any]:
        """Synthesize all information into final report"""
        print("📝 Generating final report...")
        
        # Create comprehensive travel report
        report_parts = []
        
        # Destination overview
        if "researched_destinations" in state:
            dest_info = state["researched_destinations"]
            report_parts.append(f"# 🌍 {state['destination'].upper()} TRAVEL PLAN")
            report_parts.append(f"**Description**: {dest_info.get('description', 'N/A')}")
            report_parts.append(f"**Best Season**: {dest_info.get('best_season', 'N/A')}")
            report_parts.append(f"**Cost Level**: {dest_info.get('cost_level', 'N/A')}")
            report_parts.append("")
        
        # Itinerary
        if "daily_itinerary" in state:
            report_parts.append("## 📅 DAILY ITINERARY")
            for day in state["daily_itinerary"]:
                report_parts.append(f"### Day {day['day']}")
                report_parts.append(f"- **Morning**: {day['morning']}")
                report_parts.append(f"- **Afternoon**: {day['afternoon']}")
                report_parts.append(f"- **Evening**: {day['evening']}")
                report_parts.append(f"- **Meals**: {day['meals']}")
                report_parts.append(f"- **Accommodation**: {day['accommodation_type']}")
                report_parts.append("")
        
        # Budget
        if "budget_breakdown" in state:
            budget = state["budget_breakdown"]
            report_parts.append("## 💰 BUDGET BREAKDOWN")
            report_parts.append(f"**Total Budget**: ${budget['total_budget']}")
            report_parts.append(f"**Budget Level**: {budget['budget_level']}")
            report_parts.append(f"**Daily Budget**: ${budget['budget_per_day']}")
            report_parts.append(f"**Per Person**: ${budget['budget_per_person']}")
            report_parts.append("")
            report_parts.append("**Category Breakdown**:")
            for category, amount in budget["budget_breakdown"].items():
                category_name = category.replace('_', ' ').title()
                report_parts.append(f"- {category_name}: ${amount}")
            report_parts.append("")
        
        # Weather
        if "weather_info" in state:
            weather = state["weather_info"]
            report_parts.append("## 🌤️ WEATHER & PACKING")
            report_parts.append(f"**Temperature**: {weather['temperature']}")
            report_parts.append(f"**Conditions**: {weather['weather_conditions']}")
            report_parts.append(f"**Rainfall**: {weather['average_rainfall']}")
            report_parts.append(f"**Sunlight**: {weather['daily_sunlight']}")
            report_parts.append("")
            report_parts.append("**Packing Recommendations**:")
            for item in weather["packing_recommendations"]:
                report_parts.append(f"- {item}")
        
        final_report = "\n".join(report_parts)
        
        return {
            "final_report": final_report,
            "status": "completed",
            "messages": [HumanMessage(content=f"Travel plan completed! Report:\n\n{final_report}")]
        }
    
    def should_continue(self, state: TravelState) -> str:
        """Decide whether to continue or end the workflow"""
        last_message = state["messages"][-1]
        
        # If we have tool calls, continue to synthesizer
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            return "continue"
        
        # If we already have a final report, end
        if state.get("final_report"):
            return "end"
            
        return "continue"
    
    def build_graph(self):
        """Build the LangGraph workflow"""
        workflow = StateGraph(TravelState)
        
        # Add nodes
        workflow.add_node("planner", self.planner_node)
        workflow.add_node("tools", self.tools_node)
        workflow.add_node("synthesizer", self.synthesizer_node)
        
        # Define workflow
        workflow.set_entry_point("planner")
        workflow.add_edge("planner", "tools")
        workflow.add_conditional_edges(
            "tools",
            self.should_continue,
            {
                "continue": "synthesizer",
                "end": END
            }
        )
        workflow.add_edge("synthesizer", END)
        
        self.graph = workflow.compile()
    
    def plan_trip(self, 
                 destination: str,
                 duration: int,
                 budget: float,
                 travel_style: str = "mixed",
                 traveler_count: int = 1,
                 interests: List[str] = None,
                 travel_month: str = None) -> Dict[str, Any]:
        """Main method to plan a complete trip"""
        
        if interests is None:
            interests = ["sightseeing"]
        
        if travel_month is None:
            travel_month = "May"  # Default to spring
        
        initial_state = {
            "destination": destination,
            "trip_duration": duration,
            "budget": budget,
            "travel_style": travel_style,
            "traveler_count": traveler_count,
            "interests": interests,
            "travel_month": travel_month,
            "messages": [],
            "status": "initialized"
        }
        
        print(f"🚀 Starting travel planning for {destination}...")
        result = self.graph.invoke(initial_state)
        print("✅ Travel planning completed!")
        
        return result