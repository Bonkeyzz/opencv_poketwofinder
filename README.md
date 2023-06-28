# OpenCV Pokétwo Finder

Helper to identify Pokétwo spawns with OpenCV.

This script uses OpenCV's feature matching algorithm to determine which pokemon is in the *Source* image. It was originally planned to be an automatic catcher for the [Pokétwo](https://poketwo.net/) discord bot a long time ago but i abandoned that idea as i don't find any need for such tool, not to add the risk of getting banned from using Pokétwo (and discord, if it was implemented into a self-bot).

***THIS WILL NOT CATCH POKEMON AUTOMATICALLY IN DISCORD AND SUCH FEATURE WILL NOT BE ADDED***

## Screenshot

![image](https://github.com/Bonkeyzz/opencv_poketwofinder/assets/23555978/c53d2e85-fd3e-4d0a-bdf7-9aeb59483a1a)

## How to use

1. Download the script.
2. Install the requirements. `pip install -r requirements.txt`
3. In the script you can edit the `poketwo_spawn` variable to point into any file from the folder `test_poketwo_spawns`
4. You can run it with the command: `python matcher.py`

If you want to add your own templates in the `templates` folder, use [Bulbapedia](https://bulbapedia.bulbagarden.net/). Use the first pokemon picture from the site.
**Make sure to include ONLY the name of the pokemon in the template picture e.g. `deino.png`.**


If you like my work, buy me a coffee :^) **[Donate](https://ko-fi.com/bonkeyzz)**
