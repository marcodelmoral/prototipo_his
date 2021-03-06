from django.urls import path

from dengue.views import (
    AnalisisDengueAppView,
    ClusteringDengueAppView,
    SeriesAppView,
    SeriesDengueAppView,
    VectoresAppView,
    VectoresAppView2,
    )

app_name = "dengue"

urlpatterns = [
    path(
        "analisis_dengue",
        AnalisisDengueAppView.as_view(),
        name="analisis_dengue",
        ),
    path(
        "clustering_dengue",
        ClusteringDengueAppView.as_view(),
        name="clustering_dengue",
        ),
    path(
        "tablero_dengue",
        SeriesDengueAppView.as_view(),
        name="series_dengue",
        ),
    path("series", SeriesAppView.as_view(), name="series"),
    path("vectores", VectoresAppView.as_view(), name="vectores"),
    path("vectores2", VectoresAppView2.as_view(), name="vectores2"),
    ]
