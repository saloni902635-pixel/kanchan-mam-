
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="For Kanchan Ma'am ♡", page_icon="🌷", layout="centered")

PHOTO = Path(__file__).parent / "assets" / "kanchan_mam.png"

if "page" not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1
    st.rerun()

def restart():
    st.session_state.page = 0
    st.rerun()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500;1,600&display=swap');
.stApp{background:radial-gradient(circle at 8% 10%,rgba(245,180,192,.34),transparent 25%),radial-gradient(circle at 92% 10%,rgba(238,211,161,.30),transparent 25%),radial-gradient(circle at 50% 100%,rgba(215,193,228,.26),transparent 30%),#fffaf7;color:#493a40}
.block-container{max-width:780px;padding:1.4rem 1.2rem 3rem}
#MainMenu,footer{visibility:hidden}*{font-family:'DM Sans',sans-serif}
.top{display:flex;justify-content:space-between;padding:8px 3px 15px;border-bottom:1px solid rgba(120,90,100,.14);color:#a28d94;font-size:.59rem;letter-spacing:2px}.top b{color:#795d68}.top span{color:#b27e68}
.hero{text-align:center;padding:48px 0 30px}.eyebrow{color:#b27785;font-size:.62rem;font-weight:700;letter-spacing:3.5px;text-transform:uppercase}
.hero h1{font-family:'Playfair Display',serif;font-size:clamp(3.3rem,9vw,6rem);line-height:.9;font-weight:500;color:#5d414d;margin:17px 0;letter-spacing:-1.5px}.hero h1 em{color:#aa7a65}
.hero p{color:#8c777f;line-height:1.8;font-size:.95rem}
.ornament{text-align:center;color:#c5947b;font-family:'Playfair Display',serif;font-size:1.5rem;margin:10px}
.letter{background:rgba(255,255,255,.88);border:1px solid #eadfe0;border-radius:25px;padding:30px;box-shadow:0 20px 55px rgba(112,74,91,.10);position:relative}.letter:before{content:"";position:absolute;inset:11px;border:1px solid rgba(216,167,173,.35);border-radius:17px;pointer-events:none}
.meta{display:flex;justify-content:space-between;color:#aa9299;font-size:.56rem;letter-spacing:1.8px;text-transform:uppercase;position:relative}
.quote{font-family:'Playfair Display',serif;color:#634955;text-align:center;font-size:1.38rem;line-height:1.55;margin:28px auto 22px;max-width:620px;position:relative}.quote i{color:#b47d88}
.divider{width:60px;height:1px;background:#cda17e;margin:0 auto 16px}.small{text-align:center;color:#907c83;font-size:.78rem;line-height:1.8}
.cta{max-width:320px;margin:24px auto}.stButton>button{width:100%;height:49px;border:0;border-radius:999px;color:#fff;background:linear-gradient(90deg,#b97987,#c58c71);font-weight:700;font-size:.66rem;letter-spacing:1.5px;box-shadow:0 12px 28px rgba(166,103,119,.2)}.stButton>button:hover{background:linear-gradient(90deg,#a96878,#b77d62);color:#fff;transform:translateY(-2px)}
.flower{position:fixed;color:#c88e99;opacity:.28;pointer-events:none}.a{left:7%;top:24%;font-size:2rem}.b{right:7%;top:36%;font-size:1.6rem}.c{left:12%;bottom:20%;font-size:1.3rem}
.footer{text-align:center;color:#b19ba1;font-size:.6rem;letter-spacing:1px;margin-top:27px}
.page{text-align:center;color:#b1848e;font-size:.61rem;letter-spacing:3px;font-weight:700;margin:13px 0}.title{font-family:'Playfair Display',serif;text-align:center;color:#5d414d;font-size:2.55rem;margin:0 0 7px}.sub{text-align:center;color:#907c83;line-height:1.75;margin-bottom:25px}.card{background:rgba(255,255,255,.9);border:1px solid #eadfe0;border-radius:25px;padding:30px;box-shadow:0 18px 50px rgba(112,74,91,.09);animation:rise .6s ease}@keyframes rise{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:none}}
.chapter{padding:20px 0;border-top:1px solid #eee3e1}.chapter:first-child{border-top:0}.chapter h3{font-size:.92rem;color:#704b59;margin:0 0 7px}.chapter p{margin:0;color:#7f7076;line-height:1.8;font-size:.9rem}.num{font-family:'Playfair Display',serif;color:#bc856d;margin-right:11px;font-size:1.2rem}
.final{background:linear-gradient(145deg,#704b5b,#925f6d);color:#fff;text-align:center;border-radius:28px;padding:45px 30px;box-shadow:0 22px 55px rgba(105,70,84,.23)}.final .eyebrow{color:#f0cda9}.final h2{font-family:'Playfair Display',serif;font-size:clamp(2.5rem,8vw,4.4rem);font-weight:500;line-height:1;margin:16px 0 24px}.final .q{font-family:'Playfair Display',serif;font-size:1.32rem;line-height:1.6;color:#fff3ee}.final .copy{color:#ecdfe0;line-height:1.85;margin-top:24px}.final .sign{font-family:'Playfair Display',serif;color:#f2cda5;font-size:1.08rem;line-height:1.7;margin-top:24px}
</style>
""", unsafe_allow_html=True)

p=st.session_state.page

if p==0:
    st.markdown('<div class="flower a">✿</div><div class="flower b">❋</div><div class="flower c">✦</div>',unsafe_allow_html=True)
    st.markdown('<div class="top"><b>3RD YEAR · B.TECH BIOTECHNOLOGY</b><span>TEACHERS’ DAY · 2026</span></div>',unsafe_allow_html=True)
    st.markdown('<div class="hero"><div class="eyebrow">✦ A LITTLE SURPRISE · MADE FOR YOU ✦</div><h1>For <em>our</em><br>Kanchan Ma’am</h1><div class="ornament">— ❀ —</div><p>A little collection of words, memories and gratitude<br>from the students who have known you since 1st Year.</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="letter"><div class="meta"><span>A NOTE FOR YOU</span><span>WITH LOVE ♡</span></div><div class="quote">“Some teachers teach a subject.<br>Some quietly become a part of the <i>journey.</i>”</div><div class="divider"></div><div class="small">Three years of college deserve more than a simple greeting.<br>So we made you a little something instead.</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="cta">',unsafe_allow_html=True)
    if st.button("🌷  OPEN YOUR SURPRISE  🌷",key="p0"): next_page()
    st.markdown('</div><div class="footer">A SMALL DIGITAL MEMORY · 3RD YEAR B.TECH BIOTECHNOLOGY</div>',unsafe_allow_html=True)

elif p==1:
    st.markdown('<div class="page">01 · A FAMILIAR FACE</div><div class="title">Since Our First Year</div><div class="sub">Some faces become special because they remain familiar through different chapters.</div>',unsafe_allow_html=True)
    st.markdown('<div class="card">',unsafe_allow_html=True)
    if PHOTO.is_file(): st.image(Image.open(PHOTO).convert("RGB"),width=210)
    st.markdown('<div class="small">From our first year until today, you have been one of the familiar teachers connected with our college life. That continuity matters.</div></div>',unsafe_allow_html=True)
    if st.button("TURN THE PAGE  →",key="p1"): next_page()

elif p==2:
    st.markdown('<div class="page">02 · OUR JOURNEY</div><div class="title">Three Little Chapters</div><div class="sub">Looking back, we have changed more than we realised.</div>',unsafe_allow_html=True)
    st.markdown('<div class="card">',unsafe_allow_html=True)
    for n,h,d in [("01","FIRST YEAR","New campus, new classmates, new subjects and the excitement — and confusion — of beginning college."),("02","SECOND YEAR","We became more comfortable, more independent and slowly started finding our own rhythm."),("03","THIRD YEAR","Projects, careers, responsibilities and the growing feeling that the future is getting closer.")]:
        st.markdown(f'<div class="chapter"><h3><span class="num">{n}</span>{h}</h3><p>{d}</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="small">And through these chapters, you have remained one of the familiar teachers along the way.</div></div>',unsafe_allow_html=True)
    if st.button("CONTINUE  →",key="p2"): next_page()

elif p==3:
    st.markdown('<div class="page">03 · FROM THE HEART</div><div class="title">A Few Things We Mean</div><div class="sub">Simple words. Honestly meant.</div>',unsafe_allow_html=True)
    st.markdown('<div class="card">',unsafe_allow_html=True)
    for n,h,d in [("01","Thank you for being there.","You have been part of our college life since 1st Year, not just one short chapter."),("02","Thank you for the memories.","Years later, we may forget many ordinary college days. The people who were part of them are harder to forget."),("03","Thank you for the journey.","We are still learning, growing and figuring out our future. We are grateful that you have been part of it.")]:
        st.markdown(f'<div class="chapter"><h3><span class="num">{n}</span>{h}</h3><p>{d}</p></div>',unsafe_allow_html=True)
    st.markdown('</div>',unsafe_allow_html=True)
    if st.button("ONE LAST PAGE  →",key="p3"): next_page()

else:
    st.markdown('<div class="page">04 · THE FINAL NOTE</div>',unsafe_allow_html=True)
    st.markdown('<div class="final"><div class="eyebrow">HAPPY TEACHERS’ DAY</div><h2>Kanchan Ma’am</h2><div class="q">“Thank you for being a part of our story since the very beginning.”</div><div class="copy">From 1st Year to 3rd Year, so much has changed — our classes, our responsibilities, our plans and even the way we see the future. But some people remain part of more than one chapter.<br><br>Thank you for being one of those people, Ma’am. 🌷</div><div class="sign">With respect, gratitude & warm wishes<br>Your 3rd Year B.Tech Biotechnology Students</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="cta">',unsafe_allow_html=True)
    if st.button("♡  READ IT AGAIN",key="again"): restart()
    st.markdown('</div>',unsafe_allow_html=True)

st.markdown('<div class="footer">MADE WITH ♡ BY 3RD YEAR B.TECH BIOTECHNOLOGY</div>',unsafe_allow_html=True)
