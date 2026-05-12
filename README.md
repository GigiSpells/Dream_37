# Dream_37

## Demo
Demo Video: <>

## GitHub Repository
GitHub Repo: <https://github.com/GigiSpells/Dream_37>

## Description

### Concept
Dream 37 is a single level demo for a top down object finding mystery game inspired by a dream.
In this level the player spawns inside a house, and may move freely inside, interacting
with furniture and any objects they may find. There are items the player may collect,
some freely visible in the room, and others that they must find hidden in drawers or
cabinets. The level ends when a certain number of objects are found.

### Future Areas of Improvement
In the future I would like to complete the TODO list at the top of project.py.
I intend for there to be text associated with each object collected, that alludes
to a larger story/mystery. There is also a secondary state for each key furniture piece
(such as the fridge/cabinets being open, the fireplace/lamp being lit, etc.), and 
when the character interacts, the furniture should animate to match. I would also
like the character to animate as they walk, and face the direction they are walking.
The soundtrack should play when the player interacts with the record player, and
there should be a GUI to represent objects that have been found, rather than just
a number.

### Repository Files
src contains project.py and all other code files and assets project.py uses.

spritesheet.py contains the SpriteSheet() class, which has methods for extracting
individual images from spritesheets: one for my single row character sprite sheets
and one for my furniture and item sprite sheets.

assets contains the font for Dream 37, the spritesheets used for the map, furniture,
and items (Top-Down_Retro_Interior), and The full original CharacterSheets which
I chopped up to make sheets more suited to my needs.

graphics contains the tmx file for the map as well as map and character images 
used in the game, and a picture of an old painting of the dream that inspired the project,
currently used as a placeholder for the end screen.

