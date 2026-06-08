import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

URLS = [
    "http://www.bobsteeger.com/",
    "http://www.bobsteeger.com/p/blog-page.html",
    "http://www.bobsteeger.com/2026/03/un-named-bob-steeger-2-1-2026-03.html"
]

BASE_DIR = "live"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def save_file(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    
    local_filename = os.path.basename(urlparse(url).path)
    if not local_filename or local_filename.endswith('/'):
        local_filename = "index.html"
    
    # Ensure html extension
    if folder == BASE_DIR and not local_filename.endswith('.html'):
        local_filename += ".html"
        
    path = os.path.join(folder, local_filename)
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(path, 'wb') as f:
            f.write(response.content)
        return path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def download_asset(url, base_folder):
    parsed = urlparse(url)
    # Determine type
    ext = os.path.splitext(parsed.path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico']:
        subfolder = "images"
    elif ext == '.css':
        subfolder = "css"
    elif ext == '.js':
        subfolder = "js"
    else:
        subfolder = "other"
    
    target_folder = os.path.join(ASSETS_DIR, subfolder)
    os.makedirs(target_folder, exist_ok=True)
    
    filename = os.path.basename(parsed.path)
    if not filename:
        filename = "asset_" + re.sub(r'\W+', '_', url)[-20:]
    
    target_path = os.path.join(target_folder, filename)
    
    try:
        print(f"Downloading asset: {url}")
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        with open(target_path, 'wb') as f:
            f.write(res.content)
        return os.path.join("assets", subfolder, filename)
    except Exception as e:
        print(f"Error downloading asset {url}: {e}")
        return None

def process_page(url):
    print(f"Processing page: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Determine local filename
        parsed = urlparse(url)
        local_name = os.path.basename(parsed.path)
        if not local_name or local_name == "":
            local_name = "index.html"
        if not local_name.endswith('.html'):
            local_name += ".html"
            
        # Assets mapping
        asset_tags = {
            'img': 'src',
            'link': 'href',
            'script': 'src'
        }
        
        for tag, attr in asset_tags.items():
            for element in soup.find_all(tag, **{attr: True}):
                asset_url = element[attr]
                # Filter out external links we don't want to localize (like fonts or analytics if we prefer)
                if asset_url.startswith(('http', '//')):
                    full_url = urljoin(url, asset_url)
                    if '//' in asset_url and not asset_url.startswith('http'):
                        full_url = 'https:' + asset_url
                    
                    # Localize if it's from Blogger or related CDNs
                    if any(domain in full_url for domain in ['blogger.com', 'blogblog.com', 'googleusercontent.com', 'bp.blogspot.com']):
                        local_path = download_asset(full_url, ASSETS_DIR)
                        if local_path:
                            element[attr] = local_path
                else:
                    # Already relative or local-ish, potentially need to download too
                    full_url = urljoin(url, asset_url)
                    local_path = download_asset(full_url, ASSETS_DIR)
                    if local_path:
                        element[attr] = local_path

        # Save processed HTML
        os.makedirs(BASE_DIR, exist_ok=True)
        with open(os.path.join(BASE_DIR, local_name), 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
            
    except Exception as e:
        print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    for url in URLS:
        process_page(url)
    print("Scrape complete.")
