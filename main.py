import streamlit as st

def main():
    st.set_page_config(
        page_title="퇴사연구소",
        page_icon="🧑‍💼",
        layout="centered"
    )

    st.title("퇴사연구소 🧑‍💼")
    st.subheader("이직을 고민하는 당신을 위한 커리어 연구소")
    st.write("""
    **퇴사연구소**는 이직을 고민하는 분들이 이력서와 포트폴리오를 업로드하면  
    AI와 데이터가 최신 채용 시장 정보를 분석해  
    맞춤형 이직 조언과 추천을 제공하는 서비스입니다.
    """)

    st.markdown("---")
    st.info("왼쪽 사이드바에서 원하는 페이지를 선택하세요!")

if __name__ == "__main__":
    main()