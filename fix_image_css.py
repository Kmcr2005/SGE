import re

with open("celestia.html", "r") as f:
    html = f.read()

# Fix events images
html = re.sub(r'height: 200px; object-fit: cover;', r'height: auto; object-fit: contain;', html)
# Fix paper/poster/sports images
html = re.sub(r'height: 250px; object-fit: cover;', r'height: auto; object-fit: contain;', html)

with open("celestia.html", "w") as f:
    f.write(html)

