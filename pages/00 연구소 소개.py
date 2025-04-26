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
            # text-align: center;
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
            # justify-content: center;
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
            각 연구소(연구원)의 페르소나를 클릭해 사주풀이처럼 만나보세요!
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 페르소나 카드
    persona_list = [
        {"이름": "전나영 연구원", "연구소": "떠남점검 랩", "설명": "인사담당자 시절, 퇴사하려는 직원들을 붙잡는 게 일이었다. 그 경험 덕분에, 퇴사를 결심하는 심리를 연구하게 됐다. 퇴사가 정말 최선인가 혹은 퇴사를 하는 게 맞나 싶다면, 이 연구원이 대답해줄 수 있다.", "이모지": "🧳"},
        {"이름": "안지원 연구원", "연구소": "팩트폭격 랩", "설명": "감정 위로는 없다. 오직 냉철한 데이터와 현실만 있을 뿐. 팩트폭격랩은 당신의 이력을 철저히 분석하고, 현재 채용시장의 실태와 비교해 이직 성공 확률을 계산한다. '니가 사표 던지기 전에, 최소한 현실은 보고 가라.' 지금 퇴사하면 백수 될 확률부터 최적의 퇴사 타이밍까지, 모든 현실을 직설적으로 알려준다. 감성적인 위로보다 냉정한 현실 체크가 필요하면, 팩트폭격랩의 문을 두드려라.", "이모지": "💣"},
        {"이름": "김륜영 연구원", "연구소": "텅장 랩", "설명": "당신의 통장, 과연 퇴사를 허락할까? 텅장랩은 월 생활비, 대출 상환액, 현재 자산을 분석해 퇴사 가능성을 객관적으로 진단해준다. 퇴사는 감정이 아니라 현실이다 텅장랩과 함께 현실적인 선택을 하길 바란다", "이모지": "💰"},
        {"이름": "하상우 연구원", "연구소": "쇼생크 랩", "설명": "탈옥처럼 체계적이고 치밀한 퇴사/이직 준비! 이제 쇼생크 랩에서 여러분의 성공적인 탈옥(퇴사/이직)을 준비해보세요!", "이모지": "🕊️"},
        {"이름": "최석호 연구원", "연구소": "직무 분석 랩", "설명": "다양한 직무에 대한 채용 공고 수를 분석하여, 각 직무가 시장에서 얼마나 많이 요구되는지 파악하자.", "이모지": "🔍"},
    ]

    st.markdown('<div class="persona-grid">', unsafe_allow_html=True)
    for persona in persona_list:
        lab_url = f"/{persona['연구소'].replace(' ', '_')}"  # 띄어쓰기를 _로 변환
        st.markdown(f"""
        <a href="{lab_url}" target="_self" style="text-decoration:none;color:inherit;">
            <div class="persona-card">
                <div class="persona-title">
                    <span>{persona['이모지']}</span>
                    <span>{persona['이름']}</span>
                </div>
                <div class="persona-subtitle"><strong>담당 연구소:</strong> {persona['연구소']}</div>
                <div class="persona-description">{persona['설명']}</div>
            </div>
        </a>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        © 2025 퇴사연구소. All rights reserved.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
