import fitz  # PyMuPDF
from PIL import Image
import cv2
import os

def convert_pdf_to_images(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)

    images = []

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap()
        images.append((page_number + 1, Image.frombytes("RGB", [image.width, image.height], image.samples)))

    pdf_document.close()

    return images

def enhance_text(images):
    enhanced_images = []

    for page_number, image in images:
        # Convert PIL Image to OpenCV format
        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Apply image enhancement (e.g., contrast and sharpness adjustments)
        enhanced_image = cv2.convertScaleAbs(cv_image, alpha=1.5, beta=30)

        # Convert back to PIL Image
        enhanced_image_pil = Image.fromarray(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB))
        enhanced_images.append((page_number, enhanced_image_pil))

    return enhanced_images

def save_images(images, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for page_number, image in images:
        image_path = f"{output_folder}/enhanced_page_{page_number}.png"
        image.save(image_path)
        print(f"Enhanced page {page_number} saved as {image_path}")

def main():
    pdf_path = "english.pdf"
    output_folder = "enhanced_images"

    images = convert_pdf_to_images(pdf_path, output_folder)
    enhanced_images = enhance_text(images)

    # Sort images based on page number
    enhanced_images = sorted(enhanced_images, key=lambda x: x[0])

    save_images(enhanced_images, output_folder)

if __name__ == "__main__":
    main()
