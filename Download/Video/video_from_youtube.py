from yt_dlp import YoutubeDL

def download_video(url: str) -> None:
    opts = {
        "format": "best[ext=mp4]/best",
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,
        'socket_timeout': 60,
        'retries': 10,
        'continuedl': True,
        'merge_output_format': 'mp4',
    }

    with YoutubeDL(opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    download_video("https://youtu.be/mg9Kq1YaENI?si=gIrDfyqwNlUnSp8B")
