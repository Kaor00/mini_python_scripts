import instaloader

inst = instaloader.Instaloader()

user = ''

inst.download_profile(user, profile_pic_only=True)

# не работает без VPN
