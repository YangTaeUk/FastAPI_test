from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

import app_model

app = FastAPI()

model = app_model.AppModel()

@app.get("/say")
def say_app(text: str = Query()):
    response = model.get_response(text)
    return response.content

#
# # app = FastAPI()  # FastAPI 인스턴스 생성
# #
# # @app.get("/")  # GET 메서드로 "/" 엔드포인트에 접근할 때
# # def read_root():
# #     return {"message": "Hello, FastAPI!"}
#
#
# from dotenv import load_dotenv
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
#
# # .env 파일 로드
# load_dotenv()
#
# # API 키 가져오기
# google_api_key = os.getenv("GEMINI_API_KEY")
#
# # Gemini 모델 초기화
# # llm = ChatGoogleGenerativeAI(
# #     model="gemini-1.5-flash",  # 텍스트 전용 모델, "gemini-pro-vision"은 멀티모달
# #     google_api_key=google_api_key,
# #     timeout=30,  # 초 단위, 지원 여부는 문서 확인
# #     temperature=0.7
# # )
# #
# # # 간단한 텍스트 테스트
# # response = llm.invoke("안녕, Gemini는 뭐야?")
# # print(response.content)
#
# from langchain_core.prompts import ChatPromptTemplate
#
# system_template = "Translate the following from English into korean"
#
# prompt_template = ChatPromptTemplate.from_messages(
#     [("system", system_template), ("user", "{text}")]
# )
# prompt = prompt_template.invoke({"language": "korean", "text": "hi!"})
# print(prompt)