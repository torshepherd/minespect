execute if entity @s[tag=idle_right, tag=!idle_left] run function inspect:right/inspect
# execute if entity @s[tag=!idle_right, tag=idle_left] run function inspect:left/inspect
# execute if entity @s[tag=idle_right, tag=idle_left] run function inspect:both/inspect
execute if entity @s[tag=!idle_right, tag=!idle_left] run say Nothing to inspect.
