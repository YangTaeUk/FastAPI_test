from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate


class AppModel:
    def __init__(self):
        # .env 로드
        load_dotenv()
        google_api_key = os.getenv("GEMINI_API_KEY")  # 키 이름 확인 필요

        if not google_api_key:
            raise ValueError("GOOGLE_API_KEY가 .env 파일에 설정되지 않았습니다.")

        # Gemini 모델 초기화
        self.model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # 모델 이름 확인 (2025년 2월 기준 유효한지 체크)
            google_api_key=google_api_key,
            timeout=30,  # 타임아웃 설정 (지원 여부는 문서 확인)
            temperature=0.7
        )

        # 번역 프롬프트 템플릿
        system_template = "Translate the following from English into {language}"
        self.prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}")]
        )

    # 간단한 텍스트 응답
    def get_response(self, message):
        return self.model.invoke([HumanMessage(content=message)])

    # 번역 응답
    def get_prompt_response(self, message):
        prompt = self.prompt_template.invoke({"language": "Italian", "text": message})
        return self.model.invoke(prompt)

    # 스트리밍 응답
    def get_streaming_response(self, messages):
        return self.model.astream(messages)


# 테스트 코드
if __name__ == "__main__":
    app = AppModel()

    # 간단한 텍스트 테스트
    print("간단 응답:", app.get_response("Hello, how are you?").content)

    # 번역 테스트
    print("번역 응답:", app.get_prompt_response("Hello, how are you?").content)

    # 스트리밍 테스트
    print("스트리밍 응답:", end=" ")
    for chunk in app.get_streaming_response([HumanMessage(content="Tell me a story")]):
        print(chunk.content, end="", flush=True)
    print()  # 줄바꿈