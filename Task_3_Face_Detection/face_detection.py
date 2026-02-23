# Face Detection using Haar Cascade
# CodSoft AI Internship - Task 3


import cv2
import os
import time


def load_cascade():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cascade_path = os.path.join(current_dir, "haarcascade_frontalface_default.xml")

    if not os.path.exists(cascade_path):
        print("Haar cascade file not found.")
        exit()

    return cv2.CascadeClassifier(cascade_path)


def detect_and_save(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    count = 0

    for (x, y, w, h) in faces:
        count += 1

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Add label
        cv2.putText(frame, "Face Detected", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2)

        # Save face crop
        face_crop = frame[y:y + h, x:x + w]
        save_path = os.path.join(os.path.dirname(__file__), f"detected_face_{count}.jpg")
        cv2.imwrite(save_path, face_crop)

    # Show face count
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 0, 255), 2)

    return frame


def webcam_mode(face_cascade):
    cap = cv2.VideoCapture(1)

    # Give camera time to initialize
    time.sleep(1)

    if not cap.isOpened():
        print("Camera could not be opened.")
        return

    print("Press 'q' inside the camera window to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            continue

        frame = detect_and_save(frame, face_cascade)

        cv2.imshow("Webcam Face Detection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exiting webcam mode...")
            break

    cap.release()
    cv2.destroyAllWindows()


def image_mode(face_cascade):
    image_path = input("Enter image file path: ")

    if not os.path.exists(image_path):
        print("Image not found.")
        return

    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    image = detect_and_save(image, face_cascade)

    cv2.imshow("Image Face Detection", image)
    print("Press any key inside the image window to close.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    face_cascade = load_cascade()

    print("\nSelect Mode:")
    print("1. Webcam Detection")
    print("2. Image Detection")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        webcam_mode(face_cascade)
    elif choice == "2":
        image_mode(face_cascade)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()