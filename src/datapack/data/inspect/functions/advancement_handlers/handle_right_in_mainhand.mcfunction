# INFO: this callback happens when a player's inventory changes and the item they are holding has an inspecting:1b tag and the player has a not_inspecting_right tag

say Callback: detect_right_in_mainhand: Trying to reset item in hand (right)...

tag @s add reset_right
advancement revoke @s only inspect:detect_right_in_mainhand
