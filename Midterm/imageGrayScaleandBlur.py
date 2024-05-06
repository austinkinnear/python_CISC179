from PIL import Image, ImageFilter
import os

def process_images(source_folder, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # List to keep track of new file names
    new_file_names = []

    # Process each file in the source directory
    for filename in os.listdir(source_folder):
        if filename.endswith('.jpg'):  # Check for JPEG files
            # Construct full file path for source and output
            source_path = os.path.join(source_folder, filename)
            output_filename = filename.replace('.jpg', '.png')
            output_path = os.path.join(output_folder, output_filename)

            # Open the image, convert to grayscale
            with Image.open(source_path) as img:
                gray_img = img.convert('L')

                # Apply Gaussian blur to the grayscale image
                blurred_img = gray_img.filter(ImageFilter.GaussianBlur(radius=10))
                blurred_img.save(output_path)

            # Append the output file name to the list
            new_file_names.append(output_filename)

    # Write the list of new file names to a README file
    with open(os.path.join(output_folder, 'READ ME.txt'), 'w') as readme_file:
        for name in new_file_names:
            readme_file.write(name + '\n')

# Define the paths
source_folder = r'C:\Users\austi\OneDrive\Desktop\python_CISC179\Midterm'
output_folder = r'C:\Users\austi\OneDrive\Desktop\python_CISC179\midtermProject\Midterm\ProcessedImages'

# Call the function
process_images(source_folder, output_folder)
