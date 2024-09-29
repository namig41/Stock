from fastapi import FastAPI

def create_app():
    return FastAPI(
       title='dddpy',
       docs_url='/api/docs',
       description='dddpy',
       debug=True
    )