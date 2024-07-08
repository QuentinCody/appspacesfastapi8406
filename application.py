from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/transactions/daily-totals")
async def get_transactions_with_details_test():
    return {"message": "2nd API endpoint works!"}