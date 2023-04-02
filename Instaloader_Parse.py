import instaloader


il = instaloader.Instaloader()
profile = instaloader.Profile.from_username(il.context, "coding_unicorn")

print(f"Profile info:\n{profile.biography}\nPosts count: {profile.mediacount}\nFollowers:"
      f"{profile.followers}")

# Не работает
