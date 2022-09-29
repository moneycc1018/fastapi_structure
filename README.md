# FastAPI Structure
此Repo提供一個開發FastAPI的基礎公版。

![project_tree](images/project_tree.png)

* api: 存放所有與API有關的檔案
    * endpoints: 存放設定API router的檔案
        * products.py: 設定有關product的API router
        * users.py: 設定有關user的API router
    * api.py: 整合所有API router
* models: 存放所有pydantic model
    * products.py: 設定有關product的model(取名與endpoints內檔案一致)
    * users.py: 設定有關user的model(取名與endpoints內檔案一致)
* tests: 存放所有測試檔案
    * test_products.py: 測試products.py
    * test_users.py: 測試users.py
* main.py: 整個project的主要設定(如CORS等)

## Refernce
[FastAPI - Project Generation - Template](https://fastapi.tiangolo.com/project-generation/)