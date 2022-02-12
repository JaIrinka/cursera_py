# *****************************
#    СОПРОГРАММА. ВЫЗОВЫ
# *****************************


def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_pupka_no_coroutine():
    g = grep("pupka")
    next(g)
    g.send("my little pupka")
    g.close()


def grep_sooska_coroutine():
    g = grep("soos")
    yield from g


if __name__ == "__main__":
    # не сопрограмма! PEP 380
    g = grep_pupka_no_coroutine()
    print(g)
    print("---------------------------")

    # сопрограмма! yield from PEP 0380
    g = grep_sooska_coroutine()
    print(g)
    g.send(None)
    g.send("it is soos! wow!")
