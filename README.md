# fastapi를 이용한 웹서버

가상환경을 구성 하기 위해서 

```powershell
python -m venv fastapi_web
cd fastapi_web

Scripts\activate

>>> (fastapi_web) C:\apps\fastapi_web>
```

.gitignore 파일 생성후

```powershell
/Lib
/Include
/Scripts
pyvenv.cfg
```

파이썬을 이용해서 웹서버를 구현하기 위해 flask 라이브러리 및 framework 를 사용한다.

pip를 이용해서 설치 한다.

```powershell
pip install fastapi[all] uvicorn
```

라이브러리 설치 목록을 따로 만들어 관리하면 다른 곳에서 프로젝트를 구현할때 편리하다.

```powershell
pip freeze > requirements.txt
```

requirements.txt 에 있는 내용대로 라이브러리를 설치하는 방법은 다음과 같다.

```powershell
pip install -r requirements.txt
```

![image](https://github.com/kbigdata005/web_server/assets/139095086/ae2a74f9-df59-447e-b0ca-249d26dd935e)


위와 같은 구조로 웹서버를 만든다.

![image](https://github.com/kbigdata005/web_server/assets/139095086/15a7cc1e-aaa6-4129-9b7e-47ccc859d982)

다음과 같은 기능을 구현하기 위해

url : http://localhost:8000

method : GET 방식

data : Hello World!! 텍스트 데이터가 클라이언트에 전송되도록 한다.

main.py를 생성후 다음과 같이 코드를 추가한다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main():
    return {"message":"Hello World"}
```