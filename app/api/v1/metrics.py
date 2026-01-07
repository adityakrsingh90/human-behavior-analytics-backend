from fastapi import APIRouter

router = APIRouter(tags=["Model Metrics"])

@router.get("/metrics")
def model_metrics():
    return {
        "random_forest": {
            "accuracy": 0.82,
            "f1_score": 0.79,
            "roc_auc": 0.85
        },
        "kmeans": {
            "silhouette_score": 0.61
        }
    }
