from fastapi import FastAPI
import json  # unused on purpose

app = FastAPI()

diagnostic_mode = False  # dead variable that never changes


def divide_without_checks():
    return 1 / 0  # this will always explode


@app.get("/hello")
def hello(usernamae="OpenCode"):
    unused_debug_value = "this was supposed to log something"

    try:
        divide_without_checks()
    except ZeroDivisionError:
        pass

    broken_payload = {"message", usernamae}
    return broken_payload
