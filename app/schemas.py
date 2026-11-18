
from pydantic import BaseModel, HttpUrl
from typing import List


class LinkAnalysisRequest(BaseModel):
    url: HttpUrl


class CompetitorDetails(BaseModel):
    brand_name: str
    competitor_name: str
    comparison: str


class SearchQueries(BaseModel):
    google: List[str]
    facebook: List[str]
    instagram: List[str]
    linkedin: List[str]
    x: List[str]


class SEOImprovements(BaseModel):
    keywords: List[str]
    suggested_title: str
    meta_description: str
    supporting_content: List[str]


class TopServices(BaseModel):
    services: List[str]


class TargetAudience(BaseModel):
    audience: List[str]


class LinkAnalysisResponse(BaseModel):
    competitor_vs_brand: CompetitorDetails
    target_search_queries: SearchQueries
    seo_improvements: SEOImprovements
    top_services: TopServices
    target_audience: TargetAudience
