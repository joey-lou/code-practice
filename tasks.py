from invoke import task

PY_DIRECTORIES = [
    "old_code",
    "py_problems",
    "tasks.py",
]


@task(aliases=["fmt"])
def format(c):
    c.run(" ".join(["black", *PY_DIRECTORIES]))
    c.run(" ".join(["isort", *PY_DIRECTORIES]))
    c.run(
        " ".join(
            [
                "autoflake",
                "--in-place",
                "--remove-all-unused-imports",
                "--remove-unused-variables",
                "--remove-duplicate-keys",
                "--recursive",
                *PY_DIRECTORIES,
            ]
        )
    )
