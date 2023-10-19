# FastApi - Authentication

<aside>
💡 API Key 是一種簡單而有效的驗證方法，常被用來控制訪問 API 的權限。通常，API Key 是一串唯一的字串，會在 HTTP 請求的 header 或 URL 參數中被發送到服務器端。服務器端會驗證這個 API Key，確保其有效性後才會處理相對應的請求。

</aside>

## **驗證 API Key 的一種方式**

### 1. **Header 驗證**：

將 API Key 放在 HTTP 請求的 header 中。這是一種常見的做法，通常會使用 **`Authorization`** 這個 header 字段來儲存 API Key。

## **實現方法**

在 **`fastapi`** 中，可使用Depends來實現 API Key 的驗證。以下是一個如何實現的範例：

### 1. **設置 API Key**

首先需要定義一個固定的 API Key。這個 Key 應該保密，只有被授權的用戶才能知道。

```python
API_KEY = "ab0fbe70-eac9-4ceb-a1ed-717af2a7d776"
```

### 2. **建立 API Key 驗證函數**

然後建立一個函數來驗證 API Key。在這個函數中，從 HTTP 的 Authorization header 中獲取 API Key，並檢查它是否與預設的 API Key 匹配。

```python
from fastapi import Depends, HTTPException, security

api_key_header = security.HTTPBearer(auto_error=False)

def get_api_key(authorization: security.HTTPAuthorizationCredentials = Depends(api_key_header)):
    if authorization and authorization.credentials == API_KEY:
        return authorization.credentials
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
```

在這個函數中，**`security.HTTPBearer(auto_error=False)`** 創建了一個Depends項目，這會從請求的 Authorization header 獲取值。

### 3. **在路由中使用 API Key 驗證**

在路由中使用依賴來實現 API Key 驗證。需要將驗證函數作為依賴添加到路由函數的參數中。

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/protected-endpoint")
async def protected_endpoint(
	api_key: str = Depends(get_api_key)
):
    return {"message": "This is a protected endpoint."}
```

這樣就只有在請求 header 中包含有效的 API Key 的請求才能訪問此端點，否則將返回 401 Unauthorized 錯誤。

## 使用**方法**

接下來透過範例來解釋如何在呼叫 API 時在 header 中帶入 key 值，以及如何在 Swagger UI 中加入這個 key 值。

### 1. **在 HTTP 請求中帶入 API Key**

當發送 HTTP 請求到被保護的端點時，需要在請求的 header 中加入 API Key。可以使用各種 HTTP 客戶端工具或程式庫，如 **`curl`**、Postman 或 Python 的 **`requests`** 库來完成這個任務。

**使用 curl：**

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/protected-endpoint' \
  -H 'Authorization: Bearer YOUR_API_KEY'
```

**使用 Python 的 requests 库：**

```python
import requests

headers = {
    "Authorization": f"Bearer YOUR_API_KEY"
}

response = requests.get('http://127.0.0.1:8000/protected-endpoint', headers=headers)
print(response.json())
```

### 2. **在 Swagger UI 中加入 API Key**

FastAPI 的 Swagger UI 提供了一個界面可直接在瀏覽器中測試 API 端點。在 Swagger UI 中使用 API Key可按照以下步驟操作：

1. **開啟 Swagger UI：** 在瀏覽器中輸入 **`http://127.0.0.1:8000/docs`** 來開啟 Swagger UI。
2. **輸入 API Key：**
    - 在 Swagger UI 的界面上方，會看到一個 “Authorize” 的按鈕。點擊它。
        
        ![Untitled](FastApi%20-%20Authentication%20ac180b0c88fd4b06afb11fafaa2d97d8/Untitled.png)
        
    - 在彈出的對話框中，會看到一個可以輸入 API Key 的欄位。在這個欄位中輸入你的API Key，並且確保前面有 “Bearer” 這個字眼。
        
        ![Untitled](FastApi%20-%20Authentication%20ac180b0c88fd4b06afb11fafaa2d97d8/Untitled%201.png)
        
    - 例如：**`Bearer YOUR_API_KEY`**
    - 點擊 "Authorize" 來關閉對話框。
3. **測試端點：**選擇一個端點並且點擊 "Try it out" 來測試。Swagger UI 會自動在請求的 header 中加入之前輸入的 API Key。