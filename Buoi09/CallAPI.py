import requests
import json

api_end_point = "https://dummyjson.com/products"

req = requests.get(api_end_point)
if req.status_code == 200: # Success
    result = req.json()
    print(json.dumps(result, indent=4))
    
    # Muốn lưu mảng product xuống file products.json
    # Mỗi product chỉ lấy id, title, price, thumbnail
    my_data = []
    for prod in result["products"]:
        my_data.append({
            "id": prod["id"],
            "name": prod["title"],
            "price": prod["price"],
            "image": prod["thumbnail"]
        })
    with open("products.json", "w", encoding="utf8") as my_file:
        json.dump(my_data, my_file, indent=4)
        