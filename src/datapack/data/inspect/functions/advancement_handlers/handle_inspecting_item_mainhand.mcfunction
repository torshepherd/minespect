#say Trying to reset item in hand...
# TODO: Item loses tag when dropped and picked up. need better way of storing
function inspect:right/try_reset_animation

advancement revoke @s only inspect:stop_inspecting_item_mainhand
