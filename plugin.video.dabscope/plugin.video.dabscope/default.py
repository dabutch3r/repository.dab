# -*- coding: utf-8 -*-
import xbmcaddon,os,xbmc,xbmcgui,urllib,re,xbmcplugin,sys,logging
__USERAGENT__ = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
__addon__ = xbmcaddon.Addon()
__cwd__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
Addon = xbmcaddon.Addon()
user_dataDir = xbmc.translatePath(Addon.getAddonInfo("profile"))
if not os.path.exists(user_dataDir):
     os.makedirs(user_dataDir)
import requests
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
base_image='https://ws0.cocoscope.com/covers/63934.jpg'
base_icon='https://musically.com/wp-content/uploads/2019/09/Screen-Shot-2019-09-04-at-11.jpg'
if KODI_VERSION<=18:
    
    que=urllib.quote_plus
    que_n=urllib.quote
    url_encode=urllib.urlencode
    unque=urllib.unquote_plus
else:
    
    que_n=urllib.parse.quote
    que=urllib.parse.quote_plus
    url_encode=urllib.parse.urlencode
    unque=urllib.parse.unquote_plus
def get_params():
        param=[]
        if len(sys.argv)>=2:
          paramstring=sys.argv[2]
          if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param     
def utf8_urlencode(params):
    try:
        import urllib as u
        enc=u.urlencode
    except:
        from urllib.parse import urlencode
        enc=urlencode
    # problem: u.urlencode(params.items()) is not unicode-safe. Must encode all params strings as utf8 first.
    # UTF-8 encodes all the keys and values in params dictionary
    for k,v in list(params.items()):
        # TRY urllib.unquote_plus(artist.encode('utf-8')).decode('utf-8')
        if type(v) in (int, float):
            params[k] = v
        else:
            try:
                params[k.encode('utf-8')] = v.encode('utf-8')
            except Exception as e:
                pass
                #logging.warning( '**ERROR utf8_urlencode ERROR** %s' % e )
    
    return enc(params).encode().decode('utf-8')
def addNolink( name, url,mode,isFolder, iconimage="DefaultFolder.png"):
 

          
         
          u=sys.argv[0]+"?url="+que(url)+"&mode="+str(mode)+"&name="+que(name)
          if KODI_VERSION<=18:
            liz = xbmcgui.ListItem( name, iconImage=iconimage, thumbnailImage=iconimage)
          else:
            liz = xbmcgui.ListItem( name)
          liz.setInfo(type="Video", infoLabels={ "Title": unque( name)   })

          liz.setProperty("IsPlayable","false")
          liz.setProperty( "Fanart_Image", iconimage )
          xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description,page='0'):
        params={}
        params['url']=url
        params['mode']=mode
        params['name']=name
        params['data']=data
        params['iconimage']=iconimage
        params['fanart']=fanart
        params['description']=description
        params['page']=page
        all_ur=utf8_urlencode(params)
        u=sys.argv[0]+"?mode="+str(mode)+'&'+all_ur
          
        
        ok=True
        if KODI_VERSION<=18:
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        else:
            liz=xbmcgui.ListItem(name)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        
        return ok



def addLink( name, url,mode,isFolder, iconimage,fanart,description,data=''):
          params={}
          params['url']=url
          params['mode']=mode
          params['name']=name
          params['data']=data
          params['iconimage']=iconimage
          params['fanart']=fanart
          params['description']=description
          
          all_ur=utf8_urlencode(params)
          u=sys.argv[0]+"?mode="+str(mode)+'&'+all_ur
          
          menu_items=[]
          menu_items.append(('Video Info', 'RunPlugin(%s)' % ('%s?url=%s&mode=4')%(sys.argv[0],str(url))))
          menu_items.append(('Links from Video', 'RunPlugin(%s)' % ('%s?url=%s&mode=3')%(sys.argv[0],str(url))))
          video_info={}
         
          video_info['title']=name
          video_info['plot']=description
       
          
          #u=sys.argv[0]+"?url="+que(url)+"&mode="+str(mode)+"&name="+que(name)
          if KODI_VERSION<=18:
            liz = xbmcgui.ListItem( name, iconImage=iconimage, thumbnailImage=iconimage)
          else:
            liz = xbmcgui.ListItem( name)
          liz.addContextMenuItems(menu_items, replaceItems=False)
          liz.setInfo(type="Video", infoLabels=video_info)
          art = {}
          art.update({'poster': iconimage})
          liz.setArt(art)
          liz.setProperty("IsPlayable","true")
          liz.setProperty( "Fanart_Image", fanart )
          xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)


def read_site_html(url_link):
    '''
    req = urllib2.Request(url_link)
    req.add_header('User-agent',__USERAGENT__)# 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    html = urllib2.urlopen(req).read()
    '''
    import requests
    html=requests.get(url_link).content
    return html

