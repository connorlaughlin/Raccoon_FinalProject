# Name: Kaileb Strasser, Max Schiller, & Connor Laughlin
# email: strassks@mail.uc.edu, schillms@mail.uc.edu, laughlcd@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypt text and json files to uncover details about taking a group photo on campus with a movie quote
# Brief Description of what this module does: Finds the image and loads it.
# Citations: Chat GPT
# Anything else that's relevant:

# ImageLoaderClass.py

from PIL import Image

class ImageLoader:
    def __init__(self, file_path):
        '''
      Constructor for the ImageLoaderClass
      @Param: file_path: The path to the image
      '''
        # Constructor to initialize the file path
        self.file_path = file_path

    def load_image(self):
        '''
        Returns an image
        @Return: Image
        '''
        try:
            # Try opening the image file using PIL's Image.open method
            with Image.open(self.file_path) as img:
                # Show the image using PIL's show method
                img.show()
                # Return the loaded image object
                return img
        except FileNotFoundError:
            # Handle the case where the file is not found
            print('Image not found')