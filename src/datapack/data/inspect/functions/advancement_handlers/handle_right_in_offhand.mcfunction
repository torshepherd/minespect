# INFO: this callback happens when a player's inventory changes and the item they are holding has an inspecting:1b tag and the player has a not_inspecting_left tag

say Callback: detect_right_in_offhand: Trying to reset item in hand (left)...

tag @s add swapped_hands
advancement revoke @s only inspect:detect_right_in_offhand
