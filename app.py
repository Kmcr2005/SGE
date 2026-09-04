import os

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Site content. Kept as plain data structures so the templates stay simple
# and the copy can be edited in one place without touching HTML.
# ---------------------------------------------------------------------------

SITE = {
    "org_short": "SGE",
    "org_name": "Society of Geoinformatics Engineers",
    "parent": "Institute of Remote Sensing, College of Engineering Guindy, Anna University",
    "coordinates": "13.0110\u00b0 N, 80.2354\u00b0 E",
    "location": "Chennai, Tamil Nadu",
}

NAV_LINKS = [
    ("About", "#about"),
    ("Vision & Mission", "#vision"),
    ("Leadership", "#leadership"),
    ("Events", "#events"),
    ("Gallery", "#gallery"),
    ("Sponsors", "#sponsors"),
    ("Alumni", "#alumni"),
]

ABOUT_TEXT = (
    "The Society of Geoinformatics Engineers (SGE), a student-led organisation under the "
    "Institute of Remote Sensing (IRS), College of Engineering Guindy, Anna University, was "
    "formed with the main aim of promoting knowledge, innovation, and professional growth in "
    "the field of Geoinformatics. As part of a leading institute in Remote Sensing and "
    "Geoinformatics education, SGE offers students a platform to explore and develop their "
    "expertise in Remote Sensing, Geographic Information Systems (GIS), Earth Observation, "
    "Surveying, and other emerging geospatial technologies. The association supports technical "
    "learning, research, teamwork, and industry engagement through various activities such as "
    "workshops, expert talks, competitions, and major events like GEOHORIZON and CELESTIA. "
    "Comprised of both students and faculty members, SGE works to connect academic learning "
    "with practical geospatial applications and help shape the future of geospatial "
    "professionals and innovators."
)

VISION_TEXT = (
    "Given that Geoinformatics is a rapidly advancing and influential field, SGE is committed "
    "to creating a forward-thinking environment that supports knowledge sharing, technical "
    "learning, and innovation for students and faculty. The association encourages students to "
    "explore different areas of Geoinformatics through technical sessions, workshops, expert "
    "discussions, and hands-on activities, building a learning culture that is student-driven "
    "and supported by faculty and industry experts. SGE also aims to bring together individuals "
    "from diverse backgrounds who share a passion for Geoinformatics, fostering collaboration, "
    "research, and technological progress while inspiring students to contribute to a smarter, "
    "more sustainable, and geospatially advanced society."
)

MISSION_TEXT = (
    "SGE aims to promote excellence in Geoinformatics by offering students opportunities to "
    "improve their technical knowledge, practical skills, and understanding of newer geospatial "
    "technologies. The association focuses on creating an interactive and collaborative "
    "environment through workshops, technical sessions, competitions, expert engagements, and "
    "various academic programs. It encourages students to get involved in research, innovation, "
    "and knowledge-sharing while connecting them with academicians, industry professionals, "
    "researchers, and other geospatial enthusiasts. These initiatives help bridge the gap "
    "between classroom learning and real-world geospatial applications, preparing students to "
    "tackle current challenges using geospatial technologies. SGE remains dedicated to building "
    "a community of skilled, creative, and socially responsible geospatial professionals who can "
    "make meaningful contributions to the geospatial community."
)

LEADERSHIP = [
    {
        "role": "Director's Note",
        "name": "Dr. R Vidhya",
        "designation": "Director & Professor, Institute of Remote Sensing",
        "image": "director.png",
        "note": (
            " 'The Society of Geoinformatics Engineers (SGE), established in 2004, has evolved into a "
            "vibrant platform for innovation, learning, collaboration, and professional exposure in "
            "Geoinformatics. As geospatial technologies continue to play an increasingly important"
            "role in national development and decision-making, SGE provides students with"
            "opportunities to learn, explore, and contribute to this dynamic field"
            "I encourage every student to dream big, embrace"
            "challenges, and pursue excellence with dedication, carrying forward SGE legacy of"
            "learning, innovation, and meaningful contribution to society.' "
        ),
    },
    {
        "role": "President's Note",
        "name": "Dr. Shanmugam",
        "designation": "President, SGE",
        "image": "president.jpeg",
        "note": (
            " 'SGE is a community driven by curiosity, collaboration and a passion "
            "for geospatial technology. Our aim is to create opportunities for "
            "students to learn beyond the classroom, exchange ideas and build "
            "solutions that connect technology with real-world challenges.' "
        ),
    },
    {
        "role": "Treasurer's Note",
        "name": "Dr. Navamunniyamal",
        "designation": "Treasurer, SGE",
        "image": "treasurer.jpeg",
        "note": (
            " 'Every successful initiative at SGE is made possible through the "
            "collective effort of our students, faculty, alumni and partners. "
            "We remain committed to supporting meaningful events and activities "
            "that contribute to the growth of the geospatial community.' "
        ),
    },
]



