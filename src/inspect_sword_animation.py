from animation import *
import numpy as np, matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

animation_name = 'sword_1'
create_animation_from_timeline('sword_1', model_parent='handheld')
create_animation_from_timeline('sword_2', model_parent='handheld')

for item in ['wooden_sword', 'stone_sword', 'iron_sword', 'golden_sword', 'diamond_sword', 'netherite_sword']:
    write_model(item, animation_name='sword_2')
