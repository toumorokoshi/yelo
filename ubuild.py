REQUIREMENTS = {
    "django": "==1.9.1",
    "djangorestframework": "==3.3.2",
    "gunicorn": None,
    "jedi": None,
    "pep8": None
}


def main(build):
    for pkg, version in REQUIREMENTS.items():
        build.packages.install(pkg, version=version)
