extension = input("Enter extension: ")

match extension:
    case "pdf":
        print("Document")
    case "jpg":
        print("Image")
    case "png":
        print("Image")
    case "mp3":
        print("Audio File")
    case "mp4":
        print("Video File")
    case _:
        print("Unknown File Type")