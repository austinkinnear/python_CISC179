from PIL import Image, ImageFilter
import os

def process_images(source_folder, output_folder):
    # List to keep track of new file names
    newFile = []

    for filename in os.listdir(source_folder):
        if filename.endswith('.jpg'):  # Makes sure we are working with jpg which we will convert to png
            # paths for source and output of Picture#
            source_path = os.path.join(source_folder, filename)
            output_filename = filename.replace('.jpg', '.png')
            output_path = os.path.join(output_folder, output_filename)

            # Converts each image to grayscale
            with Image.open(source_path) as img:
                gray_img = img.convert('L')

                # Gaussian blur to the grayscaled image, adjusting the radius increases or decreases the blur
                blurred_img = gray_img.filter(ImageFilter.GaussianBlur(radius=2))
                blurred_img.save(output_path)

            # Append the output file name to the list
            newFile.append(output_filename)

    # Writes the new file name within the txt file
    with open(os.path.join(output_folder, 'READ ME.txt'), 'w') as readme_file:
        for name in newFile:
            readme_file.write(name + '\n')

# Paths to my source and output
source_folder = r'C:\Users\austi\OneDrive\Desktop\python_CISC179\Midterm'
output_folder = r'C:\Users\austi\OneDrive\Desktop\python_CISC179\midtermProject\Midterm\ProcessedImages'

process_images(source_folder, output_folder)