EVENTS = [
    {
        "title": "GEOHORIZON",
        "subtitle": "Inaugural Edition",
        "date": "2025",
        "description": "A flagship SGE event bringing together geospatial professionals, students, researchers and industry experts.",
        "images": [
            {
                "src": "geohorizon_1.jpg",
                "caption": "GEOHORIZON event"
            },
            {
                "src": "geohorizon_2.jpeg",
                "caption": "GEOHORIZON inaugural session"
            },
            {
                "src": "geohorizon_3.jpg",
                "caption": "GEOHORIZON"
            }
        ]
    },

    {
        "title": "CELESTIA",
        "subtitle": "Astronomy & Space Science",
        "date": "2025",
        "description": "An astronomy-focused event exploring space science, observation and the growing role of geospatial technologies.",
        "images": [
            {
                "src": "celestia_1.jpg",
                "caption": "CELESTIA"
            },
            {
                "src": "celestia_2.jpeg",
                "caption": "CELESTIA session"
            },
            {
                "src": "celestia_3.jpg",
                "caption": "CELESTIA event"
            }
        ]
    },

    {
        "title": "SPACE WEEK",
        "subtitle": "World Space Week",
        "date": "2025",
        "description": "A celebration of space science and exploration featuring educational activities, exhibits and outreach programmes.",
        "images": [
            {
                "src": "spaceweek_1.jpeg",
                "caption": "Space on Wheels"
            },
            {
                "src": "spaceweek_2.jpeg",
                "caption": "ISRO models"
            },
            {
                "src": "spaceweek_3.jpg",
                "caption": "Space Week"
            }
        ]
    }
]

GALLERY = [
    {"src": "geohorizon_inaugural.jpeg", "caption": "GEOHORIZON inaugural session"},
    {"src": "celestia_session.jpeg", "caption": "CELESTIA technical session"},
    {"src": "space_on_wheels.jpeg", "caption": "Space on Wheels exhibition bus"},
    {"src": "isro_models.jpeg", "caption": "ISRO launch vehicle models"},
    {"src": "spaceweek_expert.jpeg", "caption": "Expert interaction with school students"},
    {"src": "spaceweek_students.jpeg", "caption": "School students at Space Week outreach"},
    {"src": "irs_building.jpeg", "caption": "Institute of Remote Sensing, CEG"},
    {"src": "celestia_banner.jpeg", "caption": "CELESTIA '25, National Space Week"},
]

SPONSORS = [
    "SR Infra", "Cygnus Technical", "Hexamap Solutions", "Redplanet", "Alterra",
    "Gridline Surveys", "G. D. Chiplunkar", "Alphics Phonix", "TTDC", "Redconnect",
    "Utest Asia",
]

ALUMNI = [
    "Alumni 2003\u20132007 Batch",
    "Alumni \u2014 Hari",
    "Alumni 2016\u20132020",
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        site=SITE,
        nav_links=NAV_LINKS,
        about_text=ABOUT_TEXT,
        vision_text=VISION_TEXT,
        mission_text=MISSION_TEXT,
        leadership = LEADERSHIP,
        events=EVENTS,
        gallery=GALLERY,
        sponsors=SPONSORS,
        alumni=ALUMNI,
        year=2026,
    )


if __name__ == "__main__":
    # Render (and most PaaS hosts) inject the port to bind via $PORT.
    # Locally this falls back to 5001.
    port = int(os.environ.get("PORT", 5001))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(debug=debug, host="0.0.0.0", port=port)
