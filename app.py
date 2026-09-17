import streamlit as st
import pandas as pd

# إعداد واجهة الأداة
st.set_page_config(page_title="أداة صفاء الذكية للمحتوى والنمو", layout="wide")

st.title("🎯 أداة صفاء المتقدمة لتحليل المحتوى واستخراج الكلمات والسيناريوهات")
st.write("أداتكِ الخاصة لتوليد الكلمات المفتاحية، أفكار الفيديوهات الفايرال، والسيناريوهات باللغتين العربية والإنجليزية.")

# الشريط الجانبي للإعدادات
st.sidebar.header("⚙️ إعدادات الأداة")

selected_language = st.sidebar.selectbox(
    "لغة العمل والمحتوى:",
    ["العربية (Arabic)", "الإنجليزية (English)"]
)

target_platform = st.sidebar.selectbox(
    "المنصة المستهدفة:",
    ["يوتيوب (YouTube)", "تيك توك (TikTok)", "إنستجرام (Instagram)", "فيسبوك (Facebook)"]
)

st.sidebar.markdown("---")
page_mode = st.sidebar.radio(
    "اخترِ القسم المطلوب:",
    ["🔥 توليد أفكار والخطافات (Hooks)", "🔑 الكلمات المفتاحية والهاشتاجات المخصصة", "💡 صياغة نصوص وسيناريوهات الفيديوهات"]
)

# ---------------------------------------------------------
# القسم الأول: توليد أفكار والخطافات بناءً على ما تكتبينه
# ---------------------------------------------------------
if page_mode == "🔥 توليد أفكار والخطافات (Hooks)":
    st.header("🔥 مولد الأفكار والخطافات الفايرال الذكي")
    
    user_topic = st.text_input("اكتبِ المجال أو الشخصية أو الموضوع الذي تريدين العمل عليه (مثلاً: احمد يونس، قصص أطفال، تسويق):", "")
    
    if user_topic:
        st.success(تم توليد الأفكار بنجاح لـ: `{user_topic}` باللغة `{selected_language}`)
        
        if "العربية" in selected_language:
            ideas_df = pd.DataFrame({
                "فكرة الفيديو المقترحة": [
                    f"السر الخفي وراء نجاح {user_topic} الذي لم يلاحظه أحد",
                    f"لماذا يفشل الجميع في {user_topic}، وكيف تتجنب ذلك؟",
                    f"تجربة شخصية: ماذا حدث عندما طبقت قاعدة {user_topic} لمدة 24 ساعة؟"
                ],
                "نوع الخطاف (Hook) لجذب الانتباه في أول ثوانٍ": [
                    "بدء الفيديو بصدمة بصرية أو معلومة غير متوقعة تماماً",
                    "طرح سؤال استفزامي يجعل المشاهد ينتظر الإجابة للنهاية",
                    "عرض النتيجة النهائية المرغوبة فوراً قبل بدء القصة"
                ],
                "احتمالية الانتشار": ["عالية جداً 🔥", "مرتفعة", "قوية"]
            })
        else:
            ideas_df = pd.DataFrame({
                "Suggested Video Idea": [
                    f"The secret behind {user_topic} nobody is talking about",
                    f"Why most people fail at {user_topic} and how to fix it",
                    f"What happened when I tried {user_topic} for 24 hours"
                ],
                "Viral Hook (First 3 Seconds)": [
                    "Start with a shocking visual or an unexpected fact",
                    "Ask a provocative question that keeps viewers watching",
                    "Show the final amazing result right at the beginning"
                ],
                "Viral Potential": ["Very High 🔥", "High", "Strong"]
            })
            
        st.table(ideas_df)

# ---------------------------------------------------------
# القسم الثاني: الكلمات المفتاحية والهاشتاجات المخصصة
# ---------------------------------------------------------
elif page_mode == "🔑 الكلمات المفتاحية والهاشتاجات المخصصة":
    st.header("🔑 استخراج الكلمات المفتاحية والهاشتاجات الحقيقية")
    
    keyword_input = st.text_input("اكتبِ الكلمة أو الاسم لاستخراج كلماتها المفتاحية:", "قصص أطفال")
    
    if keyword_input:
        col1, col2 = st.columns(2)
        
        if "العربية" in selected_language:
            with col1:
                st.subheader("📌 الكلمات المفتاحية لمحركات البحث (SEO):")
                st.code(f"{keyword_input}, أسرار {keyword_input}, كيف أبدأ في {keyword_input}, أفضل طريقة لـ {keyword_input}, دليلك الشامل لـ {keyword_input}, تجربة {keyword_input}", language="text")
            with col2:
                st.subheader("🏷️ الهاشتاجات الفايرال:")
                st.code(f"#{keyword_input.replace(' ', '')} #اكسبلور #تريند #محتوى_هادف #مبدع #2026", language="text")
        else:
            with col1:
                st.subheader("📌 SEO Keywords:")
                st.code(f"{keyword_input}, best {keyword_input}, how to {keyword_input}, ultimate guide to {keyword_input}, {keyword_input} tips, secrets of {keyword_input}", language="text")
            with col2:
                st.subheader("🏷️ Viral Hashtags:")
                st.code(f"#{keyword_input.replace(' ', '')} #trending #viral #contentcreator #explore #2026", language="text")

# ---------------------------------------------------------
# القسم الثالث: صياغة النصوص والسيناريوهات
# ---------------------------------------------------------
elif page_mode == "💡 صياغة نصوص وسيناريوهات الفيديوهات":
    st.header("💡 مساعدك الذكي لكتابة السيناريو (Scriptwriting Assistant)")
    
    script_topic = st.text_input("اكتبِ عنوان أو موضوع الفيديو الذي ستصورينه:", "")
    
    if script_topic:
        st.info(f"📝 **هيكل السيناريو المقترح لفيديو ({script_topic}) على منصة {target_platform}:**")
        st.markdown(f"""
        1. **المقدمة / الخطاف (0 إلى 5 ثوانٍ):** 
           * *النص المقترح:* "هل تظن أنك تعلم كل شيء عن {script_topic}؟ ما ستراه الآن سيغير رأيك تماماً..."
        2. **المشكلة أو إثارة الفضول (5 إلى 30 ثانية):** 
           * استعراض تفاصيل المشكلة أو القصة بطريقة سريعة وجذابة تمنع المشاهد من مغادرة الفيديو.
        3. **المحتوى الجوهري (لب الفيديو):** 
           * تقديم النقاط الأساسية أو الحلول بشكل مرتب ومبسط.
        4. **الخاتمة ودعوة لاتخاذ إجراء (CTA):** 
           * *النص المقترح:* "إذا اعجبتك القصة، اكتب رأيك في التعليقات واشترك ليوصلك كل جديد!"
        """)
