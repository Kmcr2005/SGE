import re

with open("celestia.html", "r") as f:
    html = f.read()

# Update Paper Presentation
html = re.sub(
    r'(<h3[^>]*>Paper Presentation</h3>\s*<p[^>]*>.*?Prize Pool: ₹2,000<br>\s*Date: 13 October 2026\s*)(</p>)',
    r'\1<br><strong>📍 Venue:</strong> Anna University, Chennai<br><br>📞 Sadhana (6381311492) | Srikavi (9363888060)\2',
    html,
    flags=re.DOTALL
)

# Update Poster Presentation
html = re.sub(
    r'(<h3[^>]*>Poster Presentation</h3>\s*<p[^>]*>.*?Last Date: 12\.10\.2026<br>\s*Venue: Flood Lab, IRS\s*)(</p>)',
    r'\1<br><br>📞 Sariga Sri (93442 17237) | Mahalakshmi (76049 23610)\2',
    html,
    flags=re.DOTALL
)

# Fix pixel hunters organizer names to include numbers if they exist?
# Actually, Pixel Hunters text: "Naveena Nava Bharathi P T, Suvetha K, Susmitha V" (No numbers in the docx text)

with open("celestia.html", "w") as f:
    f.write(html)
