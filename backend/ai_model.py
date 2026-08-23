def predict_price(crop_name, rainfall):
    # Simple AI Logic for demo
    base_price = {"Paddy": 2300, "Coconut": 3500, "Banana": 1800}
    price = base_price.get(crop_name, 2000)
    if rainfall > 500:
        price += 300
    return {"crop": crop_name, "predicted_price": price, "advice": "Sell after 2 weeks"}