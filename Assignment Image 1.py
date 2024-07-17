#imports
import cv2 as cv2
import numpy as np
import pygame
import sys



#read and show orignal image
image = cv2.imread('hambola.jpg',0)


'''
print(image)
print(image.shape)
cv2.imshow('Image', image)
'''


#convert each pixel from decimal to binary
height,width=image.shape
binary_image = []
for i in range(0,height):
    for j in range(0,width):
         binary_image.append(np.binary_repr(image[i][j] ,width=8))
'''        
print(binary_image)
print(len(binary_image))
'''


#put each bit in list to create 8 lists
first_digits = []
second_digits = []
third_digits = []
fourth_digits = []
fifth_digits = []
sixth_digits = []
seventh_digits = []
eighth_digits = []

for inner_binary_image in binary_image:
    first_digits.append(inner_binary_image[7])
    second_digits.append(inner_binary_image[6])
    third_digits.append(inner_binary_image[5])
    fourth_digits.append(inner_binary_image[4])
    fifth_digits.append(inner_binary_image[3])
    sixth_digits.append(inner_binary_image[2])
    seventh_digits.append(inner_binary_image[1])
    eighth_digits.append(inner_binary_image[0])
'''
print("Original list:", binary_image)

print("First digits list:", first_digits)
print("Second digits list:", second_digits)
print("Third digits list:", third_digits)
print("Fourth digits list:", fourth_digits)
print("Fifth digits list:", fifth_digits)
print("Sixth digits list:", sixth_digits)
print("Seventh digits list:", seventh_digits)
print("Eighth digits list:", eighth_digits)

print(len(binary_image))

print(len(first_digits))
print(len(second_digits))
print(len(third_digits))
print(len(fourth_digits))
print(len(fifth_digits))
print(len(sixth_digits))
print(len(seventh_digits))
print(len(eighth_digits))
'''



#reshape all list to be 2d matrix and check about them
matrix_first_digits = np.reshape(first_digits, (height,width))
matrix_second_digits = np.reshape(second_digits, (height,width))
matrix_third_digits = np.reshape(third_digits, (height,width))
matrix_fourth_digits = np.reshape(fourth_digits, (height,width))
matrix_fifth_digits = np.reshape(fifth_digits, (height,width))
matrix_sixth_digits = np.reshape(sixth_digits, (height,width))
matrix_seventh_digits = np.reshape(seventh_digits, (height,width))
matrix_eighth_digits = np.reshape(eighth_digits, (height,width))


'''
print("First digits list:", matrix_first_digits)
print("Second digits list:", matrix_second_digits)
print("Third digits list:", matrix_third_digits)
print("Fourth digits list:", matrix_fourth_digits)
print("Fifth digits list:", matrix_fifth_digits)
print("Sixth digits list:", matrix_sixth_digits)
print("Seventh digits list:", matrix_seventh_digits)
print("Eighth digits list:", matrix_eighth_digits)

print(matrix_first_digits.shape)
print(matrix_second_digits.shape)
print(matrix_third_digits.shape)
print(matrix_fourth_digits.shape)
print(matrix_fifth_digits.shape)
print(matrix_sixth_digits.shape)
print(matrix_seventh_digits.shape)
print(matrix_eighth_digits.shape)
'''



#contert each binary list into decimal according to its index
new1=matrix_first_digits.astype(np.uint8) * 2**0
new2=matrix_second_digits.astype(np.uint8) * 2**1
new3=matrix_third_digits.astype(np.uint8) * 2**2
new4=matrix_fourth_digits.astype(np.uint8) * 2**3
new5=matrix_fifth_digits.astype(np.uint8) * 2**4
new6=matrix_sixth_digits.astype(np.uint8) * 2**5
new7=matrix_seventh_digits.astype(np.uint8) * 2**6
new8=matrix_eighth_digits.astype(np.uint8) * 2**7

'''
#show 8 bit plane images
print("1:")
cv2.imshow('Image1', new1)
print("")
print("2:")
cv2.imshow('Image2', new2)
print("")
print("3:")
cv2.imshow('Image3', new3)
print("")
print("4:")
cv2.imshow('Image4', new4)
print("")
print("5:")
cv2.imshow('Image5', new5)
print("")
print("6:")
cv2.imshow('Image6', new6)
print("")
print("7:")
cv2.imshow('Image7', new7)
print("")
print("8:")
cv2.imshow('Image8', new8)
print("")
'''



#summution operation
summution=new1+new2+new3+new4+new5+new6+new7+new8
'''
cv2.imshow('summation', summution)
'''


'''
#check original minus summution
dif=image-summution
print(dif)
cv2.imshow('dif', dif)
'''



#write image to create them
cv2.imwrite("image1.jpg", new1)
cv2.imwrite("image2.jpg", new2)
cv2.imwrite("image3.jpg", new3)
cv2.imwrite("image4.jpg", new4)
cv2.imwrite("image5.jpg", new5)
cv2.imwrite("image6.jpg", new6)
cv2.imwrite("image7.jpg", new7)
cv2.imwrite("image8.jpg", new8)
cv2.imwrite("summutionimage.jpg", summution)




