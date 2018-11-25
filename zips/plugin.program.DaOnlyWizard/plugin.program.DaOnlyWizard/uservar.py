import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR blue][B]DaOnlyWizard[/B][/COLOR]'
BUILDERNAME    = 'daonlywizard'
#########################Make sure to change the repo to yours!!!!
EXCLUDES       = [ADDON_ID, 'repository.dab', 'roms', 'My_Builds', 'backupdir']
BUILDFILE      = 'http://www.dabutcher.org/tools/builds1.txt'
UPDATECHECK    = 0
APKFILE        = 'http://ftg.000webhostapp.com/newwiz/ftgapk.xml'
YOUTUBETITLE   = 'DaBs Help Videos ' 
YOUTUBEFILE    = 'http://dabutcher.org/tools/youtube.txt'
ADDONFILE      = 'https://pastebin.com/raw/7srQRedq'
ADVANCEDFILE   = 'http://'
ROMPACK        = 'http://ftg.000webhostapp.com/newwiz/rom-packs.txt'
EMUAPKS        = 'http://ftg.000webhostapp.com/newwiz/emuapks.txt'
ADDONPACK      = 'http://'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################

##Alway test to see the color combo!!

#### NEW GUI THEME ###################################
# Choose from the following 
# Only these colors avalable
# white , blue , orange , yellow , red , purple , pink , lime , cyan, green
#Button focus color
FOCUS_BUTTON_COLOR = 'red'
EXIT_BUTTON_COLOR = 'lime'
#Highlight outline for lists
HIGHLIGHT_LIST = 'red'
##No TXT file Banner
NO_TXT_FILE = 'pink'

############################################
############################################
### The full list of colors for below can found @ https://forum.kodi.tv/showthread.php?tid=210837

#Top Main buttons
MAIN_BUTTONS_TEXT = 'dodgerblue'
#All other buttons
OTHER_BUTTONS_TEXT = 'gold'
#all list text color
##FYI any color placed in the txt file will overide this
LIST_TEXT = 'gold'


#Description text title color
DES_T_COLOR = 'dodgerblue'
#Description color
DESCOLOR = 'white'

#Wizard title name and verion color
WIZTITLE = 'DaOnlyWizard  by   DaButcher'
WIZTITLE_COLOR = 'red'
VERTITLE_COLOR = 'dodgerblue'
VER_NUMBER_COLOR = 'red'
############################################################

## The colors and theme below is still used for the pop up dialogs
##Alway test to see the color combo
# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'white'
COLOR2         = 'yellow'
COLOR3         = 'red'
COLOR4         = 'snow'
COLOR5         = 'lime'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'



#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://dabutcher.org/img/wizard/dab2.jpg'
ICONMAINT      = 'http://dabutcher.org/img/wizard/maint.png'
ICONAPK        = 'http://dabutcher.org/img/wizard/apk.png'
ICONADDONS     = 'http://i.imgur.com/E7oBc7x.png'
ICONYOUTUBE    = 'http://dabutcher.org/img/wizard/dab1.jpg'
ICONSAVE       = 'http://dabutcher.org/img/wizard/save.png'
ICONTRAKT      = 'http://dabutcher.org/img/wizard/trakt.png'
ICONREAL       = 'http://dabutcher.org/img/wizard/real.png'
ICONLOGIN      = 'http://dabutcher.org/img/wizard/login.png'
ICONCONTACT    = 'http://dabutcher.org/img/wizard/contact.png'
ICONSETTINGS   = 'http://dabutcher.org/img/wizard/settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '~'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'ThX for using my DaOnlyWizard.\r\nWebsite: http://dabutcher.org/repo\r\nContact us on facebook at http://www.youtube.com/c/ToddBDaButcher'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'icon.png')
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'http://'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://'
# Url to folder zip is located in
REPOZIPURL     =  'http://'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://dabutcher.org/tools/message.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font20'
HEADERMESSAGE  = 'DaOnlyWizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font20'
# Background for Notification Window
BACKGROUND     = 'http://i.imgur.com/DZGGDJl.jpg'
############################    #############################