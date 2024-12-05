import streamlit as st
import cv2
import numpy as np
from PIL import Image
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
            # Convert the uploaded image to a NumPy array
            image = Image.open(uploaded_file)
            image_np = np.array(image)
            
            # Detect growth stage button and results display
            if st.button("Detect Growth Stage"):
                results = model(image_np)
                boxes = results[0].boxes.xyxy.cpu().numpy()  # Convert to numpy
                confidences = results[0].boxes.conf.cpu().numpy()
                labels = results[0].boxes.cls.cpu().numpy()
                detected_labels = [results[0].names[int(label)] for label in labels]
                updated_labels = []

                label_map = {
                    'Flowering': 'Growing',
                    'Vegetative': 'Growing',
                    'Germination': 'Germination',
                    'Harvesting': 'Harvesting'
                }
                
                for label in detected_labels:
                    if label in label_map:
                        updated_labels.append(label_map[label])
                    else:
                        updated_labels.append(label)

                # Annotate the image using OpenCV
                annotated_image = image_np.copy()
                for i, (box, newlabel, confidence) in enumerate(zip(boxes, updated_labels, confidences)):
                    x1, y1, x2, y2 = map(int, box)
                    color = (255, 255, 0)
                    cv2.rectangle(annotated_image, (x1, y1), (x2, y2), color, 2)
                    label_str = f"{newlabel} ({confidence:.2f})"
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 0.5
                    font_thickness = 1
                    text_size = cv2.getTextSize(label_str, font, font_scale, font_thickness)[0]
                    text_x, text_y = x1, y1 - 10
                    label_bg_x2 = text_x + text_size[0] + 4
                    label_bg_y2 = text_y + text_size[1] + 4
                    cv2.rectangle(annotated_image, (text_x - 2, text_y - text_size[1] - 4), 
                                  (label_bg_x2, label_bg_y2), (255, 255, 0), -1)
                    cv2.putText(annotated_image, label_str, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)
                
                # Convert the annotated image back to RGB for display in Streamlit
                annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                st.image(annotated_image_rgb, caption="Detected Growth Stages", use_column_width=True)
    
    st.write("")
    st.write("Made by Team 45")
                    
# Run the app
if __name__ == '__main__':
    main()
