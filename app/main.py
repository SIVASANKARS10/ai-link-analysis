
from fastapi import FastAPI, HTTPException
import httpx

from app.schemas import LinkAnalysisRequest, LinkAnalysisResponse
from app.services.analysis_service import perform_link_analysis


app = FastAPI(
    title="AI-Powered Website Link Analysis API",
    description="Analyze website content, competitors, SEO and target audience using Gemini AI.",
    version="1.0.0"
)


@app.get("/")
async def home():
    return {
        "message": "AI Website Link Analysis API is running!",
        "status": "success"
    }


@app.post("/link-analysis", response_model=LinkAnalysisResponse)
async def link_analysis(request: LinkAnalysisRequest):
    try:
        result = await perform_link_analysis(str(request.url))
        return result

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except httpx.HTTPError as error:
        print("HTTP ERROR:", repr(error))
        raise HTTPException(
            status_code=502,
            detail="Unable to fetch the requested website."
        )

    except Exception as error:
        print("ERROR DETAILS:", repr(error))
        raise HTTPException(
            status_code=500,
            detail="Website analysis failed. Please try again."
        )
