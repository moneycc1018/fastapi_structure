# api/api/api_v1/endpoint/agent/auth.py

from fastapi import Depends, HTTPException, security

# Define the API_KEY variable which holds the secret key used for authentication.
API_KEY = "ab0fbe70-eac9-4ceb-a1ed-717af2a7d776"

# Define the api_key_header, using HTTPBearer scheme for authentication.
# auto_error=False means that if there is no valid authentication, it won’t automatically return an error.
# Instead, it will continue to execute the next dependencies.
api_key_header = security.HTTPBearer(auto_error=False)

# Define a function get_api_key that takes in the HTTP Authorization Credentials.
def get_api_key(authorization: security.HTTPAuthorizationCredentials = Depends(api_key_header)):
    
    # Check if the authorization object exists and if the credentials match the predefined API_KEY.
    if authorization and authorization.credentials == API_KEY:
        
        # If the credentials are correct, return the credentials.
        return authorization.credentials
    
    else:
        
        # If the credentials are incorrect or missing, raise an HTTP 401 Unauthorized error.
        raise HTTPException(status_code=401, detail="Unauthorized")
