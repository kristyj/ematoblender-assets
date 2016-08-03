""" These properties describe features of the ematoblender assets.
    They are referenced in the construction scripts as necessary."""
__author__ = "Kristy"

# TODO: Upon integration with ematoblender these should also be accessible from within ematoblender/from the blend file

# game logic default options
hifreq_sensor_skips = 5
bge_script_path = 'ematoblender.scripts.ema_blender.ema_bge.bge_emareadin.main'


## location of menu scenes (relative to current .blend) ##
# TODO: Move to set location within the repo for storing these things
# location of status/webcam scene for overlay
rel_loc_of_statusbar_dot_blend = '../resources'
statusbar_dot_blend = 'text_video_scene_latest.blend'
path_to_statusbar_in_dot_blend = "Scene"
name_of_statusbar_object = "TextScene"

# name of an avatar to demonstrate rotation if available
rotation_avatar = 'Avatar'

# location of popup menu scene for occasional overlay
rel_loc_of_popup_dot_blend = "../resources"
popup_dot_blend = "popup_menu_latest.blend"
path_to_popup_in_dot_blend = "Scene"
name_of_popup_object = "PopupMenu"

# aesthetic settings
game_background_color = (0.07, 0.07, 0.07) # light grey, best visibility
game_contrast_color = (0.5, 0.5, 0.5) # medium grey, pleasant contrast

