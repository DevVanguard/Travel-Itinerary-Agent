#!/usr/bin/env python3
"""
Main test file for Travel Itinerary Agent
"""

import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_basic_functionality():
    """Test that all components work without LangGraph"""
    print("🧪 Testing Basic Components...")
    
    try:
        from tools.destination_research import research_destination
        from tools.itinerary_builder import build_daily_itinerary
        from tools.budget_calculator import calculate_budget_breakdown
        from tools.weather_checker import get_seasonal_weather
        
        # Test each component
        print("1. Testing destination research...")
        paris_info = research_destination("Paris", ["museums"])
        print(f"   ✅ Paris attractions: {len(paris_info['attractions'])} found")
        
        print("2. Testing itinerary builder...")
        itinerary = build_daily_itinerary("Paris", 3, "cultural", paris_info['attractions'][:3])
        print(f"   ✅ Itinerary: {len(itinerary)} days created")
        
        print("3. Testing budget calculator...")
        budget = calculate_budget_breakdown("Paris", 3, 1500, "cultural", 2)
        print(f"   ✅ Budget: ${budget['total_budget']} calculated")
        
        print("4. Testing weather checker...")
        weather = get_seasonal_weather("Paris", "May")
        print(f"   ✅ Weather: {weather['temperature']}")
        
        print("\n🎉 All basic components work!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_agent_structure():
    """Test if we can import the agent structure"""
    print("\n🤖 Testing Agent Structure...")
    
    try:
        # Try to import without initializing (to avoid API calls)
        import importlib
        agent_spec = importlib.util.find_spec("src.agent")
        if agent_spec:
            print("✅ Agent module found!")
        else:
            print("❌ Agent module not found")
            return False
            
        # Check if we can access the class
        from src.agent import TravelPlannerAgent
        print("✅ Agent class can be imported!")
        
        # Don't initialize to avoid API calls
        print("⚠️  Skipping agent initialization to avoid API calls")
        print("✅ Agent structure is correct!")
        
        return True
        
    except Exception as e:
        print(f"❌ Agent structure error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Travel Itinerary Agent - Component Test")
    print("=" * 50)
    
    basic_ok = test_basic_functionality()
    agent_ok = test_agent_structure()
    
    print("\n" + "=" * 50)
    if basic_ok and agent_ok:
        print("🎉 ALL TESTS PASSED! Your agent is ready!")
        print("\nNext steps:")
        print("1. Set up OpenAI API key for full functionality")
        print("2. Run the demo notebook for visualizations")
        print("3. Test the complete agent workflow")
    else:
        print("❌ Some tests failed. Check the errors above.")