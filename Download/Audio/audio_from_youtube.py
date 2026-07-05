from yt_dlp import YoutubeDL


def download_audio(url: str) -> None:
    opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,
        "socket_timeout": 60,
        "retries": 10,
        "continued": True,
        "javascript_runtimes": ["node"],

    }

    with YoutubeDL(opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    download_audio("https://youtube")
