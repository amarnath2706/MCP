from fastmcp import FastMCP
from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()
mcp = FastMCP("demo server")

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b 


@app.post("/amar/mcp/multiply")  #client
def call_multiply(data: dict=Body(...)): #receive the data from my client - client send the data in the form of JSON
    #take the complete body of the request from client and three dots represent iam expecting some input
    #result = mcp.call("multiply", data)
    return {"result" : multiply(data.get("a",0),data.get("b",0))} 
    #This help me out to get the data from client whenever client is goinf to call and the multiply
    #and give you the result


@app.get("/") #route url
#how client will be able to call? I have to expose the above function to the client, iam going to use
#FastAPI to expose this function
def home():
    return{"message":"Hello from server mcp"}

#invoke the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
    #uvicorn.run(app, host="