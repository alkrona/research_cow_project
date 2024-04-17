import os
import sys
import random
import json
def create_image_file():
    file_list = []
    dir_path = '/Users/bijubiju/Downloads/cutie4/masks'

    # Create the target directory if it doesn't exist
    target_dir = '/Users/bijubiju/Desktop/ml projects/current/research_cow_project/test/test_images'
    os.makedirs(target_dir, exist_ok=True)

    for item in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, item)):
            file_list.append(os.path.join(dir_path, item))

    test_file_paths = []
    for _ in range(4):
        test_file_paths.append(random.choice(file_list))

    for file_path in test_file_paths:
        file_name = os.path.basename(file_path)
        target_path = os.path.join(target_dir, file_name)
    os.rename(file_path, target_path)
def create_json_file():
    test_files = {}
    list_of_number_of_objectgs_in_each_image =[20,18,17,16]
    file_path_test_images = "/Users/bijubiju/Desktop/ml projects/current/research_cow_project/test/test_images"
    for file_path in os.listdir(file_path_test_images):
        print("echo")
if __name__ =='__main__':
    globals()[sys.argv[1]]()