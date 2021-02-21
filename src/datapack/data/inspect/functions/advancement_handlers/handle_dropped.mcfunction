execute as @s[tag=idle_right] run tag @s remove idle_right
execute as @s[tag=idle_left] run tag @s remove idle_left

advancement revoke @s only inspect:dropped_mainhand
say Dropped inspecting item
