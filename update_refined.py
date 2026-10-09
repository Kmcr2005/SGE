import re

with open("celestia.html", "r") as f:
    html = f.read()

# Replace GEO REWIND
html = re.sub(
    r'(<h3[^>]*>1\. GEO REWIND: THEN VS NOW</h3>\s*<p[^>]*>).*?(</p>\s*<a)',
    r'\1Step into the past, compare it with the present, and uncover how places have evolved.<br><br><strong>📍 Spot the change. Capture the journey.</strong><br><br><strong>Deadline:</strong> 10 October\2',
    html,
    flags=re.DOTALL
)

# Replace TAMIL
html = re.sub(
    r'(<h3[^>]*>2\. THE CLUES ARE OUT \(தமிழ்க்களம்\)</h3>\s*<p[^>]*>).*?(</p>\s*<p[^>]*>On-spot Registration)',
    r'\1See the clues, connect the dots, and uncover what’s hidden! An exciting clue-solving challenge.<br><br><strong>📍 Venue:</strong> Institute of Remote Sensing (IRS)<br><strong>📅 Date:</strong> 14 October 2026<br><strong>⏰ Time:</strong> 10:30 AM – 11:30 AM\2',
    html,
    flags=re.DOTALL
)

# Replace GEO PIN
html = re.sub(
    r'(<h3[^>]*>3\. GEO PIN</h3>\s*<p[^>]*>).*?(</p>\s*<p[^>]*>On-spot Registration)',
    r'\1Think you can decode the world from just a clue? Test your geospatial knowledge!<br><br><strong>📍 Venue:</strong> Institute of Remote Sensing (IRS)<br><strong>📅 Date:</strong> 14 October 2026<br><strong>⏰ Time:</strong> 9:00 AM – 10:30 AM<br><br>📞 Afzal (7603821053) | Martin (9345826698)\2',
    html,
    flags=re.DOTALL
)

# Replace MYSTERY MAP
html = re.sub(
    r'(<h3[^>]*>4\. MYSTERY MAP</h3>\s*<p[^>]*>).*?(</p>\s*<a)',
    r'\1Decode the clues, navigate the mystery, and conquer the map! Put your geospatial skills and teamwork to the test.<br><br><strong>👥 Team:</strong> 2–3 participants.<br><br>📞 Anusree (9962292616) | Varsha (7904145845)\2',
    html,
    flags=re.DOTALL
)

# Replace SLARS
html = re.sub(
    r'(<h3[^>]*>5\. SLARS 2\.0</h3>\s*<p[^>]*>).*?(</p>\s*<p[^>]*>On-spot Registration)',
    r'\1Put your skills, creativity and space knowledge to the test and compete for exciting cash prizes!<br><br><strong>📍 Venue:</strong> Institute of Remote Sensing (IRS)<br><strong>📅 Date:</strong> 14 October 2026<br><strong>⏰ Time:</strong> 10:30 AM – 11:30 AM<br><br>📞 Anupriya (6385817371) | Srinithy (8248921747)\2',
    html,
    flags=re.DOTALL
)

# Replace RS RUSH
html = re.sub(
    r'(<h3[^>]*>6\. RS RUSH</h3>\s*<p[^>]*>).*?(</p>\s*<p[^>]*>On-spot Registration)',
    r'\1How fast can you decode Remote Sensing? Test your skills, speed, and geospatial knowledge!<br><br><strong>📍 Venue:</strong> Institute of Remote Sensing (IRS)<br><strong>📅 Date:</strong> 13 October 2026<br><strong>⏰ Time:</strong> 3:30 PM – 5:30 PM<br><br>📞 Preyadarshini (9600165207) | Jayalakshmi (6374429756)\2',
    html,
    flags=re.DOTALL
)

# Replace GEO CONNECTIONS
html = re.sub(
    r'(<h3[^>]*>7\. GEO CONNECTIONS</h3>\s*<p[^>]*>).*?(</p>\s*<p[^>]*>On-spot Registration)',
    r'\1A thrilling Link & Match challenge where every clue leads you closer to the answer!<br><br><strong>📍 Venue:</strong> Institute of Remote Sensing (IRS)<br><strong>📅 Date:</strong> 14 October 2026<br><strong>⏰ Time:</strong> 11:30 AM – 12:30 PM<br><br>📞 Shantha (8610763732) | Kaviyarasan (9790270438)\2',
    html,
    flags=re.DOTALL
)

# Replace PIXEL HUNTERS
html = re.sub(
    r'(<h3[^>]*>8\. PIXEL HUNTERS</h3>\s*<p[^>]*>).*?(</p>\s*<p[^>]*>On-spot Registration)',
    r'\1The FCC Interpretation Challenge. Decode. Digitize. Dominate.<br><br><strong>📍 Venue:</strong> GIS Lab, IRS<br><strong>📅 Date:</strong> 13 October 2026<br><strong>⏰ Time:</strong> 3:30 PM – 5:30 PM<br><br>👥 Naveena | Suvetha | Susmitha\2',
    html,
    flags=re.DOTALL
)

# Refine Sports
html = re.sub(
    r'(<h3[^>]*>Badminton Tournament</h3>\s*<p[^>]*>).*?(</p>\s*<a)',
    r'\1<strong>Smash into Celestia\'26!</strong> 🏸<br><br>Boys & Girls – Doubles<br>Win exciting cash prizes and certificates!<br><strong>💸 Entry fee:</strong> ₹50<br><br>📞 Dhinesh (9600209318) | Sanjana (9629349611)\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h3[^>]*>Kabaddi Tournament</h3>\s*<p[^>]*>).*?(</p>\s*<a)',
    r'\1<strong>Kabaddi Kabaddi Kabaddi!</strong> 🔥<br><br>Open to boys from CEG, MIT, ACT & SAP<br><strong>📅 Date:</strong> Oct 09 & 10<br><strong>📍 Venue:</strong> CEG Ground<br><strong>💸 Entry fee:</strong> ₹100 per team<br><br>📞 Kalai (9677789964) | Hari (9360214693)\2',
    html,
    flags=re.DOTALL
)


with open("celestia.html", "w") as f:
    f.write(html)

