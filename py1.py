import streamlit as st

st.set_page_config(page_title="عرض تفاعلي بايثون", layout="centered", page_icon="🐍")

st.title("مرحباً بك في عالم بايثون! 🐍")
st.write("""
هنا تبدأ أول خطوة فعلية في رحلتك البرمجية.  
راح تكتب أول كود لك وتشوف كيف الكمبيوتر يرد عليك!
""")

user_code = st.text_input("✏️ اكتب كود لطباعة 'أنا بدأت أبرمج بايثون' باستخدام print:")

if user_code:
    try:
        exec(user_code)
        st.success("✅ الكود صحيح! ممتاز 👏")
    except:
        st.error("❌ فيه خطأ في الكود، جرّب تراجع الصياغة")

