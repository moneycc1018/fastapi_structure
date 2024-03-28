# FastAPI Structure
此 Repo 提供一個開發 FastAPI 的樣板，僅供參考。

```
.
├── api
│   ├── routers
│   │   ├── rss.py
│   │   └── user.py
│   ├── dependencies.py
│   └── router.py
├── crud
│   ├── rss.py
│   └── user.py
├── db
│   └── database.py
├── models
│   ├── rss_info.py
│   └── user.py
├── schemas
│   ├── rss.py
│   └── user.py
├── tests
│   ├── test_rss.py
│   └── test_user.py
├── .gitignore
├── Dockerfile
├── README.md
├── config.py
├── main.py
└── requirements.txt
```

* api
    * routers
        * rss.py：有關 rss 的 API router
        * user.py：有關 user 的 API router
    * dependencies.py：依賴項
    * router.py：所有 API router 的整合
* crud
    * rss.py：有關 rss 的 CRUD
    * user.py：有關 user 的 CRUD
* db
    * database.py：資料庫設定 (如 engine 等)
* models
    * rss_info.py：資料庫中 rss_info table 的對應欄位設定
    * user.py：資料庫中 user table 的對應欄位設定
* schemas
    * rss.py：有關 rss 的 pydantic model
    * user.py：有關 user 的 pydantic model
* tests
    * test_rss.py：有關 rss 的測試檔
    * test_user.py：有關 user 的測試檔
* config.py：設定檔
* main.py：整個 project 的設定 (如 CORS 等)

## Run
### Local
```
pyenv exec python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
uvicorn main:app --reload
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
