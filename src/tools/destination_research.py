from typing import List, Dict

def research_destination(destination: str, interests: List[str] = None) -> Dict:
    """Research destination attractions and activities"""
    
    if interests is None:
        interests = ["sightseeing"]
    
    # Enhanced destination database with Pakistan cities
    destinations_db = {
        # Pakistan Cities
        "islamabad": {
            "attractions": ["Faisal Mosque", "Daman-e-Koh", "Pakistan Monument", "Lok Virsa Museum", "Margalla Hills", "Rawal Lake"],
            "activities": ["Hiking in Margalla Hills", "Mosque visits", "Museum tours", "Boating", "Cultural shows"],
            "best_season": "Spring (March-May) and Autumn (September-November)",
            "cost_level": "Medium",
            "description": "Capital city with beautiful mountains and modern architecture"
        },
        "karachi": {
            "attractions": ["Clifton Beach", "Mazar-e-Quaid", "Frere Hall", "Port Grand", "Mohatta Palace", "Churna Island"],
            "activities": ["Beach activities", "Historical site visits", "Seafood dining", "Shopping", "Island trips"],
            "best_season": "Winter (November-February)",
            "cost_level": "Medium",
            "description": "Vibrant coastal metropolis and economic hub"
        },
        "lahore": {
            "attractions": ["Lahore Fort", "Badshahi Mosque", "Shalimar Gardens", "Lahore Museum", "Wagah Border", "Anarkali Bazaar"],
            "activities": ["Historical tours", "Food street visits", "Shopping in bazaars", "Cultural shows", "Border ceremony"],
            "best_season": "Winter (October-March)",
            "cost_level": "Low",
            "description": "Cultural heart of Pakistan with Mughal heritage"
        },
        "hunza": {
            "attractions": ["Baltit Fort", "Attabad Lake", "Passu Cones", "Rakaposhi View", "Eagle's Nest", "Khunjerab Pass"],
            "activities": ["Mountain trekking", "Lake visits", "Fort exploration", "Photography", "Cultural immersion"],
            "best_season": "Summer (May-September)",
            "cost_level": "Low",
            "description": "Breathtaking mountain valley in the Karakoram range"
        },
        "swat": {
            "attractions": ["Malam Jabba", "Mahodand Lake", "White Palace", "Ushu Forest", "Butkara Stupa", "Swat Museum"],
            "activities": ["Skiing", "Hiking", "Lake visits", "Historical exploration", "Photography"],
            "best_season": "Summer (April-September)",
            "cost_level": "Low", 
            "description": "Switzerland of Pakistan with stunning valleys"
        },
        
        # Original destinations
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