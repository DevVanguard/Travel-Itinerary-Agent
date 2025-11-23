from typing import List, Dict
import random

def build_daily_itinerary(destination: str, duration: int, travel_style: str, attractions: List[str]) -> List[Dict]:
    """Build a detailed daily itinerary"""
    
    if not attractions:
        attractions = ["main attractions", "local experiences", "cultural sites"]
    
    itineraries = []
    
    # Different templates based on travel style
    templates = {
        "adventure": {
            "morning": "Adventure activity and exploration",
            "afternoon": "Outdoor experiences and local adventures", 
            "evening": "Relaxation and local dining"
        },
        "cultural": {
            "morning": "Museum and historical site visits",
            "afternoon": "Cultural workshops and local experiences",
            "evening": "Traditional performances and dining"
        },
        "relaxation": {
            "morning": "Spa treatments and leisurely breakfast",
            "afternoon": "Beach time or peaceful gardens", 
            "evening": "Fine dining and sunset views"
        },
        "mixed": {
            "morning": "Sightseeing and main attractions",
            "afternoon": "Local experiences and exploration",
            "evening": "Entertainment and dining"
        }
    }
    
    template = templates.get(travel_style, templates["mixed"])
    
    for day in range(1, duration + 1):
        attraction = attractions[(day - 1) % len(attractions)]
        
        daily_plan = {
            "day": day,
            "morning": f"{template['morning']} at {attraction}",
            "afternoon": f"{template['afternoon']} in {destination}",
            "evening": f"{template['evening']} with local cuisine",
            "meals": "Breakfast at accommodation, Lunch at local restaurant, Dinner at recommended spot",
            "accommodation_type": "Hotel" if travel_style != "budget" else "Hostel/Guesthouse"
        }
        itineraries.append(daily_plan)
    
    return itineraries