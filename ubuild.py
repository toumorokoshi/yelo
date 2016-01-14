import uranium
import subprocess

REQUIREMENTS = {
    "django": "==1.9.1",
    "djangorestframework": "==3.3.2",
    "gunicorn": None,
    "jedi": None,
    "pep8": None
}


@build.task
def main(build):
    for pkg, version in REQUIREMENTS.items():
        build.packages.install(pkg, version=version)
    return setup_db(build)


def setup_db(build):
    return subprocess.call(["./manage.py", "migrate"])


@uranium.task_requires(main)
def develop(build):
    return subprocess.call(
        ["./manage.py", "runserver", "0.0.0.0:9001"]
    )


@uranium.task_requires(main)
def test(build):
    build.packages.install("py.test")
    return subprocess.call(["py.test", "tests"])
