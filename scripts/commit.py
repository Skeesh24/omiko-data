from subprocess import call


values = input()

branch = message = " "

if ":" in values:
    message = values.split(":")[0]
    branch = values.split(":")[1]
else:
    message = values

call(
    [
        "git",
        "add",
        ".",
    ]
)

call(
    [
        "git",
        "commit",
        "-m",
        message,
    ]
)
