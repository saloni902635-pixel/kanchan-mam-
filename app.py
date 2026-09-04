
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="For Kanchan Ma'am 💐", page_icon="💐", layout="centered")

PHOTO = Path(__file__).parent / "assets" / "kanchan_mam.png"

if "page" not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page = min(st.session_state.page + 1, 4)

def restart():
    st.session_state.page = 0

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Playfair+Display:wght@600;700&display=swap');
.stApp{background:radial-gradient(circle at 15% 10%,#ffe8d6,transparent 27%),radial-gradient(circle at 90% 15%,#e9ddff,transparent 28%),#fffaf7;color:#4b3944}
.block-container{max-width:760px;padding-top:2.4rem}
*{font-family:'DM Sans',sans-serif}
.top{text-align:center;text-transform:uppercase;letter-spacing:4px;font-size:.72rem;font-weight:700;color:#a27857}
.title{font-family:'Playfair Display',serif;text-align:center;font-size:clamp(2.6rem,8vw,4.8rem);line-height:1.05;color:#614452;margin:14px 0}
.sub{text-align:center;color:#8b7580;line-height:1.7}
.page{text-align:center;color:#b097a5;font-size:.76rem;margin-bottom:18px}
.book{background:rgba(255,255,255,.82);border:1px solid white;border-radius:34px;padding:32px 28px;box-shadow:0 25px 70px rgba(89,58,76,.13);animation:rise .7s ease}
@keyframes rise{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
.quote{font-family:'Playfair Display',serif;text-align:center;color:#65495a;font-size:1.42rem;line-height:1.55}
.note{margin-top:22px;padding:18px 20px;background:#fff8ed;border-left:4px solid #d7a06e;border-radius:0 18px 18px 0;color:#74636c;line-height:1.8}
.memory{display:flex;gap:15px;text-align:left;margin:20px 0;line-height:1.7;color:#74636c}
.num{min-width:42px;height:42px;border-radius:50%;background:#f2e1ea;color:#8a536e;display:flex;align-items:center;justify-content:center;font-weight:700}
.memory b{color:#77475f}
.photo-frame{width:210px;margin:4px auto 24px;background:white;padding:9px 9px 15px;box-shadow:0 18px 45px rgba(70,50,60,.18);transform:rotate(-2deg);animation:photo .8s ease}
@keyframes photo{from{opacity:0;transform:rotate(-8deg) scale(.92)}to{opacity:1;transform:rotate(-2deg) scale(1)}}
.photo-frame img{width:100%;height:250px;object-fit:cover}
.caption{text-align:center;font-family:'Playfair Display',serif;color:#765a67;margin-top:10px}
.final{text-align:center;background:linear-gradient(145deg,#fffdf7,#fff0f5)}
.signature{font-family:'Playfair Display',serif;color:#7b4c65;font-size:1.2rem;line-height:1.7;margin-top:22px}
.stButton>button{border:0;border-radius:999px;padding:.78rem 1.3rem;font-weight:700;color:white;background:linear-gradient(90deg,#a56d52,#b85878,#775da2);box-shadow:0 10px 25px rgba(110,65,90,.18)}
.stButton>button:hover{transform:translateY(-2px)}
.footer{text-align:center;color:#b39aa8;font-size:.74rem;margin-top:26px}
</style>
""", unsafe_allow_html=True)

p = st.session_state.page

if p == 0:
    st.markdown('<div style="text-align:center;font-size:2.5rem">💐 ✨ 💐</div>', unsafe_allow_html=True)
    st.markdown('<div class="top">A little surprise for someone special</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">For Kanchan Ma’am</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">Happy Teachers’ Day 🌸<br>From your 3rd Year B.Tech Biotechnology students</div>', unsafe_allow_html=True)
    st.markdown('<div class="book" style="margin-top:24px">', unsafe_allow_html=True)
    st.markdown('<div class="quote">“Some teachers teach lessons.<br>Some become part of the journey.”</div>', unsafe_allow_html=True)
    st.markdown('<div class="note">A small digital memory, made especially for the teacher who has been with us since our very first year.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("💌 Open the Surprise", key="b0"): next_page(); st.rerun()

elif p == 1:
    st.markdown('<div class="page">MEMORY 01 • A FAMILIAR FACE</div>', unsafe_allow_html=True)
    st.markdown('<div class="top">Since our first year</div>', unsafe_allow_html=True)
    st.markdown('<div class="book">', unsafe_allow_html=True)
    if PHOTO.is_file():
        img = Image.open(PHOTO).convert("RGB")
        st.image(img, width=210)
    else:
        st.error("Photo missing: assets/kanchan_mam.png")
    st.markdown('<div class="caption">A familiar face through our college journey 💐</div>', unsafe_allow_html=True)
    st.markdown('<div class="note">When we entered college in 1st Year, so much was new. Years later, we are in 3rd Year — and you are still one of the teachers connected with our journey.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("🌷 Turn the Page", key="b1"): next_page(); st.rerun()

elif p == 2:
    st.markdown('<div class="page">MEMORY 02 • THE JOURNEY</div>', unsafe_allow_html=True)
    st.markdown('<div class="top">Look how far we have come</div>', unsafe_allow_html=True)
    st.markdown('<div class="book">', unsafe_allow_html=True)
    st.markdown('<div class="quote">“We did not realise that ordinary college days would one day become memories.”</div>', unsafe_allow_html=True)
    st.markdown('<div class="memory"><div class="num">1</div><div><b>First Year</b><br>New campus, new classmates, new subjects and a lot of things to learn.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="memory"><div class="num">2</div><div><b>Second Year</b><br>We became more comfortable, more confident and a little more responsible.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="memory"><div class="num">3</div><div><b>Third Year</b><br>Now we are building projects, thinking about careers and trying to find our direction.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="note"><b>And through these chapters,</b> you have remained a familiar part of our college life.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("✨ Continue", key="b2"): next_page(); st.rerun()

elif p == 3:
    st.markdown('<div class="page">MEMORY 03 • UNSAID WORDS</div>', unsafe_allow_html=True)
    st.markdown('<div class="top">Things we wanted to say</div>', unsafe_allow_html=True)
    st.markdown('<div class="book">', unsafe_allow_html=True)
    st.markdown('<div class="memory"><div class="num">🌱</div><div><b>Thank you for being there from the beginning.</b><br>You have been part of more than one academic year of our lives.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="memory"><div class="num">📚</div><div><b>Thank you for being part of our learning journey.</b><br>The people around us are a part of what makes college memorable.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="memory"><div class="num">💫</div><div><b>Thank you for the familiarity.</b><br>Sometimes simply seeing a familiar teacher through different years means more than we say.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="note">From 1st Year to 3rd Year, we have changed a lot. We are still learning, still growing, and still making memories.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("❤️ One Last Page", key="b3"): next_page(); st.rerun()

else:
    st.markdown('<div class="page">FINAL MEMORY • 04</div>', unsafe_allow_html=True)
    st.markdown('<div class="book final">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:2.7rem">💐</div>', unsafe_allow_html=True)
    st.markdown('<div class="title" style="font-size:clamp(2.3rem,7vw,4rem)">Happy Teachers’ Day</div>', unsafe_allow_html=True)
    st.markdown('<div class="quote">“Thank you for being a part of our story since 1st Year.”</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#74616b;line-height:1.9;margin-top:22px">Kanchan Ma’am, as we move through 3rd Year and towards the future, there will be many teachers, many classrooms and many new chapters. But the teachers who were part of our journey from the beginning will always hold a special place in our memories.</p>', unsafe_allow_html=True)
    st.markdown('<div class="signature">With respect, gratitude & warm wishes 🌸<br>— Your 3rd Year B.Tech Biotechnology Students</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("🔄 Read It Again", key="b4"): restart(); st.rerun()

st.markdown('<div class="footer">Made with ❤️ by the 3rd Year B.Tech Biotechnology class</div>', unsafe_allow_html=True)
