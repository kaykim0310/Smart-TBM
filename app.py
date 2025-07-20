import streamlit as st

# GitHub에서 복사했던 HTML 파일의 'Raw' URL을 여기에 넣으세요.
# 'SmartTBM' 리포지토리에 올리신 HTML 파일의 Raw URL이어야 합니다.
html_url = "https://raw.githubusercontent.com/kaykim0310/Smart-TBM/main/Smart-TBM.html" 

# Streamlit 앱 제목 설정
st.title("GitHub HTML 파일 표시하기")

# st.components.v1.iframe을 사용해 HTML 파일 보여주기
st.components.v1.iframe(html_url, height=600, scrolling=True)
