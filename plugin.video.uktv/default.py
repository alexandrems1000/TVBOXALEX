# -*- coding: cp1254 -*-
# please visit http://www.iptvxtra.net

mainurl="http://srv1.iptvxtra.net/xbmc/xml/uk-streams.xml"

import base64
import cookielib,sys
import urllib2,urllib,re,os

from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
import resources.lib.requests as requests
import xbmcplugin,xbmcgui,xbmc,xbmcaddon 

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'albums')
Addon = xbmcaddon.Addon('plugin.video.uktv')
profile = xbmc.translatePath(Addon.getAddonInfo('profile'))
addonsettings = xbmcaddon.Addon(id='plugin.video.uktv')
__language__ = addonsettings.getLocalizedString
home = addonsettings.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER)
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
code1 = 'http://nix02.'

try:
 response = urllib2.urlopen('http://s.IPTVxtra.net/code02')
 for codex in response:
  c = codex	
 c = c.strip()
 c = c.replace('&key=','')
 c = c.partition("code=")
 code2 = c[2]
except:
 code2 = 'xxxxxxxxxxxxx'
 
def main():
    url = mainurl
    link=get_url(url)
	
    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    items = soup.findAll("item")
    for item in items:
            try:
                videoTitle=item.title.string
            except: pass
            try:
                url=item.link.string
                if 'totiptv' in url: url = code1 + url + '?oid=1&pt=3&dt=1&ra=1&code=' + code2 + '&key='
                #url = url + '|User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:18.0) Gecko/20100101 Firefox/18.0'
            except: pass
            try:
                thumbnail=item.thumbnail.string
            except: pass

            addLink(videoTitle,url,thumbnail)
    
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def addLink(name,url,iconimage):
        ok=True
        if 'giniko' in url:
            url = ginico(url)
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def ginico(url):
    x = url.partition('---')
    url = x[0]
    id = x[2].replace('xxx','')
    r = requests.get("http://giniko.com/watch.php?id=" + id)
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    r = requests.get("http://giniko.com/watch.php?id=37")
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    r = requests.get("http://giniko.com/watch.php?id=220")
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    else: return url
	
main()

xbmc.executebuiltin("Container.SetViewMode(500)")

