import os
import requests
import typer
from dotenv import dotenv_values
from typing_extensions import Annotated, Optional

def run(
        day: Annotated[str, typer.Argument(help="Write here the number of the day, eg 1")],
        year: Annotated[Optional[str], typer.Argument()] = 2024
):
    print(day, year)
    # download input
    if not os.path.isfile(f"./{year}/input.txt"):
        # download input with session, stored in .env as "SESSION=<session-cookie-value>"
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        config = dotenv_values(".env")

        cookies = {
                'session': config["SESSION"]
            }
        resp = requests.get(url, cookies=cookies)
        with open(f"./{year}/input.txt", mode="wb") as file:
            file.write(resp.content)

    os.chdir(f"./{year}")
    os.system(f"python day{day}.py")

if __name__ == "__main__":
    typer.run(run)
