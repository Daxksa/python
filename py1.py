import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="أول كود بايثون", page_icon="👨‍💻", layout="centered")

# تنسيقات CSS مخصصة
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #4F8BF9;
            margin-bottom: 20px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #333;
        }
        .codebox textarea {
            font-size: 18px !important;
            background-color: #f0f0f0 !important;
        }
        .success {
            background-color: #d2f8d2;
            color: #207520;
            padding: 10px;
            border-radius: 8px;
        }
        .error {
            background-color: #ffd9d9;
            color: #a60000;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.markdown('<div class="title">👋 مرحباً بك في عالم بايثون!</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">هنا تبدأ أول خطوة فعلية في رحلتك البرمجية 💻<br>اكتب أول كود لك وشوف كيف الكمبيوتر يستجيب لأوامرك!</div><br>', unsafe_allow_html=True)

# إدخال الكود من المستخدم
user_code = st.text_area("🧠 اكتب كود يستخدم print ويطبع: 'أنا بدأت أبرمج بايثون'", height=100)

# زر تنفيذ الكود
if st.button("🚀 نفّذ الكود"):
    if user_code:
        try:
            exec(user_code)
            st.markdown('<div class="success">✅ ممتاز! الكود تم تنفيذه بنجاح 👏</div>', unsafe_allow_html=True)
        except:
            st.markdown('<div class="error">❌ فيه خطأ في كتابة الكود، جرّب تراجع الصياغة 👀</div>', unsafe_allow_html=True)
    else:
        st.warning("📌 اكتب الكود أولاً")

