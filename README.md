# OpenCV Poketwo Finder

Helper to identify poketwo spawns with OpenCV.

This program is currently just a PoC, i'm just trying to learn OpenCV. I originally planned on making this into an automatic catcher but this was a long ago. As of now i'm not planning on implementing integrations with discord myself as i'm not interested in catching pokemon using this method. 
If discord integration (self-bot probably) is properly implemented you are at risk of getting banned from using Poketwo (and maybe discord as well cause self-bots) by using this script.

***THIS WILL NOT CATCH POKEMON AUTOMATICALLY IN DISCORD***

## Screenshot:

![image](https://github.com/Bonkeyzz/opencv_poketwofinder/assets/23555978/c53d2e85-fd3e-4d0a-bdf7-9aeb59483a1a)

## How to use

1. Download the script.
2. Install the requirements. `pip install -r requirements.txt`
3. In the script you can edit the `poketwo_spawn` variable to point into any file from the folder `test_poketwo_spawns`
4. You can run it with the command: `python matcher.py`

If you want to add your own templates in the `templates` folder, use [Bulbapedia](https://bulbapedia.bulbagarden.net/). Use the first pokemon picture from the site.
**Make sure to include ONLY the name of the pokemon in the template picture e.g. `deino.png`.**


If you like my work, buy me a coffee :^) **[Donate](https://ko-fi.com/bonkeyzz)**