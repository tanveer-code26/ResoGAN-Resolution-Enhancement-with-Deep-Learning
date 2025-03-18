import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf

def preprocess_image(image, target_size):
    """Resize and normalize the input image.""" 
    image = image.resize(target_size)
    image_array = np.array(image) / 255.0  # Normalize to [0, 1]
    return np.expand_dims(image_array, axis=0)  # Add batch dimension

def postprocess_image(image_array):
    """Convert the model output to a displayable image."""
    image_array = (image_array[0] * 255.0).clip(0, 255).astype(np.uint8)
    return Image.fromarray(image_array)

# Load the trained generator model
generator = load_model("generator_model.h5", compile=False)

def main():
    st.title("Image Quality Enhancer")
    st.write("Upload a low-resolution image, and the model will enhance its quality.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.write("### Uploaded Image")
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Process the image
        st.write("### Enhanced Image")
        with st.spinner("Enhancing image quality..."):
            input_image = preprocess_image(image, target_size=(64, 64))  # Match generator input size
            enhanced_image_array = generator.predict(input_image)
            enhanced_image = postprocess_image(enhanced_image_array)

        # Display the enhanced image
        st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)

if __name__ == "__main__":
    main()