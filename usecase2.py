from PIL import Image
import pytesseract

# Set the tesseract executable path (if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your tesseract path

def extract_text_from_image(image_path):
    # Open the image using PIL
    img = Image.open(image_path)
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img)
    
    return text

# Example usage
image_path = r'"C:\Users\vishv\OneDrive\Desktop\inportan\download.png"'  # Replace with your image path
text = extract_text_from_image(image_path)
print(text)
