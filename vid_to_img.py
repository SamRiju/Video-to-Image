import cv2
import os

def extract_frames(video_path, output_folder):
    """
    Extracts frames from the given video file and saves them as JPEG images
    in the specified output_folder.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Save the frame as a JPEG file with zero-padded numbering
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()

def main():
    



    input_folder = "D:/Sam/Main PROJECT/ACTION DETECTION/!test dataset/my"  # Change this to folder path





    if not os.path.isdir(input_folder):
        print("Provided path is not a folder.")
        return

    # Create a parent output folder
    base_name = os.path.basename(os.path.normpath(input_folder))
    output_parent_folder = os.path.join(input_folder, base_name + "_frames")
    os.makedirs(output_parent_folder, exist_ok=True)

    # Define allowed video file extensions
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')

    # Process each video in the folder
    for file in os.listdir(input_folder):
        if file.lower().endswith(video_extensions):
            video_path = os.path.join(input_folder, file)
            video_name = os.path.splitext(file)[0]

            # Create a folder for this video's frames
            video_output_folder = os.path.join(output_parent_folder, video_name)
            os.makedirs(video_output_folder, exist_ok=True)

            print(f"Processing: {video_path}")
            extract_frames(video_path, video_output_folder)
            print(f"Frames saved in: {video_output_folder}")

if __name__ == "__main__":
    main()
