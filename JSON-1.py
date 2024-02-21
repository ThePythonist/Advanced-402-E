import json

data = {
    "url": "https://www.youtube.com/watch?v=UmljXZIypDc",
    "title": "django tutorial part 1",
    "date": "1397",
    "comments": True,
    "list_of_comments": [
        {
            "shahla": "awesome!",
        },
        {
            "rajab": "keep it up",
        }
    ],
    "suggestions": ["flask tutorial", "fastapi tutorial"],
    "likes": None,
}

# Serialize

# json_data = json.dumps(data, indent=4) # Converts python data into json string
# print(json_data)

file = open("data.json", "w")  # Converts python data into json file
json.dump(data, file, indent=4)
