from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model import anxiety_model
import uvicorn

app = FastAPI(
    title="Exam Anxiety Detector API",
    description="API for detecting anxiety levels from student test reflections using BERT.",
    version="1.0.0"
)

# Enable CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InferenceRequest(BaseModel):
    text: str

class InferenceResponse(BaseModel):
    prediction_id: int
    prediction_label: str
    confidence: float
    text_processed: str

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Exam Anxiety Detector API is running."}

@app.post("/predict", response_model=InferenceResponse)
def predict_anxiety(request: InferenceRequest):
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
        
    try:
        # Use the loaded model for prediction
        result = anxiety_model.predict(request.text)
        
        if "error" in result:
             raise HTTPException(status_code=500, detail=result["error"])
             
        return InferenceResponse(
            prediction_id=result["prediction_id"],
            prediction_label=result["prediction_label"],
            confidence=result["confidence"],
            text_processed=request.text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
