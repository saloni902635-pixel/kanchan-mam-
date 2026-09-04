
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="For Kanchan Ma'am 💐",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

PHOTO = Path(__file__).parent / "assets" / "kanchan_mam.png"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background:
      radial-gradient(circle at 10% 10%, rgba(255,235,190,.55), transparent 26%),
      radial-gradient(circle at 90% 15%, rgba(215,195,255,.38), transparent 28%),
      linear-gradient(145deg,#fffaf1 0%,#fff7fb 50%,#f7f3ff 100%);
    color:#3d3040;
}
.block-container { max-width:820px; padding-top:2rem; padding-bottom:3rem; }
* { font-family:'DM Sans',sans-serif; }

.topline {
    text-align:center; color:#9b7a51; font-size:.76rem; font-weight:700;
    letter-spacing:3px; text-transform:uppercase;
}
.hero {
    font-family:'Playfair Display',serif; text-align:center;
    font-size:clamp(2.6rem,8vw,4.8rem); line-height:1.04;
    margin:14px 0 10px;
    background:linear-gradient(90deg,#9c6744,#b14c72,#71569f);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.sub { text-align:center; color:#806d79; font-size:1.05rem; line-height:1.7; }

.card {
    background:rgba(255,255,255,.72); border:1px solid rgba(255,255,255,.9);
    box-shadow:0 18px 55px rgba(93,65,83,.12);
    border-radius:30px; padding:28px; margin:18px 0;
    backdrop-filter:blur(12px);
}
.goldcard {
    background:linear-gradient(135deg,rgba(255,250,237,.9),rgba(255,242,248,.78));
    border:1px solid rgba(194,157,93,.22);
}
.quote {
    font-family:'Playfair Display',serif; text-align:center;
    color:#594353; font-size:1.48rem; line-height:1.55;
}
.center { text-align:center; }
.reveal { animation:reveal .85s ease both; }
@keyframes reveal {
    from { opacity:0; transform:translateY(24px) scale(.98); }
    to { opacity:1; transform:translateY(0) scale(1); }
}
.sparkle { text-align:center; font-size:1.8rem; letter-spacing:8px; }
.photo {
    display:block; margin:16px auto 10px; width:min(215px,55vw);
    aspect-ratio:1/1; object-fit:cover; object-position:center;
    border-radius:50%; border:7px solid white;
    box-shadow:0 18px 45px rgba(106,65,83,.22);
    animation:float 4s ease-in-out infinite;
}
@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }

.timeline {
    border-left:2px solid #d8b9c9; padding-left:20px; margin:10px 4px;
}
.item { margin:18px 0; }
.item b { color:#874c6b; }
.badge {
    display:inline-block; padding:6px 12px; border-radius:999px;
    background:#f5e7ee; color:#87506d; font-size:.78rem; font-weight:700;
}
.stButton > button {
    border:0; border-radius:999px; padding:.78rem 1.2rem;
    font-weight:700; color:white;
    background:linear-gradient(90deg,#9b624c,#b84e75,#755ba1);
    box-shadow:0 10px 25px rgba(120,72,100,.18);
}
.stButton > button:hover { transform:translateY(-2px); }

.finalbox {
    text-align:center; border-radius:32px; padding:34px 26px;
    background:linear-gradient(145deg,rgba(255,255,255,.86),rgba(255,238,245,.82));
    border:1px solid rgba(183,126,157,.22);
    box-shadow:0 20px 60px rgba(98,62,88,.14);
}
.signature { font-family:'Playfair Display',serif; color:#7d4965; font-size:1.25rem; }
.progress { text-align:center; color:#a48898; font-size:.8rem; margin-bottom:18px; }
.footer { text-align:center; color:#ae94a5; font-size:.78rem; margin-top:28px; }
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = 0

def go_next():
    st.session_state.page = min(4, st.session_state.page + 1)

def restart():
    st.session_state.page = 0

page = st.session_state.page

# Layer 1 — personal opening
if page == 0:
    st.markdown('<div class="sparkle">💐 ✨ 🌷 ✨ 💐</div>', unsafe_allow_html=True)
    st.markdown('<div class="topline">A special note from your students</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero">Happy Teachers’ Day</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">For our wonderful <b>Kanchan Ma’am</b> 🌸</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card goldcard reveal">
      <div class="quote">“Some teachers enter your classroom.<br>
      The special ones become a part of your journey.”</div>
      <p class="center" style="color:#766575;margin-top:18px;line-height:1.8;">
      This is a small surprise for the teacher who has been with us
      <b>since our very first year</b>.
      </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🌷 Begin the Surprise", key="start"):
        go_next(); st.rerun()

# Layer 2 — photo reveal
elif page == 1:
    st.markdown('<div class="progress">A LITTLE SURPRISE • 1 OF 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="topline">The teacher behind so many memories</div>', unsafe_allow_html=True)

    if PHOTO.is_file():
        image = Image.open(PHOTO).convert("RGB")
        st.markdown('<div class="reveal">', unsafe_allow_html=True)
        st.image(image, width=215)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Photo file is missing. Keep assets/kanchan_mam.png in the repository.")

    st.markdown("""
    <div class="card reveal">
      <h2 class="center" style="color:#804a67;">Our Dearest Kanchan Ma’am 💐</h2>
      <p class="center" style="line-height:1.8;color:#716171;">
      From the first year of our B.Tech Biotechnology journey to where we are today,
      you have been one of the familiar faces in our college life.
      And that continuity is something students remember.
      </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 Next", key="n1"):
        go_next(); st.rerun()

# Layer 3 — journey
elif page == 2:
    st.markdown('<div class="progress">A LITTLE SURPRISE • 2 OF 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="topline">Four years are made of little moments</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card reveal">
      <div class="timeline">
        <div class="item"><span class="badge">1st Year</span><br>
        <b>New faces, new campus, new beginning.</b><br>
        <span style="color:#756474;">Everything felt unfamiliar, but teachers like you made the journey easier to settle into.</span></div>

        <div class="item"><span class="badge">2nd Year</span><br>
        <b>We started finding our rhythm.</b><br>
        <span style="color:#756474;">The nervous first-year version of us slowly became more confident.</span></div>

        <div class="item"><span class="badge">3rd Year</span><br>
        <b>Now we are building our own path.</b><br>
        <span style="color:#756474;">Projects, responsibilities, plans and a lot more to figure out.</span></div>
      </div>
    </div>
    <div class="card goldcard reveal">
      <div class="quote">“Thank you for being a familiar part of our journey from the beginning.”</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("✨ There’s More", key="n2"):
        go_next(); st.rerun()

# Layer 4 — thoughts
elif page == 3:
    st.markdown('<div class="progress">A LITTLE SURPRISE • 3 OF 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="topline">What we would like you to know</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card reveal">
      <p>🌱 <b>You have seen us grow</b> — from first-year students figuring everything out to the people we are becoming now.</p>
      <p>📚 <b>You have been part of our college story</b> — not just one semester or one subject.</p>
      <p>💫 <b>Your presence became familiar</b> — and sometimes that quiet familiarity means more than we realise.</p>
      <p>🧬 <b>We are still learning</b> — and we hope the lessons we carry forward are not limited to textbooks.</p>
    </div>
    <div class="card goldcard reveal">
      <div class="quote">“A teacher may teach for a year,<br>but the impression can last much longer.”</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("❤️ Final Surprise", key="n3"):
        go_next(); st.rerun()

# Layer 5 — final
else:
    st.markdown('<div class="progress">FINAL SURPRISE • 4 OF 4</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="finalbox reveal">
      <div style="font-size:2.6rem;">💐</div>
      <div class="hero" style="font-size:clamp(2.4rem,7vw,4rem);">Thank You, Ma’am</div>
      <div class="quote">
        “From our first year to today,<br>
        thank you for being a part of our journey.”
      </div>
      <p style="color:#746273;line-height:1.85;margin-top:22px;">
        We may not remember every lecture, every deadline or every ordinary college day.
        But we do remember the teachers who were there through different chapters of our life.
        <br><br>
        <b>Happy Teachers’ Day, Kanchan Ma’am.</b><br>
        Thank you for being a part of our story since 1st year. ❤️
      </p>
      <div class="signature">With respect &amp; warm wishes 🌸<br>
      — Your 3rd Year B.Tech Biotechnology Students</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Replay the Surprise", key="again"):
        restart(); st.rerun()

st.markdown(
    '<div class="footer">Made with ❤️ by the 3rd Year B.Tech Biotechnology class</div>',
    unsafe_allow_html=True
)
