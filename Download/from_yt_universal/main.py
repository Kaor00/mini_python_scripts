from yt_dlp import YoutubeDL

def dl(url: str, **kwargs: dict[str, str]) -> None:
    opts = {
        **kwargs,
        "quiet": True,
        "socket_timeout": 60,
        "retries": 10,
        "continued": True,
        "--js-runtimes": [r"node:C:\Program Files\nodejs\node.exe"],
    }

    with YoutubeDL(opts) as ydl:
        ydl.download([url])

"""Позволяет скачать видео или аудио в зависимости от передаваемого формата
    Функция принимает кортеж массивов, где каждый массив это набор следующих данных
    1 - ссылка на видео
    2 - краткое название для терминала (для понимания)
    3 - формат файла (видео или аудио)
    4 - место для сохранения (создает папку, если её нет)"""
if __name__ == "__main__":
    lst = (
        # ["https://www.youtube.com/watch?v=", "1", "video", r"D:\EXAMPLE\%(title)s.%(ext)s"],
        ["https://www.youtube.com/watch?v=", "1", "audio", r"D:\EXAMPLE\AUDIO\%(title)s.%(ext)s"],
        # ["", ""],
    )
    for u, name, _type, path in lst:
        try:
            obj = {
                "format": "best" if _type == "video" else "bestaudio/best",
                "outtmpl": path
            }
            print(f"{name} started")
            dl(u, **obj)
        except BaseException as BE:
            print(f"{name} break. {BE}")
            continue
    print("end cycle")
