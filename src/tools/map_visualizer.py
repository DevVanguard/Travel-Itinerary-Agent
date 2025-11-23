import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from typing import List, Dict
import io
import base64

def generate_itinerary_map(destination: str, itinerary: List[Dict], attractions: List[str] = None) -> str:
    """Generate a visual itinerary map/timeline"""
    
    # Destination coordinates (simplified for demo)
    destination_coords = {
        "paris": {"x": 50, "y": 50, "color": "#FF6B6B"},
        "tokyo": {"x": 80, "y": 30, "color": "#4ECDC4"}, 
        "bali": {"x": 60, "y": 70, "color": "#45B7D1"},
        "default": {"x": 50, "y": 50, "color": "#96CEB4"}
    }
    
    dest_data = destination_coords.get(destination.lower(), destination_coords["default"])
    
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Set background color
    fig.patch.set_facecolor('#F8F9FA')
    ax.set_facecolor('#F8F9FA')
    
    # Draw destination circle
    destination_circle = patches.Circle(
        (dest_data["x"], dest_data["y"]), 
        radius=15, 
        facecolor=dest_data["color"],
        edgecolor='white',
        linewidth=3,
        alpha=0.8
    )
    ax.add_patch(destination_circle)
    
    # Add destination text
    ax.text(
        dest_data["x"], dest_data["y"], 
        destination.upper(), 
        ha='center', va='center', 
        fontsize=16, fontweight='bold', 
        color='white'
    )
    
    # Draw itinerary timeline
    day_height = 60
    start_y = 20
    
    for i, day in enumerate(itinerary):
        day_y = start_y + (i * day_height)
        
        # Day box
        day_box = FancyBboxPatch(
            (10, day_y), 80, 15,
            boxstyle="round,pad=0.02",
            facecolor='#E9ECEF',
            edgecolor='#495057',
            linewidth=1.5
        )
        ax.add_patch(day_box)
        
        # Day number
        ax.text(15, day_y + 7.5, f"DAY {day['day']}", 
                fontsize=12, fontweight='bold', color='#495057')
        
        # Activities for the day
        activities = [
            f"🌅 {day['morning'][:25]}...",
            f"🌇 {day['afternoon'][:25]}...", 
            f"🌃 {day['evening'][:25]}..."
        ]
        
        for j, activity in enumerate(activities):
            ax.text(25, day_y + 11 - (j * 3), activity, 
                    fontsize=9, color='#6C757D')
    
    # Add attractions if provided
    if attractions:
        ax.text(5, start_y + len(itinerary) * day_height + 10, 
                "🏛️ KEY ATTRACTIONS:", fontsize=12, fontweight='bold', color='#495057')
        
        for i, attraction in enumerate(attractions[:4]):  # Show max 4 attractions
            ax.text(5, start_y + len(itinerary) * day_height + 5 - (i * 4), 
                    f"• {attraction}", fontsize=9, color='#6C757D')
    
    # Set limits and remove axes
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Add title
    plt.suptitle(f'{destination.upper()} TRAVEL ITINERARY', 
                 fontsize=20, fontweight='bold', color='#343A40', y=0.95)
    
    # Convert to base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=120, facecolor=fig.get_facecolor())
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode()
    plt.close()
    
    return f"data:image/png;base64,{img_str}"

def generate_budget_vs_duration_chart(destination: str, budget_data: Dict) -> str:
    """Generate a chart showing budget distribution"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.patch.set_facecolor('#F8F9FA')
    
    # Pie chart for budget breakdown
    categories = []
    amounts = []
    
    for category, amount in budget_data['budget_breakdown'].items():
        display_name = category.replace('_', ' ').title()
        categories.append(display_name)
        amounts.append(amount)
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFE66D', '#6A0572']
    wedges, texts, autotexts = ax1.pie(amounts, labels=categories, colors=colors, 
                                      autopct='%1.1f%%', startangle=90)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax1.set_title('Budget Breakdown', fontsize=14, fontweight='bold', pad=20)
    
    # Bar chart for daily breakdown
    daily_categories = [cat.replace('_', ' ').title() for cat in budget_data['daily_breakdown'].keys()]
    daily_amounts = list(budget_data['daily_breakdown'].values())
    
    bars = ax2.bar(daily_categories, daily_amounts, color='#4ECDC4', alpha=0.8)
    ax2.set_title('Daily Budget Allocation', fontsize=14, fontweight='bold', pad=20)
    ax2.set_ylabel('Amount ($)')
    ax2.tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar, amount in zip(bars, daily_amounts):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'${amount}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    
    # Convert to base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=120, facecolor=fig.get_facecolor())
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode()
    plt.close()
    
    return f"data:image/png;base64,{img_str}"