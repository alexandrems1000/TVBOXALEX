# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Cooking on YouTube by coldkeys
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.yt-cook'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "americastestkitchen"
YOUTUBE_CHANNEL_ID_2 = "JamieOliver"
YOUTUBE_CHANNEL_ID_3 = "bettyskitchen"
YOUTUBE_CHANNEL_ID_4 = "LauraVitalesKitchen"
YOUTUBE_CHANNEL_ID_5 = "OnePotChefShow"
YOUTUBE_CHANNEL_ID_6 = "sortedfood"
YOUTUBE_CHANNEL_ID_7 = "EverydayFoodVideos"
YOUTUBE_CHANNEL_ID_8 = "foodwishes"
YOUTUBE_CHANNEL_ID_9 = "easyturkishrecipes"
YOUTUBE_CHANNEL_ID_10 = "TitliNihaan"
YOUTUBE_CHANNEL_ID_11 = "allrecipes"
YOUTUBE_CHANNEL_ID_12 = "AllrecipesUK"
YOUTUBE_CHANNEL_ID_13 = "homecookingvideos"
YOUTUBE_CHANNEL_ID_14 = "TheCooknShare"
YOUTUBE_CHANNEL_ID_15 = "TheArtOfCooking"
YOUTUBE_CHANNEL_ID_16 = "Siuscooking"
YOUTUBE_CHANNEL_ID_17 = "HelenRecipes"
YOUTUBE_CHANNEL_ID_18 = "PailinsKitchen"
YOUTUBE_CHANNEL_ID_19 = "Maangchi"
YOUTUBE_CHANNEL_ID_20 = "JapaneseCooking101"
YOUTUBE_CHANNEL_ID_21 = "joecookingitalian"
YOUTUBE_CHANNEL_ID_22 = "gordoneriksen"
YOUTUBE_CHANNEL_ID_23 = "hilahcooking"
YOUTUBE_CHANNEL_ID_24 = "BrothersGreenEats"
YOUTUBE_CHANNEL_ID_25 = "Indiafoodnetwork"
YOUTUBE_CHANNEL_ID_26 = "sanjeevkapoorkhazana"
YOUTUBE_CHANNEL_ID_27 = "ShowMeTheCurry"
YOUTUBE_CHANNEL_ID_28 = "FrenchGuyCooking"
YOUTUBE_CHANNEL_ID_29 = "RebeccaBrandRecipes"
YOUTUBE_CHANNEL_ID_30 = "cookingwithplants"
YOUTUBE_CHANNEL_ID_31 = "CookingShooking"
YOUTUBE_CHANNEL_ID_32 = "ladyrosie1983"
YOUTUBE_CHANNEL_ID_33 = "HellthyJunkFood"
YOUTUBE_CHANNEL_ID_34 = "divascancook"
YOUTUBE_CHANNEL_ID_35 = "thedomesticgeek1"
YOUTUBE_CHANNEL_ID_36 = "howtocookthat"
YOUTUBE_CHANNEL_ID_37 = "MyCupcakeaddiction"
YOUTUBE_CHANNEL_ID_38 = "cheekyricho"
YOUTUBE_CHANNEL_ID_39 = "robjnixon"
YOUTUBE_CHANNEL_ID_40 = "gordonramsay"
YOUTUBE_CHANNEL_ID_41 = "epicuriousdotcom"
YOUTUBE_CHANNEL_ID_42 = "popsugartvyum"
YOUTUBE_CHANNEL_ID_43 = "dietplan101"
YOUTUBE_CHANNEL_ID_44 = "danispies"
YOUTUBE_CHANNEL_ID_45 = "MindOverMunch"
YOUTUBE_CHANNEL_ID_46 = "dhftns"
YOUTUBE_CHANNEL_ID_47 = "TheSweetestVegan"
YOUTUBE_CHANNEL_ID_48 = "stillcurrentstudios"
YOUTUBE_CHANNEL_ID_49 = "readysteadyeat"
YOUTUBE_CHANNEL_ID_50 = "BarbecueWeb"


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="America's Test Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-xD86CT1wq-c/AAAAAAAAAAI/AAAAAAAAAAA/2ZahY6VfMt0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jamie Oliver",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-z-x-8qjnmVU/AAAAAAAAAAI/AAAAAAAAAAA/W78fUrsBhCw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Betty's Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-XE7K9JuKMUI/AAAAAAAAAAI/AAAAAAAAAAA/6Ba3h5JBpUQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Laura Vitale's Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-kTsKONJu72w/AAAAAAAAAAI/AAAAAAAAAAA/U2wrC4qn3Kw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="One Pot Chef Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-MiUEGcrYzCo/AAAAAAAAAAI/AAAAAAAAAAA/MlzK3lGqXg8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SORTED Food",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-_PpucBgidwc/AAAAAAAAAAI/AAAAAAAAAAA/N2BC-vxthTg/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Everyday Food",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/--LNjtIfd_Q4/AAAAAAAAAAI/AAAAAAAAAAA/Ab-m2XbhGgI/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Food Wishes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-5ykHXf0Zeos/AAAAAAAAAAI/AAAAAAAAAAA/3si8boxZuJU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Easy Turkish Recipes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-HTOIQ5mQBzw/AAAAAAAAAAI/AAAAAAAAAAA/Zi5SpmCVVbQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Titlis Busy Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-kBJpggP9aDQ/AAAAAAAAAAI/AAAAAAAAAAA/LNjuJpcAWpY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Allrecipes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-nVEDlVwhNrs/AAAAAAAAAAI/AAAAAAAAAAA/RGAs3-lUDS4/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Allrecipes UK & Ireland",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-nVEDlVwhNrs/AAAAAAAAAAI/AAAAAAAAAAA/RGAs3-lUDS4/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Home Cooking Adventure",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-jac9k97j704/AAAAAAAAAAI/AAAAAAAAAAA/Djre7UW8vio/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="TheCooknShare",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-AfeT6HOklew/AAAAAAAAAAI/AAAAAAAAAAA/koigLLmjn2Y/s100-c-k-no/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="The Art Of Cooking (Chinese)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-igTkS4n_Pgk/AAAAAAAAAAI/AAAAAAAAAAA/YfgL1KUFwXg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Siu's Cooking (Chinese)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-1m4yOL6qyhM/AAAAAAAAAAI/AAAAAAAAAAA/1mXoLpaQx4c/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Helen's Recipes (Vietnamese Food)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-lXWCk1JjtDQ/AAAAAAAAAAI/AAAAAAAAAAA/WimPbqGFPHw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hot Thai Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-xijgR9EMgkY/AAAAAAAAAAI/AAAAAAAAAAA/YvmUK7dIZYU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Maangchi (Korean Cuisine)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-d0KStw-ZOOM/AAAAAAAAAAI/AAAAAAAAAAA/0Im0I-Sr9cg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JapaneseCooking101",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-gQ4UdaZ1fNo/AAAAAAAAAAI/AAAAAAAAAAA/ixkQFf02zdY/s100-c-k-no/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Joe Cooking Italian",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-2hI56a3l-1g/AAAAAAAAAAI/AAAAAAAAAAA/t2G0RPZf94Q/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SoGood.TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://i.ytimg.com/i/u5MCVa62UrHyVTECGjA2Wg/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hilah Cooking",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://i.ytimg.com/i/sWI5ZtPt7xykS9C24lfSzA/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Brothers Green Eats",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/-Pcx3L1v-Du8/AAAAAAAAAAI/AAAAAAAAAAA/pAL6nLMRZDQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="India Food Network",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/-loutHGQgpts/AAAAAAAAAAI/AAAAAAAAAAA/GMuoes2sxuo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sanjeev Kapoor Khazana",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/-SLq5rBwrfLg/AAAAAAAAAAI/AAAAAAAAAAA/eOADBA11SoE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ShowMeTheCurry.com",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-kPT8Va9eWDI/AAAAAAAAAAI/AAAAAAAAAAA/j2tm-a2onKI/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Alex French Guy Cooking",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/-IqvaTmOcYjI/AAAAAAAAAAI/AAAAAAAAAAA/vUtcpnqYv08/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rebecca Brand Recipes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/-Es3Y70b51ec/AAAAAAAAAAI/AAAAAAAAAAA/ME4TnzCVabo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CookingWithPlants",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://yt3.ggpht.com/-ocWwtGLmLnk/AAAAAAAAAAI/AAAAAAAAAAA/PobuFg0P7Qo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CookingShooking",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-CkCDx2Hxfmk/AAAAAAAAAAI/AAAAAAAAAAA/x7mHoTvVkfI/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="I Heart Recipes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/-1gTOVl9lNHE/AAAAAAAAAAI/AAAAAAAAAAA/kdeGqXmb85g/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="HellthyJunkFood",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-Qem4v4UWM9Q/AAAAAAAAAAI/AAAAAAAAAAA/WGx4D54SG_0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Divas Can Cook",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-SgnJwkGPXxM/AAAAAAAAAAI/AAAAAAAAAAA/sYHNul8yLgU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Domestic Geek",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-iRk89ilP7cY/AAAAAAAAAAI/AAAAAAAAAAA/WKCKACnjP6g/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="How To Cook That (Cakes & Desserts)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-BVr3FGmxht8/AAAAAAAAAAI/AAAAAAAAAAA/Xvh_CKEbu4Y/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="MyCupcakeAddiction",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-Bd5CaBQNrDE/AAAAAAAAAAI/AAAAAAAAAAA/1aJkHROOS1U/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="cheekyricho",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-xsCnhDAR-os/AAAAAAAAAAI/AAAAAAAAAAA/osH89C3V16M/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Nicko's Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-R-PA4kxVgkE/AAAAAAAAAAI/AAAAAAAAAAA/JOEZ7x59uWE/s100-c-k-no/photo.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Gordon Ramsay",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-MHLcgh1gv0o/AAAAAAAAAAI/AAAAAAAAAAA/7Gg7Zf7Zw4A/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Epicurious",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/-2rdh0ZW7Sr4/AAAAAAAAAAI/AAAAAAAAAAA/E2VP5W4xbcE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="POPSUGAR Food",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-v3jpBf46isE/AAAAAAAAAAI/AAAAAAAAAAA/i_IxYn7oSis/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dietplan-101.com",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/-EYRvC5oh0So/AAAAAAAAAAI/AAAAAAAAAAA/736gbNSRD1o/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Clean & Delicious",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/-xW77slWb5ac/AAAAAAAAAAI/AAAAAAAAAAA/6Xcf9ZZYf-o/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mind Over Munch",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://yt3.ggpht.com/-Gxsg_j8OqBI/AAAAAAAAAAI/AAAAAAAAAAA/fJFVR5UbCJI/s100-c-k-no/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="The Protein Chef",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://yt3.ggpht.com/-riwhmCauy38/AAAAAAAAAAI/AAAAAAAAAAA/uDmh4Trdqdg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tasha Edwards - The Sweetest Vegan",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/-iHmHrbEezEY/AAAAAAAAAAI/AAAAAAAAAAA/u_reqkFdKwo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Edgy Veg",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://yt3.ggpht.com/-BUxo6M-pteg/AAAAAAAAAAI/AAAAAAAAAAA/uPicPfu31aM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ReadySteadyEat",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://yt3.ggpht.com/-EJ_ueYZikHg/AAAAAAAAAAI/AAAAAAAAAAA/stQTsAKAhW8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="BBQ Pit Boys",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://yt3.ggpht.com/-w5MgnW1qxCw/AAAAAAAAAAI/AAAAAAAAAAA/ywS4ukZBIaM/s100-c-k-no/photo.jpg",
        folder=True )
run()
