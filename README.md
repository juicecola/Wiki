Wiki Encyclopedia Project Readme
Background
This project involves creating a Wikipedia-like online encyclopedia using Django, a web framework for Python. The encyclopedia entries are written in Markdown, a lightweight markup language. The goal is to build a web application that allows users to view, search, create, edit, and explore encyclopedia entries.

Getting Started
Download the distribution code from wiki.zip.
Unzip the downloaded file.
Review the existing code and project structure.
Project Structure
encyclopedia: Django app containing the core functionality.
urls.py: Defines URL patterns for the app.
util.py: Contains utility functions for managing encyclopedia entries.
views.py: Defines views for rendering pages.
templates/encyclopedia: Contains HTML templates.
entries: Directory where Markdown files representing encyclopedia entries are stored.
python-markdown2: External library for converting Markdown to HTML.
Specifications
Entry Page
Visiting /wiki/TITLE should render a page displaying the contents of the encyclopedia entry.
If the entry does not exist, show an error page.
Index Page
Update index.html to allow users to click on entry names to go directly to the entry page.
Search
Allow users to search for encyclopedia entries.
Redirect users to the entry page if there's an exact match.
Display a search results page with entries containing the query as a substring.
New Page
Clicking "Create New Page" should take the user to a page for creating a new entry.
Users can enter a title and Markdown content.
Prevent saving if an entry with the same title already exists.
Save the new entry and redirect to its page.
Edit Page
Each entry page should have a link to edit the content.
Users can edit the Markdown content in a textarea.
Save changes and redirect back to the entry page.
Random Page
Clicking "Random Page" should take the user to a random entry.
Markdown to HTML Conversion
Convert Markdown content to HTML using the python-markdown2 package.
Hints
Use Django templates and the safe filter for rendering HTML content.
Explore Django's URL patterns, views, and templates for efficient page rendering.
To install the python-markdown2 package, use pip3 install markdown2.
Optionally, try implementing the Markdown to HTML conversion without external libraries, using regular expressions

Acknowledgments
This project is part of the CS50 Web Programming with Python and JavaScript course at Harvard University.
