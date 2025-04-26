from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd
import glob
from collections import Counter
import re
import matplotlib.pyplot as plt
import seaborn as sns

def crawl_saramin_jobs():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 창 띄우지 않음
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        url = "https://www.saramin.co.kr/zf_user/jobs/list/job-category"
        driver.get(url)

        # 1. 채용공고 개수 요소가 나타날 때까지 최대 10초 대기
        try:
            count_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.count"))
            )
            job_count = count_elem.text.strip()
            print(f"채용공고 개수: {job_count}")
        except Exception as e:
            print("채용공고 개수 추출 실패:", e)
            job_count = None

        # 2. 채용공고 제목(최대 5개) 추출
        try:
            # 제목이 나타날 때까지 최대 10초 대기
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.area_job > h2.job_tit > a"))
            )
            job_titles = driver.find_elements(By.CSS_SELECTOR, "div.area_job > h2.job_tit > a")
            print("\n일부 채용공고 제목:")
            for i, title in enumerate(job_titles[:5]):
                print(f"{i+1}. {title.text.strip()}")
        except Exception as e:
            print("채용공고 제목 추출 실패:", e)

        return job_count, job_titles

    finally:
        driver.quit()

def load_job_data():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        
        json_files = []
        for directory in [current_dir, parent_dir]:
            json_files.extend(glob.glob(os.path.join(directory, 'wanted_analysis_*.json')))
        
        if not json_files:
            st.error("분석 데이터가 없습니다. 먼저 crawl_jobs.py를 실행해주세요.")
            return None
            
        latest_file = max(json_files, key=os.path.getctime)
        print(f"로드한 파일: {latest_file}")
        
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not data:
            st.error("데이터가 비어있습니다.")
            return None
            
        return data
    except Exception as e:
        st.error(f"데이터 로드 중 오류 발생: {str(e)}")
        return None

def analyze_job_categories(df):
    """직무 카테고리 분석"""
    categories = {
        '프론트엔드': ['frontend', '프론트엔드', 'front-end', '프론트', 'react', 'vue', 'angular', 'javascript', 'js', 'html', 'css', '웹', 'ui', 'ux'],
        '백엔드': ['backend', '백엔드', 'back-end', '백엔드', 'java', 'spring', 'python', 'django', 'flask', 'node', 'express', 'php', 'laravel', '서버', 'api'],
        '풀스택': ['fullstack', '풀스택', 'full-stack', 'full stack', '풀 스택'],
        '데이터': ['data', '데이터', 'ai', 'ml', 'machine learning', '딥러닝', 'deep learning', '데이터 분석', '데이터 사이언스'],
        '인프라': ['infra', '인프라', 'devops', '클라우드', 'cloud', 'aws', 'azure', 'gcp', 'kubernetes', 'docker'],
        '모바일': ['mobile', '모바일', 'ios', 'android', 'react native', 'flutter', '앱', 'app']
    }
    
    category_counts = {category: 0 for category in categories.keys()}
    category_keywords = {category: Counter() for category in categories.keys()}
    
    for _, row in df.iterrows():
        title = str(row['직무']).lower()
        desc = str(row['채용내용']).lower()
        
        found_category = False
        for category, keywords in categories.items():
            if any(keyword in title or keyword in desc for keyword in keywords):
                category_counts[category] += 1
                found_category = True
                
                words = re.findall(r'\b\w+\b', desc)
                category_keywords[category].update(words)
                break
        
        if not found_category:
            category_counts['기타'] = category_counts.get('기타', 0) + 1
    
    top_keywords = {}
    for category, counter in category_keywords.items():
        if counter:
            stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'as', 'is', 'are', 'was', 'were', 'be', 'been', 'being'}
            filtered_words = {word: count for word, count in counter.items() if word not in stop_words and len(word) > 1}
            top_keywords[category] = dict(sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)[:5])
    
    return category_counts, top_keywords

def create_visualizations(category_counts, top_keywords):
    """시각화 생성"""
    # 1. 카테고리 분포 파이 차트
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%')
    ax1.set_title('직무 카테고리 분포')
    
    # 2. 카테고리별 채용공고 수 바 차트
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    categories = list(category_counts.keys())
    counts = list(category_counts.values())
    ax2.bar(categories, counts)
    ax2.set_title('카테고리별 채용공고 수')
    plt.xticks(rotation=45)
    
    # 3. 카테고리별 주요 키워드 히트맵
    fig3, ax3 = plt.subplots(figsize=(12, 8))
    keywords_data = []
    for category in categories:
        if category in top_keywords:
            keywords_data.append(list(top_keywords[category].values()))
        else:
            keywords_data.append([0] * 5)
    
    sns.heatmap(keywords_data, annot=True, fmt='d', cmap='YlOrRd',
                xticklabels=['1위', '2위', '3위', '4위', '5위'],
                yticklabels=categories)
    ax3.set_title('카테고리별 주요 키워드 빈도')
    
    return fig1, fig2, fig3

