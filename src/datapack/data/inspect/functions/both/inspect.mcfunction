# INFO: this function should only be called by inspect:inspect

# say Inspecting (both)...
function inspect:left/tag_add_inspecting
function inspect:right/tag_add_inspecting
scoreboard players set @s anim_left -20
scoreboard players set @s anim_right 0
function inspect:left/try_start_animation
function inspect:right/try_start_animation

function inspect:left/update_animation
function inspect:right/update_animation
