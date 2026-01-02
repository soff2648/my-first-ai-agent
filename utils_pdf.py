# utils_pdf.py
import pypdf

def get_pdf_text(uploaded_file, max_pages=5):
    """
    读取 PDF 文件并返回文本。
    :param uploaded_file: Streamlit 上传的文件对象
    :param max_pages: 限制读取页数，防止 Token 爆炸
    """
    text = ""
    try:
        reader = pypdf.PdfReader(uploaded_file)
        for i, page in enumerate(reader.pages):
            if i >= max_pages: 
                break
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"PDF 读取错误: {e}") # 这里用 print，因为工具层不应该直接操作 UI (st.error)
        return ""
    return text