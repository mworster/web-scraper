🕸️ Python Web Scraper with Virtual Environment
This project demonstrates how to set up and run a simple Python web scraper inside a virtual environment. It includes setup instructions, package management, and an overview of the scraper's design and behavior.

🧰 Environment Setup Instructions
🔹 1. Create a Virtual Environment
Run the following from your project directory:

Linux/macOS:

    python3 -m venv .venv
    source .venv/bin/activate

Windows:

    python -m venv .venv
    .venv\Scripts\activate

This creates a .venv/ folder containing an isolated Python environment.

🔹 2. Install Packages
Inside the virtual environment, install your dependencies using pip:

    pip install requests beautifulsoup4

🔹 3. Save the Installed Packages
To save the exact versions of all installed packages:

    pip freeze > requirements.txt
    
This creates a requirements.txt file which allows others (or future you) to recreate the environment.

🔹 4. Recreate the Environment Later
Any time you want to start fresh (on another machine, or after deleting .venv):

    python3 -m venv .venv
    source .venv/bin/activate  # or .venv\Scripts\activate on Windows
    pip install -r requirements.txt

🔹 5. Deactivate the Virtual Environment
When you're done working:

    deactivate

Web Scraper Overview
📌 Goal
Build a Python script that scrapes the front page of Hacker News to extract article titles and links, and save the output to a timestamped .json file.

📋 High-Level Requirements
Use only Python 3 and open-source packages

Run inside an isolated virtual environment

Use requests to fetch the HTML

Use BeautifulSoup to parse HTML

Extract title and URL of each story

Save the results as structured JSON

Name the output file with the current timestamp

⚙️ How It Works
The script sends a GET request to https://news.ycombinator.com/.

Parses the HTML response to find all story links ('span', class_='titleline').

Extracts each story’s title and URL.

Saves the list of stories in a results_YYYYMMDD_HHMMSS.json file.

🧾 Inputs
No command-line arguments or user inputs required.

Script scrapes the live Hacker News front page by default.

🧾 Outputs
A JSON file in the format:

    [
      {
        "title": "Example Story Title",
         "url": "https://example.com/story-link"
      },
      ...
    ]
    
File is saved as:

    results_20250625_230301.json

📂 Project Structure

    web-scraper/
    ├── scraper.py
    ├── requirements.txt
    ├── README.md
    └── .venv/               # created by you; not tracked in Git
