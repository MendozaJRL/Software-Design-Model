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
    option = st.selectbox("Select Plant Type:", ["None", "Olmetie Lettuce", "Thurinus Lettuce"])
    
    # Conditional display for file uploader based on plant type selection
    if option != "None":
        st.write(f"Plant Type: {option}")
        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
        
        if uploaded_file:
            # Detect growth stage button and results display
            if st.button("Detect Growth Stage"):
                # Placeholder for model inference (add your detection logic here)
                st.markdown("### Results:")
                st.write("Detection complete! (Placeholder for model output)")
    
    st.write("")
    st.write("Made by Team 45")
                    
# Run the app
if __name__ == '__main__':
    main()
