def main():
    file_name = input("Name: ")
    extension_finder(file_name)

def extension_finder(name):

    redundant, extension = name.strip().split(".")

    match extension:
        case "aac":
            print("audio/aac")
        case "avi":
            print("video/x-msvideo")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case _:
            print("We don't know!")

main()
