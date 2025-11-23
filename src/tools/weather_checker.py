import requests
from typing import Dict, List
import datetime

def get_seasonal_weather(destination: str, travel_month: str = None) -> Dict[str, any]:
    """Get seasonal weather information for a destination"""
    
    # Seasonal weather patterns by destination
    seasonal_data = {
        "paris": {
            "spring": {
                "temperature": "10-18°C",
                "conditions": "Mild with occasional rain",
                "recommendations": ["Light jacket", "Umbrella", "Layered clothing"],
                "avg_rainfall": "Moderate",
                "sunlight_hours": "12-14 hours"
            },
            "summer": {
                "temperature": "18-25°C", 
                "conditions": "Warm and pleasant",
                "recommendations": ["Light clothing", "Sunglasses", "Sun protection"],
                "avg_rainfall": "Low",
                "sunlight_hours": "14-16 hours"
            },
            "autumn": {
                "temperature": "8-15°C",
                "conditions": "Cool and crisp",
                "recommendations": ["Sweaters", "Waterproof jacket", "Comfortable shoes"],
                "avg_rainfall": "Moderate", 
                "sunlight_hours": "10-12 hours"
            },
            "winter": {
                "temperature": "2-8°C",
                "conditions": "Cold with possible snow",
                "recommendations": ["Warm coat", "Scarf", "Gloves", "Boots"],
                "avg_rainfall": "Low to Moderate",
                "sunlight_hours": "8-9 hours"
            }
        },
        "tokyo": {
            "spring": {
                "temperature": "12-20°C",
                "conditions": "Mild with cherry blossoms",
                "recommendations": ["Light layers", "Comfortable walking shoes", "Camera"],
                "avg_rainfall": "Moderate",
                "sunlight_hours": "12-14 hours"
            },
            "summer": {
                "temperature": "22-30°C",
                "conditions": "Hot and humid",
                "recommendations": ["Light breathable clothing", "Hat", "Water bottle", "Sunscreen"],
                "avg_rainfall": "High",
                "sunlight_hours": "13-15 hours"
            },
            "autumn": {
                "temperature": "15-22°C", 
                "conditions": "Cool and comfortable",
                "recommendations": ["Light jacket", "Layered clothing", "Walking shoes"],
                "avg_rainfall": "Moderate",
                "sunlight_hours": "11-13 hours"
            },
            "winter": {
                "temperature": "2-10°C",
                "conditions": "Cold and dry",
                "recommendations": ["Warm coat", "Thermal layers", "Scarf", "Gloves"],
                "avg_rainfall": "Low",
                "sunlight_hours": "9-10 hours"
            }
        },
        "bali": {
            "dry_season": {
                "temperature": "26-32°C",
                "conditions": "Warm and sunny",
                "recommendations": ["Light clothing", "Swimwear", "Sunscreen", "Hat"],
                "avg_rainfall": "Low",
                "sunlight_hours": "12 hours",
                "season_note": "Dry Season (April-September)"
            },
            "wet_season": {
                "temperature": "24-30°C", 
                "conditions": "Warm with heavy rainfall",
                "recommendations": ["Light rain jacket", "Quick-dry clothing", "Waterproof bag"],
                "avg_rainfall": "High",
                "sunlight_hours": "10-11 hours", 
                "season_note": "Wet Season (October-March)"
            }
        }
    }
    
    # Month to season mapping
    month_to_season = {
        "december": "winter", "january": "winter", "february": "winter",
        "march": "spring", "april": "spring", "may": "spring", 
        "june": "summer", "july": "summer", "august": "summer",
        "september": "autumn", "october": "autumn", "november": "autumn"
    }
    
    dest_lower = destination.lower()
    
    # Handle Bali separately (tropical climate)
    if dest_lower == "bali":
        if travel_month and travel_month.lower() in ["april", "may", "june", "july", "august", "september"]:
            season_key = "dry_season"
        else:
            season_key = "wet_season"
    else:
        # For other destinations
        if travel_month:
            season_key = month_to_season.get(travel_month.lower(), "spring")
        else:
            season_key = "spring"  # Default
    
    # Get weather data
    if dest_lower in seasonal_data:
        weather_info = seasonal_data[dest_lower].get(season_key, {})
        if weather_info:
            return {
                "destination": destination,
                "season": season_key,
                "travel_month": travel_month,
                "temperature": weather_info["temperature"],
                "weather_conditions": weather_info["conditions"],
                "packing_recommendations": weather_info["recommendations"],
                "average_rainfall": weather_info["avg_rainfall"],
                "daily_sunlight": weather_info["sunlight_hours"],
                "special_notes": weather_info.get("season_note", "")
            }
    
    # Default response for unknown destinations
    return {
        "destination": destination,
        "season": "unknown",
        "travel_month": travel_month,
        "temperature": "15-25°C",
        "weather_conditions": "Moderate weather conditions",
        "packing_recommendations": ["Versatile clothing", "Comfortable shoes", "Light jacket"],
        "average_rainfall": "Moderate",
        "daily_sunlight": "10-12 hours",
        "special_notes": "Check local weather forecast before travel"
    }