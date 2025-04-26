import streamlit as st
import openai
import os
import sys
import json

# UTF-8 인코딩 설정
sys.stdout.reconfigure(encoding='utf-8')
# API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 페이지 설정
st.set_page_config(page_title="팩트폭격랩 퇴사진단기 🔥", page_icon="🔥", layout="centered")

# CSS 스타일 적용
st.markdown("""
<style>
    /* 전체 스타일 */
    .main {
        background-color: #f8f9fa;
        font-family: 'Pretendard', -apple-system, sans-serif;
    }
    
    /* 제목 스타일 */
    h1 {
        color: #FF4500;
        text-align: center;
        font-weight: bold;
    }
    
    /* 부제목 스타일 */
    .subheader {
        color: #666;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* 질문 카드 스타일 */
    .question-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        border-left: 5px solid #FF4500;
    }
    
    /* 질문 텍스트 스타일 */
    .question-text {
        font-size: 1.1rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
    }
    
    /* 입력 필드 스타일 */
    .stTextInput > div > div > input {
        border: 2px solid #FF4500;
        border-radius: 8px;
    }
    
    /* 버튼 스타일 */
    .stButton > button {
        background-color: #FF4500;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #E63900;
        box-shadow: 0 4px 8px rgba(230, 57, 0, 0.2);
    }
    
    /* 결과 텍스트 영역 */
    .result-area {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border-left: 5px solid #FF4500;
        margin-top: 1rem;
        line-height: 1.6;
    }
    
    /* 프로그레스 바 */
    .progress-bar {
        height: 10px;
        background-color: #f1f1f1;
        border-radius: 5px;
        margin-bottom: 2rem;
    }
    
    .progress-bar-fill {
        height: 100%;
        background-color: #FF4500;
        border-radius: 5px;
        transition: width 0.3s ease;
    }
    
    /* 단계 표시 */
    .step-indicator {
        text-align: center;
        color: #FF4500;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* 스피너 스타일 */
    .stSpinner > div > div {
        border-top-color: #FF4500 !important;
    }
</style>
""", unsafe_allow_html=True)

# 제목 및 부제목
st.title("팩트폭격랩 퇴사진단기 🔥")
st.markdown("<div class='subheader'>퇴사 고민? 팩트부터 조져보자.</div>", unsafe_allow_html=True)

# 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 1
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []

# 프로그레스 바 표시
def show_progress(step):
    total_steps = 5
    progress = min((step - 1) / total_steps, 1.0)
    st.markdown(f"""
        <div class="step-indicator">STEP {min(step, 5)}/5</div>
        <div class="progress-bar">
            <div class="progress-bar-fill" style="width: {progress * 100}%;"></div>
        </div>
    """, unsafe_allow_html=True)

# 질문 표시 함수
def ask_question(prompt, key, next_step):
    st.markdown(f"""
        <div class="question-card">
            <div class="question-text">{prompt}</div>
        </div>
    """, unsafe_allow_html=True)
    return st.text_input("대답:", key=key)

# 메인 로직
show_progress(st.session_state.step)

if st.session_state.step == 1:
    answer = ask_question("퇴사 고민 있지? 왜 그렇게 빡쳤냐.", "first_answer", 2)
    if answer:
        st.session_state.user_answers.append(answer)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    answer = ask_question("오케이. 니 경력 몇 년 차.", "second_answer", 3)
    if answer:
        st.session_state.user_answers.append(answer)
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    answer = ask_question("지금까지 무슨 일 했냐. 짧게.", "third_answer", 4)
    if answer:
        st.session_state.user_answers.append(answer)
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    answer = ask_question("써본 툴, 기술 뭐 있냐.", "forth_answer", 5)
    if answer:
        st.session_state.user_answers.append(answer)
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    answer = ask_question("연봉은 얼마 받고 싶냐.", "fifth_answer", 6)
    if answer:
        st.session_state.user_answers.append(answer)
        st.session_state.step = 6
        st.rerun()

elif st.session_state.step == 6:
    # 응답 요약 표시
    st.markdown("<div class='question-card'>", unsafe_allow_html=True)
    st.subheader("입력 정보 확인")
    
    questions = [
        "퇴사 고민 이유",
        "경력 연차",
        "이전 업무 경험",
        "보유 기술",
        "희망 연봉"
    ]
    
    for i, (q, a) in enumerate(zip(questions, st.session_state.user_answers)):
        st.write(f"**{q}**: {a}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("팩폭 분석 시작하기 ⚡"):
        with st.spinner("팩폭 분석 중..."):
            try:
                user_message = st.session_state.user_answers

                prompt = f"""
                [유저 입력 정보]
                퇴사 고민 이유: {user_message[0]}
                경력 연차: {user_message[1]}
                이전 업무 경험: {user_message[2]}
                보유 기술: {user_message[3]}
                희망 연봉: {user_message[4]}

                [지침]
                - '1. 2. 3.' 같은 목록 나열 절대 금지.
                - 사람 말투처럼 자연스럽게 이어가되, 짧게 끊는 문장으로 팩트폭격해.
                - 감정 위로나 착한 말투 절대 쓰지 마라. 친절 ❌, 싸늘하게 ❌, 무심하게 팩트만 말해.
                - 이모티콘 금지.
                - 현실 직격: 경력과 스킬을 냉정하게 평가하고, 시장 상황을 깔끔하게 박살내고, 끝에 현실 조언 한 줄로 정리해.
                - 가능하면 확률(%)이나 예상 기간(개월) 같은 숫자도 자연스럽게 섞어줘.

                [참고 예시 스타일]
                "프로그래머로 5년 일했다고? 코드 퀄리티 보니까 유지보수 걱정 생긴다. 대충 넘길 스펙 아님.
                지금 개발자 시장? 공고 하나에 지원자 수백 명 몰린다. 니 스킬셋으론 그냥 묻힌다.
                신규 프로젝트 들어가고 싶으면, 코드부터 다시 닦고 최신 트렌드 따라잡아. 할 자신 없으면 그냥 현상유지나 해."
                """

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "유저 이력을 바탕으로 냉철한 피드백을 작성하는 퇴사 진단 AI입니다."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )

                llm_answer = response.choices[0].message.content
                
                # 결과 표시
                st.markdown("<div class='result-area'>", unsafe_allow_html=True)
                st.subheader("팩폭 결과 💣")
                st.write(llm_answer)
                st.markdown("</div>", unsafe_allow_html=True)
                
                # 재시작 버튼
                if st.button("처음부터 다시하기 🔄"):
                    st.session_state.step = 1
                    st.session_state.user_answers = []
                    st.rerun()

            except Exception as e:
                st.error(f"오류 발생: {e}")

# 푸터 추가
st.markdown("""
<div style="text-align:center; margin-top:2rem; font-size:0.8rem; color:#666;">
    © 2025 퇴사연구소. All rights reserved.
</div>
""", unsafe_allow_html=True)