# Create a script that lets the user type in a search term and open and search on the browser for that term on Google

import webbrowser
query = input("Enter the search : ")
webbrowser.open(f"https://www.google.com/search?q={query}")