import requests
import os
import re
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
# Hardcoded NASA APOD API key (replace with your actual key)
NASA_API_KEY = os.getenv('NASA_API_KEY')
 
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

def fetch_image(query=None):
    """
    Fetches an image from NASA APOD and saves it with a query-based filename.
    Returns the file path of the downloaded image.
    """
    # Use the current date if no query is provided or if the query is not a valid date
    try:
        date = datetime.strptime(query, '%Y-%m-%d').strftime('%Y-%m-%d') if query else datetime.now().strftime('%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Using the current date instead.")
        date = datetime.now().strftime('%Y-%m-%d')
    
    params = {
        'api_key': NASA_API_KEY,
        'date': date
    }
    try:
        response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'url' in data:
            image_url = data['url']
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            
            # Generate a meaningful filename
            filename = get_next_filename(date)
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