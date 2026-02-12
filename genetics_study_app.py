#!/usr/bin/env python3
"""
تطبيق دراسة علم الوراثة - Genetics Study App
تطبيق Streamlit تفاعلي لدراسة الوراثة الجينية
"""

import streamlit as st
import random
from typing import Dict, List, Any
import json

# ============================================================
# بيانات JSON المضمنة - Embedded JSON Data
# ============================================================

GENETICS_DATA = {
  "topic": "الوراثة المرتبطة بالكروموزوم (Y)",
  "sections": [
    {
      "id": 1,
      "title": "خصائص الكروموزوم (Y)",
      "introduction": "يُعد الكروموزوم Y فريداً من نوعه في الخارطة الجينية البشرية.",
      "points": [
        {"feature": "الثبات الهيكلي", "description": "هو أكثر الكروموزومات ثباتاً من حيث البنية."},
        {"feature": "مقاومة الطفرات", "description": "يعتبر الأقل تعرضاً للطفرات الجينية مقارنة بغيره."},
        {"feature": "الحماية البيئية", "description": "هو الأقل تأثراً بالعوامل الخارجية والبيئية، مما يجعله مخزناً جينياً آمناً."}
      ]
    },
    {
      "id": 2,
      "title": "تتبع الأصول والأجيال (Genetic Genealogy)",
      "introduction": "يُستخدم كأداة رئيسية بسبب الثبات العالي.",
      "uses": [
        {"type": "تتبع السلالات", "description": "معرفة أصول العائلات والشعوب (من أين انحدرت كل سلالة)."},
        {"type": "الدراسات الجينية التاريخية", "description": "يُعتمد عليه في علم الأنساب الجيني لتحديد المسارات التاريخية للهجرات البشرية من جهة الأب."}
      ]
    },
    {
      "id": 3,
      "title": "الوظائف الجينية للكروموزوم (Y)",
      "introduction": "على الرغم من أن المعلومات حوله كانت تُعتبر ضحلة سابقاً، إلا أن العلم الحديث كشف عن أدوار محورية له.",
      "functions": [
        {"category": "عدد الجينات", "details": "يحتوي على حوالي 200 جين تقريباً."},
        {"category": "الخصوبة والنشاط الجنسي", "details": "معظم جيناته لا تكتفي بتحديد الجنس فقط.", "sub_functions": ["تنشيط النشاط الجنسي.", "تكوين النطاف (Sperms) وحيويتها وكفاءتها."]},
        {"category": "النمو والبنية الجسدية", "details": "هناك جينات (مثل جين SHOX) تعمل بالتنسيق مع الكروموزومات الجسمية (Autosomes).", "sub_functions": ["تحفيز النمو الطولي.", "بناء الكتلة العضلية وقوة العظام."]}
      ]
    }
  ],
  "topics": [
    {
      "id": "review",
      "title": "مراجعة أنماط الوراثة (Inheritance Patterns)",
      "patterns": [
        {"type": "الوراثة الجسمية (Autosomal Inheritance)", "description": "المرتبطة بالكروموزومات غير الجنسية."},
        {"type": "الوراثة المرتبطة بالكروموزوم (X)", "sub_types": ["الوراثة المرتبطة بـ X المتنحية (X-linked Recessive)", "الوراثة المرتبطة بـ X السائدة (X-linked Dominant)"]},
        {"type": "الوراثة المرتبطة بالكروموزوم (Y)", "status": "تمت مناقشتها اليوم", "closing_note": {"statement": "إن الكروموزوم Y ليس مجرد محدد للجنس، بل هو عنصر حيوي في التطور الفيزيولوجي والجسدي للذكر", "future_outlook": "الأبحاث المستقبلية لا تزال تعد بالكثير من الاكتشافات حول جيناته التي كانت تُعتبر صامتة سابقاً."}}
      ]
    },
    {
      "id": "mitochondrial",
      "title": "الوراثة المتقدّرية (Mitochondrial Inheritance)",
      "sections": [
        {"order": 1, "subtitle": "المتقدرة: معامل الطاقة في الخلية", "definition": "تُعرف المتقدرات بأنها محطات توليد الطاقة في الخلية.", "functions": [{"name": "التنفس الخلوي (Cellular Respiration)", "description": "العملية التي تحول الغذاء إلى طاقة."}, {"name": "الأكسدة الفسفرية (Oxidative Phosphorylation)", "description": "المسار الحيوي الذي ينتج جزيئات الـ ATP (الطاقة الكيميائية)."}]},
        {"order": 2, "subtitle": "الاستقلالية الجينية للمتقدرات", "core_feature": "تتميز المتقدرة بامتلاكها مادة وراثية خاصة بها (mtDNA).", "characteristics": [{"feature": "جينوم مستقل", "detail": "تحتوي المتقدرة على DNA خاص بها، منفصل عن جينوم النواة."}, {"feature": "عدد الجينات", "detail": "يحتوي جينوم المتقدرة على 37 جيناً، جميعها مخصصة وحيوية لعملية التنفس الخلوي."}, {"feature": "التنظيم الذاتي", "detail": "تمتلك المتقدرات رايبوزومات (Ribosomes) خاصة بها لتصنيع بروتيناتها داخلياً، مما يجعلها تبدو ككيان مستقل"}]},
        {"order": 3, "subtitle": "العلاقة بين جينوم النواة وجينوم المتقدرة", "context": "بالرغم من استقلالية المتقدرة، إلا أن هناك تعاوناً وثيقاً مع النواة.", "interactions": [{"element": "جينات النواة (nDNA)", "role": "تشرف بشكل غير مباشر على عمل المتقدرة."}, {"element": "الدور البنائي", "role": "بعض الإنزيمات والبروتينات المسؤولة عن بناء هيكل المتقدرة الخارجي وتنشيط عملياتها تُشفر بواسطة جينات موجودة في النواة وليس المتقدرة."}]}
      ]
    }
  ],
  "mitochondrial_diseases": {
    "title": "الأمراض المرتبطة بالوراثة المتقدّرية",
    "fundamental_rule": {"term": "Maternal Inheritance (وراثة أموية)", "explanation": "تنتج عن طفرات في DNA المتقدرة، وتأتي حصراً من البويضة (الأم) لأن النطفة لا تساهم بالمتقدرات للجنين."},
    "inheritance_pattern": {
      "title": "نمط التوريث المتقدّري",
      "description": "يظهر بوضوح في شجرة العائلة (Pedigree) من خلال انحيازه التام لجهة الأم.",
      "golden_rules": [
        {"rule": "الإصابة تشمل الجنسين", "detail": "يصاب الذكور والإناث بالمرض على حد سواء."},
        {"rule": "التوريث عبر الأم فقط", "detail": "الأم المصابة تنقل المورثة لجميع أبنائها (ذكوراً وإناثاً)."},
        {"rule": "الذكور طريق مسدود وراثياً", "detail": "الأب المصاب لا ينقل المرض نهائياً لأي من أبنائه."}
      ]
    }
  },
  "genetic_testing": {
    "title": "التحاليل الجينية (Genetic Testing)",
    "test_types": [
      {"name": "تحليل الكروموزومات (Karyotyping)", "use": "دراسة عدد وشكل الكروموزومات (مثل متلازمة داون).", "level": "الخط الأول", "precision": "منخفضة - يرى الخلل الكبير فقط"},
      {"name": "تقنية FISH", "use": "الكشف عن الحذف والتكرار والتبادل الموضعي.", "level": "الخط الثاني", "precision": "متوسطة - دقة مجهرية"},
      {"name": "تقنية MLPA", "use": "فحص عدة مقاطع جينية (Exons) في وقت واحد.", "level": "الخط الثاني", "precision": "عالية - كشف الحذوفات الميكروية"},
      {"name": "تقنية aCGH", "use": "مسح شامل للجينوم للبحث عن أي نقص أو زيادة.", "level": "الخط الثاني", "precision": "عالية جداً - مسح كامل"},
      {"name": "تسلسل سانجر (Sanger)", "use": "قراءة جين واحد بدقة ذهبية.", "level": "الخط الثالث", "precision": "عالية جداً - المرجع الذهبي"},
      {"name": "تسلسل الإكسوم (WES)", "use": "قراءة جميع الأجزاء الفعالة في الجينات.", "level": "الخط الثالث", "precision": "عالية جداً - 85% من الطفرات"},
      {"name": "تسلسل الجينوم (WGS)", "use": "قراءة المادة الوراثية كاملة.", "level": "الخط الثالث", "precision": "قصوى - 100% من الجينوم"}
    ],
    "indications": [
      {"category": "التنبؤ الصحي المستقبلي", "description": "الكشف عن المخاطر الصحية المستقبلية قبل ظهور الأعراض.", "examples": ["أمراض القلب", "مرض الزهايمر", "جينات BRCA"]},
      {"category": "فحص الحاملين للمرض", "description": "تحديد وجود طفرات متنحية قد تورث للأبناء.", "examples": ["التلاسيميا", "التليف الكيسي"]},
      {"category": "التشخيص قبل الولادة", "description": "الكشف عن الشذوذات الصبغية للجنين.", "examples": ["NIPT", "بزل السلى"]},
      {"category": "علم الجينوم الدوائي", "description": "اختيار الدواء الأنسب بناءً على التركيبة الجينية.", "examples": ["CYP2C19", "Imatinib"]},
      {"category": "علم الأورام والجينات", "description": "تشخيص السرطانات وتحديد المتلازمات المرتبطة بها.", "examples": ["كروموزوم فيلادلفيا", "متلازمة بلوم"]}
    ]
  },
  "case_study": {
    "name": "كروموزوم فيلادلفيا",
    "karyotype_symbol": "t(9;22)(q34;q11)",
    "description": "تبادل قطع بين الكروموزوم 9 والكروموزوم 22",
    "molecular_mechanism": {
      "process": "انتقال متبادل",
      "gene_fusion": "BCR-ABL1 Fusion Gene",
      "result": "بروتين كيناز يعمل كمفتاح تشغيل دائم"
    },
    "clinical_effects": ["انقسام جنوني لخلايا الدم البيضاء", "فشل التمايز الخلوي", "مقاومة الموت الخلوي المبرمج"],
    "diagnosis": {"karyotype": "يرى التبادل الشكلي", "FISH": "يرى تداخل الألوان", "PCR": "يقرأ نقطة الكسر"},
    "treatment": {"drug": "Imatinib (Gleevec)", "mechanism": "مثبط Tyrosine Kinase", "effect": "إغلاق المفتاح الجيني الهجين"}
  },
  "key_concepts": [
    {"term": "DNA Fingerprinting", "definition": "تحديد الهوية عبر تحليل تكرارات STRs", "applications": ["الطب الشرعي", "إثبات النسب", "الكوارث الجماعية"]},
    {"term": "SNP", "definition": "تغير في حرف واحد في الجينوم لدى أكثر من 1% من البشر", "applications": ["التنبؤ بالأمراض", "تحديد المخاطر"]},
    {"term": "PGD", "definition": "الفحص الوراثي قبل الانغراس", "applications": ["منع الأمراض الوراثية"]},
    {"term": "NIPT", "definition": "الفحص غير الجراحي قبل الولادة", "applications": ["كشف متلازمات داون وإدواردز وباتو"]}
  ],
  "syndromes": [
    {"name": "متلازمة داون", "cause": "Trisomy 21", "detection": "Karyotype, FISH, NIPT"},
    {"name": "متلازمة تورنر", "cause": "X0 (Monosomy X)", "detection": "Karyotype, FISH"},
    {"name": "متلازمة كلاينفلتر", "cause": "XXY", "detection": "Karyotype, FISH"},
    {"name": "متلازمة دي جورج", "cause": "حذف 22q11.2", "detection": "FISH, aCGH"},
    {"name": "متلازمة برادر-ويلي", "cause": "حذف 15q11-q13 (أبوي)", "detection": "MS-MLPA"},
    {"name": "متلازمة أنجلمان", "cause": "حذف 15q11-q13 (أمومي)", "detection": "MS-MLPA"},
    {"name": "ضمور العضلات الشوكي (SMA)", "cause": "حذف SMN1", "detection": "MLPA"},
    {"name": "حاصل دوشين العضلي (DMD)", "cause": "طفرات في جين Dystrophin", "detection": "MLPA, Sequencing"}
  ],
  "quiz_questions": [
    {"question": "ما هو عدد الجينات في الكروموزوم Y تقريباً؟", "options": ["50 جين", "200 جين", "500 جين", "1000 جين"], "correct": 1, "explanation": "يحتوي الكروموزوم Y على حوالي 200 جين تقريباً."},
    {"question": "ما هي الوراثة التي تأتي حصراً من الأم؟", "options": ["الوراثة الجسمية", "الوراثة المرتبطة بـ X", "الوراثة المتقدرية", "الوراثة المرتبطة بـ Y"], "correct": 2, "explanation": "الوراثة المتقدرية تأتي حصراً من البويضة (الأم) لأن النطفة لا تساهم بالمتقدرات للجنين."},
    {"question": "ما هي التقنية المعروفة بالمرجع الذهبي للتسلسل الجيني؟", "options": ["NGS", "Sanger Sequencing", "WES", "WGS"], "correct": 1, "explanation": "تسلسل سانجر (Sanger Sequencing) هو المرجع الذهبي بدقة تقترب من 100%."},
    {"question": "ما هو كروموزوم فيلادلفيا؟", "options": ["Trisomy 21", "t(9;22)", "t(8;14)", "X0"], "correct": 1, "explanation": "كروموزوم فيلادلفيا هو تبادل بين الكروموزوم 9 و22 يسبب سرطان الدم CML."},
    {"question": "كم عدد الجينات في جينوم المتقدرة؟", "options": ["13 جين", "37 جين", "200 جين", "50 جين"], "correct": 1, "explanation": "يحتوي جينوم المتقدرة على 37 جيناً، جميعها مخصصة لعملية التنفس الخلوي."},
    {"question": "ما هي التقنية الأفضل لكشف الحذوفات الميكروية في جينات ضخمة مثل DMD؟", "options": ["Karyotype", "FISH", "MLPA", "WES"], "correct": 2, "explanation": "MLPA هي الأفضل لفحص عشرات الإكسونات في جينات ضخمة في تفاعل واحد."},
    {"question": "ما هي نسبة الطفرات الممرضة التي يغطيها WES؟", "options": ["50%", "65%", "85%", "100%"], "correct": 2, "explanation": "WES يغطي 85% من الطفرات الممرضة المعروفة سريرياً."},
    {"question": "الأب المصاب بمرض متقدري ينقل المرض لـ:", "options": ["جميع أبنائه", "أبنائه الذكور فقط", "أبنائه الإناث فقط", "لا ينقله لأي من أبنائه"], "correct": 3, "explanation": "الذكور طريق مسدود وراثياً في الوراثة المتقدرية - لا ينقل المرض نهائياً."},
    {"question": "ما هي التقنية المستخدمة في تحديد الهوية (DNA Fingerprinting)؟", "options": ["SNP", "STR", "CNV", "WGS"], "correct": 1, "explanation": "STR (Short Tandem Repeats) هي التقنية المستخدمة في بصمة DNA."},
    {"question": "ما هو الدواء الموجه لعلاج كروموزوم فيلادلفيا؟", "options": ["Aspirin", "Imatinib", "Insulin", "Metformin"], "correct": 1, "explanation": "Imatinib (Gleevec) هو مثبط Tyrosine Kinase لعلاج CML."}
  ]
}

