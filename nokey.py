import typer
import typing
import signal, sys

from nokey import Setup

app = typer.Typer()


def gracefully_exit(sig, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, gracefully_exit)


@app.command()
def url(*, url: str = typer.Argument(...), user: typing.Optional[int] = 0):

    if url.startswith("https://meet.google.com/") or url.startswith(
        "http://meet.google.com/"
    ):
        url += f"?authuser={user}"
        meet_app = Setup()
        meet_app.run(url)
    else:
        err_msg = typer.style(
            "Invalid URL format! : ", fg=typer.colors.BRIGHT_BLUE, bg=typer.colors.BLACK
        )
        err_url = typer.style(url, fg=typer.colors.BRIGHT_RED, bg=typer.colors.BLACK)
        typer.echo(err_msg + err_url)
        raise typer.Exit()


@app.command()
def Code(code: str = typer.Argument(...), user: typing.Optional[int] = 0):

    if len(code) < 12 or len(code) > 12:
        code_msg = typer.style(code, fg=typer.colors.BRIGHT_RED, bg=typer.colors.BLACK)
        msg = typer.style(
            "Invalid CODE format! → ",
            fg=typer.colors.BRIGHT_BLUE,
            bg=typer.colors.BLACK,
        )
        help_msg = typer.style(
            "Must be like → ",
            fg=typer.colors.BRIGHT_BLUE,
            bg=typer.colors.BLACK,
        )
        help_code = typer.style(
            "abc-defg-hij", fg=typer.colors.BRIGHT_CYAN, bg=typer.colors.BLACK
        )
        typer.echo(msg + code_msg, err=True)
        typer.echo(help_msg + help_code)
        raise typer.Exit()
    elif user < 0:
        err_msg = typer.style(
            "User Index cannot be -ve",
            fg=typer.colors.BRIGHT_RED,
            bg=typer.colors.BLACK,
        )
        typer.echo(err_msg, err=True)
        raise typer.Exit()
    else:

        url = f"https://meet.google.com/{code}/"
        url += f"?authuser={user}"
        meet_app = Setup()
        meet_app.run(url)


if __name__ == "__main__":
    app()