'''
#read them as new images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')
image3 = cv2.imread('image3.jpg')
image4 = cv2.imread('image4.jpg')
image5 = cv2.imread('image5.jpg')
image6 = cv2.imread('image6.jpg')
image7 = cv2.imread('image7.jpg')
image8 = cv2.imread('image8.jpg')
'''




# Initialize Pygame
pygame.init()

# Set the window size
window_width, window_height = 1500, 700

# Create the window
window = pygame.display.set_mode((window_width, window_height))


# Set the background color to black
background_color = (255, 255, 255)  # RGB color tuple
window.fill(background_color)


# Load the images
imagenew1 = pygame.image.load("image1.jpg")
imagenew2 = pygame.image.load("image2.jpg")
imagenew3 = pygame.image.load("image3.jpg")
imagenew4 = pygame.image.load("image4.jpg")
imagenew5 = pygame.image.load("image5.jpg")
imagenew6 = pygame.image.load("image6.jpg")
imagenew7 = pygame.image.load("image7.jpg")
imagenew8 = pygame.image.load("image8.jpg")
summutionimage = pygame.image.load("summutionimage.jpg")

# resize the images
imagenew1 = pygame.transform.scale(imagenew1, (200, 200))
imagenew2 = pygame.transform.scale(imagenew2, (200, 200))
imagenew3 = pygame.transform.scale(imagenew3, (200, 200))
imagenew4 = pygame.transform.scale(imagenew4, (200, 200))
imagenew5 = pygame.transform.scale(imagenew5, (200, 200))
imagenew6 = pygame.transform.scale(imagenew6, (200, 200))
imagenew7 = pygame.transform.scale(imagenew7, (200, 200))
imagenew8 = pygame.transform.scale(imagenew8, (200, 200))
summutionimage= pygame.transform.scale(summutionimage, (200, 200))

# Get the image size
imagenew1_width, imagenew1_height = imagenew1.get_size()
imagenew2_width, imagenew2_height = imagenew2.get_size()
imagenew3_width, imagenew3_height = imagenew3.get_size()
imagenew4_width, imagenew4_height = imagenew4.get_size()
imagenew5_width, imagenew5_height = imagenew5.get_size()
imagenew6_width, imagenew6_height = imagenew6.get_size()
imagenew7_width, imagenew7_height = imagenew7.get_size()
imagenew8_width, imagenew8_height = imagenew8.get_size()
summutionimage_width,summutionimage_height = summutionimage.get_size()

# Blit the image onto the window
window.blit(image, (0, 0))
window.blit(imagenew1, (5, 15))
window.blit(imagenew2, (imagenew1_width+15, 15))
window.blit(imagenew3, (imagenew2_width*2+25, 15))
window.blit(imagenew4, (imagenew3_width*3+35, 15))
window.blit(imagenew5, (5, imagenew1_height+40))
window.blit(imagenew6, (imagenew1_width+15, imagenew2_height+40))
window.blit(imagenew7, (imagenew2_width*2+25, imagenew3_height+40))
window.blit(imagenew8, (imagenew3_width*3+35, imagenew4_height+40))
window.blit(summutionimage, (1100,300))


# Set up the font
font = pygame.font.Font(None, 20)
# Render the text surface
text_surface1 = font.render("bit 1 image:", True, (0, 0, 0))
text_surface2 = font.render("bit 2 image:", True, (0, 0, 0))
text_surface3 = font.render("bit 3 image:", True, (0, 0, 0))
text_surface4 = font.render("bit 4 image:", True, (0, 0, 0))
text_surface5 = font.render("bit 5 image:", True, (0, 0, 0))
text_surface6 = font.render("bit 6 image:", True, (0, 0, 0))
text_surface7 = font.render("bit 7 image:", True, (0, 0, 0))
text_surface8 = font.render("bit 8 image:", True, (0, 0, 0))
text_surface9 = font.render("The Summution Of All 8 Bits:", True, (0, 0, 0))
# Draw the text surface on the window
window.blit(text_surface1, (5, 0))
window.blit(text_surface2, (imagenew1_width+15, 0))
window.blit(text_surface3, (imagenew2_width*2+25, 0))
window.blit(text_surface4, (imagenew3_width*3+35, 0))
window.blit(text_surface5, (5, imagenew1_height+20))
window.blit(text_surface6, (imagenew1_width+15, imagenew2_height+20))
window.blit(text_surface7, (imagenew2_width*2+25, imagenew3_height+20))
window.blit(text_surface8, (imagenew3_width*3+35, imagenew4_height+20))
window.blit(text_surface9, (1100,280))

# Update the display
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


cv2.waitKey(0)
cv2.destroyAllWindows()