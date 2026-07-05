from yt_dlp import YoutubeDL


def download_video(url: str) -> None:
    opts = {
        "format": "best",
        "outtmpl": r"D:\VIDEO\MUSIC\%(title)s.%(ext)s",
        "quiet": True,
        "socket_timeout": 60,
        "retries": 10,
        "continued": True,
        "--js-runtimes": [r"node:C:\Program Files\nodejs\node.exe"],
    }

    with YoutubeDL(opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    lst = (
        ["https://www.youtube.com/watch?v=PBwECcU8Dag", "1"],
        # ["", ""],
    )
    for u, name in lst:
        try:
            print(f"{name} started")
            download_video(u)
        except BaseException as BE:
            print(f"{name} break. {BE}")
            continue
    print("end cycle")
