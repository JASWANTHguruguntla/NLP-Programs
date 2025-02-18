import cv2
import numpy as np

def detect_emotion_by_color(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return "Error: Unable to load image. Check the file path."

    # Convert image to HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Calculate the average hue (color tone)
    avg_hue = np.mean(hsv[:, :, 0])

    # Emotion mapping based on color psychology
    if avg_hue < 20 or avg_hue > 160:  
        emotion = "Angry (Red tones detected)"
    elif 20 <= avg_hue < 40:  
        emotion = "Happy (Yellow tones detected)"
    elif 40 <= avg_hue < 75:  
        emotion = "Relaxed (Green tones detected)"
    elif 75 <= avg_hue < 130:  
        emotion = "Sad (Blue tones detected)"
    else:  
        emotion = "Neutral (Balanced colors detected)"

    return f"Detected Emotion: {emotion}"

# Get image path from user
for i in range(0,10):
   ip=input("Enter the image file path (e.g., ./angry.jpg): ")
   if(ip=='exit'):
       break
   else:
       image_path =ip.strip()
       print(detect_emotion_by_color(image_path))
