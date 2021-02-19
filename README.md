# minespect
![](https://img.shields.io/badge/animated%20models-48%25-yellow)

minespect adds the inspect weapon functionality from CoD, CS, and TF2 into vanilla Minecraft (no mods required).

Currently, only Java edition 1.17 (snapshot 21w07a) is supported.

## Installing
[![homepage][1]][2] [![homepage][3]][4]

[1]:  https://img.shields.io/badge/-datapack-854f2b?style=for-the-badge
[2]:  https://github.com/torshepherd/minespect/releases/latest/download/datapack.zip
[3]:  https://img.shields.io/badge/-resourcepack-70b237?style=for-the-badge
[4]:  https://github.com/torshepherd/minespect/releases/latest/download/resourcepack.zip
1. Download the resourcepack to .minecraft/resourcepacks
1. Download the datapack to .minecraft/saves/YOURWORLD/datapacks

If you're not sure where to find .minecraft/, pause the game and select 'Resource Packs'. From there, select 'Open Resource Pack Folder' and navigate up one level.

## Usage
For now, the only functionality is to type ```/function inspect:inspect``` into the chat. If you forget the command, type ```/reload``` and click the prompt.

## Todo
1. Fix attackSpeed modifier system, conditions
2. Get length of animation somehow to know when to end, or just make all have same length
3. Add inspecting left hand animation too
   1. If tool in both hands, use second delayed scoreboard value for left hand animation
   2. Else, just use regular scoreboard for left hand
4. Add in keybind or other trigger for inspecting
   1. Standing still for a while, bring up prompt in chat?
5. Custom animations for enchanted items?
   1. Add smoke particles to inspect fire aspect sword
   2. Fancy twirl for sharpness or efficiency tools
   3. Swirling XP orbs for mending tools?
6. Multiple animations per item? Maybe select from menu?
7. Ping system datapack...
8. 
