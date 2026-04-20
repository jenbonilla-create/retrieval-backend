from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import bookings, users, operators
from app.database import engine
from app.models import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Retrieval Backend API",
    description="Risk-managed on-demand retrieval platform",
    version="1.0.0"
)

# Enable CORS for web and mobile clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(bookings.router, prefix="/api/v1/bookings", tags=["bookings"])
app.include_router(operators.router, prefix="/api/v1/operators", tags=["operators"])

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "retrieval-backend"}