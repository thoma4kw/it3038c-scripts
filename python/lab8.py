pip install googlesearch-python

from googlesearch import search

# Define the search query
query = "NFL scores"

# Perform the Google search and extract search results
search_results = search(query, num=10, stop=10, pause=2.0)

# Search results and print them
for result in search_results:
    print(result)
