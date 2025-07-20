import streamlit as st

# URL 맨 뒤에 보이지 않는 공백을 제거한 올바른 주소입니다.
html_url = "https://kaykim0310.github.io/Smart-TBM/Smart-TBM.html"

# Streamlit 앱 제목 설정
st.title("GitHub HTML 파일 표시하기")

# st.components.v1.iframe을 사용해 HTML 파일 보여주기
st.components.v1.iframe(html_url, height=600, scrolling=True)
