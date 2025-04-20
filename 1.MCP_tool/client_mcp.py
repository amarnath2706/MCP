import requests

def test_multiply(a,b):
    response = requests.post("http://127.0.0.1:8080/amar/mcp/multiply", json={"a":a,"b":b})
    if response.status_code == 200:
        print("Multiplication MCP called successfully",response.json()["result"])
    else:
        print("Error in calling MCP:", response.status_code, response.text)


if __name__ == "__main__":
    test_multiply(20,6)
    #test_multiply(20,6) #call the function and pass the two numbers to be multiplied