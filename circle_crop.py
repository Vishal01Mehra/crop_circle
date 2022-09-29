
import numpy as np
from PIL import Image, ImageDraw
  
tempImg=Image.open("image.jpg")
#display(img)
left_1 = 500
top_1 = 30
right_1 = 3350
bottom_1 = 2850

img = imgres_1 = tempImg.crop((left_1, top_1, right_1, bottom_1))

height,width = img.size
lum_img = Image.new('L', [height,width] , 0)
  
draw = ImageDraw.Draw(lum_img)
draw.pieslice([(50,70), (height,width)], 0, 360, 
              fill = 255, outline = "white")
img_arr =np.array(img)
lum_img_arr =np.array(lum_img)
#display(Image.fromarray(lum_img_arr))
final_img_arr = np.dstack((img_arr,lum_img_arr))
finalPhoto = Image.fromarray(final_img_arr)
finalPhoto.save("output.png")
