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
        "code": "01",
        "name": "GEOHORIZON",
        "tagline": "GEOVERSE: Connecting Data, Intelligence and Innovation",
        "meta": "Inter-college technical symposium · March 14–16, 2026",
        "text": (
            "GEOHORIZON is a key event organised by the Society of Geoinformatics Engineers "
            "(SGE), part of the Institute of Remote Sensing, College of Engineering Guindy, "
            "Anna University. This event provides an exciting platform for students to engage "
            "with the growing and diverse areas of Geoinformatics, Remote Sensing, GIS, Earth "
            "Observation, and related technologies. Through a mix of technical activities, "
            "workshops, competitions, expert talks, and knowledge-sharing sessions, GEOHORIZON "
            "helps students refine their technical skills, exchange ideas, and discover new "
            "applications of geospatial technologies."
        ),
        "facts": [
            "20+ tech & non-tech events",
            "₹120,000 prize pool",
            "Open to all colleges in India"
        ],
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
                "caption": "GEOHORIZON audience"
            },
        ],
    },

    {
        "code": "02",
        "name": "CELESTIA",
        "tagline": "Where space science meets geospatial technology",
        "meta": "Held alongside National Space Week · October 14–15",
        "text": (
            "CELESTIA is a student-focused event organised by the Society of Geoinformatics "
            "Engineers (SGE), bringing together the exciting fields of space science, Earth "
            "observation, Remote Sensing, and Geospatial Technology. The event seeks to raise "
            "awareness and spark interest among students about the role of space and satellite "
            "technologies in solving real-world problems. Through technical sessions, expert "
            "discussions, competitions, and engaging activities, CELESTIA allows students to "
            "learn, collaborate, and explore new possibilities in the space and geospatial "
            "sectors."
        ),
        "facts": [
            "Technical sessions & expert talks",
            "Student competitions",
            "Run with National Space Week"
        ],
        "images": [
            {
                "src": "celestia_1.jpg",
                "caption": "CELESTIA event"
            },
            {
                "src": "celestia_2.jpeg",
                "caption": "CELESTIA technical session"
            },
            {
                "src": "celestia_3.jpg",
                "caption": "CELESTIA programme"
            },
        ],
    },

    {
        "code": "03",
        "name": "SPACE WEEK",
        "tagline": "An outreach programme for the next generation",
        "meta": "Campus & school outreach initiative",
        "text": (
            "SPACE WEEK is an outreach program designed to raise awareness and inspire "
            "enthusiasm for space science, satellite technology, Earth observation, and their "
            "various geospatial applications. This initiative gives students the chance to "
            "understand the importance of space technology in fields such as environmental "
            "monitoring, disaster management, agriculture, urban planning, climate studies, and "
            "navigation."
        ),
        "facts": [
            "ISRO 'Space on Wheels' exhibition bus",
            "School outreach sessions",
            "Hands-on ISRO exhibits"
        ],
        "images": [
            {
                "src": "spaceweek_1.jpeg",
                "caption": "ISRO Space on Wheels exhibition bus"
            },
            {
                "src": "spaceweek_2.jpeg",
                "caption": "ISRO launch vehicle models"
            },
            {
                "src": "spaceweek_3.jpg",
                "caption": "Space Week outreach programme"
            },
        ],
    },
]

GALLERY = [
    {"src": "geohorizon_2.jpeg", "caption": "GEOHORIZON inaugural session"},
    {"src": "celestia_2.jpeg", "caption": "CELESTIA technical session"},
    {"src": "spaceweek_1.jpeg", "caption": "Space on Wheels exhibition bus"},
    {"src": "spaceweek_3.jpg", "caption": "ISRO launch vehicle models"},
    {"src": "spaceweek_expert.jpeg", "caption": "Expert interaction with school students"},
    {"src": "spaceweek_students.jpeg", "caption": "School students at Space Week outreach"},
    {"src": "irs_building.jpeg", "caption": "Institute of Remote Sensing, CEG"},
    {"src": "trimble_meet.jpg", "caption": "Trimble Team Meet"},
    {"src": "SGE_inaugration.jpg", "caption": "SGE Inaugration 2025"},
    {"src": "mapjam.jpg", "caption": "Mapjam Event - GeoHorizon'26"},
    {"src": "lifeskill_workshop.jpg", "caption": "Lifeskill Workshop - GeoHorizon'26"},
    {"src": "ideathon.jpg", "caption": "Ideathon Event - GeoHorizon'26"},
    {"src": "healthGIS_workshop.jpg", "caption": "HealthGIS Workshop"},
    {"src": "geonex.jpg", "caption": "GeoNex Hackathon - GeoHorizon'26"},
    {"src": "geonex_panel.jpg", "caption": "GeoNex Hackathon Judges"},
    {"src": "celestia_event.jpg", "caption": "Celestia'25 events session"}
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
