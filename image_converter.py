from PIL import Image, ImageFilter
import os
from pathlib import Path


question = input('Please input you image filepath: ').strip('"')
image_name = os.path.basename(question)
folder_path = "C:/Users/ddddd/Downloads"
output_folder = os.makedirs(folder_path, exist_ok=True)

img = Image.open(question)
print(os.path.basename(img.filename))



if '.png' in os.path.basename(img.filename):
    ask = input(f'''What will you like to do with this({image_name}) image?:
           a- PNG to JPG
           b- PNG to JPEG
''').lower()
    if ask == 'a':
       clean_name = os.path.splitext(image_name)[0]
       file_name = f'{clean_name}.jpg'
       save_image = os.path.join(folder_path, file_name)
       img.save(save_image)
       print('Successful')
    elif ask == 'b':
        clean_name = os.path.splitext(image_name)[0]
        file_name = f'{clean_name}.jpeg'
        save_image = os.path.join(folder_path, file_name)
        img.save(save_image)
        print('Successful')
    else:
       print('Incorrect prompt')
elif '.jpg' in os.path.basename(img.filename):
   ask = input(f'''What will you like to do with this({image_name}) image?:
               a- JPG to JPEG
               b- JPG to PNG
    ''').lower()
   if ask == 'a':
       clean_name = os.path.splitext(image_name)[0]
       file_name = f'{clean_name}.jpeg'
       save_image = os.path.join(folder_path, file_name)
       img.save(save_image)
       print('Successful')
   elif ask == 'b':
       clean_name = os.path.splitext(image_name)[0]
       file_name = f'{clean_name}.png'
       save_image = os.path.join(folder_path, file_name)
       img.save(save_image)
       print('Successful')
   else:
      print('Incorrect prompt')
elif '.jpeg' in os.path.basename(img.filename):
   ask = input(f'''What will you like to do with this({image_name}) image?:
                  a- JPEG to PNG
                  b- JPEG to JPG
       ''').lower()
   if ask == 'a':
       clean_name = os.path.splitext(image_name)[0]
       file_name = f'{clean_name}.png'
       save_image = os.path.join(folder_path, file_name)
       img.save(save_image)
       print('Successful')
   elif ask == 'b':
       clean_name = os.path.splitext(image_name)[0]
       file_name = f'{clean_name}.jpg'
       save_image = os.path.join(folder_path, file_name)
       img.save(save_image)
       print('Successful')
   else:
       print('Incorrect prompt')
else:
   print('Only PNG, JPG, JPEG')



# input_image = Image.open(question)
