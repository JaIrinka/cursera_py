# *****************************
#         СОПРОГРАММА
#
# сопрограмма = корутина = coroutine
# *****************************


def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


if __name__ == "__main__":
    g = grep("python")

    next(g)
    # g.send(None)

    g.send("golang is better?")
    g.send("python is simple!")
    g.send("golang or python?")
