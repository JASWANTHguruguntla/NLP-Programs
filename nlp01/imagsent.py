import cv2
from deepface import DeepFace
import os

def analyze_emotion(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Check if the image was loaded correctly
    if img is None:
        print(f"Could not open or find the image: {image_path}")
        return

    # Perform emotion analysis using DeepFace
    try:
        analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
        # Extract emotion results
        dominant_emotion = analysis[0]['dominant_emotion']
        print(f"Dominant emotion detected: {dominant_emotion}")
    except Exception as e:
        print(f"Error in emotion analysis: {e}")

def main():
    folder_path = input("Enter the folder path containing the images: ")

    # Validate the folder path
    if not os.path.exists(folder_path):
        print(f"The folder path {folder_path} does not exist.")
        return
    
    # Get all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png'))]

    if not image_files:
        print("No images found in the folder.")
        return

    # Analyze each image in the folder
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print(f"\nAnalyzing image: {image_file}")
        analyze_emotion(image_path)

if __name__ == "__main__":
    main()
