import re

with open("celestia.html", "r") as f:
    content = f.read()

# We will replace everything from <!-- Events Section --> to </main>
new_sections = """
  <!-- Events Section -->
  <section id="events" class="section section--paper">
    <div class="section__head" style="text-align: center; margin-bottom: 3rem;">
      <h2 class="section__title">Events</h2>
    </div>
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 3rem; padding: 0 1.5rem;">
      <img src="static/images/celestia_1.jpg" alt="Celestia Events" style="width: 100%; max-height: 400px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <div style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.3rem;">1. GEO REWIND: THEN VS NOW</h3>
          <p style="color: var(--ink-soft); font-size: 0.95rem; margin-top: 0.5rem;">Step into the past, compare it with the present, and uncover how places have evolved. Spot the Change.</p>
          <a href="https://docs.google.com/forms/d/e/1FAIpQLSdoAfGd2wz860o0cD42vVb4J5jPqtXTRzvqA0trmcKSuJ3IaQ/viewform" target="_blank" class="btn btn--primary" style="margin-top: 1rem; padding: 8px 16px; font-size: 0.9rem;">Register</a>
        </div>
        <div style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.3rem;">2. THE CLUES ARE OUT (தமிழ்க்களம்)</h3>
          <p style="color: var(--ink-soft); font-size: 0.95rem; margin-top: 0.5rem;">See the clues, connect the dots, and uncover what's hidden! (14 Oct, 10:30 AM)</p>
          <p style="margin-top: 1rem; font-weight: bold; color: var(--brass-dim);">On-spot Registration</p>
        </div>
        <div style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.3rem;">3. GEO PIN</h3>
          <p style="color: var(--ink-soft); font-size: 0.95rem; margin-top: 0.5rem;">Identify the location and test your geospatial knowledge! (14 Oct, 9:00 AM)</p>
          <p style="margin-top: 1rem; font-weight: bold; color: var(--brass-dim);">On-spot Registration</p>
        </div>
        <div style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.3rem;">4. MYSTERY MAP</h3>
          <p style="color: var(--ink-soft); font-size: 0.95rem; margin-top: 0.5rem;">Decode the clues, navigate the mystery, and conquer the map! Team of 2-3.</p>
          <a href="https://docs.google.com/forms/d/e/1FAIpQLSchHQwSL3J0fKvi-0VTnmSTJohBaDolXZXj2CFMNzU0rB2N5g/viewform" target="_blank" class="btn btn--primary" style="margin-top: 1rem; padding: 8px 16px; font-size: 0.9rem;">Register</a>
        </div>
        <div style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.3rem;">5. SLARS 2.0</h3>
          <p style="color: var(--ink-soft); font-size: 0.95rem; margin-top: 0.5rem;">Put your skills, creativity and space knowledge to the test. (14 Oct, 10:30 AM)</p>
          <p style="margin-top: 1rem; font-weight: bold; color: var(--brass-dim);">On-spot Registration</p>
        </div>
        <div style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.3rem;">6. RS RUSH</h3>
          <p style="color: var(--ink-soft); font-size: 0.95rem; margin-top: 0.5rem;">How fast can you decode Remote Sensing? (13 Oct, 3:30 PM)</p>
          <p style="margin-top: 1rem; font-weight: bold; color: var(--brass-dim);">On-spot Registration</p>
        </div>
        <div style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.3rem;">7. GEO CONNECTIONS</h3>
          <p style="color: var(--ink-soft); font-size: 0.95rem; margin-top: 0.5rem;">A thrilling Link & Match challenge where every clue leads you closer to the answer! (14 Oct, 11:30 AM)</p>
          <p style="margin-top: 1rem; font-weight: bold; color: var(--brass-dim);">On-spot Registration</p>
        </div>
        <div style="background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.3rem;">8. PIXEL HUNTERS</h3>
          <p style="color: var(--ink-soft); font-size: 0.95rem; margin-top: 0.5rem;">The FCC Interpretation Challenge. Decode. Digitize. Dominate. (13 Oct, 3:30 PM)</p>
          <p style="margin-top: 1rem; font-weight: bold; color: var(--brass-dim);">On-spot Registration</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Paper & Poster Section -->
  <section id="paper-poster" class="section" style="background-color: var(--navy-900);">
    <div class="section__head" style="text-align: center; margin-bottom: 3rem;">
      <h2 class="section__title" style="color: var(--paper);">Paper and Poster Presentation</h2>
    </div>
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 3rem; padding: 0 1.5rem;">
      <img src="static/images/celestia_2.jpeg" alt="Paper and Poster" style="width: 100%; max-height: 400px; object-fit: cover; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.3);">
      <div style="display: flex; flex-wrap: wrap; gap: 2rem;">
        <div style="flex: 1 1 450px; background: rgba(255,255,255,0.05); padding: 2rem; border-radius: 8px;">
          <h3 style="color: var(--brass); font-size: 1.5rem;">Paper Presentation</h3>
          <p style="color: var(--paper-dim); margin-top: 1rem; line-height: 1.6;">
            <strong>PRESENT. SHARE. INSPIRE.</strong><br>
            Individual / Team of up to 3 members<br>
            5 mins Presentation + 2 mins Q&A<br>
            Maximum 15 slides<br>
            Prize Pool: ₹2,000<br>
            Date: 13 October 2026
          </p>
          <a href="https://docs.google.com/forms/d/e/1FAIpQLSceU9ycnXgBwGjexdQ6OwqOu6G7UBrNKuLI98iKR3J4sF2RwQ/viewform?usp=header" target="_blank" class="btn btn--primary" style="margin-top: 1.5rem; background-color: var(--brass); color: var(--navy-900); border: none;">Register Now</a>
        </div>
        <div style="flex: 1 1 450px; background: rgba(255,255,255,0.05); padding: 2rem; border-radius: 8px;">
          <h3 style="color: var(--brass); font-size: 1.5rem;">Poster Presentation</h3>
          <p style="color: var(--paper-dim); margin-top: 1rem; line-height: 1.6;">
            Have an idea that can shape the future of Geospatial Technology, Earth Observation & Space Science?<br>
            It’s time to put your ideas on the poster!<br>
            Prize Pool: ₹2,000/-<br>
            Last Date: 12.10.2026<br>
            Venue: Flood Lab, IRS
          </p>
          <a href="https://docs.google.com/forms/d/e/1FAIpQLSe2d6HsQgEUWHkwlXDSkguy_nfVf3PUdQ9hvb4pM6-czXTcBQ/viewform?usp=header" target="_blank" class="btn btn--primary" style="margin-top: 1.5rem; background-color: var(--brass); color: var(--navy-900); border: none;">Register Now</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Sports Section -->
  <section id="sports" class="section section--paper">
    <div class="section__head" style="text-align: center; margin-bottom: 3rem;">
      <h2 class="section__title">Sports</h2>
    </div>
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 3rem; padding: 0 1.5rem;">
      <img src="static/images/celestia_3.jpg" alt="Sports" style="width: 100%; max-height: 400px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
      <div style="display: flex; flex-wrap: wrap; gap: 2rem;">
        <div style="flex: 1 1 450px; background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.5rem;">Badminton Tournament</h3>
          <p style="color: var(--ink-soft); margin-top: 1rem; line-height: 1.6;">
            <strong>Smash into Celestia'26!</strong><br>
            Boys & Girls – Doubles<br>
            Win exciting cash prizes and certificates<br>
            Entry fee: just ₹50
          </p>
          <a href="https://docs.google.com/forms/d/18narqBISoWRuRqOmGs4Ahw35_hwzTQwJv55_Af6vkZc/edit" target="_blank" class="btn btn--primary" style="margin-top: 1.5rem;">Register Now</a>
        </div>
        <div style="flex: 1 1 450px; background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h3 style="color: var(--navy-900); font-size: 1.5rem;">Kabaddi Tournament</h3>
          <p style="color: var(--ink-soft); margin-top: 1rem; line-height: 1.6;">
            <strong>Kabaddi Kabaddi Kabaddi!</strong><br>
            Open to boys from CEG, MIT, ACT & SAP<br>
            Date: Oct 09 & 10 @ CEG Ground<br>
            Entry fee: ₹100 per team
          </p>
          <a href="https://docs.google.com/forms/d/1LbLH611pAnU9cpitahjHwbyMpbdlp0jfHUvgkKePHuc/edit" target="_blank" class="btn btn--primary" style="margin-top: 1.5rem;">Register Now</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""

new_content = re.sub(r'<!-- Events Section -->.*?</main>', new_sections, content, flags=re.DOTALL)

with open("celestia.html", "w") as f:
    f.write(new_content)
