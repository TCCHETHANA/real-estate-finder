"""backend.routes package initializer"""
from .search import search_bp
from .predict import predict_bp

__all__ = ["search_bp", "predict_bp"]
