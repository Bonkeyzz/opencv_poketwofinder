import cv2
from os import walk, remove
import json
from PIL import Image

def match_with_features(img1, img2):
	orb = cv2.ORB_create(nfeatures=500)
	kp1, des1 = orb.detectAndCompute(img1, None)
	kp2, des2 = orb.detectAndCompute(img2, None)

	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	matches = bf.match(des1, des2)

	return len(matches)

def match_features_and_draw(img1, img2, name, result, sort=True):
	orb = cv2.ORB_create(nfeatures=500)
	kp1, des1 = orb.detectAndCompute(img1, None)
	kp2, des2 = orb.detectAndCompute(img2, None)
	# The font to display this in (hate it)
	font = cv2.FONT_HERSHEY_DUPLEX
	# Org - Position of text
	org = (0, 25)
	# Scale of the font
	fontScale = 1
	# Cyan color
	color = (255, 255, 5)
	thickness = 2

	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	matches = bf.match(des1, des2)
	if sort: matches = sorted(matches, key=lambda x: x.distance)
	img2 = cv2.putText(img2, 'Source', org, font, fontScale, color, thickness, cv2.LINE_AA)
	img1 = cv2.putText(img1, 'Template', org, font, fontScale, color, thickness, cv2.LINE_AA)
	match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None)

	cv2.imshow(f"Source matches with: '{name}' Score: {result}", match_img)
	cv2.waitKey()

class Cv2Image():
	def __init__(self, img_name):
		self.template = cv2.imread(f'{img_name}')
		self.__name = img_name
	def __str__(self):
		return self.__name

filenames = next(walk('./templates'), (None, None, []))[2]
test_poketwo_spawns = next(walk('./test_poketwo_spawns'), (None, None, []))[2]
template_list = []

#NOTE - You can change this to any test spawns you want.
#TODO - Integrate into discord as a self-bot application.
poketwo_spawn = Cv2Image('./test_poketwo_spawns/poketwo_deino.png')

def check_matching(src, templ): 
	#FIXME - Matching may fail if picture is flipped
	#FIXME - Completely different pokemon may still be matched as there's no way (at the moment) to determine if we have template image of a pokemon for the source image (poketwo)
	#match_len = match_with_features(src, templ)
	templ_flipped = cv2.flip(templ, 1)
	match_len_flipped = match_with_features(src, templ_flipped)

	#if match_len_flipped >= match_len: return match_len_flipped
	#else: 
	return match_len_flipped

def jpg2png(input: str):
	im1 = Image.open(input, 'r')
	im1.save(input.replace(".jpg", ".png"))
	im1.close()
	remove(input)

# NOTE - This will be removed probably. Its just for debug.
def check_and_convert_jpgs():
	for spawn in test_poketwo_spawns:
		if('.jpg' in spawn):
			jpg2png(f'./test_poketwo_spawns/{spawn}')

match_canditates = []
def main():
	check_and_convert_jpgs()
	with open('config.json') as f:
		config = json.load(f)
	print('[*] Initializing template pictures...')

	for filename in filenames:
		if('.jpg' in filename):
			jpg2png(filename)
		print(f'[*] Loaded "./templates/{filename}"!')
		template_list.append(Cv2Image(f"./templates/{filename}"))
	print(f"[*] Testing source: {str(poketwo_spawn)}")
	for template in template_list:
		match_canditates.append({"name": str(template), "template": template.template, "result": check_matching(poketwo_spawn.template, template.template)})
	match_canditates.sort(key=lambda x: x['result'])
	best_match = match_canditates.pop()
	print(f"[*] Potential Match: '{best_match['name']}' with score: {best_match['result']}")
	match_features_and_draw(best_match['template'], poketwo_spawn.template, best_match['name'], best_match['result'])

if __name__ == "__main__":
	main()