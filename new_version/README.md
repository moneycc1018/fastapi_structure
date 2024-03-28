# FastAPI Structure
此 Repo 提供一個開發 FastAPI 的樣板，僅供參考。

```
.
├── app
│   ├── rss
│   │   ├── dependencies.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── service.py
│   ├── user
│   │   ├── dependencies.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── service.py
│   ├── config.py
│   ├── database.py
│   └── main.py
├── tests
│   ├── test_rss.py
│   └── test_user.py
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

* api
    * rss
        * dependencies.py：依賴項
        * models.py：有關 rss 的資料庫欄位設定
        * router.py：有關 rss 的 API router
        * schemas.py：有關 rss 的 pydantic model
        * service.py：有關 rss 的業務邏輯，包括 CRUD 等
    * user
        * dependencies.py：依賴項
        * models.py：有關 user 的資料庫欄位設定
        * router.py：有關 user 的 API router
        * schemas.py：有關 user 的 pydantic model
        * service.py：有關 user 的業務邏輯，包括 CRUD 等
    * config.py：設定檔
    * database.py：資料庫設定 (如 engine 等)
    * main.py：所有 API router 的整合及整個 project 的設定 (如 CORS 等)
    * user.py：有關 user 的 pydantic model
* tests
    * test_rss.py：有關 rss 的測試檔
    * test_user.py：有關 user 的測試檔

## Run
### Local
```
pyenv exec python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload
```
### Docker
```
docker build -t fastapi_structure .
docker run -d --name fastapi_structure -p 9527:80 fastapi_structure
```

## Interactive API docs
[http://0.0.0.0:9527/docs](http://0.0.0.0:9527/docs)

## Reference
[tiangolo/full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template)

[zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)

[fastapi-practices/fastapi_best_architecture](https://github.com/fastapi-practices/fastapi_best_architecture)
