import instaloader


loader = instaloader.Instaloader()
username = input("Enter username: ")
loader.download_profile(username, profile_pic_only=True)
loader.download_profile(username, download_stories_only=True)
loader.download_profile(username, download_tagged_only=True)

# НЕ работает
