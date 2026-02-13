"""
Initialize database with default activities
"""
from app.database import init_db, SessionLocal, Activity
from datetime import datetime

def seed_default_activities():
    """Add default activities to database"""
    db = SessionLocal()
    
    # Check if activities already exist
    existing = db.query(Activity).count()
    if existing > 0:
        print(f"✅ Database already has {existing} activities")
        db.close()
        return
    
    # Default activities (same as our hardcoded ones)
    default_activities = [
        {"name": "Factory Floor Calisthenics", "category": "olahraga", "duration": 10, "icon": "⚙️", "intensity": "high"},
        {"name": "Conveyor Belt Sprint", "category": "olahraga", "duration": 5, "icon": "🏃", "intensity": "extreme"},
        {"name": "Hydraulic Press Push-ups", "category": "olahraga", "duration": 7, "icon": "💪", "intensity": "high"},
        {"name": "Assembly Line Desk Organization", "category": "produktivitas", "duration": 15, "icon": "🏭", "intensity": "medium"},
        {"name": "Quality Control: Check Emails", "category": "produktivitas", "duration": 10, "icon": "📧", "intensity": "low"},
        {"name": "Inventory Brainstorm Session", "category": "produktivitas", "duration": 20, "icon": "🧠", "intensity": "medium"},
        {"name": "Steam Valve Breathing Exercise", "category": "kesehatan", "duration": 5, "icon": "🌫️", "intensity": "low"},
        {"name": "Circuit Board Meditation", "category": "kesehatan", "duration": 10, "icon": "🧘", "intensity": "low"},
        {"name": "Safety Goggle Eye Rest", "category": "kesehatan", "duration": 3, "icon": "👁️", "intensity": "low"},
        {"name": "Blueprint Doodle Session", "category": "kreatif", "duration": 15, "icon": "📐", "intensity": "medium"},
        {"name": "Machine Learning (Actual Learning)", "category": "edukasi", "duration": 25, "icon": "🤖", "intensity": "high"},
        {"name": "Weld New Ideas Together", "category": "kreatif", "duration": 20, "icon": "🔧", "intensity": "medium"},
        {"name": "Sync Gears with Co-worker", "category": "sosial", "duration": 15, "icon": "👥", "intensity": "medium"},
        {"name": "Coffee Break Protocol", "category": "sosial", "duration": 10, "icon": "☕", "intensity": "low"},
        {"name": "Union Meeting Prep", "category": "sosial", "duration": 20, "icon": "📋", "intensity": "medium"},
        {"name": "System Reboot: Power Nap", "category": "kesehatan", "duration": 15, "icon": "⏸️", "intensity": "low"},
        {"name": "Overheat Prevention: Hydrate", "category": "kesehatan", "duration": 2, "icon": "💧", "intensity": "low"},
        {"name": "Error Debugging: Walk Around", "category": "kesehatan", "duration": 5, "icon": "🐛", "intensity": "medium"},
        {"name": "Precision Tool Sharpening", "category": "skill", "duration": 25, "icon": "⚒️", "intensity": "high"},
        {"name": "Read Technical Manual", "category": "edukasi", "duration": 30, "icon": "📖", "intensity": "medium"},
    ]
    
    # Add to database
    for activity_data in default_activities:
        activity = Activity(
            name=activity_data["name"],
            category=activity_data["category"],
            duration=activity_data["duration"],
            icon=activity_data["icon"],
            intensity=activity_data["intensity"],
            submitted_by="system",
            is_user_submitted=False,
            is_approved=True
        )
        db.add(activity)
    
    db.commit()
    print(f"✅ Added {len(default_activities)} default activities")
    db.close()

if __name__ == "__main__":
    # Initialize database
    init_db()
    
    # Seed with default activities
    seed_default_activities()
    
    print("🎉 Database setup complete!")