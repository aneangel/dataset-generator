import getpass

counter = 0

username = getpass.getuser()
file_path = "/Users/{0}/dataset-image-detection/images/*.jpg".format(username)


for image in file_path:
    counter += 1

print(counter)