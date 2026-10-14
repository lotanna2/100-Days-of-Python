import cologram

colors = cologram.extract("image.jpg", 30) # Extracts 30 dominant colors from the image "image.jpg"

rgb_colors = [] # List to store the RGB values of the extracted colors

for color in colors: 

    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    color_tuple = (r, g, b) # Create a tuple of RGB values
    rgb_colors.append(color_tuple) # Append the tuple to the list of RGB colors

print(rgb_colors) # Print the list of RGB colors