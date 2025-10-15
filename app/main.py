import uvicorn
from app import create_app

if __name__=="__main__":
    import sqlalchemy

    print(sqlalchemy.__version__)
    uvicorn.run("app:create_app",host="localhost",port=8080,reload=True,factory=True)