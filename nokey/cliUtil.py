import typer
import arrow

BLUE = typer.colors.BRIGHT_BLUE
BLACK = typer.colors.BLACK
RED = typer.colors.BRIGHT_RED
GREEN = typer.colors.BRIGHT_GREEN
YELLOW = typer.colors.BRIGHT_YELLOW


class Util:
    def __init__(self, url) -> None:
        self.url = url
        self.code = self.url[24 : 24 + 12]

    def join_msg(self):

        joined = typer.style("Joined - ", fg=BLUE, bg=BLACK)
        code = typer.style(self.code, fg=RED, bg=BLACK)
        timeStmp = typer.style(str(arrow.now().format("hh:mm-A")), fg=YELLOW, bg=BLACK)
        typer.echo(f"{joined} - {code} : {timeStmp}")

    def listen(self):
        timeStmp = typer.style(str(arrow.now().format("hh:mm-A")), fg=YELLOW, bg=BLACK)
        typer.secho(f"Listening to - {self.code} : {timeStmp}\n", fg=GREEN, bg=BLACK)

    def newPt(self, name):
        timeStmp = typer.style(str(arrow.now().format("hh:mm-A")), fg=YELLOW, bg=BLACK)
        name = typer.style(name, fg=GREEN, bg=BLACK)
        info = typer.style(f"+ PARTICIPANT : ", fg=BLUE, bg=BLACK)
        typer.echo(f"{info}{name} : {timeStmp}")

    def levPt(self, name):
        timeStmp = typer.style(str(arrow.now().format("hh:mm-A")), fg=YELLOW, bg=BLACK)
        name = typer.style(name, fg=GREEN, bg=BLACK)
        info = typer.style(f"- PARTICIPANT : ", fg=RED, bg=BLACK)
        typer.echo(f"{info}{name} : {timeStmp}")


if __name__ == "__main__":
    n = Util("https://meet.google.com/vvp-urnh-cgr")
    n.join_msg()
    n.newPt("Aadil")
    n.levPt("Aadil")
