import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="أول كود بايثون", page_icon="💻", layout="centered")

# ألوان مخصصة - سماوي
sky_blue = "#4F8BF9"
dark_sky = "#1D3557"

# تنسيق مخصص
st.markdown(f"""
    <style>
        html, body {{
            background-color: #0E1117;
            color: {sky_blue};
            font-family: 'Cairo', sans-serif;
        }}
        .title {{
            text-align: center;
            font-size: 38px;
            font-weight: bold;
            color: {sky_blue};
        }}
        .subtitle {{
            text-align: center;
            font-size: 20px;
            color: #aaa;
            margin-bottom: 30px;
        }}
        .codebox textarea {{
            font-size: 18px !important;
            background-color: #f0f0f0 !important;
        }}
        .success {{
            background-color: #d2f8d2;
            color: #207520;
            padding: 10px;
            border-radius: 8px;
        }}
        .error {{
            background-color: #ffd9d9;
            color: #a60000;
            padding: 10px;
            border-radius: 8px;
        }}
    </style>
""", unsafe_allow_html=True)

# العنوان والنص
st.markdown(f'<div class="title">👋 مرحباً بك في عالم بايثون</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">هنا تبدأ أول خطوة فعلية في رحلتك البرمجية 💻<br>اكتب أول كود لك وشوف كيف الكمبيوتر يستجيب لأوامرك!</div>', unsafe_allow_html=True)

# التلميح
st.markdown(f"🧠 <span style='color:{dark_sky}; font-size:16px'>اكتب كود يستخدم <code>print</code> ويطبع: <strong>أنا بدأت أبرمج بايثون</strong></span>", unsafe_allow_html=True)

# إدخال الكود
user_code = st.text_area("", placeholder="اكتب كودك هنا...", height=100)

# زر التنفيذ
if st.button("🚀 نفّذ الكود"):
    if user_code:
        try:
            exec(user_code)
            st.markdown('<div class="success">✅ ممتاز! الكود تم تنفيذه بنجاح 👏</div>', unsafe_allow_html=True)
        except:
            st.markdown('<div class="error">❌ فيه خطأ في كتابة الكود، جرّب تراجع الصياغة 👀</div>', unsafe_allow_html=True)
    else:
        st.warning("📌 اكتب الكود أولاً")
س
