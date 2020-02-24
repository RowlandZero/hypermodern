# noxfile.py
import nox

locations = "src", "tests", "noxfile.py"
nox.options.session = "lint", "tests", "mypy"


@nox.session(python=["3.8"])
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.8"])
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8", "flake8-bandit", "flake8-black", "flake8-bugbear",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8"])
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.8"])
def mypy(session) -> None:
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)
