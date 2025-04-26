import streamlit as st

def main():
    st.set_page_config(
        page_title="우리의 페르소나 - 퇴사연구소",
        page_icon="🎭",
        layout="wide"
    )

    # CSS 스타일 정의
    st.markdown("""
    <style>
        /* 폰트 및 전체 배경 */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap');

        html, body, [data-testid="stApp"] {
            font-family: 'Noto Sans KR', sans-serif;
            background-color: white; /* 하얀 배경 */
            color: #374151; /* 기본 글자색 */
        }

        /* 앱 컨테이너 중앙 정렬 */
        .app-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* 헤더 */
        .header {
            text-align: center;
            margin-bottom: 3rem;
        }
        .title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #111827;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            font-size: 1.25rem;
            color: #6B7280;
        }

        /* 콘텐츠 박스 */
        .content-section {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            margin-bottom: 2rem;
            border: 1px solid #E5E7EB;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        }
        .content-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        .content-text {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #4B5563;
        }
        .quote {
            background: #F9FAFB;
            border-left: 4px solid #3B82F6;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            font-style: italic;
            margin: 1.5rem 0;
            color: #4B5563;
        }

        /* 페르소나 카드 레이아웃 */
        .persona-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .persona-card {
            background: #ffffff;
            border: 1px solid #E5E7EB;
            border-radius: 0.75rem;
            padding: 1.5rem;
            transition: box-shadow 0.3s ease;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: start;
            margin-bottom: 15px;
        }
        .persona-card:hover {
            box-shadow: 0 6px 10px rgba(0,0,0,0.08);
        }
        .persona-title {
            font-size: 1.25rem;
            font-weight: 600;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }
        .persona-subtitle {
            font-size: 1rem;
            color: #6B7280;
            margin-bottom: 1rem;
        }
        .persona-description {
            font-size: 0.95rem;
            color: #4B5563;
            line-height: 1.6;
        }

        /* 푸터 */
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #9CA3AF;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #E5E7EB;
        }
    </style>
    """, unsafe_allow_html=True)

    # 앱 시작
    st.markdown('<div class="app-container">', unsafe_allow_html=True)

    # 헤더
    st.markdown("""
    <div class="header">
        <div class="title">🎭 우리의 페르소나</div>
        <div class="subtitle">퇴사는 감정이 아니라 전략이다 - 퇴사연구소 일동</div>
    </div>
    """, unsafe_allow_html=True)

    # 페르소나 소개
    st.markdown("""
    <div class="content-section">
        <div class="content-title">페르소나란?</div>
        <div class="content-text">
            <strong>페르소나(persona)</strong>는 원래 연극에서 배우가 쓰던 '가면'에서 유래한 말이에요.<br>
            심리학에서는 '사회적 역할' 또는 '타인에게 보여지는 나'를 의미하죠.<br>
            서비스 기획에서는 제품이나 서비스의 주요 고객을 대표하는 가상의 인물을 뜻하기도 해요.
        </div>
        <div class="quote">
            진짜 나와는 조금 다를 수 있지만, 사회와 관계 속에서 내가 보여주는 모습,<br>
            또는 우리 팀이 세상에 보여주고 싶은 얼굴이 바로 페르소나입니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 퇴사연구소 철학
    st.markdown("""
    <div class="content-section">
        <div class="content-title">퇴사연구소의 철학</div>
        <div class="quote">
            퇴사는 감정이 아니라 전략이다.
        </div>
        <div class="content-text">
            우리는 퇴사를 단순한 감정적 선택이 아닌,<br>
            더 나은 커리어와 삶을 위한 전략적 결정으로 바라봅니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 사주풀이 설명
    st.markdown("""
    <div class="content-section">
        <div class="content-title">퇴사연구소 사주풀이</div>
        <div class="content-text">
            퇴사연구소에는 각기 다른 색깔과 전문성을 가진 5명의 연구원이 있습니다.<br>
            각 연구소(팀원)의 페르소나를 클릭해 사주풀이처럼 만나보세요!
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 페르소나 카드
    persona_list = [
        {"이름": "김륜영", "연구소": "통장연구소", "설명": "설명..", "이모지": "💰"},
        {"이름": "안지원", "연구소": "팩트폭격연구실", "설명": "설명..", "이모지": "💣"},
        {"이름": "최석호", "연구소": "직무 분석 연구소", "설명": "설명..", "이모지": "🔍"},
        {"이름": "하상우", "연구소": "쇼생크 랩스", "설명": "설명..", "이모지": "🕊️"},
        {"이름": "전나영", "연구소": "떠남점검 연구소", "설명": "설명..", "이모지": "🧳"},
    ]

    st.markdown('<div class="persona-grid">', unsafe_allow_html=True)
    for persona in persona_list:
        st.markdown(f"""
        <div class="persona-card">
            <div class="persona-title">
                <span>{persona['이모지']}</span>
                <span>{persona['이름']}</span>
            </div>
            <div class="persona-subtitle"><strong>연구소:</strong> {persona['연구소']}</div>
            <div class="persona-description">{persona['설명']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        © 2024 퇴사연구소. All rights reserved.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
