from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.tools import analyze_all_candidates
from agent.utils import load_candidates

app = FastAPI()

# Configuration CORS pour permettre au Frontend de communiquer avec le Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze-all")
async def analyze_all():
    candidates = load_candidates()
    results = analyze_all_candidates(candidates)
    return results

@app.post("/analyze-one")
async def analyze_one(candidate: dict):
    # Simule l'analyse d'un candidat envoyé via JSON
    candidate["__file__"] = "nouveau_candidat.json"
    results = analyze_all_candidates([candidate])
    return results[0]