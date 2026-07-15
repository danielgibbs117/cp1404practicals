NAME_TO_CODE = {"aliceblue": "#f0f8ff", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                "antiquewhite": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff", "asparagus": "#87a96b",
                "aureolin": "#fdee00", "beaver": "#9f8170"}
print(NAME_TO_CODE)

color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        print(color_name, "is", NAME_TO_CODE[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()

