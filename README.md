# MiniPress

## Overview

**MiniPress** is a minimalistic, Flask-powered blog template. It reads your posts directly from Markdown files - no database or admin panels required.

## Installation

1. Clone the repo
```sh
git clone https://github.com/w1ldb1t/MiniPress.git
cd MiniPress
```
2. Install dependencies
```sh
pip install -r requirements.txt
```
3. Override Pygments CSS (Optional)
```sh
pygmentize -S THEME_NAME -f html > static/pygments.css
```
4. Run the app
```
flask run
```

## Project Structure
```
MiniPress/
├── app.py            # Main Flask app
├── posts/
│   └── example.md    # Sample post file
├── static/
│   ├── style.css     # Custom site styles
│   └── pygments.css  # Syntax highlighting theme
├── templates/
│   ├── index.html    # Homepage template
│   ├── post.html     # Single-post template
│   └── about.html    # About page template
└── requirements.txt  # Python dependencies
```

## Writing Posts

Each post markdown file should:
1. Start with a level-1 heading for the title:
```
# The post title
```
2. Follow with a date on the next line (ISO format):
```
2025-04-21
```
3. Add a blank line, then your content in Markdown
```
Hello, world! *This* is my first **post**.
```
