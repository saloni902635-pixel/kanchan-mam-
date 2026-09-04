
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="For Kanchan Ma'am", page_icon="💐", layout="centered")

PHOTO = Path(__file__).parent / "assets" / "kanchan_mam.png"

if "page" not in st.session_state:
    st.session_state.page = 0

def nxt():
    st.session_state.page += 1
    st.rerun()

def reset():
    st.session_state.page = 0
    st.rerun()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Playfair+Display:wght@600;700&display=swap');
.stApp{background:radial-gradient(circle at 8% 8%,rgba(255,184,92,.17),transparent 24%),radial-gradient(circle at 92% 20%,rgba(221,83,145,.15),transparent 26%),linear-gradient(145deg,#101217,#18131a 55%,#10161c);color:#f7eee8}
.block-container{max-width:740px;padding-top:2.3rem;padding-bottom:3rem}
#MainMenu,footer{visibility:hidden}
*{font-family:'DM Sans',sans-serif}

.opening-wrap{text-align:center;position:relative;min-height:680px;padding-top:12px;overflow:hidden}
.opening-kicker{font-family:'DM Sans',sans-serif;font-size:.7rem;letter-spacing:4px;color:#d9aa72;margin-top:15px}
.opening-title{font-family:'Playfair Display',serif;font-size:clamp(3.5rem,10vw,6.2rem);line-height:.9;color:#fff8ef;margin:28px 0 22px;text-shadow:0 15px 45px rgba(0,0,0,.35);animation:titleIn .9s ease}
.opening-title span{font-size:.42em;font-style:italic;color:#d5c0bc}
.opening-line{width:110px;height:1px;margin:auto;background:linear-gradient(90deg,transparent,#d9aa72,transparent)}
.opening-sub{margin-top:22px;color:#bdb1b7;line-height:1.8;font-size:1rem;animation:fadeIn 1s .2s both}
.opening-sub b{color:#e2bd91}
.letter-teaser{width:min(480px,88%);margin:42px auto 28px;padding:24px 25px 20px;background:linear-gradient(135deg,rgba(255,255,255,.1),rgba(255,255,255,.025));border:1px solid rgba(217,170,114,.32);border-radius:5px 28px 5px 28px;box-shadow:0 28px 70px rgba(0,0,0,.38),inset 0 0 50px rgba(217,170,114,.04);transform:rotate(-1.5deg);animation:cardIn .9s .3s both}
.teaser-top,.teaser-bottom{display:flex;justify-content:space-between;align-items:center;font-family:'Space Mono',monospace;font-size:.58rem;letter-spacing:1.8px;color:#91838a}
.teaser-top span:last-child{font-size:1rem;color:#d9aa72}
.teaser-quote{font-family:'Playfair Display',serif;color:#fff1e5;font-size:1.65rem;line-height:1.25;margin:25px 0}
.teaser-bottom{border-top:1px solid rgba(217,170,114,.18);padding-top:15px}
.floating{position:absolute;color:#d9aa72;opacity:.45;pointer-events:none;animation:floaty 4s ease-in-out infinite}
.f1{left:8%;top:15%;font-size:2.3rem}.f2{right:9%;top:29%;font-size:1.6rem;animation-delay:1s}.f3{left:14%;bottom:13%;font-size:1.4rem;animation-delay:1.7s}
@keyframes floaty{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-13px) rotate(9deg)}}
@keyframes titleIn{from{opacity:0;transform:translateY(25px) scale(.97)}to{opacity:1;transform:none}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes cardIn{from{opacity:0;transform:rotate(4deg) translateY(25px)}to{opacity:1;transform:rotate(-1.5deg)}}

.eyebrow{text-align:center;color:#d7aa72;font-size:.68rem;font-weight:700;letter-spacing:4px;text-transform:uppercase}
h1.hero{font-family:'Playfair Display',serif;text-align:center;font-size:clamp(3rem,10vw,5.2rem);line-height:.98;color:#fff6ed;margin:14px 0}
.sub{text-align:center;color:#bdb1b7;line-height:1.8}
.card{background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.1);border-radius:28px;padding:30px;margin-top:25px;box-shadow:0 25px 65px rgba(0,0,0,.3);animation:up .7s ease}
@keyframes up{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
.quote{font-family:'Playfair Display',serif;text-align:center;font-size:1.5rem;line-height:1.55;color:#fff1e5}
.line{height:1px;background:linear-gradient(90deg,transparent,#d7aa72,transparent);margin:24px 0}
.note{padding:18px 20px;border-radius:16px;background:rgba(215,170,114,.08);border:1px solid rgba(215,170,114,.18);color:#c9bec3;line-height:1.8}
.counter{text-align:center;color:#837980;font-size:.68rem;letter-spacing:2px;margin-bottom:15px}
.stButton>button{width:100%;border:0;border-radius:14px;padding:.9rem;color:#181319;background:#d7aa72;font-weight:700}
.stButton>button:hover{background:#e4bb86;transform:translateY(-2px)}
.chapter{display:grid;grid-template-columns:58px 1fr;gap:17px;margin:22px 0}
.dot{width:58px;height:58px;border:1px solid #d7aa72;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#d7aa72;font-weight:700}
.chapter h3{margin:2px 0 5px;color:#fff0e5;font-size:1.05rem}
.chapter p{margin:0;color:#b9adb3;line-height:1.7}
.photo-label{text-align:center;font-family:'Playfair Display',serif;color:#584b4f;margin-top:8px}
.final{text-align:center}
.bigheart{font-size:2.5rem;text-align:center}
.sig{font-family:'Playfair Display',serif;color:#e0b27b;font-size:1.2rem;line-height:1.7;text-align:center;margin-top:23px}
.footer{text-align:center;color:#786e75;font-size:.7rem;margin-top:25px}
</style>
""", unsafe_allow_html=True)

p = st.session_state.page

if p == 0:
    st.markdown('<div class="opening-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="floating flower f1">✿</div><div class="floating flower f2">✦</div><div class="floating flower f3">❋</div>', unsafe_allow_html=True)
    st.markdown('<div class="opening-kicker">TEACHERS’ DAY • A LITTLE SURPRISE</div>', unsafe_allow_html=True)
    st.markdown('<div class="opening-title"><span>Dear</span><br>Kanchan Ma’am</div>', unsafe_allow_html=True)
    st.markdown('<div class="opening-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="opening-sub">For the teacher who has been part of our story<br>since <b>1st Year</b> 🌷</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="letter-teaser">
      <div class="teaser-top"><span>TO: KANCHAN MA’AM</span><span>♥</span></div>
      <div class="teaser-quote">“Some teachers<br>become part of<br>the story.”</div>
      <div class="teaser-bottom"><span>3rd Year B.Tech Biotechnology</span><span>01</span></div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("✦  OPEN YOUR SURPRISE  ✦", key="a"):
        nxt()
    st.markdown('</div>', unsafe_allow_html=True)

elif p == 1:
    st.markdown('<div class="counter">PAGE 01 / 04</div>', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">A FACE WE HAVE KNOWN FOR YEARS</div>', unsafe_allow_html=True)
    if PHOTO.is_file():
        img = Image.open(PHOTO).convert("RGB")
        st.image(img, width=210)
    else:
        st.warning("Please add assets/kanchan_mam.png to the GitHub repository.")
    st.markdown('<div class="photo-label">Kanchan Ma’am • Since 1st Year 💐</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <div class="quote">“Some familiarity becomes special only when you look back.”</div>
      <div class="line"></div>
      <div class="note">When we entered college, almost everything was new. Today we are in 3rd Year, and you are still one of the teachers whose presence connects different chapters of our journey.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("TURN THE PAGE  →", key="b"): nxt()

elif p == 2:
    st.markdown('<div class="counter">PAGE 02 / 04</div>', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">THREE YEARS IN THREE MOMENTS</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <div class="chapter"><div class="dot">01</div><div><h3>THE BEGINNING</h3><p>1st Year — new campus, new classmates, new subjects and a lot of questions about what comes next.</p></div></div>
      <div class="chapter"><div class="dot">02</div><div><h3>THE CHANGE</h3><p>2nd Year — we became more comfortable, more independent and slowly started finding our own rhythm.</p></div></div>
      <div class="chapter"><div class="dot">03</div><div><h3>WHERE WE ARE NOW</h3><p>3rd Year — projects, careers, plans and the slightly scary question of what we want to do next.</p></div></div>
      <div class="line"></div>
      <div class="note">And through all these chapters, you have been one of the familiar teachers along the way. That itself is something worth remembering.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("KEEP READING  →", key="c"): nxt()

elif p == 3:
    st.markdown('<div class="counter">PAGE 03 / 04</div>', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">A FEW THINGS WE WANTED TO SAY</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <div class="chapter"><div class="dot">♥</div><div><h3>THANK YOU FOR BEING THERE</h3><p>You have been part of our college life since the first year, not just one short chapter.</p></div></div>
      <div class="chapter"><div class="dot">✦</div><div><h3>THANK YOU FOR THE MEMORIES</h3><p>One day we may forget many ordinary college days. We won't forget the people who were part of them.</p></div></div>
      <div class="chapter"><div class="dot">∞</div><div><h3>THANK YOU FOR THE JOURNEY</h3><p>We are still learning and growing. Having teachers who become familiar faces along that journey matters more than we usually say.</p></div></div>
      <div class="note"><b>From 1st Year to 3rd Year:</b> we have changed a lot. Thank you for being a part of those years.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("READ THE LAST PAGE  →", key="d"): nxt()

else:
    st.markdown('<div class="counter">PAGE 04 / 04 • THE LAST PAGE</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card final">
      <div class="bigheart">💐</div>
      <div class="eyebrow">HAPPY TEACHERS’ DAY</div>
      <h1 class="hero" style="font-size:clamp(2.5rem,8vw,4.2rem)">Kanchan Ma’am</h1>
      <div class="line"></div>
      <div class="quote">“Thank you for being a part of our story since the very beginning.”</div>
      <div class="note">As we move from 3rd Year towards whatever comes next, there will be new classrooms, new people and new chapters. But the teachers who were there from the beginning will always have a place in our memories.</div>
      <div class="sig">With respect, gratitude & warm wishes 🌸<br>Your 3rd Year B.Tech Biotechnology Students</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("↻ START AGAIN", key="e"): reset()

st.markdown('<div class="footer">MADE WITH ❤️ • 3RD YEAR B.TECH BIOTECHNOLOGY</div>', unsafe_allow_html=True)
