import requests, datetime

lessons = ["Geography, Accounting, Math, Break (assembly), Physics (11:15), EDG, Break (13:00), English (13:40)", #0
           "English, Physics, Afrikaans, Break, Biology (11:10), LO, Break (12:55 IT duty), Math (13:30)", #1
           "History, TTS, Break (assembly), Geography, English, Break (13:20), Math (13:40)", #2
           "English, Accounting, Art, Break, Math (10:55), Physics, Afrikaans, Break (13:20), Biology (13:40)", #3
           "Accounting, Drama, Math, Break (assembly), Afrikaans (11:10), Art, Break (12:45), History (13:20)", #4

           "English, Physics, Accounting, Break (assembly), Math (11:15), EDG, Break (13:00), Geography (13:40)", #5
           "English, Math, Accounting, Break, Afrikaans (11:10), Biology, Break (12:55 IT duty) , Drama (13:30)", #6
           "Drama, TTS, Break (assembly), Math, Afrikaans, Break (13:20), English (13:40)", #7
           "History, Art, Afrikaans, Break, Physics (10:55), Math, English, Break (13:20), Geography (13:40)", #8
           "Accounting, EDG, Math, Break (assembly), Biology (11:10), History, Break (12:45), Afrikaans (13:20)"] #9


def calculateDay():
    with open("dayInfo.txt") as f:
        dayInfo = f.read()

    lastSchoolDay = int(dayInfo[:2])
    date = dayInfo[-10:]
    day = datetime.datetime.now().weekday()

    if day != 5 or 6:
        if lastSchoolDay >= 10:
            lastSchoolDay = 0
        else:
           lastSchoolDay += 1

        notification(lessons[lastSchoolDay])

        date = datetime.datetime.now().date()
        with open("dayInfo.txt", "w") as f:
            f.write(f"{lastSchoolDay} {date}")

    else:
        pass


def notification(message):
    report = {}
    report["value1"] = message
    requests.post("https://maker.ifttt.com/trigger/{channel name}/with/key/{key here}", data=report)
    print("Posted data")

if __name__ == '__main__':
    calculateDay()
    with open("dayInfo.txt") as f:
        dayInfo = f.read()
    print(dayInfo)
