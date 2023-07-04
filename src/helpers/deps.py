from fastapi import Depends, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import HTTPException
from model.user import User
from config import settings

# For now I'm using a different header called 'Authentication' instead of 'Authorization'
# for Basic auth
def basic_auth(Authentication=Header(None, description="Use 'Basic email@domain.com'")):
    if not Authentication or not Authentication.startswith("Basic "):
        return None
    user = User.get_by_email(Authentication.split("Basic ")[1])
    if not settings.env in ["dev", "testing"]:
        raise HTTPException(status_code=403, detail="Forbidden scheme")
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


def jwt_auth(
    auth: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
):
    # Decode and validate tokens here, like JWTs
    # `auth` will contain the token
    return None


async def auth(jwt_result=Depends(jwt_auth), basic_result=Depends(basic_auth)):
    if not (basic_result or jwt_result):
        raise HTTPException(status_code=401, detail="Unauthorized user")
    return basic_result or jwt_result
