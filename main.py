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
                results = model.predict(source=image, save=False, conf=0.25)
                st.markdown("### Results:")
                for r in results:
                    st.write(f"Detected {r['name']} with confidence: {r['confidence']:.2f}")

                # Save and display the prediction image with annotations
                annotated_image = results[0].plot()  # Annotate first result
                st.image(annotated_image, caption="Detected Growth Stages", use_column_width=True)
                    
    st.write("")
    st.write("Made by Team 45")
                    
# Run the app
if __name__ == '__main__':
    main()
