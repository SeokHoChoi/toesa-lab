import streamlit as st

def display_job_categories_and_keywords(data):
    st.set_page_config(
        page_title="채용공고 분석",
        page_icon="📊",
        layout="wide"
    )

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap');
        
        * {
            font-family: 'Noto Sans KR', sans-serif;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: #F9FAFB;
        }

        .header {
            padding: 2rem 0;
            text-align: center;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 0 0 1.5rem 1.5rem;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }

        .title {
            font-size: 1.5rem;
            font-weight: 700;
            letter-spacing: -0.5px;
        }

        .category-card {
            background: white;
            border-radius: 1rem;
            padding: 2rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            border: 1px solid #E5E7EB;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .category-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        }

        .category-title {
            font-size: 1.8rem;
            font-weight: 700;
            color: #374151;
            margin-bottom: 1.5rem;
        }

        .category-description {
            font-size: 1rem;
            color: #6B7280;
            margin-bottom: 1.5rem;
        }

        .keyword-list {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .keyword-item {
            background: #E5E7EB;
            padding: 0.5rem 1.5rem;
            border-radius: 1.25rem;
            font-size: 1rem;
            color: #4B5563;
            transition: all 0.3s ease;
            cursor: pointer;
            margin-bottom: 10px;
        }

        .keyword-item:hover {
            background: #D1D5DB;
            transform: translateY(-2px);
        }

        .metric-card {
            background: white;
            border-radius: 1rem;
            padding: 2rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            text-align: center;
            border: 1px solid #E5E7EB;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin-bottom: 50px;
        }

        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        }

        .metric-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #2563EB;
            margin-bottom: 0.75rem;
        }

        .metric-label {
            font-size: 1.2rem;
            color: #6B7280;
        }

        .footer {
            text-align: center;
            color: #9CA3AF;
            padding-top: 3rem;
            padding-bottom: 2rem;
            border-top: 1px solid #E5E7EB;
        }
    </style>
    """, unsafe_allow_html=True)

    # 헤더
    st.markdown("""
    <div class="header">
        <div class="title">채용공고 분석 📊</div>
    </div>
    """, unsafe_allow_html=True)

    # 직무별 채용공고 수 분석
    st.markdown("""
    <div class="category-title">직무별 채용공고 수</div>
    """, unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{data['frontend_count']}</div>
            <div class="metric-label">프론트엔드</div>
        </div>
        """, unsafe_allow_html=True)

    with cols[1]:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{data['backend_count']}</div>
            <div class="metric-label">백엔드</div>
        </div>
        """, unsafe_allow_html=True)

    # 직무별 주요 기술스택
    st.markdown("""
    <div class="category-title">직무별 주요 기술스택</div>
    """, unsafe_allow_html=True)

    # 프론트엔드 기술스택
    st.markdown("""
    <div class="category-card">
        <div class="category-title">프론트엔드</div>
        <div class="category-description">프론트엔드 개발은 사용자 인터페이스(UI) 및 사용자 경험(UX) 디자인과 밀접하게 관련되어 있습니다. 주요 기술은 HTML, CSS, JavaScript, React, Vue 등이 포함됩니다.</div>
        <div class="keyword-list">
    """, unsafe_allow_html=True)

    for keyword, count in data['frontend_keywords'].items():
        st.markdown(f"""
        <div class="keyword-item">{keyword} ({count})</div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # 백엔드 기술스택
    st.markdown("""
    <div class="category-card">
        <div class="category-title">백엔드</div>
        <div class="category-description">백엔드 개발은 서버, 데이터베이스, API 등을 다루며, 애플리케이션의 논리적 처리를 담당합니다. 주요 기술은 Java, Spring, Python, Node.js 등이 있습니다.</div>
        <div class="keyword-list">
    """, unsafe_allow_html=True)

    for keyword, count in data['backend_keywords'].items():
        st.markdown(f"""
        <div class="keyword-item">{keyword} ({count})</div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        © 2024 퇴사연구소. All rights reserved.
    </div>
    """, unsafe_allow_html=True)

# Streamlit 앱 실행
if __name__ == "__main__":
    # 예시 데이터 (실제 데이터는 load_job_data() 함수를 통해 로드)
    example_data = {
        'frontend_count': 120,
        'backend_count': 80,
        'frontend_keywords': {'React': 25, 'JavaScript': 15, 'CSS': 12, 'Vue': 10, 'HTML': 8},
        'backend_keywords': {'Java': 20, 'Spring': 15, 'Python': 12, 'Node.js': 10, 'Express': 8},
    }

    display_job_categories_and_keywords(example_data)
