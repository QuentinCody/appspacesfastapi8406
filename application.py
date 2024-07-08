from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/transactions_with_details?page=1&page_size=20&sort_order=asc&timezone=America%2FNew_York HTTP/1.1")
async def get_transactions_with_details_test():
    return {"message": "2nd API endpoint works!"}