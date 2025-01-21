import requests

def fetch_section_data(section_id):
    try:
        # Send GET request to the API
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{section_id}/')
        
        # Check if the response status code is 200 (OK)
        if response.status_code != 200:
            raise Exception(f"HTTP Error! Status Code: {response.status_code}")
        
        # Convert the JSON response to a Python dictionary
        data = response.json()
        
        # Return the dictionary
        return data
    except Exception as e:
        print(f"Error fetching section data: {e}")
        return None

# Fetch data for a specific section (e.g., section 1)
section_id = 2
section_data = fetch_section_data(section_id)

if section_data:
    # Cool stuff you can do with the Python dictionary
    print("Section Title:", section_data["title"])
    print("Section Body:", section_data["body"])
    
    # Example: Count the number of words in the body
    word_count = len(section_data["body"].split())
    print("Word Count in Section Body:", word_count)