def main_menu(page):
    
    if not page:
        page=0
    page=int(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    params = (
        ('layout', 'blank'),
        ('controller', 'ajax'),
        ('action', 'get_videos'),
        ('offset', str(page*24)),
        ('category_id', '0'),
        ('channel_id', '63934'),
        ('sort_id', 'date'),
        ('status', '0'),
        ('videos_per_load', '24'),
    )

    response = requests.get('https://www.cocoscope.com/', headers=headers, params=params,verify=False).json()
    for items in response:
        lk=items['id']
        nm=items['name']
        ic=items['thumbnail_url']
        plot=items['fancy_date_2']+'\n'+items['view_string']+'\n'+items['time_elapsed']
        addLink( nm, lk,2,False, ic,ic,plot)
    addDir3( '[COLOR lightblue]Next Page[/COLOR]', str(int(page+1)),'0', base_icon,base_image,'Next Page')
    

def files_from(name,url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    params = (
        ('v', url),
    )

    response = requests.get('https://www.cocoscope.com/watch', headers=headers, params=params,verify=False).content.decode('utf-8')
    regex='meta property="og:description" content="(.+?)"'
    m=re.compile(regex,re.DOTALL).findall(response)[0]
    
    m=m.split('\n')
    all_l=[]
    for itt in m:
        logging.warning(itt)
        regex='http(.+?)(?: |$)'
        all_links=re.compile(regex).findall(itt)
        if len(all_links)>0:
            if 't.me' in all_links[0] or 'twitter' in all_links[0]:
                continue
       
            all_l.append('http'+all_links[0])
    ret = xbmcgui.Dialog().select('Choose', all_l)
    if ret!=-1:
        ok=xbmcgui.Dialog().yesno("Add as kodi source?",all_l[ret])
        
        if ok:
            
                setting_path=xbmc.translatePath("special://userdata")
                s_file=os.path.join(setting_path,'sources.xml')
                
                
                
                search_entered='Repo'
                keyboard = xbmc.Keyboard(search_entered, 'Enter Source name')
                keyboard.doModal()
                if keyboard.isConfirmed():
                    if os.path.exists(s_file):
                        file = open(s_file, 'r') 
                        file_r= file.read()
                        file.close()
                        if all_l[ret] in file_r:
                            xbmcgui.Dialog().ok('Error ','Source already exists')
                            return 0
                        regex='<files>(.+?)</files>'
                        o_data=re.compile(regex,re.DOTALL).findall(file_r)[0]
                        
                        o_data_full='<files>%s</files>'
                        added_txt='''\
                        <source>
                            <name>%s</name>
                            <path pathversion="1">%s</path>
                            <allowsharing>true</allowsharing>
                        </source>
                        '''
                        f_lk=all_l[ret].replace('\n','').replace('\r','').replace('\t','').strip()
                        new_o_data=file_r.replace(o_data_full%o_data,o_data_full%(o_data+added_txt%(keyboard.getText(),f_lk)))
                    else:
                        new_o_data='''\
<sources>
    <programs>
        <default pathversion="1"></default>
    </programs>
    <video>
        <default pathversion="1"></default>
    </video>
    <music>
        <default pathversion="1"></default>
    </music>
    <pictures>
        <default pathversion="1"></default>
    </pictures>
    <files>
        <default pathversion="1"></default>
        <source>
            <name>%s</name>
            <path pathversion="1">%s</path>
            <allowsharing>true</allowsharing>
        </source>
    </files>
</sources>


                        '''
                        f_lk=all_l[ret].replace('\n','').replace('\r','').replace('\t','').strip()
                        new_o_data=new_o_data%(keyboard.getText(),f_lk)
                    file = open(s_file, 'w') 
                    file.write(new_o_data)
                    file.close()
                    xbmcgui.Dialog().ok('Done','Need to restart kodi for changes')
            
    else:
      sys.exit()
def play_link(name,url,plot):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    params = (
        ('v', url),
    )

    response = requests.get('https://www.cocoscope.com/watch', headers=headers, params=params,verify=False).content.decode('utf-8')
    regex='source src="(.+?)"'
    m=re.compile(regex).findall(response)
    
    regex='meta property="og:description" content="(.+?)"'
    p=re.compile(regex,re.DOTALL).findall(response)[0]
    listItem = xbmcgui.ListItem(name, path=m[0]) 
 
    listItem.setInfo(type='Video', infoLabels={'title':name,'plot':p})


    listItem.setProperty('IsPlayable', 'true')

    xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass
def video_data(name,url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    params = (
        ('v', url),
    )

    response = requests.get('https://www.cocoscope.com/watch', headers=headers, params=params,verify=False).content.decode('utf-8')
    regex='meta property="og:description" content="(.+?)"'
    m=re.compile(regex,re.DOTALL).findall(response)[0]
    
    m=m.split('\n')
    all_l=[]
    for itt in m:
 
        regex='http(.+?)(?: |$)'
        all_links=re.compile(regex).findall(itt)
        if len(all_links)>0:
            #if 't.me' in all_links[0] or 'twitter' in all_links[0]:
            #    continue
       
            all_l.append('[COLOR khaki][B]'+'http'+all_links[0]+'[/B][/COLOR]')
        else:
            all_l.append(itt)
    
    showText('Description', '\n'.join(all_l))
    
params=get_params()

url=None
name=None
mode=0
iconimage=None
fanart=None
description=None
data=None
page=0
try:
        url=unque(params["url"])
except:
        pass
try:
        name=unque(params["name"])
except:
        pass
try:
        iconimage=unque(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=unque(params["fanart"])
except:
        pass
try:        
        description=unque(params["description"])
except:
        pass
try:        
        data=unque(params["data"])
except:
        pass
try:        
        page=unque(params["page"])
except:
        pass

if mode==0 :
        main_menu(url)
elif mode==2:
    play_link(name,url,description)
elif mode==3:
    files_from(name,url)
elif mode==4:
    video_data(name,url)
xbmcplugin.setContent(int(sys.argv[1]), 'movies')


xbmcplugin.endOfDirectory(int(sys.argv[1]))

