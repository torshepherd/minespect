from animation import *
import numpy as np, matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

animation_name = 'sword_animation_1'
create_animation_from_timeline('sword_animation_1', model_parent='handheld')
create_animation_from_timeline('sword_animation_2', model_parent='handheld')

for item in ['wooden_sword', 'stone_sword', 'iron_sword', 'golden_sword', 'diamond_sword', 'netherite_sword']:
    write_model(item, animation_name='sword_animation_2')

# seed = 1
# noise = PerlinNoise(3, seed)

# frames = 30

# output = np.array([noise(i/25) for i in range(frames)])

# plt.plot(np.arange(frames), output)
# plt.show()
