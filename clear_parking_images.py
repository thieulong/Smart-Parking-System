import os, shutil
folder = 'parking_areas/'

for filename in os.listdir(folder):

    file_path = os.path.join(folder, filename)

    try:

        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
            print("[INFO] Successfully removed {}".format(filename))

        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            print("[INFO] Successfully removed {}".format(filename))

    except Exception as e:
        print('[ERROR] Failed to delete %s. Reason: %s' % (file_path, e))

dir = os.listdir(folder)

if len(dir) == 0:
    print("[INFO] Successfully deleted all files in {}".format(folder))