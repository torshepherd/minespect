# INFO: This function should only ever be called by inspect:right/try_reset_animation
item entity @s weapon.mainhand modify inspect:reset_inspecting_tag
item entity @s weapon.mainhand modify inspect:normal_attack_speed
item entity @s weapon.mainhand modify inspect:reset_model_data

say Resetting animation (right)...
