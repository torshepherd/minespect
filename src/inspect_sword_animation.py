from animation import *
import numpy as np, matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

animation_name = 'sword_1'
# create_animation_from_timeline('sword_1', model_parent='handheld')
# create_animation_from_timeline('sword_2', model_parent='handheld')
# create_animation_from_timeline('item_1', model_parent='generated')

get_overview_of_models(os.path.join(PATH_TO_MODELS, 'item/unused/items_1_16_3'))

for item in ['wooden_sword',
             'stone_sword',
             'iron_sword',
             'golden_sword',
             'diamond_sword',
             'netherite_sword',
             'wooden_pickaxe',
             'stone_pickaxe',
             'iron_pickaxe',
             'golden_pickaxe',
             'diamond_pickaxe',
             'netherite_pickaxe',
             'wooden_axe',
             'stone_axe',
             'iron_axe',
             'golden_axe',
             'diamond_axe',
             'netherite_axe',
             'wooden_shovel',
             'stone_shovel',
             'iron_shovel',
             'golden_shovel',
             'diamond_shovel',
             'netherite_shovel',
             'wooden_hoe',
             'stone_hoe',
             'iron_hoe',
             'golden_hoe',
             'diamond_hoe',
             'netherite_hoe']:
    write_model(item, animation_name='sword_2')

for item in ['acacia_boat',
             'stone_hoe',
             'iron_hoe',
             'golden_hoe',
             'diamond_hoe',
             'netherite_hoe']:
    write_model(item, animation_name='item_1')
