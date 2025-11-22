import requests

def main():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()

    if data.get("type") == "single":
        print("\nBlague :")
        print(data["joke"])
    else:
        print("\nBlague :")
        print(data["setup"])
        print(data["delivery"])

if __name__ == "__main__":
    main()
