import speedtest


st = speedtest.Speedtest()

download_speed = float(str(st.download())[0:2] + "." + str(round(st.download(), 2))[1])*0.125
upload_speed = float(str(st.upload())[0:2] + '.' + str(round(st.upload(), 2))[1])*0.125

print(f'Скорость скачивания: {download_speed} MB/s')
print(f'Скорость загрузки: {upload_speed} MB/s')