# ============================================================
# إعدادات الصفحة - Page Configuration
# ============================================================

st.set_page_config(
    page_title="علم الوراثة - Genetics Study",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# RTL Support CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif;
    }
    
    .main {
        direction: rtl;
        text-align: right;
    }
    
    .stSidebar {
        direction: rtl;
        text-align: right;
    }
    
    h1, h2, h3, h4, h5, h6 {
        direction: rtl;
        text-align: right;
    }
    
    .stMarkdown, .stText {
        direction: rtl;
        text-align: right;
    }
    
    .card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 10px 0;
    }
    
    .info-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 15px;
        border-radius: 10px;
        color: white;
        margin: 5px 0;
    }
    
    .warning-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 15px;
        border-radius: 10px;
        color: white;
        margin: 5px 0;
    }
    
    .success-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 15px;
        border-radius: 10px;
        color: white;
        margin: 5px 0;
    }
    
    .quiz-option {
        padding: 10px;
        margin: 5px 0;
        border-radius: 8px;
        border: 2px solid #ddd;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .quiz-option:hover {
        border-color: #667eea;
        background-color: #f0f0f0;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# إدارة الجلسة - Session State Management
# ============================================================

if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_total' not in st.session_state:
    st.session_state.quiz_total = 0
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = []
if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
if 'quiz_answered' not in st.session_state:
    st.session_state.quiz_answered = False
if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = None
if 'flashcard_index' not in st.session_state:
    st.session_state.flashcard_index = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'study_progress' not in st.session_state:
    st.session_state.study_progress = {}

# ============================================================
# الدوال المساعدة - Helper Functions
# ============================================================

def display_card(title: str, content: str, card_type: str = "info"):
    """عرض بطاقة معلومات"""
    css_class = f"{card_type}-card"
    st.markdown(f"""
    <div class="{css_class}">
        <h4>{title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def display_progress(current: int, total: int, label: str = "التقدم"):
    """عرض شريط التقدم"""
    progress = current / total if total > 0 else 0
    st.markdown(f"""
    <div style="margin: 10px 0;">
        <p style="margin-bottom: 5px;">{label}: {current}/{total}</p>
        <div style="background-color: #e0e0e0; border-radius: 5px; overflow: hidden;">
            <div class="progress-bar" style="width: {progress * 100}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# الشريط الجانبي - Sidebar
# ============================================================

def render_sidebar():
    """عرض الشريط الجانبي"""
    st.sidebar.title("🧬 علم الوراثة")
    st.sidebar.markdown("---")
    
    # قائمة التنقل
    page = st.sidebar.radio(
        "اختر القسم:",
        [
            "🏠 الرئيسية",
            "🧬 كروموزوم Y",
            "⚡ الوراثة المتقدرية",
            "🔬 التحاليل الجينية",
            "🏥 المتلازمات",
            "📋 دراسة الحالة",
            "❓ اختبار قصير",
            "🎴 البطاقات التعليمية",
            "🔍 البحث"
        ]
    )
    
    st.sidebar.markdown("---")
    
    # إحصائيات التقدم
    st.sidebar.subheader("📊 إحصائيات")
    if st.session_state.quiz_total > 0:
        accuracy = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
        st.sidebar.metric("نسبة النجاح", f"{accuracy:.1f}%")
        st.sidebar.metric("الإجابات الصحيحة", st.session_state.quiz_score)
        st.sidebar.metric("إجمالي الأسئلة", st.session_state.quiz_total)
    
    # زر إعادة التعيين
    if st.sidebar.button("🔄 إعادة تعيين التقدم"):
        st.session_state.quiz_score = 0
        st.session_state.quiz_total = 0
        st.session_state.quiz_index = 0
        st.session_state.flashcard_index = 0
        st.session_state.study_progress = {}
        st.rerun()
    
    return page

# ============================================================
# صفحات التطبيق - Application Pages
# ============================================================

def home_page():
    """الصفحة الرئيسية"""
    st.title("🧬 مرحباً بك في تطبيق علم الوراثة")
    st.markdown("---")
    
    # بطاقات الترحيب
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>📚 المحتوى</h3>
            <p>دروس شاملة عن الوراثة الجينية</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>❓ اختبارات</h3>
            <p>اختبر معلوماتك بالاختبارات القصيرة</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="success-card">
            <h3>🎴 بطاقات</h3>
            <p>بطاقات تعليمية للمراجعة السريعة</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # المواضيع الرئيسية
    st.header("📖 المواضيع الرئيسية")
    
    topics_data = [
        ("🧬 كروموزوم Y", "خصائصه ووظائفه الجينية", "خصائص الكروموزوم Y وتتبع الأصول"),
        ("⚡ الوراثة المتقدرية", "mtDNA والوراثة الأموية", "الأمراض المرتبطة بالميتوكوندريا"),
        ("🔬 التحاليل الجينية", "Karyotyping إلى WGS", "التقنيات الحديثة في التشخيص"),
        ("🏥 المتلازمات", "داون، تورنر، وغيرها", "الأسباب وطرق الكشف")
    ]
    
    for i, (title, subtitle, desc) in enumerate(topics_data):
        with st.expander(f"{title} - {subtitle}"):
            st.write(desc)
    
    # مفاهيم أساسية
    st.header("💡 مفاهيم أساسية")
    
    cols = st.columns(2)
    for i, concept in enumerate(GENETICS_DATA["key_concepts"]):
        with cols[i % 2]:
            st.info(f"**{concept['term']}**: {concept['definition']}")

def y_chromosome_page():
    """صفحة كروموزوم Y"""
    st.title("🧬 الوراثة المرتبطة بالكروموزوم (Y)")
    st.markdown("---")
    
    for section in GENETICS_DATA["sections"]:
        st.header(f"📌 {section['title']}")
        st.write(section.get('introduction', section.get('reason', '')))
        
        if 'points' in section:
            for point in section['points']:
                st.markdown(f"""
                <div class="info-card">
                    <strong>{point['feature']}</strong><br>
                    {point['description']}
                </div>
                """, unsafe_allow_html=True)
        
        if 'uses' in section:
            for use in section['uses']:
                st.markdown(f"""
                <div class="success-card">
                    <strong>{use['type']}</strong><br>
                    {use['description']}
                </div>
                """, unsafe_allow_html=True)
        
        if 'functions' in section:
            for func in section['functions']:
                with st.expander(f"🔧 {func['category']}"):
                    st.write(func['details'])
                    if 'sub_functions' in func:
                        st.markdown("**الوظائف الفرعية:**")
                        for sf in func['sub_functions']:
                            st.markdown(f"- {sf}")
        
        st.markdown("---")
    
    # مراجعة أنماط الوراثة
    st.header("📋 مراجعة أنماط الوراثة")
    
    patterns = GENETICS_DATA["topics"][0]["patterns"]
    for pattern in patterns:
        with st.expander(f"🔹 {pattern['type']}"):
            if 'description' in pattern:
                st.write(pattern['description'])
            if 'sub_types' in pattern:
                st.markdown("**الأنواع الفرعية:**")
                for stype in pattern['sub_types']:
                    st.markdown(f"- {stype}")
            if 'closing_note' in pattern:
                st.success(f"💡 {pattern['closing_note']['statement']}")
                st.info(f"🔮 {pattern['closing_note']['future_outlook']}")

def mitochondrial_page():
    """صفحة الوراثة المتقدرية"""
    st.title("⚡ الوراثة المتقدّرية (Mitochondrial Inheritance)")
    st.markdown("---")
    
    # المتقدرة
    st.header("🔋 المتقدرة: معامل الطاقة في الخلية")
    
    for section in GENETICS_DATA["topics"][1]["sections"]:
        with st.expander(f"📖 {section['subtitle']}"):
            if 'definition' in section:
                st.info(section['definition'])
            if 'core_feature' in section:
                st.success(section['core_feature'])
            if 'functions' in section:
                for func in section['functions']:
                    st.markdown(f"""
                    <div class="info-card">
                        <strong>{func['name']}</strong><br>
                        {func['description']}
                    </div>
                    """, unsafe_allow_html=True)
            if 'characteristics' in section:
                for char in section['characteristics']:
                    st.markdown(f"- **{char['feature']}**: {char['detail']}")
            if 'interactions' in section:
                for inter in section['interactions']:
                    st.markdown(f"- **{inter['element']}**: {inter['role']}")
    
    # الأمراض المتقدرية
    st.markdown("---")
    st.header("🏥 الأمراض المرتبطة بالوراثة المتقدّرية")
    
    mito_disease = GENETICS_DATA["mitochondrial_diseases"]
    
    st.subheader(mito_disease["title"])
    
    # القاعدة الأساسية
    st.markdown(f"""
    <div class="warning-card">
        <h4>{mito_disease['fundamental_rule']['term']}</h4>
        <p>{mito_disease['fundamental_rule']['explanation']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # القواعد الذهبية
    st.subheader("⭐ القواعد الذهبية للتوريث المتقدّري")
    
    for rule in mito_disease["inheritance_pattern"]["golden_rules"]:
        st.markdown(f"""
        <div class="success-card">
            <strong>{rule['rule']}</strong><br>
            {rule['detail']}
        </div>
        """, unsafe_allow_html=True)
    
    # رسم توضيحي للوراثة
    st.subheader("📊 نمط التوريث المتقدّري")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **✅ الأم المصابة:**
        - تنقل المرض لجميع أبنائها
        - الذكور والإناث يصابون بالتساوي
        
        **❌ الأب المصاب:**
        - لا ينقل المرض لأي من أبنائه
        - طريق مسدود وراثياً
        """)
    
    with col2:
        st.markdown("""
        ```
           أم مريضة         أب سليم
              │                │
              └──────┬─────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
       👦 مريض    👧 مريضة    👦 مريض
        ```

        """)

def genetic_testing_page():
    """صفحة التحاليل الجينية"""
    st.title("🔬 التحاليل الجينية (Genetic Testing)")
    st.markdown("---")
    
    # تصنيف التقنيات
    st.header("📊 مستويات الفحص الجيني")
    
    test_data = GENETICS_DATA["genetic_testing"]["test_types"]
    
    # تقسيم حسب المستوى
    levels = {
        "الخط الأول": [],
        "الخط الثاني": [],
        "الخط الثالث": []
    }
    
    for test in test_data:
        level = test.get("level", "الخط الأول")
        if level in levels:
            levels[level].append(test)
    
    for level, tests in levels.items():
        st.subheader(f"🎯 {level}")
        
        for test in tests:
            with st.expander(f"🔬 {test['name']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**الاستخدام:** {test['use']}")
                with col2:
                    st.markdown(f"**الدقة:** {test['precision']}")
    
    # دواعي إجراء التحاليل
    st.markdown("---")
    st.header("📋 دواعي إجراء التحاليل الجينية")
    
    for ind in GENETICS_DATA["genetic_testing"]["indications"]:
        with st.expander(f"🔹 {ind['category']}"):
            st.write(ind['description'])
            st.markdown("**أمثلة:**")
            for ex in ind['examples']:
                st.markdown(f"- {ex}")
    
    # مقارنة التقنيات
    st.markdown("---")
    st.header("⚖️ مقارنة سريعة بين التقنيات")
    
    comparison_data = {
        "التقنية": [t["name"] for t in test_data],
        "الدقة": [t["precision"] for t in test_data],
        "الاستخدام الرئيسي": [t["use"][:50] + "..." for t in test_data]
    }
    
    st.table(comparison_data)

def syndromes_page():
    """صفحة المتلازمات"""
    st.title("🏥 المتلازمات الجينية")
    st.markdown("---")
    
    syndromes = GENETICS_DATA["syndromes"]
    
    # البحث والفلترة
    search = st.text_input("🔍 ابحث عن متلازمة:")
    
    filtered = [s for s in syndromes if search.lower() in s["name"].lower() or search.lower() in s["cause"].lower()] if search else syndromes
    
    # عرض المتلازمات
    cols = st.columns(2)
    
    for i, syndrome in enumerate(filtered):
        with cols[i % 2]:
            with st.expander(f"🩺 {syndrome['name']}"):
                st.markdown(f"**السبب:** {syndrome['cause']}")
                st.markdown(f"**طرق الكشف:** {syndrome['detection']}")
    
    # إحصائيات
    st.markdown("---")
    st.header("📊 إحصائيات سريعة")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("إجمالي المتلازمات", len(syndromes))
    with col2:
        aneuploidy = len([s for s in syndromes if "Trisomy" in s["cause"] or "Monosomy" in s["cause"] or "XXY" in s["cause"] or "X0" in s["cause"]])
        st.metric("اضطرابات عددية", aneuploidy)
    with col3:
        deletion = len([s for s in syndromes if "حذف" in s["cause"]])
        st.metric("متلازمات حذف", deletion)

def case_study_page():
    """صفحة دراسة الحالة"""
    st.title("📋 دراسة حالة: كروموزوم فيلادلفيا")
    st.markdown("---")
    
    case = GENETICS_DATA["case_study"]
    
    # المعلومات الأساسية
    st.header("🔬 المعلومات الأساسية")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>{case['name']}</h3>
            <p><strong>الرمز:</strong> {case['karyotype_symbol']}</p>
            <p><strong>الوصف:</strong> {case['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="warning-card">
            <h4>الآلية الجزيئية</h4>
            <p><strong>العملية:</strong> {case['molecular_mechanism']['process']}</p>
            <p><strong>الجين المندمج:</strong> {case['molecular_mechanism']['gene_fusion']}</p>
            <p><strong>النتيجة:</strong> {case['molecular_mechanism']['result']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # التأثيرات السريرية
    st.header("⚡ التأثيرات السريرية")
    
    for effect in case['clinical_effects']:
        st.markdown(f"- ⚠️ {effect}")
    
    # طرق التشخيص
    st.markdown("---")
    st.header("🔍 طرق التشخيص")
    
    diag = case['diagnosis']
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>🔬 Karyotype</h4>
            <p>{}</p>
        </div>
        """.format(diag['karyotype']), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-card">
            <h4>🌈 FISH</h4>
            <p>{}</p>
        </div>
        """.format(diag['FISH']), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="warning-card">
            <h4>🧬 PCR</h4>
            <p>{}</p>
        </div>
        """.format(diag['PCR']), unsafe_allow_html=True)
    
    # العلاج
    st.markdown("---")
    st.header("💊 العلاج الموجه")
    
    treatment = case['treatment']
    
    st.markdown(f"""
    <div class="success-card">
        <h3>💊 {treatment['drug']}</h3>
        <p><strong>الآلية:</strong> {treatment['mechanism']}</p>
        <p><strong>التأثير:</strong> {treatment['effect']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ملخص بصري
    st.markdown("---")
    st.header("📊 ملخص بصري للآلية")
    
    st.markdown("""
    ```
    الكروموزوم 9          الكروموزوم 22
         │                      │
         │    ABL1              │    BCR
         │  ┌──────┐            │  ┌──────┐
         └──┤      ├────────────┴──┤      ├──┘
            └──────┘               └──────┘
                    │
                    ▼
            ┌──────────────────┐
            │   BCR-ABL1       │
            │   Fusion Gene    │
            └──────────────────┘
                    │
                    ▼
            ┌──────────────────┐
            │   BCR-ABL        │
            │   Tyrosine       │
            │   Kinase         │
            └──────────────────┘
                    │
                    ▼
            ┌──────────────────┐
            │   CML            │
            │   (سرطان الدم)   │
            └──────────────────┘
    ```
    """)

def quiz_page():
    """صفحة الاختبار القصير"""
    st.title("❓ اختبار قصير")
    st.markdown("---")
    
    # إعداد الاختبار
    if not st.session_state.current_quiz or st.button("🔄 اختبار جديد"):
        st.session_state.current_quiz = random.sample(GENETICS_DATA["quiz_questions"], 
                                                       min(5, len(GENETICS_DATA["quiz_questions"])))
        st.session_state.quiz_index = 0
        st.session_state.quiz_answered = False
        st.session_state.selected_answer = None
        st.rerun()
    
    # عرض التقدم
    total_questions = len(st.session_state.current_quiz)
    current_idx = st.session_state.quiz_index
    
    display_progress(current_idx + 1, total_questions, "السؤال الحالي")
    
    # عرض السؤال الحالي
    if current_idx < total_questions:
        question = st.session_state.current_quiz[current_idx]
        
        st.markdown(f"""
        <div class="card">
            <h3>السؤال {current_idx + 1}</h3>
            <p style="font-size: 18px;">{question['question']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # خيارات الإجابة
        for i, option in enumerate(question['options']):
            button_type = "secondary"
            if st.session_state.quiz_answered:
                if i == question['correct']:
                    button_type = "primary"
            
            if st.button(option, key=f"opt_{i}_{current_idx}", 
                        type=button_type if st.session_state.quiz_answered else "secondary",
                        disabled=st.session_state.quiz_answered):
                st.session_state.selected_answer = i
                st.session_state.quiz_answered = True
                st.session_state.quiz_total += 1
                if i == question['correct']:
                    st.session_state.quiz_score += 1
                st.rerun()
        
        # عرض التفسير
        if st.session_state.quiz_answered:
            is_correct = st.session_state.selected_answer == question['correct']
            
            if is_correct:
                st.success(f"✅ إجابة صحيحة! {question['explanation']}")
            else:
                st.error(f"❌ إجابة خاطئة! الإجابة الصحيحة: {question['options'][question['correct']]}")
                st.info(f"💡 {question['explanation']}")
            
            if st.button("➡️ السؤال التالي"):
                st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.session_state.selected_answer = None
                st.rerun()
    
    else:
        # نهاية الاختبار
        st.header("🎉 انتهى الاختبار!")
        
        if st.session_state.quiz_total > 0:
            accuracy = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("النتيجة", f"{st.session_state.quiz_score}/{st.session_state.quiz_total}")
            with col2:
                st.metric("نسبة النجاح", f"{accuracy:.1f}%")
            with col3:
                if accuracy >= 80:
                    st.metric("التقييم", "⭐⭐⭐ ممتاز!")
                elif accuracy >= 60:
                    st.metric("التقييم", "⭐⭐ جيد")
                else:
                    st.metric("التقييم", "⭐ يحتاج مراجعة")
        
        if st.button("🔄 ابدأ اختباراً جديداً"):
            st.session_state.current_quiz = random.sample(GENETICS_DATA["quiz_questions"], 
                                                           min(5, len(GENETICS_DATA["quiz_questions"])))
            st.session_state.quiz_index = 0
            st.session_state.quiz_answered = False
            st.rerun()

def flashcards_page():
    """صفحة البطاقات التعليمية"""
    st.title("🎴 البطاقات التعليمية")
    st.markdown("---")
    
    # إعداد البطاقات
    flashcards = []
    
    # من المفاهيم الأساسية
    for concept in GENETICS_DATA["key_concepts"]:
        flashcards.append({
            "front": concept["term"],
            "back": concept["definition"],
            "category": "مفاهيم"
        })
    
    # من المتلازمات
    for syndrome in GENETICS_DATA["syndromes"]:
        flashcards.append({
            "front": syndrome["name"],
            "back": f"السبب: {syndrome['cause']}\nالكشف: {syndrome['detection']}",
            "category": "متلازمات"
        })
    
    # من التقنيات
    for test in GENETICS_DATA["genetic_testing"]["test_types"]:
        flashcards.append({
            "front": test["name"],
            "back": f"الاستخدام: {test['use']}\nالدقة: {test['precision']}",
            "category": "تقنيات"
        })
    
    # فلترة حسب الفئة
    categories = list(set([f["category"] for f in flashcards]))
    selected_category = st.selectbox("📂 اختر الفئة:", ["الكل"] + categories)
    
    if selected_category != "الكل":
        flashcards = [f for f in flashcards if f["category"] == selected_category]
    
    # عرض البطاقة الحالية
    if flashcards:
        idx = st.session_state.flashcard_index % len(flashcards)
        card = flashcards[idx]
        
        # بطاقة تفاعلية
        if st.session_state.show_answer:
            st.markdown(f"""
            <div class="success-card" style="text-align: center; padding: 40px; min-height: 200px;">
                <h3>{card['front']}</h3>
                <hr style="border-color: white;">
                <p style="font-size: 18px;">{card['back']}</p>
                <p><small>📁 {card['category']}</small></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="card" style="text-align: center; padding: 40px; min-height: 200px;">
                <h2>{card['front']}</h2>
                <p>📁 {card['category']}</p>
                <p><small>انقر على "إظهار الإجابة"</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        # أزرار التحكم
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("⬅️ السابق"):
                st.session_state.flashcard_index = (idx - 1) % len(flashcards)
                st.session_state.show_answer = False
                st.rerun()
        
        with col2:
            if st.button("👁️ إظهار/إخفاء الإجابة"):
                st.session_state.show_answer = not st.session_state.show_answer
                st.rerun()
        
        with col3:
            if st.button("➡️ التالي"):
                st.session_state.flashcard_index = (idx + 1) % len(flashcards)
                st.session_state.show_answer = False
                st.rerun()
        
        # شريط التقدم
        display_progress(idx + 1, len(flashcards), "البطاقة الحالية")
        
        # خلط البطاقات
        if st.button("🔀 خلط البطاقات"):
            random.shuffle(flashcards)
            st.session_state.flashcard_index = 0
            st.session_state.show_answer = False
            st.rerun()

def search_page():
    """صفحة البحث"""
    st.title("🔍 البحث في المحتوى")
    st.markdown("---")
    
    # حقل البحث
    search_query = st.text_input("🔎 أدخل كلمة البحث:", placeholder="مثال: DNA, متلازمة, كروموزوم...")
    
    if search_query:
        results = []
        query_lower = search_query.lower()
        
        # البحث في الأقسام
        for section in GENETICS_DATA["sections"]:
            if query_lower in section["title"].lower():
                results.append({"type": "قسم", "title": section["title"], "source": "كروموزوم Y"})
            for point in section.get("points", []):
                if query_lower in point["feature"].lower() or query_lower in point["description"].lower():
                    results.append({"type": "ميزة", "title": point["feature"], "source": section["title"]})
        
        # البحث في المتلازمات
        for syndrome in GENETICS_DATA["syndromes"]:
            if query_lower in syndrome["name"].lower() or query_lower in syndrome["cause"].lower():
                results.append({"type": "متلازمة", "title": syndrome["name"], "source": syndrome["cause"]})
        
        # البحث في التقنيات
        for test in GENETICS_DATA["genetic_testing"]["test_types"]:
            if query_lower in test["name"].lower() or query_lower in test["use"].lower():
                results.append({"type": "تقنية", "title": test["name"], "source": test["use"][:50]})
        
        # عرض النتائج
        st.subheader(f"📋 نتائج البحث ({len(results)})")
        
        if results:
            for result in results:
                with st.expander(f"📌 {result['title']} ({result['type']})"):
                    st.write(f"**المصدر:** {result['source']}")
        else:
            st.warning("لم يتم العثور على نتائج. جرب كلمة بحث مختلفة.")
    
    # اقتراحات
    st.markdown("---")
    st.header("💡 اقتراحات للبحث")
    
    suggestions = ["DNA", "متلازمة داون", "كروموزوم", "FISH", "WES", "متقدرة", "وراثة", "SMA"]
    
    cols = st.columns(4)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 4]:
            if st.button(suggestion, key=f"sug_{i}"):
                st.rerun()

# ============================================================
# التشغيل الرئيسي - Main Execution
# ============================================================

def main():
    """الوظيفة الرئيسية"""
    page = render_sidebar()
    
    # توجيه الصفحات
    if page == "🏠 الرئيسية":
        home_page()
    elif page == "🧬 كروموزوم Y":
        y_chromosome_page()
    elif page == "⚡ الوراثة المتقدرية":
        mitochondrial_page()
    elif page == "🔬 التحاليل الجينية":
        genetic_testing_page()
    elif page == "🏥 المتلازمات":
        syndromes_page()
    elif page == "📋 دراسة الحالة":
        case_study_page()
    elif page == "❓ اختبار قصير":
        quiz_page()
    elif page == "🎴 البطاقات التعليمية":
        flashcards_page()
    elif page == "🔍 البحث":
        search_page()

if __name__ == "__main__":
    main()
