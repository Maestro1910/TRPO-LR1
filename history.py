history = []


def save(record):
    history.append(record)


def show():
    for item in history:
        print(item)
