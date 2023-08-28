import requests
import streamlit as st
from streamlit_lottie import st_lottie




st.set_page_config(page_title="مصنف الأسماء العربية", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("مرحبًا، أنا آلة تصنيف الأسماء العربية :wave:")
    st.title("أستطيع أن أصنف الأسماء العربية حسب الجنس ")
    

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("ماذا أفعل ؟")
        st.write("##")
        st.write(
            """
            ذكاؤنا الصناعي يقوم بتحليل الاسم إما على مستوى صوتي، حيث يتم تحليل الأصوات الموجودة في الاسم، أو على مستوى الأحرف، حيث يتم تحليل ترتيب وأنواع الأحرف في الاسم. هذا التحليل يمكن أن يوفر تفاصيل مهمة تتعلق بالاسم وقد يكون له تأثير كبير على التنبؤ بالجنس
            
            استخدام ملامح محددة للأسماء:
            نحن نأخذ ملامح معينة من الأسماء لاستخدامها في التنبؤ بالجنس. مثلًا، نأخذ في الاعتبار الحرف الأول في الاسم والحرف الأخير، وقد تشمل الملامح الأخرى أنماط الأحرف الموجودة في الاسم
            
            استخدام خوارزميات تعلم الآلة:
            استخدام تقنيات تعلم الآلة، يقوم الذكاء الصناعي بتدريب نماذج تعتمد على البيانات المتاحة لديه. يتم تزويد هذه النماذج بالملامح المأخوذة من الأسماء بالإضافة إلى البيانات المعروفة عن جنس الأشخاص ذوي تلك الأسماء. بناءً على هذه البيانات، تتعلم النماذج كيفية ربط ملامح الأسماء بجنسها
            
            التنبؤ بالجنس:
            بعد تدريب النماذج ومعرفة كيفية ترجمة الملامح إلى توقعات بناءً على بيانات التدريب، يمكن للذكاء الصناعي أن يستخدم هذه النماذج للتنبؤ بجنس الأسماء الجديدة التي تم تقديمها إليه
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")



# ---- Try the AI ----
with st.container():
    st.write("---")
    st.header("جرب الآن")
    st.write("##")
    user_input = st.text_input("أدخل اسمك الكامل", "")
    
    if st.button("أرسل"):
        response = requests.post('http://mlapi:5000/predict', json={'text': user_input})
        
        if response.status_code == 200:
            predictions = response.json()
            st.write("توقع:", predictions)
        else:
            st.write("Error:", response.text)