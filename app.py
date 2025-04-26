from flask import Flask, render_template, abort
from pathlib import Path
import markdown
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
POSTS_DIR = BASE_DIR / 'posts'

# Configure Markdown renderer once
MD = markdown.Markdown(
    extensions=['fenced_code', 'codehilite'],
    output_format='html5'
)

@dataclass
class Post:
    title: str
    date: str
    body: str
    excerpt: str
    slug: str


def parse_post(filepath: Path) -> Post:
    """Read a markdown file and return a Post object."""
    lines = filepath.read_text(encoding='utf-8').splitlines()
    title = lines[0].lstrip('#').strip()
    date = lines[1].strip()
    body_md = "\n".join(lines[2:])

    # Render HTML
    body_html = MD.reset().convert(body_md)

    # Create excerpt
    soup = BeautifulSoup(body_html, 'html.parser')
    text = soup.get_text()
    excerpt = text[:300] + ('...' if len(text) > 300 else '')

    slug = filepath.stem
    return Post(title=title, date=date, body=body_html, excerpt=excerpt, slug=slug)


def get_posts() -> List[Post]:
    """Return all posts sorted by date descending."""
    markdown_files = sorted(POSTS_DIR.glob('*.md'), reverse=True)
    posts = [parse_post(md_file) for md_file in markdown_files]
    return posts


@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)


@app.route('/post/<slug>')
def show_post(slug: str):
    filepath = POSTS_DIR / f"{slug}.md"
    if not filepath.exists():
        abort(404)
    post = parse_post(filepath)
    return render_template('post.html', post=post)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
