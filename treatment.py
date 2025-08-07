def get_recommendations(disease_name):
    recommendations = {
        "Tomato_Bacterial_spot": {
            "organic": "Use copper sprays and remove infected plants.",
            "chemical": "Apply streptomycin in early stages.",
            "prevention": "Avoid splashing water and rotate crops."
        },
        "Tomato_Early_blight": {
            "organic": "Neem oil and compost teas help.",
            "chemical": "Use chlorothalonil or mancozeb.",
            "prevention": "Prune lower leaves and avoid wet foliage."
        },
        "Tomato_Late_blight": {
            "organic": "Copper fungicides and good airflow are key.",
            "chemical": "Use fluazinam-based fungicides.",
            "prevention": "Destroy infected plants and avoid high humidity."
        },
        "Tomato_healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Monitor regularly and maintain hygiene."
        },
        "Potato___Early_blight": {
            "organic": "Neem oil or compost tea sprays help.",
            "chemical": "Use chlorothalonil or mancozeb.",
            "prevention": "Rotate crops and avoid overhead irrigation."
        },
        "Potato___Late_blight": {
            "organic": "Use copper-based sprays frequently.",
            "chemical": "Apply fungicides like fluazinam.",
            "prevention": "Remove infected plants and avoid waterlogging."
        },
        "Potato___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Water at soil level and rotate annually."
        },
        "Pepper__bell___Bacterial_spot": {
            "organic": "Apply copper-based sprays weekly.",
            "chemical": "Use streptomycin sprays cautiously.",
            "prevention": "Use disease-free seeds and avoid water splash."
        },
        "Pepper__bell___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Ensure adequate spacing and sunlight."
        }
    }
    return recommendations.get(disease_name, {
    "organic": "No specific organic treatment found.",
    "chemical": "Consult local agricultural extension.",
    "prevention": "Maintain hygiene and rotate crops."
})
