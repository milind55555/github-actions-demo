import os

api_key = os.getenv("API_KEY")

print("API Key Loaded:", api_key is not None)

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Addition:", add(5, 3))
