# *****************************
#    СОПРОГРАММА. ИСКЛЮЧЕНИЯ
# *****************************


def grep(pattern):
    print("start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")


if __name__ == "__main__":
    g = grep("python")

    next(g)

    g.send("golang is better?")
    g.send("python is simple!")
    g.send("golang or python?")
    g.close()

    print("---------------------------")

    g = grep("python")

    g.send(None)

    g.send("golang or python?")
    # будет ровно эта ошибка ровно с этим текстом
    g.throw(RuntimeError, "something wrong")
