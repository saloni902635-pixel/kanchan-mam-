
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="For Kanchan Ma'am", page_icon="✦", layout="centered")
PHOTO = Path(__file__).parent / "assets" / "kanchan_mam.png"

if "page" not in st.session_state: st.session_state.page = 0
def nxt(): st.session_state.page += 1; st.rerun()
def reset(): st.session_state.page = 0; st.rerun()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
.stApp{background:#f4f1eb;color:#17212b}.block-container{max-width:780px;padding-top:1.6rem;padding-bottom:3rem}
#MainMenu,footer{visibility:hidden}*{font-family:'DM Sans',sans-serif}
.nav{display:flex;justify-content:space-between;border-bottom:1px solid #d9d5cc;padding:8px 2px 18px;color:#7b8389;font-size:.63rem;letter-spacing:2px}
.nav b{color:#202a33}.gold{color:#9b7540!important}
.hero{text-align:center;padding:72px 0 48px}.eyebrow{font-size:.66rem;letter-spacing:3.5px;font-weight:700;color:#a07843}
.hero h1{font-family:'Playfair Display',serif;font-size:clamp(3.2rem,9vw,6rem);line-height:.9;font-weight:600;letter-spacing:-2px;color:#18232c;margin:20px 0}
.hero h1 em{font-weight:500;color:#88745f}.hero p{max-width:570px;margin:auto;color:#6d777f;line-height:1.8}
.letter{background:#fff;border:1px solid #ddd8cf;box-shadow:0 22px 55px rgba(22,31,39,.09);padding:32px 36px;position:relative}
.letter:before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:#b18a55}
.meta{display:flex;justify-content:space-between;color:#8b9298;font-size:.61rem;letter-spacing:1.8px}
.bigquote{font-family:'Playfair Display',serif;text-align:center;font-size:1.48rem;line-height:1.55;color:#29343d;margin:30px 0}
.small{text-align:center;color:#78828a;font-size:.82rem;line-height:1.8}.line{width:65px;height:1px;background:#b18a55;margin:0 auto 16px}
.stButton>button{width:100%;background:#18232c;color:white;border:0;border-radius:2px;height:48px;font-weight:700;font-size:.68rem;letter-spacing:1.5px}
.stButton>button:hover{background:#a07843;color:white}
.cta{max-width:330px;margin:24px auto}.foot{text-align:center;color:#9aa0a4;font-size:.63rem;letter-spacing:1px;margin-top:30px}
.label{text-align:center;color:#a07843;font-size:.64rem;font-weight:700;letter-spacing:3px;margin-bottom:15px}
.title{font-family:'Playfair Display',serif;text-align:center;font-size:2.5rem;color:#18232c;margin-bottom:8px}
.sub{text-align:center;color:#707a82;line-height:1.7;margin-bottom:25px}.card{background:#fff;border:1px solid #ddd8cf;padding:32px;box-shadow:0 18px 45px rgba(22,31,39,.07)}
.photo{width:210px;margin:0 auto 25px}.photo img{width:100%;height:260px;object-fit:cover}
.row{border-top:1px solid #e0ddd7;padding:21px 0}.row:first-child{border-top:0}.row h3{font-size:.95rem;color:#29343d;margin:0 0 6px}.row p{color:#6d777f;line-height:1.75;margin:0}
.final{background:#18232c;color:white;text-align:center;padding:48px 34px;box-shadow:0 22px 55px rgba(22,31,39,.18)}.final h2{font-family:'Playfair Display',serif;font-size:clamp(2.6rem,8vw,4.4rem);font-weight:500;margin:15px 0 25px}.final .q{font-family:'Playfair Display',serif;font-size:1.35rem;line-height:1.6;color:#eee8df}.final .copy{color:#b9c0c5;line-height:1.85;margin-top:24px}.sign{color:#d4ae76;font-family:'Playfair Display',serif;font-size:1.1rem;line-height:1.7;margin-top:25px}
</style>
""", unsafe_allow_html=True)

p=st.session_state.page

if p==0:
    st.markdown('<div class="nav"><span><b>3RD YEAR</b> · B.TECH BIOTECHNOLOGY</span><span class="gold">TEACHERS’ DAY</span></div>',unsafe_allow_html=True)
    st.markdown('<div class="hero"><div class="eyebrow">✦ A PERSONAL NOTE ✦</div><h1>For <em>our</em><br>Kanchan Ma’am</h1><p>A small, thoughtfully made message for a teacher who has been a familiar part of our journey since the very first year.</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="letter"><div class="meta"><span>A NOTE OF GRATITUDE</span><span>05 · 09 · 2026</span></div><div class="bigquote">“The teachers we remember are not always the ones who taught us the most — they are the ones who became part of the <span style="color:#a07843">journey.</span>”</div><div class="line"></div><div class="small">This little surprise is from your students,<br>with respect, gratitude and warm wishes.</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="cta">',unsafe_allow_html=True)
    if st.button("OPEN THE NOTE  →",key="a"): nxt()
    st.markdown('</div><div class="foot">MADE WITH CARE · 3RD YEAR B.TECH BIOTECHNOLOGY</div>',unsafe_allow_html=True)

elif p==1:
    st.markdown('<div class="label">01 · A FAMILIAR FACE</div><div class="title">Since Our First Year</div><div class="sub">Some people become part of a college journey simply by being there through its chapters.</div>',unsafe_allow_html=True)
    st.markdown('<div class="card">',unsafe_allow_html=True)
    if PHOTO.is_file(): st.image(Image.open(PHOTO).convert("RGB"),width=210)
    st.markdown('<div class="small">From our first year until today, you have been one of the familiar teachers connected with our college life. That continuity matters.</div></div>',unsafe_allow_html=True)
    if st.button("CONTINUE  →",key="b"): nxt()

elif p==2:
    st.markdown('<div class="label">02 · THE JOURNEY</div><div class="title">Three Years, Three Chapters</div><div class="sub">Looking back, the change is bigger than we realised.</div>',unsafe_allow_html=True)
    st.markdown('<div class="card">',unsafe_allow_html=True)
    for n,h,d in [("01","FIRST YEAR — THE BEGINNING","New campus, new classmates, new subjects and a lot of uncertainty about what college would be like."),("02","SECOND YEAR — THE CHANGE","We became more comfortable, more independent and slowly started finding our own rhythm."),("03","THIRD YEAR — WHERE WE ARE","Projects, careers, responsibilities and a growing sense that the future is getting closer.")]:
        st.markdown(f'<div class="row"><h3><span style="color:#a07843;font-family:serif;margin-right:14px">{n}</span>{h}</h3><p>{d}</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="small">Through these chapters, you have remained one of the teachers who connects our present with where our journey began.</div></div>',unsafe_allow_html=True)
    if st.button("CONTINUE  →",key="c"): nxt()

elif p==3:
    st.markdown('<div class="label">03 · A FEW WORDS</div><div class="title">What We Wanted to Say</div><div class="sub">Simple words, but genuinely meant.</div>',unsafe_allow_html=True)
    st.markdown('<div class="card">',unsafe_allow_html=True)
    for h,d in [("THANK YOU FOR BEING THERE","You have been part of our college life since the first year, not just one short chapter."),("THANK YOU FOR THE MEMORIES","Years later, we may forget many ordinary college days. The people who were part of them are harder to forget."),("THANK YOU FOR THE JOURNEY","We are still learning, growing and figuring out our future. We are grateful that you have been part of that journey.")]:
        st.markdown(f'<div class="row"><h3>{h}</h3><p>{d}</p></div>',unsafe_allow_html=True)
    st.markdown('</div>',unsafe_allow_html=True)
    if st.button("THE FINAL NOTE  →",key="d"): nxt()

else:
    st.markdown('<div class="label">04 · FINAL NOTE</div>',unsafe_allow_html=True)
    st.markdown('<div class="final"><div class="eyebrow">HAPPY TEACHERS’ DAY</div><h2>Kanchan Ma’am</h2><div class="q">“Thank you for being a part of our story since the very beginning.”</div><div class="copy">From 1st Year to 3rd Year, a lot has changed. New experiences, responsibilities and dreams have become part of our lives. Yet some teachers remain connected to more than one chapter.<br><br>Thank you for being one of those teachers.</div><div class="sign">With respect & gratitude<br>Your 3rd Year B.Tech Biotechnology Students</div></div>',unsafe_allow_html=True)
    if st.button("↻  READ AGAIN",key="e"): reset()

st.markdown('<div class="foot">A SMALL NOTE · MADE WITH ❤️ BY 3RD YEAR B.TECH BIOTECHNOLOGY</div>',unsafe_allow_html=True)
