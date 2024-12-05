import streamlit as st
from PIL import Image
from ultralytics import YOLO

# Streamlit app
def main():
    st.title("Lumina Flora: Plant Growth Stage Detection Model")
    st.write("The plant growth stage detecion model is a YOLOv8 Model that is capable of detecting plant growth stages specifically, germination, growing, and harvesting.")

    # Provide options for users to choose from
    option = st.selectbox("Select Plant Type:", ["Level 1: Olmetie Lettuce", "Level 2: Thurinus Lettuce"])
    
    if st.button("Detect Growth Stage"):
        # Display the calculated materials in a more organized way using Markdown
        st.markdown("### Results:")
        
    st.write("")
    st.write("Made by Team 45")
                    
# Run the app
if __name__ == '__main__':
    main()
