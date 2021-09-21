color = {
    "basic" : (0,1,1),
    "function" : (0,1,0),
    "visual" : (1,1,0),
    "input" : (1,0,1),
    "default" : (.8,.8,.8),
}
def get_color(category):
    category = category.split(".")[0]
    if category in color.keys():
        return color[category]
    else:
        return color["default"]