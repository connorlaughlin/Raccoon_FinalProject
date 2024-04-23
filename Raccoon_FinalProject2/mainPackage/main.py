# Name: Kaileb Strasser, Max Schiller, & Connor Laughlin
# email: strassks@mail.uc.edu, schillmx@mail.uc.edu, laughlcd@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypt text and json files to uncover details about taking a group photo on campus with a movie quote
# Brief Description of what this module does: Calls all the functions and classes that we created and prints desires results to console
# Citations: Chat GPT
# Anything else that's relevant:

#main.py

from functionPackage.function import *
from ImageLoaderPackage.ImageLoader import *

if __name__ == "__main__":

    encrypted_data = [42061, 44404, 28799, 298, 8848, 27781, 105654, 21723, 47096, 8021, 28420, 19312, 22147, 42049, 23887, 599, 105655, 24232, 19312, 9443]
    
    text_file = "../Files/UCEnglish.txt"
    decrypted_location = decrypt_location(encrypted_data, text_file)
    print("Decrypted location:", decrypted_location)
    
    # Decrypting the movie name
    key = b'4g8xAE7lajIzp6UTyITiAGOYMSGzs5qKeMIdoT_js6U='
    encrypted_movie = b'gAAAAABlTNM6fhccI70O7U91J2_HH6KjfNse0GcAqBZVV3h2ZO9TV8dXixIWR8UABjYYmchhPdoRnR-GlEcqJI7tY-ogTaf2fQ=='
    decrypted_movie = decrypt_message(encrypted_movie, key)
    print("Decrypted Movie Name:", decrypted_movie)
    
    # ImageLoader
    image_loader = ImageLoader("../Files/IMG_4589.jpg")
    image = image_loader.load_image()
    
    # Print the image to the console
    print("Loaded image:")
    print(image)
        
    