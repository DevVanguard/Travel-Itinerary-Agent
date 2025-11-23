#!/usr/bin/env python3
"""
Fixed test for the agent structure
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

print("🧪 Testing Agent Structure...")

try:
    # Test basic imports first
    from src.state import TravelState
    print("✅ State imported successfully!")
    
    from src.tools.destination_research import research_destination
    print("✅ Tools imported successfully!")
    
    # Now try the agent
    from src.agent import TravelPlannerAgent
    print("✅ Agent class imported successfully!")
    
    print("All imports successful! 🎉")
    
except Exception as e:
    print(f"❌ Import Error: {e}")
    import traceback
    traceback.print_exc()