import streamlit as st
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
            # Detect growth stage button and results display
            if st.button("Detect Growth Stage"):
                image = Image.open(uploaded_file)
                
                results = model(original_img)
                boxes = results[0].boxes.xyxy
                confidences = results[0].boxes.conf
                labels = results[0].boxes.cls
                detected_labels = [results[0].names[int(label)] for label in labels]
                updated_labels = []

                for label in detected_labels:
                    if label in label_map:
                        updated_labels.append(label_map[label])
                    else:
                        updated_labels.append(label)
        
                for i, (box, newlabel, confidence) in enumerate(zip(boxes, updated_labels, confidences)):
                    x1, y1, x2, y2 = map(int, box)
                    color = (255, 255, 0)
                    cv2.rectangle(original_img, (x1, y1), (x2, y2), color, 10)
                    label_str = f"{newlabel} ({confidence:.2f})"
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 1.5
                    font_thickness = 2
                    text_size = cv2.getTextSize(label_str, font, font_scale, font_thickness)[0]
                    text_x, text_y = x1, y1 - 10
                    label_bg_x2 = text_x + text_size[0] + 8
                    label_bg_y2 = text_y + text_size[1] + 4
                    cv2.rectangle(original_img, (text_x - 2, text_y - text_size[1] - 5), (label_bg_x2, label_bg_y2), (255, 255, 0), -1)
                    cv2.putText(original_img, label_str, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)
                    
    st.write("")
    st.write("Made by Team 45")
                    
# Run the app
if __name__ == '__main__':
    main()
