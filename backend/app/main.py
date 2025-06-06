from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.agents.research_agent import research_topic
from app.agents.writer_agent import write_content
from app.agents.designer_agent import get_images_for_topic
from app.agents.reviewer_agent import review_content

app = FastAPI()

# CORS ayarları – frontend'in erişebilmesi için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL'ine göre ayarla
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Research Agent Endpoint (GET)
# ----------------------------
@app.get("/api/research")
def get_research(topic: str = Query(..., min_length=3)):
    """
    ResearchAgent: Wikipedia'dan özet getirir.
    """
    result = research_topic(topic)
    return {"topic": topic, "summary": result}

# ----------------------------
# Writer Agent Endpoint (POST)
# ----------------------------
class WriteRequest(BaseModel):
    topic: str
    context: str

@app.post("/api/write")
def post_writer_agent(payload: WriteRequest):
    """
    WriterAgent: LLM ile içerik üretir.
    """
    content = write_content(payload.topic, payload.context)
    return {"content": content}

@app.get("/api/images")
def get_images(topic: str = Query(..., min_length=3)):
    images = get_images_for_topic(topic)


class ReviewRequest(BaseModel):
    content: str

@app.post("/api/review")
def post_review(payload: ReviewRequest):
    feedback = review_content(payload.content)
    return {"feedback": feedback}