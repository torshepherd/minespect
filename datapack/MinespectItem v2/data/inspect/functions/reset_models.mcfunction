# Reset attack speed of previously inspecting item
execute if score @s prev_slot matches 0 run item entity @s hotbar.0 modify inspect:normal_attack_speed
execute if score @s prev_slot matches 1 run item entity @s hotbar.1 modify inspect:normal_attack_speed
execute if score @s prev_slot matches 2 run item entity @s hotbar.2 modify inspect:normal_attack_speed
execute if score @s prev_slot matches 3 run item entity @s hotbar.3 modify inspect:normal_attack_speed
execute if score @s prev_slot matches 4 run item entity @s hotbar.4 modify inspect:normal_attack_speed
execute if score @s prev_slot matches 5 run item entity @s hotbar.5 modify inspect:normal_attack_speed
execute if score @s prev_slot matches 6 run item entity @s hotbar.6 modify inspect:normal_attack_speed
execute if score @s prev_slot matches 7 run item entity @s hotbar.7 modify inspect:normal_attack_speed
execute if score @s prev_slot matches 8 run item entity @s hotbar.8 modify inspect:normal_attack_speed

# Reset model data of previously inspecting item
execute if score @s prev_slot matches 0 run item entity @s hotbar.0 modify inspect:reset_model_data
execute if score @s prev_slot matches 1 run item entity @s hotbar.1 modify inspect:reset_model_data
execute if score @s prev_slot matches 2 run item entity @s hotbar.2 modify inspect:reset_model_data
execute if score @s prev_slot matches 3 run item entity @s hotbar.3 modify inspect:reset_model_data
execute if score @s prev_slot matches 4 run item entity @s hotbar.4 modify inspect:reset_model_data
execute if score @s prev_slot matches 5 run item entity @s hotbar.5 modify inspect:reset_model_data
execute if score @s prev_slot matches 6 run item entity @s hotbar.6 modify inspect:reset_model_data
execute if score @s prev_slot matches 7 run item entity @s hotbar.7 modify inspect:reset_model_data
execute if score @s prev_slot matches 8 run item entity @s hotbar.8 modify inspect:reset_model_data

# say Resetting stuff
tag @s remove inspecting
