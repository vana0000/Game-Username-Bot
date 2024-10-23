import requests
from UsernameLogic import api_urls
from requests.exceptions import ConnectionError as cnerr
from urllib3.exceptions import NameResolutionError

def get_player_by_ign(ign: str = None):
    """Check if an IGN exists and return a message indicating availability."""
    headers = {
        "content-type": "application/json",
    }
    
    try:
        # Send the request to the API with the username (IGN)
        response = requests.get(url=f"{api_urls.username_api_uri}{ign}", headers=headers)
        
        # If the request is successful (status code 200), the username is taken
        if response.status_code == 200:
            return f"❌ Username '{ign}' is already taken."

        # If the server returns a 500 error, assume the profile does not exist, so the username is available
        elif response.status_code == 500:
            return f"✅ Username '{ign}' is available."

        # Handle other response errors with their status codes
        else:
            return f"⚠️ Error: {response.status_code}. Unable to check username '{ign}'."
    
    # Handle network issues and other common errors gracefully
    except cnerr:
        return "❌ Network error occurred. Please check your connection."
    except NameResolutionError:
        return "❌ Failed to resolve the API URL."
    except Exception as e:
        return f"❌ An unexpected error occurred: {e}"
