import numpy as np
from PIL import Image

# Function to create and save gradient images
def create_gradient_image(equation, size, save_path, color_map):
    width, height = size
    image = Image.new("RGB", size)
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            # Normalize x and y to be in the range [0, 1]
            nx = x / width
            ny = y / height
            # Compute the equation value
            value = equation(nx, ny)
            # Apply the color map to the value
            r = int(color_map(value)[0] * 255)
            g = int(color_map(value)[1] * 255)
            b = int(color_map(value)[2] * 255)
            pixels[x, y] = (r, g, b)

    image.save(save_path)

# Define mathematical equations
equations = [
    (lambda x, y: (x + y) / 2, 'Linear Gradient'),
    (lambda x, y: np.sin(10 * (x**2 + y**2)), 'Sinusoidal Gradient'),
    (lambda x, y: np.cos(10 * (x * y)), 'Cosine Gradient'),
    (lambda x, y: np.sin(10 * np.sqrt(x**2 + y**2)), 'Radial Sinusoidal Gradient'),
    (lambda x, y: np.cos(10 * np.sqrt(x**2 + y**2)), 'Radial Cosine Gradient'),
]

# Define color maps
color_maps = [
    lambda v: (v, 0, 1 - v),  # Blue to red
    lambda v: (v**2, v, 1 - v),  # Custom gradient
    lambda v: (np.sin(v * np.pi), np.cos(v * np.pi), 0.5),  # Sinusoidal gradient
]

# Create and save images
size = (800, 800)
for i, (equation, title) in enumerate(equations):
    for j, color_map in enumerate(color_maps):
        create_gradient_image(equation, size, f"{title.replace(' ', '_')}_{j}.png", color_map)

print("Gradient images have been generated.")