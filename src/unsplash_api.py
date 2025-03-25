import requests
import os
import re

# Hardcoded Unsplash API key (replace with your actual key)

from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()
# Hardcoded NASA APOD API key (replace with your actual key)
# UNSPLASH_API_KEY = os.getenv('UNSPLASH_API_KEY')
UNSPLASH_API_KEY = "MvoLPu92DRz6Q2kf1bDsPF2Y7MgoXO5gACIH6PF0oRM"

 
def sanitize_query(query):
    """Sanitize the query to create a valid filename (e.g., 'sunset beach' -> 'sunset_beach')."""
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', query)  # Replace special characters with underscores
    return sanitized.lower().strip('_')

def get_next_filename(query, directory="wallpapers"):
    """Get the next available filename for a query (e.g., 'nature_1.jpg')."""
    sanitized = sanitize_query(query)
    os.makedirs(directory, exist_ok=True)
    existing_files = [f for f in os.listdir(directory) if f.startswith(sanitized)]
    
    # Extract the highest number from existing filenames
    max_num = 0
    for file in existing_files:
        match = re.match(rf"{sanitized}_(\d+)\.jpg", file)
        if match:
            num = int(match.group(1))
            max_num = max(max_num, num)
    
    # Increment the number for the new file
    new_num = max_num + 1
    return f"{directory}/{sanitized}_{new_num}.jpg"

def fetch_image(query, orientation="landscape", resolution=None):
    """
    Fetches an image from Unsplash and saves it with a query-based filename.
    Returns the file path of the downloaded image.
    """
    headers = {'Authorization': f'Client-ID {UNSPLASH_API_KEY}'}
    params = {
        'query': query,
        'orientation': orientation,
        'per_page': 1
    }
    try:
        response = requests.get('https://api.unsplash.com/search/photos', headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['results']:
            image_url = data['results'][0]['urls']['full']
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            
            # Generate a meaningful filename
            filename = get_next_filename(query)
            with open(filename, 'wb') as f:
                f.write(image_response.content)
            
            print(f"✅ Image saved at {filename}")
            return filename
        else:
            print("No images found for the query.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
        return None