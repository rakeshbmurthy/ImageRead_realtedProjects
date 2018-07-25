from PIL import Image

img = Image.open('C:/Users/D E L L/Pictures/Saved Pictures/Calibration_Print_Adobe_RGB.jpg').convert('L')
#img.show()
img.save('C:/Users/D E L L/Pictures/Saved Pictures/Calibration_Print_Adobe_RGB_L.png')