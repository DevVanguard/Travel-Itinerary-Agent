from typing import Dict, List
import matplotlib.pyplot as plt
import io
import base64

def calculate_budget_breakdown(destination: str, duration: int, total_budget: float, 
                             travel_style: str, traveler_count: int = 1) -> Dict[str, float]:
    """Calculate detailed budget breakdown for a trip"""
    
    # Cost multipliers based on destination
    destination_costs = {
        "paris": {"base_daily": 150, "multiplier": 1.3},
        "tokyo": {"base_daily": 180, "multiplier": 1.5},
        "bali": {"base_daily": 80, "multiplier": 0.8},
        # Pakistan cities - ADDED NEW DATA
        "islamabad": {"base_daily": 60, "multiplier": 1.1},
        "karachi": {"base_daily": 50, "multiplier": 1.0},
        "lahore": {"base_daily": 45, "multiplier": 0.9},
        "hunza": {"base_daily": 40, "multiplier": 0.8},
        "swat": {"base_daily": 35, "multiplier": 0.7},
        "default": {"base_daily": 120, "multiplier": 1.0}
    }
    
    # Style multipliers
    style_multipliers = {
        "luxury": 1.8,
        "comfort": 1.2,
        "cultural": 1.0,
        "adventure": 0.9,
        "relaxation": 1.3,
        "budget": 0.6,
        "mixed": 1.0
    }
    
    # Get destination cost data
    dest_data = destination_costs.get(destination.lower(), destination_costs["default"])
    style_multiplier = style_multipliers.get(travel_style, 1.0)
    
    # Calculate base daily budget per person
    base_daily = dest_data["base_daily"] * style_multiplier * dest_data["multiplier"]
    total_base = base_daily * duration * traveler_count
    
    # Adjust if user's budget is different from our calculation
    budget_adjustment = total_budget / total_base if total_base > 0 else 1.0
    
    # Budget allocation percentages
    allocation = {
        "accommodation": 0.35,
        "food_dining": 0.25,
        "activities_entertainment": 0.20,
        "transportation": 0.12,
        "shopping_souvenirs": 0.05,
        "emergency_misc": 0.03
    }
    
    # Calculate actual amounts
    budget_breakdown = {}
    for category, percentage in allocation.items():
        budget_breakdown[category] = round(total_budget * percentage, 2)
    
    # Calculate per-day amounts
    daily_breakdown = {
        category: round(amount / duration, 2) 
        for category, amount in budget_breakdown.items()
    }
    
    return {
        "total_budget": total_budget,
        "trip_duration": duration,
        "traveler_count": traveler_count,
        "budget_breakdown": budget_breakdown,
        "daily_breakdown": daily_breakdown,
        "budget_per_day": round(total_budget / duration, 2),
        "budget_per_person": round(total_budget / traveler_count, 2),
        "budget_level": "Luxury" if base_daily > 200 else "Comfort" if base_daily > 120 else "Budget"
    }

def generate_budget_chart(budget_breakdown: Dict[str, float]) -> str:
    """Generate a pie chart visualization of the budget breakdown"""
    
    # Prepare data for plotting
    categories = []
    amounts = []
    
    for category, amount in budget_breakdown.items():
        # Format category names for display
        display_name = category.replace('_', ' ').title()
        categories.append(display_name)
        amounts.append(amount)
    
    # Create pie chart
    plt.figure(figsize=(10, 8))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0']
    
    wedges, texts, autotexts = plt.pie(
        amounts, 
        labels=categories, 
        colors=colors,
        autopct='%1.1f%%',
        startangle=90
    )
    
    # Style the chart
    plt.title('Trip Budget Breakdown', fontsize=16, fontweight='bold', pad=20)
    
    # Improve text styling
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    # Equal aspect ratio ensures pie is drawn as circle
    plt.axis('equal')
    
    # Convert plot to base64 for display
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode()
    plt.close()
    
    return f"data:image/png;base64,{img_str}"