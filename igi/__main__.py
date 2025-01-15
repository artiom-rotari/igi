from typer import Typer

from igi.qvm import app as qvm_app

app = Typer()

app.add_typer(qvm_app, name="qvm")


if __name__ == "__main__":
    app()
