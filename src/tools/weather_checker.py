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
        },
        # PAKISTAN CITIES - ADDED NEW DATA WITHOUT REMOVING ORIGINAL
        "islamabad": {
            "spring": {
                "temperature": "15-25°C",
                "conditions": "Pleasant with blooming flowers",
                "recommendations": ["Light jacket", "Comfortable shoes", "Sunglasses"],
                "avg_rainfall": "Low",
                "sunlight_hours": "12-14 hours"
            },
            "summer": {
                "temperature": "25-35°C", 
                "conditions": "Warm with occasional rain",
                "recommendations": ["Light clothing", "Umbrella", "Sunscreen"],
                "avg_rainfall": "Moderate",
                "sunlight_hours": "14-15 hours"
            },
            "autumn": {
                "temperature": "18-28°C",
                "conditions": "Mild and pleasant",
                "recommendations": ["Light layers", "Walking shoes", "Camera"],
                "avg_rainfall": "Low",
                "sunlight_hours": "11-13 hours"
            },
            "winter": {
                "temperature": "5-18°C",
                "conditions": "Cool and crisp",
                "recommendations": ["Warm jacket", "Sweaters", "Comfortable boots"],
                "avg_rainfall": "Low",
                "sunlight_hours": "10-11 hours"
            }
        },
        "karachi": {
            "summer": {
                "temperature": "28-35°C",
                "conditions": "Hot and humid",
                "recommendations": ["Light cotton clothing", "Sunscreen", "Water bottle", "Hat"],
                "avg_rainfall": "Very Low",
                "sunlight_hours": "13-14 hours"
            },
            "winter": {
                "temperature": "15-25°C",
                "conditions": "Mild and pleasant",
                "recommendations": ["Light jacket", "Comfortable clothing", "Sunglasses"],
                "avg_rainfall": "Very Low", 
                "sunlight_hours": "10-12 hours"
            }
        },
        "lahore": {
            "summer": {
                "temperature": "25-40°C",
                "conditions": "Hot and dry",
                "recommendations": ["Light breathable fabric", "Hat", "Sunscreen", "Water"],
                "avg_rainfall": "Low",
                "sunlight_hours": "14-15 hours"
            },
            "winter": {
                "temperature": "5-20°C", 
                "conditions": "Cool with fog",
                "recommendations": ["Warm layers", "Jacket", "Scarf", "Comfortable shoes"],
                "avg_rainfall": "Low",
                "sunlight_hours": "9-11 hours"
            }
        },
        "hunza": {
            "summer": {
                "temperature": "10-25°C",
                "conditions": "Pleasant with clear skies",
                "recommendations": ["Layered clothing", "Warm jacket", "Sunglasses", "Hiking boots"],
                "avg_rainfall": "Low",
                "sunlight_hours": "14-16 hours"
            },
            "winter": {
                "temperature": "-10 to 10°C",
                "conditions": "Cold with snow",
                "recommendations": ["Heavy winter coat", "Thermal wear", "Gloves", "Warm boots"],
                "avg_rainfall": "Moderate snow",
                "sunlight_hours": "9-10 hours"
            }
        },
        "swat": {
            "summer": {
                "temperature": "15-30°C", 
                "conditions": "Pleasant with cool breezes",
                "recommendations": ["Light layers", "Comfortable shoes", "Light jacket", "Camera"],
                "avg_rainfall": "Low",
                "sunlight_hours": "13-15 hours"
            },
            "winter": {
                "temperature": "-5 to 15°C",
                "conditions": "Cold with snow in mountains",
                "recommendations": ["Warm clothing", "Winter jacket", "Boots", "Gloves"],
                "avg_rainfall": "Moderate snow",
                "sunlight_hours": "9-11 hours"
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
    
    # Handle Bali separately (tropical climate)
    if destination.lower() == "bali":
        if travel_month and travel_month.lower() in ["april", "may", "june", "july", "august", "september"]:
            season_key = "dry_season"
        else:
            season_key = "wet_season"
    # Handle Pakistan cities with different climate patterns
    elif destination.lower() in ["karachi", "lahore", "hunza", "swat"]:
        # Pakistan cities mainly have summer/winter seasons
        if travel_month and travel_month.lower() in ["november", "december", "january", "february", "march"]:
            season_key = "winter"
        else:
            season_key = "summer"
    else:
        # For other destinations
        if travel_month:
            season_key = month_to_season.get(travel_month.lower(), "spring")
        else:
            season_key = "spring"  # Default
    
    # Get weather data
    if destination.lower() in seasonal_data:
        weather_info = seasonal_data[destination.lower()].get(season_key, {})
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