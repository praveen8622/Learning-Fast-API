from fastapi import FastAPI


app =FastAPI()

@app.get('/blog')
def index(limit=10, published: bool= True):
    if published:
        return {'data': f'{limit} published blog list from db'}
    else:
        return {'data': f'{limit}  blog list from db'}


@app.get('/blog/unpublished')
def show(id: int ):
    return {'data': 'all unpublished blog'}

@app.get('/blog/{id}')
def show(id: int ):
    return {'data': id}

@app.get ('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}