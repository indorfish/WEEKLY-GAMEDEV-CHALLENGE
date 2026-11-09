# WEEKLY-GAMEDEV-CHALLENGE
Folder for the code for the Weekly Game Dev challenge.
Each week we work on a different game.
Each game gets its own folder and inside each folder expect an engine-agnostic game specification, then different subfolders that realize the game in different engines.
There may also be assets inside the game-of-the-week's folder, but this is not advised unless the assets are small in size.
To include larger assets, use git lfs.
Example structure:

- wk01_tictactoe
  - tictactoe.md/txt // specification, description
  - tictactoe_js // directory for web version
  - tictactoe_gd // directory for GodotEngine
  - tictactoe_un // directory for unity engine
  - assets_tictactoe // directory for assets if any.
    - sprites
    - audio
- wk02_whackamole
// etc.

The reason for the "wk%d" prefix is so that the directories appear in logical order when sorted alphabetically in your filesystem. Make sure to use the two-digit numbering format e.g. '00' instead of '0'.
This  challenge is intended to be a learning experience and we hope anyone who goes through this repo learns something about game development and software development in general.
The engine-agnostic specification is quite important so try reading it first before building your game.


USE OF AI:
Different people have different feelings about AI, but the point of this challenge is to learn how to build games. Using AI would be doing yourself a disservice. Using AI is not strictly forbidden, but it's not encouraged. If you do use AI, make sure to be honest about it and try to replace it with your own thoughts and ideas later.



Thanks!
