import os
from PIL import Image

# Path to the static/images folder
static_images_folder = os.path.join(os.getcwd(), "static")

# Check if the folder exists
print("Script started...")

if not os.path.exists(static_images_folder):
    print("The images folder does not exist!")
else:
    print(f"The images folder exists: {static_images_folder}")

    # List files in the folder
    print("Files in the images folder:")
    files = os.listdir(static_images_folder)
    print(files)

    # Check and compress images
    for filename in files:
        if filename.endswith((".png", ".jpg", ".jpeg", "JPG")):
            image_path = os.path.join(static_images_folder, filename)
            print(f"Found image: {image_path}")

            try:
                img = Image.open(image_path)
                img.save(image_path, format="WebP", optimize=True)
                print(f"Compressed and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


