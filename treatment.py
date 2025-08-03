def get_recommendations(disease_name):
    recommendations = {
        "Apple___Apple_scab": {
            "organic": "Apply compost tea or neem oil. Remove infected leaves.",
            "chemical": "Use fungicides with captan or mancozeb.",
            "prevention": "Prune tree regularly and ensure good air circulation."
        },
        "Apple___Black_rot": {
            "organic": "Spray copper-based fungicides and remove cankers.",
            "chemical": "Use fungicides like thiophanate-methyl.",
            "prevention": "Avoid overhead watering and sanitize pruning tools."
        },
        "Apple___Cedar_apple_rust": {
            "organic": "Apply sulfur or copper sprays during early season.",
            "chemical": "Use myclobutanil or propiconazole-based sprays.",
            "prevention": "Remove nearby juniper trees to reduce spores."
        },
        "Apple___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Maintain good watering, spacing, and pruning."
        },
        "Blueberry___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Ensure acidic soil and regular fertilization."
        },
        "Cherry_(including_sour)___Powdery_mildew": {
            "organic": "Apply neem oil or potassium bicarbonate spray.",
            "chemical": "Use sulfur-based fungicides.",
            "prevention": "Prune for airflow and avoid overhead watering."
        },
        "Cherry_(including_sour)___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Regular monitoring and pruning."
        },
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
            "organic": "Use compost teas or rotate crops.",
            "chemical": "Apply fungicides like azoxystrobin or propiconazole.",
            "prevention": "Avoid dense planting and use resistant hybrids."
        },
        "Corn_(maize)___Common_rust_": {
            "organic": "Use baking soda spray weekly.",
            "chemical": "Apply fungicides like mancozeb or chlorothalonil.",
            "prevention": "Use rust-resistant varieties and rotate crops."
        },
        "Corn_(maize)___Northern_Leaf_Blight": {
            "organic": "Neem oil and garlic extract sprays are effective.",
            "chemical": "Use fungicides containing propiconazole.",
            "prevention": "Remove crop debris and rotate corn with legumes."
        },
        "Corn_(maize)___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Ensure good field drainage and fertilization."
        },
        "Grape___Black_rot": {
            "organic": "Use sulfur dust or neem oil regularly.",
            "chemical": "Apply myclobutanil or mancozeb.",
            "prevention": "Prune infected parts and control weeds."
        },
        "Grape___Esca_(Black_Measles)": {
            "organic": "Remove affected parts and apply compost tea.",
            "chemical": "No cure, but foliar fungicides can suppress symptoms.",
            "prevention": "Avoid vine injuries and disinfect tools."
        },
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
            "organic": "Use copper or sulfur sprays.",
            "chemical": "Apply chlorothalonil or mancozeb.",
            "prevention": "Avoid overcrowding and increase airflow."
        },
        "Grape___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Regular maintenance and pruning."
        },
        "Orange___Haunglongbing_(Citrus_greening)": {
            "organic": "Remove and destroy infected trees.",
            "chemical": "No effective chemical cure.",
            "prevention": "Control psyllid insects and use disease-free stock."
        },
        "Peach___Bacterial_spot": {
            "organic": "Use Bordeaux mixture or neem oil.",
            "chemical": "Copper-based bactericides help reduce spread.",
            "prevention": "Avoid overhead watering and plant resistant varieties."
        },
        "Peach___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Mulch and prune for disease-free growth."
        },
        "Pepper,_bell___Bacterial_spot": {
            "organic": "Apply copper-based sprays weekly.",
            "chemical": "Use streptomycin sprays cautiously.",
            "prevention": "Use disease-free seeds and avoid water splash."
        },
        "Pepper,_bell___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Ensure adequate spacing and sunlight."
        },
        "Potato Early blight": {
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
        "Raspberry___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Ensure good airflow and soil drainage."
        },
        "Soybean___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Use certified seeds and rotate crops."
        },
        "Squash___Powdery_mildew": {
            "organic": "Spray with potassium bicarbonate or milk spray.",
            "chemical": "Apply sulfur-based fungicides weekly.",
            "prevention": "Grow resistant varieties and prune excess leaves."
        },
        "Strawberry___Leaf_scorch": {
            "organic": "Use compost tea or garlic spray.",
            "chemical": "Apply myclobutanil or azoxystrobin.",
            "prevention": "Avoid overcrowding and wet foliage."
        },
        "Strawberry___healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Water at the base and remove old leaves."
        },
        "Tomato___Bacterial_spot": {
            "organic": "Use copper sprays and remove infected plants.",
            "chemical": "Apply streptomycin in early stages.",
            "prevention": "Avoid splashing water and rotate crops."
        },
        "Tomato___Early_blight": {
            "organic": "Neem oil and compost teas help.",
            "chemical": "Use chlorothalonil or mancozeb.",
            "prevention": "Prune lower leaves and avoid wet foliage."
        },
        "Tomato___Late_blight": {
            "organic": "Copper fungicides and good airflow are key.",
            "chemical": "Use fluazinam-based fungicides.",
            "prevention": "Destroy infected plants and avoid high humidity."
        },
        "Tomato___Leaf_Mold": {
            "organic": "Apply baking soda or potassium bicarbonate spray.",
            "chemical": "Use fungicides like chlorothalonil.",
            "prevention": "Improve air circulation and reduce leaf wetness."
        },
        "Tomato___Septoria_leaf_spot": {
            "organic": "Neem oil or compost tea is helpful.",
            "chemical": "Use fungicides containing mancozeb or chlorothalonil.",
            "prevention": "Mulch and avoid overhead watering."
        },
        "Tomato___Spider_mites Two-spotted_spider_mite": {
            "organic": "Spray with neem oil or insecticidal soap.",
            "chemical": "Use miticides such as abamectin.",
            "prevention": "Keep humidity high and remove infected leaves."
        },
        "Tomato___Target_Spot": {
            "organic": "Use compost tea and remove affected leaves.",
            "chemical": "Apply fungicides like azoxystrobin.",
            "prevention": "Space plants properly and avoid overhead watering."
        },
        "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
            "organic": "Remove infected plants. Use reflective mulches.",
            "chemical": "No cure, control whiteflies using insecticides.",
            "prevention": "Grow resistant varieties and control insect vectors."
        },
        "Tomato___Tomato_mosaic_virus": {
            "organic": "Remove infected plants. Clean tools.",
            "chemical": "No effective chemicals available.",
            "prevention": "Avoid tobacco use during handling and sanitize equipment."
        },
        "Tomato healthy": {
            "organic": "No treatment needed.",
            "chemical": "No treatment needed.",
            "prevention": "Monitor regularly and maintain hygiene."
        }
    }
    return recommendations.get(disease_name, {
        "organic": "No specific organic treatment found.",
        "chemical": "Consult local agricultural extension.",
        "prevention": "Maintain hygiene and rotate crops."
    })
