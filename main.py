import streamlit as st

def main():
    st.set_page_config(
        page_title="퇴사연구소",
        page_icon="🧑‍💼",
        layout="centered"
    )

    if 'show_content' not in st.session_state:
        st.session_state.show_content = False

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800&display=swap');
        
        html, body, [data-testid="stApp"] {
            font-family: 'Noto Sans KR', sans-serif;
            background-color: white;
            color: #374151;
        }

        .main {
            background: white;
            padding: 4rem 3rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
            animation: fadeIn 1.2s ease;
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
            transition: opacity 0.7s cubic-bezier(.4,0,.2,1), transform 0.7s cubic-bezier(.4,0,.2,1);
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
            transition: opacity 0.7s cubic-bezier(.4,0,.2,1), transform 0.7s cubic-bezier(.4,0,.2,1);
        }

        .info-box.show {
            opacity: 1;
            transform: translateY(0);
        }

        /* 버튼 */
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
            transition: all 0.3s ease;
            margin-top: 2rem;
            box-shadow: 0 6px 12px rgba(99, 102, 241, 0.3);
        }

        div[data-testid="stButton"] button:hover,
        div[data-testid="stButton"] button:active,
        div[data-testid="stButton"] button:focus {
            background: linear-gradient(90deg, #4f46e5, #6366f1);
            color: white !important;
            outline: none;
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4);
        }

        /* 아코디언 */
        .accordion-area {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.8s cubic-bezier(.4,0,.2,1);
            will-change: max-height;
        }

        .accordion-area.show {
            max-height: 1000px;
            transition: max-height 0.8s cubic-bezier(.4,0,.2,1);
        }

        /* box */
        .box {
            background: white;
            padding: 4rem 3rem;
            border-radius: 30px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
            animation: fadeIn 1.2s ease;
        }

        /* 이미지 흔들기 및 중앙정렬 */
        div[data-testid="stImage"] {
            display: flex;
            justify-content: center;
            width: 100%;
        }

        div[data-testid="stImage"] img {
            display: block;
            animation: shake 2s infinite;
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

    st.image("images/logo.png", width=460)
    st.markdown('<h2 class="subtitle">이직을 고민하는 당신을 위한 커리어 연구소</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p class="description">
        <strong>퇴사연구소</strong>는 이직을 고민하는 분들이<br>
        이력서와 포트폴리오를 업로드하면,<br>
        AI와 데이터가 최신 채용 시장 정보를 분석해<br>
        맞춤형 이직 조언과 추천을 제공하는 서비스입니다.
    </p>
    """, unsafe_allow_html=True)

    if st.button("시작하기", key="start_btn"):
        st.session_state.show_content = True

    show_class = "show" if st.session_state.show_content else ""
    st.markdown(f"""
    <div class="accordion-area {show_class}">
        <div class="feature-grid">
            <div class="feature-item {show_class}">
                <div class="feature-icon">📊</div>
                <div class="feature-title">데이터 기반 분석</div>
                <div class="feature-description">실시간 채용 시장 데이터를 통한 깊이 있는 인사이트 제공</div>
            </div>
            <div class="feature-item {show_class}">
                <div class="feature-icon">🤖</div>
                <div class="feature-title">AI 맞춤 추천</div>
                <div class="feature-description">AI 기반 개인 맞춤형 커리어 플랜과 기업 추천</div>
            </div>
            <div class="feature-item {show_class}">
                <div class="feature-icon">🚀</div>
                <div class="feature-title">커리어 성장 지원</div>
                <div class="feature-description">지속 가능한 성장 전략과 커리어 코칭 제공</div>
            </div>
        </div>
        <hr>
        <div class="info-box {show_class}">
            🎯 왼쪽 사이드바에서 필요한 메뉴를 선택해 시작하세요!
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
