import re

with open("celestia.html", "r") as f:
    html = f.read()

# Update sLAYERS
html = re.sub(
    r'(<h3[^>]*>9\. sLAYERS</h3>\s*<p[^>]*>).*?(</p>\s*<p[^>]*>On-spot Registration)',
    r'\1Get ready to strategize, compete, and outbid your rivals!<br><br><strong>📍 Venue:</strong> Institute of Remote Sensing (IRS)<br><strong>📅 Date:</strong> 14 October 2026<br><strong>⏰ Time:</strong> 10:30 AM – 11:30 AM<br><br>📞 Monisha (9790803051) | Saai Sreenithi (8610106578)\2',
    html,
    flags=re.DOTALL
)

# Update Throw Ball
html = re.sub(
    r'(<h3[^>]*>Throw Ball Tournament</h3>\s*<p[^>]*>).*?(</p>\s*<p[^>]*>On-spot Registration)',
    r'\1<strong>Rule the court. Sync with your team.</strong> 🤾‍♀️<br><br>Girls Tournament<br><strong>💸 Entry fee:</strong> Free<br><br>📞 Bharathi (805921567) | Jeevitha (9629348240)</p>\n          <a href="https://docs.google.com/forms/d/e/1FAIpQLScvd8lYxPEWQf1pFnm5LB0rJviFWUr_OnS0pVQmoW2rY_6YLA/viewform?usp=publish-editor" target="_blank" class="btn btn--primary" style="margin-top: 1.5rem;">Register Now</a>\n        <!-- REMOVE_ME',
    html,
    flags=re.DOTALL
)

# Clean up the REMOVE_ME hack
html = html.replace('<!-- REMOVE_ME</p>\n          <p style="margin-top: 1rem; font-weight: bold; color: var(--brass-dim);">On-spot Registration</p>', '')

with open("celestia.html", "w") as f:
    f.write(html)
