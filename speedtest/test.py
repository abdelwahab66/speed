from speedtest import Speedtest

wifi = Speedtest()


print("getting download speed.....")

download = wifi.download()
print(f"download: {download / 1024 /1024 } mbps")


print("getting upload speed ....")
upload = wifi.upload()
print(f"upload : {upload / 1024 /1024} mbps")
