import os
import requests
import typer
from dotenv import dotenv_values
from typing_extensions import Annotated

def run(
        day: Annotated[str, typer.Argument(help="Write here the number of the day, eg 1")]
):
    # download input
    if not os.path.isfile("./days/input.txt"):
        # download input with session, stored in .env as "SESSION=<session-cookie-value>"
        url = f"https://adventofcode.com/2023/day/{day}/input"
        config = dotenv_values(".env")

        cookies = {
                'session': config["SESSION"]
            }
        resp = requests.get(url, cookies=cookies)
        with open("./days/input.txt", mode="wb") as file:
            file.write(resp.content)

    os.chdir("./days")
    os.system(f"python day{day}.py")

if __name__ == "__main__":
    typer.run(run)
