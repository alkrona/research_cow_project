import os
import json

from PIL import Image
import numpy as np

def populaton_percentage_array(image_path:str):
    img = Image.open(image_path)
    numpy_array=np.array(img)
    numpy_array = numpy_array.flatten()
    size = numpy_array.shape[0]
    n_bins=len(np.unique(numpy_array))
    new_array = np.histogram(numpy_array,bins=n_bins)[0]
    new_array=np.divide(new_array,size)
    array_test= np.multiply(new_array,100)
    array_test = array_test[array_test>2e-01]
    return (len(array_test))
def cow_counter_app_accuracy_rater(function):
    error_sum=0
    json_file_path="test_json/test_images.json"
    f = open(json_file_path,)
    json_data=json.load(f)
    for item in json_data:
        error = abs(item["objects"] - function(item["file_path"]))
        print(f"number of objects is {item['objects']} function output is {function(item['file_path'])}")
        error_sum= error_sum + error
    print(f"total error sum is {error_sum}")
if __name__ =="__main__":
    cow_counter_app_accuracy_rater(populaton_percentage_array)