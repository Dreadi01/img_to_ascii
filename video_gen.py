import cv2
import img_gen
import os

# Open the video file
video_path = "video_test.mp4"  # Replace "video.mp4" with the path to your video file
video = cv2.VideoCapture(video_path)

frame_count = 0
while True:
    # Read the next frame
    ret, frame = video.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Process the frame (you can perform any operations here)
    # For example, you can save the frame as an image
    frame_filename = f"frames/frame_{frame_count}.png"
    cv2.imwrite(frame_filename, frame)

    img_gen.img_gen(frame_filename)

    # Increment the frame count
    frame_count += 1

    frame_height, frame_width= 1000, 1000

# Release the video object
video.release()



# Directory containing the images
images_directory = "gen_imgs"  # Replace this with the path to your images directory

# Output video file
output_video_path = "output_video.mp4"

# Get a list of image files in the directory
image_files = [os.path.join(images_directory, file) for file in os.listdir(images_directory) if file.endswith((".jpg", ".png"))]

# Sort the image files by name
image_files.sort()

# Get the first image to determine the frame size
first_image = cv2.imread(image_files[0])
frame_height, frame_width, _ = first_image.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use other codecs as well, such as 'XVID', 'MJPG', etc.
out = cv2.VideoWriter(output_video_path, fourcc, 30, (frame_width, frame_height))  # 30 is the frame rate (change as needed)

# Loop through the image files and write them to the video
for image_file in image_files:
    frame = cv2.imread(image_file)
    out.write(frame)

# Release the VideoWriter object
out.release()
print("Video Created")