def main():
    st.set_page_config(
        page_title="채용공고 분석",
        page_icon="📊",
        layout="wide"
    )

    # CSS 스타일 정의
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap');
        
        * {
            font-family: 'Noto Sans KR', sans-serif;
        }
        
        .app-container {
            max-width: 1200px;
            margin: auto;
            padding: 2rem;
        }
        
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }
        
        .title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #374151;
        }
        
        .subtitle {
            font-size: 1.25rem;
            color: #6B7280;
        }
        
        .analysis-section {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid #E5E7EB;
        }
        
        .category-card {
            background: white;
            border-radius: 0.75rem;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            margin-bottom: 1rem;
            border: 1px solid #E5E7EB;
            transition: transform 0.3s ease;
        }
        
        .category-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        }
        
        .category-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #374151;
            margin-bottom: 1rem;
        }
        
        .keyword-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .keyword-item {
            background: #F3F4F6;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            font-size: 0.9rem;
            color: #4B5563;
            transition: all 0.3s ease;
        }
        
        .keyword-item:hover {
            background: #E5E7EB;
            transform: translateY(-1px);
        }
        
        .metric-card {
            background: white;
            border-radius: 0.75rem;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            text-align: center;
            border: 1px solid #E5E7EB;
            transition: transform 0.3s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #2563EB;
            margin-bottom: 0.5rem;
        }
        
        .metric-label {
            font-size: 1rem;
            color: #6B7280;
        }
        
        .footer {
            text-align: center;
            color: #9CA3AF;
            padding-top: 2rem;
            border-top: 1px solid #E5E7EB;
        }
    </style>
    """, unsafe_allow_html=True)

    # 앱 컨테이너
    st.markdown('<div class="app-container">', unsafe_allow_html=True)
    
    # 헤더
    st.markdown("""
    <div class="header">
        <div class="title">채용공고 분석 📊</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 데이터 로드
    with st.spinner('데이터를 불러오는 중...'):
        data = load_job_data()
    
    if data is not None:
        # 기본 정보 표시
        st.markdown("""
        <div class="analysis-section">
            <div class="metric-card">
                <div class="metric-value">{}</div>
                <div class="metric-label">현재 활성화된 채용공고</div>
            </div>
        </div>
        """.format(data['total_jobs']), unsafe_allow_html=True)
        
        # 직무별 채용공고 수 분석
        st.markdown("""
        <div class="analysis-section">
            <div class="category-title">직무별 채용공고 수</div>
        </div>
        """, unsafe_allow_html=True)
        
        # 직무별 채용공고 수 표시
        cols = st.columns(2)
        with cols[0]:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">{}</div>
                <div class="metric-label">프론트엔드</div>
            </div>
            """.format(data['frontend_count']), unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">{}</div>
                <div class="metric-label">백엔드</div>
            </div>
            """.format(data['backend_count']), unsafe_allow_html=True)
        
        # 직무별 주요 기술스택
        st.markdown("""
        <div class="analysis-section">
            <div class="category-title">직무별 주요 기술스택</div>
        </div>
        """, unsafe_allow_html=True)
        
        # 프론트엔드 기술스택
        st.markdown("""
        <div class="category-card">
            <div class="category-title">프론트엔드</div>
            <div class="keyword-list">
        """, unsafe_allow_html=True)
        
        for keyword, count in data['frontend_keywords'].items():
            st.markdown("""
            <div class="keyword-item">{} ({})</div>
            """.format(keyword, count), unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # 백엔드 기술스택
        st.markdown("""
        <div class="category-card">
            <div class="category-title">백엔드</div>
            <div class="keyword-list">
        """, unsafe_allow_html=True)
        
        for keyword, count in data['backend_keywords'].items():
            st.markdown("""
            <div class="keyword-item">{} ({})</div>
            """.format(keyword, count), unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # Footer
        st.markdown("""
        <div class="footer">
            © 2024 퇴사연구소. All rights reserved.
        </div>
        """, unsafe_allow_html=True)
    
    # 앱 컨테이너 닫기
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
