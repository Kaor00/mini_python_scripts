from fake_useragent import UserAgent


ua = UserAgent()

print(ua.ie)
print(ua.msie)
print(ua["Internet Explorer"])
print(ua.opera)
print(ua.chrome)
print(ua.googlechrome)
print(ua.firefox)
print(ua.ff)
print(ua.safari)
