import cv2
from ultralytics import YOLO

def main():
    print("Initializing Gastropod Classification System...")

    model_path = "models/ScientificName.pt"
    try:
        model = YOLO(model_path)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please verify that 'best.pt' is in your project folder.")
        return

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Error: Could not access the camera. Check your hardware connections.")
        return

    print("Camera active. Starting live video feed...")
    print("Press 'q' in the video window to safely exit.")

    #Process the live video feed
    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to grab frame from camera. Exiting...")
            break

        # Run YOLOv8 instance segmentation on the current frame
        # stream=True optimizes memory usage on the Raspberry Pi
        # conf=0.50 sets the confidence threshold (adjust if needed)
        results = model.predict(source=frame, stream=True, conf=0.50, verbose=False)
        
        for r in results:
            annotated_frame = r.plot()

        # Display the live video feed
        cv2.imshow("Gastropod Classification System", annotated_frame)

        # Safely exit the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Shutting down the classification system...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()