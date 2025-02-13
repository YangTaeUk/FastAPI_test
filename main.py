from fastapi import FastAPI

app = FastAPI()  # FastAPI 인스턴스 생성

@app.get("/")  # GET 메서드로 "/" 엔드포인트에 접근할 때
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")  # path parameter 예시
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}