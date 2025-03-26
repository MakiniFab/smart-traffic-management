import cv2

def detect_cars(image_path):
    # Load pre-trained Haar cascade model for car detection
    car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect cars in the image
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # Draw rectangles around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the processed image
    cv2.imshow("Detected Cars", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the count of detected cars
    return len(cars)

# Test with a sample traffic image
if __name__ == "__main__":
    car_count = detect_cars('static/traffic.jpg')
    print(f"Number of cars detected: {car_count}")