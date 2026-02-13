# 1. IMPORTS (paling atas)
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os

# 2. INISIALISASI FASTAPI (WAJIB PALING ATAS SEBELUM ROUTE)
app = FastAPI(title="BOREDOM BUTTON")

# 3. CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. SETUP TEMPLATES & STATIC
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

templates = Jinja2Templates(directory=TEMPLATES_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 5. ROUTES (SEMUA ROUTE DI BAWAH INI)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/submit", response_class=HTMLResponse)
async def submit_form(request: Request):
    return templates.TemplateResponse("submit.html", {"request": request})

@app.post("/submit")
async def handle_submit(
    request: Request,
    name: str = Form(...),
    category: str = Form(...),
    duration: int = Form(...),
    intensity: str = Form(...),
    icon: str = Form("😊")
):
    # TODO: Simpen ke database
    return {"message": "Activity submitted!"}

# 6. ROUTE LAIN (kalo ada)
@app.get("/random")
async def random_activity():
    # TODO: ambil activity random dari database
    return {"activity": "GOKGOKGOK"}