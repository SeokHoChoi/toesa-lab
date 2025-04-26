import streamlit as st

def main():
    st.set_page_config(
        page_title="소개 - 퇴사연구소",
        page_icon="📢",
        layout="centered"
    )

    st.title("📢 퇴사연구소 소개")
    st.write("""
    **퇴사연구소**는 퇴사를 고민하는 분들을 위해  
    AI가 이력서와 포트폴리오를 분석하고,  
    원티드/사람인/잡플래닛 등 다양한 채용 플랫폼의  
    실시간 시장 데이터를 바탕으로  
    맞춤형 이직 조언과 추천을 제공하는 웹앱입니다.

    - 이력서/포트폴리오 업로드
    - AI 기반 직무/경력 분석
    - 실시간 채용 시장 정보 제공
    - 맞춤형 커리어 추천

    이직, 혼자 고민하지 마세요.  
    **퇴사연구소**가 함께합니다! 🚀
    """)

if __name__ == "__main__":
    main()
