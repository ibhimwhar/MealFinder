import requests

# Ask the user for a meal name to search
query = input("Enter a meal to search: ")

# Build the URL with the user's input
url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"

# Make the API request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    meals = data.get("meals")

    if meals:
        for meal in meals:
            print("\n Meal:", meal["strMeal"])
            print("\nInstructions:")
            print(meal["strInstructions"])
            print("\nImage:", meal["strMealThumb"])
    else:
        print("\nNo meals found for:", query)
else:
    print("Failed to fetch data. Status code:", response.status_code)
