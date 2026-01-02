# app.py
import streamlit as st
import json
# --- 关键：导入我们自己写的模块 ---
from utils_pdf import get_pdf_text
from utils_ai import extract_resume_data

st.set_page_config(page_title="模块化简历助手", page_icon="🧩")
st.title("🧩 模块化简历助手 (Refactored)")

uploaded_file = st.file_uploader("上传简历", type=["pdf"])

if uploaded_file:
    # 1. 调用工具层
    raw_text = get_pdf_text(uploaded_file)
    
    if raw_text:
        st.info(f"读取成功，共 {len(raw_text)} 字符")
        
        if st.button("开始分析"):
            with st.spinner("AI 思考中..."):
                # 2. 调用逻辑层
                json_result = extract_resume_data(raw_text)
                
                # 3. UI 展示层
                try:
                    data = json.loads(json_result)
                    st.success("分析完成！")
                    st.json(data)
                except json.JSONDecodeError:
                    st.error("解析失败")