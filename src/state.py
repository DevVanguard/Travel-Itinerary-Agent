from typing import TypedDict, List, Dict, Any, Annotated
from langgraph.graph.message import add_messages

class TravelState(TypedDict):
    # User inputs
    messages: Annotated[List, add_messages]
    destination: str
    trip_duration: int
    budget: float
    travel_style: str
    traveler_count: int
    interests: List[str]
    travel_month: str
    
    # Research data
    researched_destinations: Dict[str, Any]
    attractions: List[str]
    
    # Planning data
    daily_itinerary: List[Dict]
    budget_breakdown: Dict[str, Any]
    weather_info: Dict[str, Any]
    
    # Visualizations
    itinerary_map: str
    budget_chart: str
    
    # Final output
    final_report: str
    status: str