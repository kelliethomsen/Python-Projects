import requests

# Define the search query
search_query = "Data Science"

# Formulate the URL for Google Scholar with the search query
url = f"https://scholar.google.com/scholar?q={search_query}"

# Make an HTTP request to fetch the page content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Store the HTML content of the page
    html_content = response.text

    print(html_content)
else:
    # Print an error message if the request fails
    print(f"Failed to fetch the page. Status code: {response.status_code}")