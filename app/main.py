import uvicorn
from app import create_app

if __name__=="__main__":

    uvicorn.run("app:create_app",host="localhost",port=8080,reload=True,factory=True)