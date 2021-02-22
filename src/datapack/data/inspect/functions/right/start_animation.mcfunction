# INFO: This function should only ever be called by inspect:right/try_start_animation
item entity @s weapon.mainhand modify inspect:hide_modifiers
item entity @s weapon.mainhand modify inspect:negative_attack_speed
item entity @s weapon.mainhand modify inspect:add_inspecting_tag_right

say Starting animation (right)...
