import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

# Streamlit app
def main():
    st.title("Lumina Flora: Plant Growth Stage Detection Model")
    st.write("The plant growth stage detection model is a YOLOv8 Model that is capable of detecting plant growth stages: germination, growing, and harvesting.")

    # Load your YOLOv8 model
    model = YOLO("40 Epoch Plant Growth Stage YOLOv8 Model.pt")
    
    # Provide options for users to choose from
    option = st.selectbox("Select Level:", ["None", "Olmetie Lettuce", "Thurinus Lettuce"])
    
    # Conditional display for file uploader based on plant type selection
    if option != "None":
        st.write(f"Plant Type: {option}")
        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
        
        if uploaded_file:
            # Read the uploaded image as a numpy array
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            
            # Display the uploaded image
            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Uploaded Image", use_column_width=True)
            
            # Detect growth stage button and results display
            if st.button("Detect Growth Stage"):
                # Make predictions
                results = model.predict(source=image, save=False, conf=0.25)  # Adjust confidence threshold as needed
                
                # Get the original image dimensions
                annotated_image = image.copy()
                
                # Loop through detections and draw bounding boxes with OpenCV
                for result in results[0].boxes.data.tolist():  # Assuming YOLOv8 outputs boxes as list
                    x1, y1, x2, y2, confidence, class_id = map(int, result[:6])
                    class_name = model.names[class_id]
                    
                    # Draw bounding box
                    cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (255, 255, 0), 8)
                    
                    # Put label
                    label = f"{class_name} ({confidence:.2f})"
                    cv2.putText(annotated_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
                
                # Convert the annotated image to RGB for display in Streamlit
                st.image(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB), caption="Detected Growth Stages", use_column_width=True)
    
    st.write("")
    st.markdown("Made by Team 45")
                    
# Run the app
if __name__ == '__main__':
    main()
