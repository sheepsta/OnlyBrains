import cv2
from fer import FER

def detect_dominant_emotion_from_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    ret, frame = cap.read()

    cap.release()

    if not ret:
        print("Error: Could not read frame from webcam.")
        return
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #### Detecting Emotions: 
    detector = FER()
    emotions = detector.detect_emotions(frame_rgb)

    if not emotions:
        print("No face detected")
        return

    dominant_emotion, emotion_score = detector.top_emotion(frame_rgb)

    ### Code for displaying the one captured frame corresponding to the emotion
    #frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
    #cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    #cv2.imshow('Captured Frame', frame)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return dominant_emotion

if __name__ == "__main__":
    # Detect and print the dominant emotion from the webcam frame
    dominant_emotion = detect_dominant_emotion_from_webcam()
    if dominant_emotion:
        print(f"Dominant emotion: {dominant_emotion}")
