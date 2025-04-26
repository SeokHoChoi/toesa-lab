import streamlit as st

def main():
    st.set_page_config(
        page_title="퇴사연구소",
        page_icon="🧑‍💼",
        layout="centered"
    )

    st.sidebar.title("퇴사연구소")

    if 'show_content' not in st.session_state:
        st.session_state.show_content = False

    # CSS 적용
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800&display=swap');
        div[data-testid="stApp"] {
            font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
            background-color: white;
            color: #374151;
            padding: 2rem 1rem;
        }
        .main {
            background: white;
            padding: 4rem 3rem;
            # box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
            animation: fadeIn 1.2s ease;
            # border-radius: 30px;
            # max-width: 900px;
            margin: 0 auto;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .title {
            background: linear-gradient(90deg, #6a11cb, #2575fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3.5rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 1rem;
        }
        .subtitle {
            font-size: 1.6rem;
            font-weight: 600;
            color: #4b5563;
            text-align: center;
            margin-bottom: 1rem;
        }
        .description {
            font-size: 1.2rem;
            color: #6b7280;
            line-height: 1.8;
            text-align: center;
            margin-bottom: 3rem;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        .feature-item {
            background: linear-gradient(135deg, #eef2f7, #ffffff);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            opacity: 0;
            transform: translateY(40px);
        }
        .feature-item.show {
            opacity: 1;
            transform: translateY(0);
        }
        .feature-icon {
            font-size: 2.5rem;
            color: #6366f1;
            margin-bottom: 1rem;
        }
        .feature-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #374151;
            margin-bottom: 0.5rem;
        }
        .feature-description {
            font-size: 1rem;
            color: #6b7280;
        }
        .info-box {
            background: linear-gradient(135deg, #c7d2fe, #e0e7ff);
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            font-size: 1.2rem;
            font-weight: 500;
            color: #3730a3;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
            opacity: 0;
            transform: translateY(40px);
        }
        .info-box.show {
            opacity: 1;
            transform: translateY(0);
        }
        div[data-testid="stButton"] {
            display: flex;
            justify-content: center;
        }
        div[data-testid="stButton"] button {
            background: linear-gradient(90deg, #6366f1, #4f46e5);
            color: white !important;
            font-size: 1.2rem;
            font-weight: 600;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            margin-top: 2rem;
            box-shadow: 0 6px 12px rgba(99, 102, 241, 0.3);
        }
        div[data-testid="stButton"] button:hover {
            background: linear-gradient(90deg, #4f46e5, #6366f1);
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4);
        }
        div[data-testid="stImage"] {
            display: flex;
            justify-content: center;
            width: 100vw;
        }
        div[data-testid="stImage"] img {
            animation: shake 2s infinite;
            margin-left: auto;
            margin-right: auto;
        }
        @keyframes shake {
            0% { transform: translateX(0);}
            10% { transform: translateX(-6px);}
            20% { transform: translateX(6px);}
            30% { transform: translateX(-6px);}
            40% { transform: translateX(6px);}
            50% { transform: translateX(0);}
            100% { transform: translateX(0);}
        }
        @media (max-width: 768px) {
            .main { padding: 2rem 1.5rem; }
            .title { font-size: 2.5rem; }
            .subtitle { font-size: 1.2rem; }
            .description { font-size: 1rem; }
        }
    </style>
    """, unsafe_allow_html=True)

    # 반드시 직접 div로 감싸고, 클래스 지정!
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.image("images/logo.png", width=460)
    # st.markdown('<div class="title">퇴사연구소</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">이직을 고민하는 당신을 위한 커리어 연구소</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="description">
        <strong>퇴사연구소</strong>는 체계적이고 합리적인 퇴사 결정을 지원하기 위해<br>
        다각도로 분석하고 방향을 제시하는 AI 기반 상담 및 분석 서비스입니다.<br>
    </div>
    """, unsafe_allow_html=True)

    if st.button("왜 감정이 아닌 전략이어야 할까?", key="start_btn"):
        st.session_state.show_content = True

    show_class = "show" if st.session_state.show_content else ""
    st.markdown(f"""
    <div class="accordion-area {show_class}">
        <div class="feature-grid">
            <div class="feature-item {show_class}">
                <div class="feature-icon">⚠️</div>
                <div class="feature-title">감정적인 퇴사는</div>
                <div class="feature-description">
                  높은 리스크를 수반합니다.
                </div>
            </div>
            <div class="feature-item {show_class}">
                <div class="feature-icon">📉</div>
                <div class="feature-title">데이터 없이 결정한 퇴사는</div>
                <div class="feature-description">
                    커리어에 손해를 입힙니다.
                </div>
            </div>
            <div class="feature-item {show_class}">
                <div class="feature-icon">💸 </div>
                <div class="feature-title">준비없이 서두른 퇴사는</div>
                <div class="feature-description">경제적 불안을 야기합니다.</div>
            </div>
            <div class="feature-item {show_class}">
                <div class="feature-icon">⏳</div>
                <div class="feature-title">방향성 없는 퇴사는</div>
                <div class="feature-description">시간 낭비로 이어집니다.</div>
            </div>
        </div>
        <hr>
        <div class="info-box {show_class}">
            🎯 왼쪽 사이드바에서 다양한 퇴직 연구소들을 체험하세요!
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # .main 닫기

if __name__ == "__main__":
    main()
