import re

with open("celestia.html", "r") as f:
    html = f.read()

# Dictionary of event titles to image filenames
event_images = {
    "1. GEO REWIND": "geo_rewind.jpeg",
    "2. THE CLUES ARE OUT": "tamil.jpeg",
    "3. GEO PIN": "GeoPin.jpeg",
    "4. MYSTERY MAP": "MysteryMap.jpeg",
    "5. SLARS 2.0": "SLARS2.jpeg",
    "6. RS RUSH": "RS_Rush.jpeg",
    "7. GEO CONNECTIONS": "GeoConnections.jpeg",
    "8. PIXEL HUNTERS": "PixelHunters.jpeg",
}

for key, filename in event_images.items():
    # Find the h3 tag for the event
    pattern = r'(<div style="[^"]*background: white;[^"]*border-radius: 8px;[^"]*padding: 1\.5rem;[^"]*box-shadow:[^"]*">)(\s*)(<h3[^>]*>' + re.escape(key) + r'.*?</h3>)'
    replacement = r'\1\2<img src="static/images/celestia events/' + filename + r'" alt="' + key + r'" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 1rem;">\2\3'
    html = re.sub(pattern, replacement, html)

# Paper and Poster
html = re.sub(
    r'(<h3[^>]*>Paper Presentation</h3>)',
    r'<img src="static/images/celestia events/Paper.jpeg" alt="Paper Presentation" style="width: 100%; height: 250px; object-fit: cover; border-radius: 4px; margin-bottom: 1rem;">\n          \1',
    html
)
html = re.sub(
    r'(<h3[^>]*>Poster Presentation</h3>)',
    r'<img src="static/images/celestia events/Poster.jpeg" alt="Poster Presentation" style="width: 100%; height: 250px; object-fit: cover; border-radius: 4px; margin-bottom: 1rem;">\n          \1',
    html
)

# Sports
html = re.sub(
    r'(<h3[^>]*>Badminton Tournament</h3>)',
    r'<img src="static/images/celestia events/Badminton.jpeg" alt="Badminton Tournament" style="width: 100%; height: 250px; object-fit: cover; border-radius: 4px; margin-bottom: 1rem;">\n          \1',
    html
)
html = re.sub(
    r'(<h3[^>]*>Kabaddi Tournament</h3>)',
    r'<img src="static/images/celestia events/Kabaddi.jpeg" alt="Kabaddi Tournament" style="width: 100%; height: 250px; object-fit: cover; border-radius: 4px; margin-bottom: 1rem;">\n          \1',
    html
)

with open("celestia.html", "w") as f:
    f.write(html)

