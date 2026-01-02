# utils_ai.py
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
client = OpenAI()

def extract_resume_data(text_content):
    """
    调用 GPT-4o 从文本中提取简历信息。
    """
    prompt = f"""
    你是一个简历数据提取器。请将以下文本转换为纯 JSON 数据。
    字段包括: name, email, phone, skills (list), summary (string)。
    如果找不到，填 null。
    
    【文本】
    {text_content}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You output JSON only."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return json.dumps({"error": str(e)}) # 发生错误时返回一个错误的 JSON