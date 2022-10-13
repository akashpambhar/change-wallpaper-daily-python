import ctypes
from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday

photos_count = 18
path_to_photos = "C:/Users/hp/Pictures/New Folder/wallpaper" + str(day_of_year % 18) + ".jpg"

ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_photos , 0);