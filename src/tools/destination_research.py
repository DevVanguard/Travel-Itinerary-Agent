from typing import List, Dict

def research_destination(destination: str, interests: List[str] = None) -> Dict:
    """Research destination attractions and activities"""
    
    if interests is None:
        interests = ["sightseeing"]
    
    # Destination database - we'll expand this later
    destinations_db = {
        "paris": {
            "attractions": ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Montmartre", "Seine River Cruise"],
            "activities": ["Museum tours", "River cruise", "Food tasting", "Shopping", "Photography"],
            "best_season": "Spring (March-May)",
            "cost_level": "Medium",
            "description": "City of Lights with rich history and culture"
        },
        "tokyo": {
            "attractions": ["Sensoji Temple", "Tokyo Skytree", "Shibuya Crossing", "Meiji Shrine", "Akihabara"],
            "activities": ["Temple visits", "Sushi making", "Anime shopping", "Gardens", "Karaoke"],
            "best_season": "Autumn (September-November)", 
            "cost_level": "High",
            "description": "Blend of traditional and ultra-modern experiences"
        },
        "bali": {
            "attractions": ["Uluwatu Temple", "Tegallalang Rice Terrace", "Ubud Monkey Forest", "Waterfalls", "Beaches"],
            "activities": ["Beach relaxation", "Temple tours", "Yoga classes", "Water sports", "Spa treatments"],
            "best_season": "Dry season (April-October)",
            "cost_level": "Low",
            "description": "Tropical paradise with rich culture and nature"
        }
    }
    
    dest_lower = destination.lower()
    if dest_lower in destinations_db:
        result = destinations_db[dest_lower]
        # Filter activities based on interests
        if interests:
            result["recommended_activities"] = [
                activity for activity in result["activities"] 
                if any(interest in activity.lower() for interest in interests)
            ]
        return result
    else:
        # Fallback for unknown destinations
        return {
            "attractions": ["City Center", "Local Markets", "Historical Sites", "Main Square"],
            "activities": ["Sightseeing", "Local cuisine", "Cultural experiences", "Shopping"],
            "best_season": "All year",
            "cost_level": "Medium",
            "description": "Popular travel destination with diverse experiences",
            "recommended_activities": ["Sightseeing", "Local cuisine"]
        }