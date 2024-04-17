import os
import json
import matplotlib.pyplot as plt
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
    
result =[]
file_paths = os.listdir('/Users/bijubiju/Downloads/Cutie 4/masks_1')
images = [img for img in os.listdir('/Users/bijubiju/Downloads/Cutie 4/masks_1') if img.endswith(".jpg")]

# Sort the image files in numerical order
images.sort(key=lambda x: int(x.split('.')[0]))

print(f"the number of files is {len(file_paths)}")
for file_path in images:
    if populaton_percentage_array(os.path.join('/Users/bijubiju/Downloads/Cutie 4/masks_1',file_path)) != None:
        result.append(populaton_percentage_array(os.path.join('/Users/bijubiju/Downloads/Cutie 4/masks_1',file_path)))

# Create an array of x values (indices)
y = result
x = np.arange(len(y))

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data with a colorful line
ax.plot(x, y, color='#FF6347', linewidth=2, label='Data')

# Customize the plot
ax.set_title('1D Array Plot', fontsize=16)
ax.set_xlabel('Index', fontsize=14)
ax.set_ylabel('Value', fontsize=14)
ax.legend(fontsize=12)
ax.grid(True)

# Adjust the color cycle for subsequent plots
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.plasma(np.linspace(0, 1, 9))))

# Display the plot
plt.show()