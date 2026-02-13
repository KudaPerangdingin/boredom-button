"""
Industrial Workaholic Activities Database
"""

ACTIVITIES = [
    {"id": 1, "name": "Factory Floor Calisthenics", "category": "olahraga", "duration": "10", "icon": "⚙️", "intensity": "high"},
    {"id": 2, "name": "Conveyor Belt Sprint", "category": "olahraga", "duration": "5", "icon": "🏃", "intensity": "extreme"},
    {"id": 3, "name": "Hydraulic Press Push-ups", "category": "olahraga", "duration": "7", "icon": "💪", "intensity": "high"},
    {"id": 4, "name": "Assembly Line Desk Organization", "category": "produktivitas", "duration": "15", "icon": "🏭", "intensity": "medium"},
    {"id": 5, "name": "Quality Control: Check Emails", "category": "produktivitas", "duration": "10", "icon": "📧", "intensity": "low"},
    {"id": 6, "name": "Inventory Brainstorm Session", "category": "produktivitas", "duration": "20", "icon": "🧠", "intensity": "medium"},
    {"id": 7, "name": "Steam Valve Breathing Exercise", "category": "kesehatan", "duration": "5", "icon": "🌫️", "intensity": "low"},
    {"id": 8, "name": "Circuit Board Meditation", "category": "kesehatan", "duration": "10", "icon": "🧘", "intensity": "low"},
    {"id": 9, "name": "Safety Goggle Eye Rest", "category": "kesehatan", "duration": "3", "icon": "👁️", "intensity": "low"},
    {"id": 10, "name": "Blueprint Doodle Session", "category": "kreatif", "duration": "15", "icon": "📐", "intensity": "medium"},
    {"id": 11, "name": "Machine Learning (Actual Learning)", "category": "edukasi", "duration": "25", "icon": "🤖", "intensity": "high"},
    {"id": 12, "name": "Weld New Ideas Together", "category": "kreatif", "duration": "20", "icon": "🔧", "intensity": "medium"},
    {"id": 13, "name": "Sync Gears with Co-worker", "category": "sosial", "duration": "15", "icon": "👥", "intensity": "medium"},
    {"id": 14, "name": "Coffee Break Protocol", "category": "sosial", "duration": "10", "icon": "☕", "intensity": "low"},
    {"id": 15, "name": "Union Meeting Prep", "category": "sosial", "duration": "20", "icon": "📋", "intensity": "medium"},
    {"id": 16, "name": "System Reboot: Power Nap", "category": "kesehatan", "duration": "15", "icon": "⏸️", "intensity": "low"},
    {"id": 17, "name": "Overheat Prevention: Hydrate", "category": "kesehatan", "duration": "2", "icon": "💧", "intensity": "low"},
    {"id": 18, "name": "Error Debugging: Walk Around", "category": "kesehatan", "duration": "5", "icon": "🐛", "intensity": "medium"},
    {"id": 19, "name": "Precision Tool Sharpening", "category": "skill", "duration": "25", "icon": "⚒️", "intensity": "high"},
    {"id": 20, "name": "Read Technical Manual", "category": "edukasi", "duration": "30", "icon": "📖", "intensity": "medium"},
]

# ✅ TAMBAHKIN INI - CATEGORIES harus didefinisikan!
CATEGORIES = {
    "all": {"name": "All Systems", "color": "#FFD700", "icon": "⚙️"},
    "olahraga": {"name": "Physical Maintenance", "color": "#FF6B6B", "icon": "💪"},
    "produktivitas": {"name": "Production Line", "color": "#4ECDC4", "icon": "🏭"},
    "kesehatan": {"name": "System Health", "color": "#95E6C1", "icon": "❤️"},
    "kreatif": {"name": "R&D Department", "color": "#FF9A76", "icon": "🔬"},
    "edukasi": {"name": "Training Module", "color": "#A3A1F6", "icon": "🎓"},
    "sosial": {"name": "Team Syncing", "color": "#FFC145", "icon": "👥"},
    "skill": {"name": "Skill Upgrade", "color": "#9D65C9", "icon": "⚡"}
}

# Fungsi helper (opsional)
def get_random_activity(category: str = None):
    """Ambil aktivitas random dari list"""
    import random
    if category and category != "all":
        filtered = [act for act in ACTIVITIES if act["category"] == category]
        if filtered:
            return random.choice(filtered)
    return random.choice(ACTIVITIES)

def get_activity_by_category(category: str):
    """Filter aktivitas berdasarkan kategori"""
    return [act for act in ACTIVITIES if act["category"] == category]

def get_categories():
    """Dapatkan semua kategori unik"""
    return list(set(act["category"] for act in ACTIVITIES))