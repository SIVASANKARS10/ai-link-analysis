
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

from app.main import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_link_analysis_success():
    mock_result = {
        "competitor_vs_brand": {
            "brand_name": "Microsoft",
            "competitor_name": "Apple",
            "comparison": "Both companies provide technology products."
        },
        "target_search_queries": {
            "google": ["query1", "query2", "query3", "query4", "query5"],
            "facebook": ["query1", "query2", "query3", "query4", "query5"],
            "instagram": ["query1", "query2", "query3", "query4", "query5"],
            "linkedin": ["query1", "query2", "query3", "query4", "query5"],
            "x": ["query1", "query2", "query3", "query4", "query5"]
        },
        "seo_improvements": {
            "keywords": ["Microsoft", "Cloud Computing"],
            "suggested_title": "Microsoft Technology",
            "meta_description": "Microsoft products and services.",
            "supporting_content": ["Product guides"]
        },
        "top_services": {
            "services": ["Cloud Computing", "Software"]
        },
        "target_audience": {
            "audience": ["Developers", "Businesses"]
        }
    }

    with patch(
        "app.main.perform_link_analysis",
        new_callable=AsyncMock
    ) as mock_analysis:

        mock_analysis.return_value = mock_result

        response = client.post(
            "/link-analysis",
            json={"url": "https://www.microsoft.com"}
        )

    assert response.status_code == 200
    assert response.json() == mock_result


def test_invalid_url():
    response = client.post(
        "/link-analysis",
        json={"url": "not-a-valid-url"}
    )

    assert response.status_code == 422


def test_analysis_failure():
    with patch(
        "app.main.perform_link_analysis",
        new_callable=AsyncMock
    ) as mock_analysis:

        mock_analysis.side_effect = ValueError("Invalid website URL")

        response = client.post(
            "/link-analysis",
            json={"url": "https://example.com"}
        )

    assert response.status_code == 400
