"""
Database setup for Boredom Button
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'boredom.db')}"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class
Base = declarative_base()

# ===== MODELS =====

class Activity(Base):
    """Main activities table"""
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    duration = Column(Integer, default=5)  # in minutes
    intensity = Column(String, default="medium")  # low, medium, high, extreme
    icon = Column(String, default="⚙️")
    
    # Submission info
    submitted_by = Column(String, default="system")  # "system" or IP/user
    submitted_at = Column(DateTime, default=datetime.utcnow)
    is_approved = Column(Boolean, default=True)
    is_user_submitted = Column(Boolean, default=False)
    
    # Stats
    times_displayed = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)
    
    def to_dict(self):
        """Convert to dict for API response"""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "duration": str(self.duration),
            "intensity": self.intensity,
            "icon": self.icon,
            "submitted_by": self.submitted_by,
            "is_user_submitted": self.is_user_submitted,
            "times_displayed": self.times_displayed,
            "likes": self.likes,
            "dislikes": self.dislikes
        }


class UserSubmission(Base):
    """User submissions waiting for approval"""
    __tablename__ = "user_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    duration = Column(Integer, default=5)
    intensity = Column(String, default="medium")
    icon = Column(String, default="⚙️")
    
    # User info (simple - just IP for now)
    user_ip = Column(String)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    
    # Moderation
    status = Column(String, default="pending")  # pending, approved, rejected
    reviewed_by = Column(String, default=None)
    reviewed_at = Column(DateTime, default=None)
    rejection_reason = Column(String, default=None)


class RateLimit(Base):
    """Rate limiting table"""
    __tablename__ = "rate_limits"
    
    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, index=True)
    endpoint = Column(String)
    count = Column(Integer, default=1)
    last_request = Column(DateTime, default=datetime.utcnow)
    window_start = Column(DateTime, default=datetime.utcnow)


# Create tables
def init_db():
    """Initialize database (create tables)"""
    Base.metadata.create_all(bind=engine)
    print(f"✅ Database initialized at: {DATABASE_URL}")


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
    print("Database tables created!")