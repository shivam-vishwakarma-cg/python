hour=int(input("hour"))
if hour>=1 and hour<=12:
    min=int(input("minutes"))
    if min>=1 and min<=59:
        sec=int(input("second"))
        if sec>=1 and sec<59:
            print("valid time",hour,":",min,":",sec)
