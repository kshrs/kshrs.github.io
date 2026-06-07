#!/usr/bin/env python3
"""
Convert a Markdown blog post to HTML with syntax highlighting.
Usage: python md_to_html.py ./blogs_md/filename.md
Output: ./filename.html (same directory as the script)
"""

import sys
import os
import re
from datetime import datetime

try:
    import markdown
except ImportError:
    print("Error: markdown library not installed. Run: pip install markdown")
    sys.exit(1)

# Navigation template – relative to blogs/ directory
NAV_TEMPLATE = '''<nav class="nav-top">
    <a href="../index.html">~/home</a>
    <a href="./index.html" class="active">~/blogs</a>
    <a href="../assets/Kishor_S_Resume_General.pdf" target="_blank">~/resume.pdf</a>
</nav>'''

FOOTER_TEMPLATE = '''<div class="post-footer">
    <p>← <a href="./index.html">back to blog index</a> &nbsp;|&nbsp;
    <a href="../index.html">home</a> &nbsp;|&nbsp;
    <a href="mailto:kishorjsk2006@gmail.com">email</a></p>
</div>'''

def extract_title_and_date(md_content):
    """Extract title from first H1 and date from metadata line."""
    lines = md_content.split('\n')
    title = "Untitled"
    date = datetime.today().strftime("%Y-%m-%d")
    
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # Look for date: YYYY-MM-DD anywhere in the file
    date_match = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', md_content, re.MULTILINE | re.IGNORECASE)
    if date_match:
        date = date_match.group(1)
    
    return title, date

def generate_html(md_path):
    """Convert markdown file to HTML in current directory."""
    if not os.path.exists(md_path):
        print(f"Error: File not found: {md_path}")
        sys.exit(1)
    
    # Read markdown content
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract metadata
    title, post_date = extract_title_and_date(md_content)
    
    # Convert Markdown to HTML with syntax highlighting
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'codehilite',
        'tables',
        'nl2br'
    ])
    html_body = md.convert(md_content)
    
    # Get the base filename (without path and extension)
    base_name = os.path.basename(md_path)
    base_name = os.path.splitext(base_name)[0]
    
    # Output path: current working directory (blogs/) with .html extension
    out_path = os.path.join(os.getcwd(), base_name + '.html')
    
    # Generate final HTML
    output = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - Kishor S">
    <title>kshrs · {title}</title>
    <link rel="icon" type="image/png" sizes="32x32" href="../assets/moon.png">
    <link rel="stylesheet" href="./blogs.css">
    <link rel="stylesheet" href="./pygments.css">
</head>
<body>
    <div class="container">
        {NAV_TEMPLATE}
        <div class="blog-post">
            {html_body}
            {FOOTER_TEMPLATE}
        </div>
    </div>
</body>
</html>'''
    
    # Write the output file
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"   Generated: {out_path}")
    print(f"   Source: {md_path}")
    print(f"   Title: {title}")
    print(f"   Date: {post_date}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python md_to_html.py ./blogs_md/filename.md")
        print("Example: python md_to_html.py ./blogs_md/emacs-config-101.md")
        print("\nOutput will be saved as ./filename.html in current directory")
        sys.exit(1)
    
    md_path = sys.argv[1]
    generate_html(md_path)

if __name__ == "__main__":
    main()
