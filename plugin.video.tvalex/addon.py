#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,base64,xmltosrt,os,sys,time
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
h = HTMLParser.HTMLParser()

ultimaversao = '0.3.4'
addon_id = 'plugin.video.tvalex'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
down_path = selfAddon.getSetting('download-folder') 
base_url = 'http://www.tuga-filmes.com/'

################################################## 


#MENUS############################################

def menus():        		
	#dialog = xbmcgui.Dialog()
	#dialog.ok("TV BOX ALEX", "[COLOR red]                             MENSAGEM IMPORTANTE:                             [/COLOR][COLOR white]CAROS CLIENTES E AMIGOS, O ADDON ESTA EM ATUALIZAÇÃO, QUALQUER ERRO PEÇO DESCULPAS, SEREI BREVE. OBRIGADO[/COLOR]                              [COLOR GREEN]CONSULTAS:[/COLOR]                                      [COLOR YELLOW]FACEBOOK: Tv Box Canais Internacionais.[/COLOR]")
	addDir('[B]CANAIS TUGA[/B]','-',3,artfolder + 'CANAISTUGA.png')
	addDir('[B]CANAIS DO BRASIL[/B]','-',9,artfolder + 'CANAISBRASIL.png')
	addDir('[B]C. TEMPORARIOS[/B]','https://dl.dropbox.com/s/rsedumwxfcprs55/CANAISTEMP.txt?dl=0',4,artfolder + 'TEMPORARIOS.png')
	addDir('[B]UK TV[/B]','https://dl.dropbox.com/s/wxloawcl620fo8s/UKTV.txt?dl=0',4,artfolder + 'CANAISUK.png')
	addDir('[B]CANAIS INFANTIS[/B]','https://dl.dropbox.com/s/0bd938oa06gujs3/Infantil.txt?dl=0',4,artfolder + 'CANAISINFANTIS.png')
	addDir('[B]DESPORTO MUNDO[/B]','https://dl.dropbox.com/s/iuxhcbk1t5a2yzw/DesportoMundo.txt?dl=0',8,artfolder + 'ESPORTESINTERN.png')
	addDir('[B]MUSICA[/B]','https://dl.dropbox.com/s/vhm1wqlbmw4rt6t/MusicaMUNDO.txt?dl=0',4,artfolder + 'MUSICAMUNDO.png')	
	#versao_disponivel()
	if "confluence" in xbmc.getSkinDir(): xbmc.executebuiltin('Container.SetViewMode(500)')
	
def tuga():
	addDir('[B]TV PORTUGUESA[/B]','https://dl.dropbox.com/s/l2vn6zeg0caj3tw/Canais.txt?dl=0',4,artfolder + 'TVTUGA.png')
	addDir('[B]DESPORTO TUGA[/B]','https://dl.dropbox.com/s/dhc3m3i0co2kta3/Desporto.txt?dl=0',4,artfolder + 'DESPORTOTUGA.png')
	addDir('[B]RADIOS TUGA[/B]','https://dl.dropbox.com/s/kywo8hlh46wwgle/MusicaTUGA.txt?dl=0',4,artfolder + 'RADIOSTUGA.png')
	addDir('[B]WEBCAM[/B]','https://dl.dropbox.com/s/7ojo3qtlggdw6n2/WEBCAM.txt?dl=0',4,artfolder + 'WEBCAM.png')
	xbmc.executebuiltin("Container.SetViewMode(500)")
	
def tvbrasil():
	addDir('CANAIS ABERTOS','https://dl.dropbox.com/s/6sndnni5e6fi3v4/CANAIS%20ABERTOS%20BR.txt?dl=0',8,artfolder + 'CANAISABERTOS.png')
	addDir('CANAIS REGIONAIS','https://dl.dropbox.com/s/uwgvixzpgl0ok2w/CANAIS%20ABERTOS%20REGIONAIS.txt?dl=0',8,artfolder + 'REGIONAL.png')
	addDir('FUTEBOL AO VIVO','https://dl.dropbox.com/s/inpcue3jec322ow/Desporto%20PFC_BR.txt?dl=0',8,artfolder + 'FUTBOLAOVIVO.png')
	addDir('RELIGIOSOS (WEBCAM)','https://dl.dropbox.com/s/t4q1p88rnwxakzj/Religiosos.txt?dl=0',8,artfolder + 'RELIGIOSOS.png')
	xbmc.executebuiltin("Container.SetViewMode(500)")


###################################################################################
#FUNCOES

def listar_canais(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Link: ' + rtmp
                  addLink(nome,rtmp,img)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")

def listar_videos(url):
	soup = getSoup(url)
	items = soup.findAll("item")
	a = []
	for item in items:
		try: nomeprog = '  [B][COLOR red]%s[/COLOR][/B]' % canais[item.sigla.string]['nomeprog'].decode("utf-8","ignore")
		except: nomeprog = ''
		try: descprog = canais[item.sigla.string]['descprog']
		except: descprog = ''
		temp = [item.link.string,"[COLOR grey]%s[/COLOR]" % item.title.text.upper() + nomeprog,item.thumbnail.string,descprog]
		if temp not in a: a.append(temp)
	total = len(a)
	for url2, titulo, img, plot in a: 
		if 'plugin' in url2: url2 = url2.replace(';=','=')
		addLink(titulo,url2,img,plot)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	if "confluence" in xbmc.getSkinDir(): xbmc.executebuiltin('Container.SetViewMode(500)')


def play(url):
	listitem = xbmcgui.ListItem()
	listitem.setPath(url)
	listitem.setProperty('mimetype', 'video/x-msvideo')
	listitem.setProperty('IsPlayable', 'true')
	try:
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(url)
	except:
		dialog = xbmcgui.Dialog()
		dialog.ok(" Erro:", " Impossível abrir vídeo! ")
		pass

def versao_disponivel():
	versao=ultimaversao
	addDir('[B][COLOR blue]Definições do Add-on[/COLOR][/B]','-',11,artfolder + 'definicoes.png',False)
	addLink('[B][COLOR white]Versão (' + versao + ')[/COLOR][/B]','',artfolder + 'versao.png')
			
################################################
#    Funções relacionadas a media.             #
#                                              #
################################################

def makeRequest(url, headers=None):
        try:
            if headers is None: headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
            req = urllib2.Request(url,None,headers)
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            return data
        except urllib2.URLError, e:
            print 'URL: '+url
            if hasattr(e, 'code'):
                print 'We failed with error code - %s.' % e.code
                xbmc.executebuiltin("XBMC.Notification(tugafree,We failed with error code - "+str(e.code)+",10000,"+icon+")")
            elif hasattr(e, 'reason'):
                addon_log('We failed to reach a server.')
                addon_log('Reason: %s' %e.reason)
                xbmc.executebuiltin("XBMC.Notification(tugafree,We failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")

def getSoup(url):
        data = makeRequest(url)
        return BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)

#eseffair 23/04/2014 - novo epg 
def getepg(url):
	print 'Epg Url: ' + url
        url=urllib.urlopen(url)
        source=url.read()
        url.close()
        soup = BeautifulSoup(source)
	programas = soup.findAll("li",  { "class" : "home" })
        programa1 = programas[2].a["title"]
	programa1_url = programas[2].a["href"]
        horario1 = programas[2].a.div.text
        programa2 = programas[3].a["title"]
        horario2 = programas[3].a.div.text
	url=urllib.urlopen('http://meuguia.tv/'+programa1_url)
        source=url.read()
        url.close()
	soup_programa = BeautifulSoup(source)
	plot = soup_programa.find("div", { "id" : "sinopse" }).prettify()
	try: plot = re.findall(r'str="(.*?)"', plot)[0]
	except: plot = ''
	print "Plot: " + plot
        return (' (%s - "%s" / %s - "%s")' % (horario1,programa1,horario2,programa2), plot)

def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def real_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.geturl()
	response.close()
	return link
	
def addLink(name,url,iconimage,plot=''):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "plot": plot } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="video", infoLabels={ "title": name, "plot": plot } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok

def videomega_resolver(referer):
	html = abrir_url(referer)
	
	ref_data={'Host':'videomega.tv',
			  'Connection':'Keep-alive',
			  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			  'User-Agent':'stagefright/1.2 (Linux;Android 4.4.4)',
			  'Referer':referer}
	
	if re.search('http://videomega.tv/iframe.js',html):
		lines = html.splitlines()
		aux = ''
		for line in lines:
			if re.search('http://videomega.tv/iframe.js',line):
				aux = line
				break;
		ref = re.compile('ref="(.+?)"').findall(line)[0]
	else:
		try:
			hash = re.compile('"http://videomega.tv/validatehash.php\?hashkey\=(.+?)"').findall(html)[0]
			ref = re.compile('ref="(.+?)"').findall(requests.get("http://videomega.tv/validatehash.php?hashkey="+hash,headers=ref_data).text)[0]
		except:
			try:
				hash = re.compile("'http://videomega.tv/validatehash.php\?hashkey\=(.+?)'").findall(html)[0]
				ref = re.compile('ref="(.+?)"').findall(requests.get("http://videomega.tv/validatehash.php?hashkey="+hash,headers=ref_data).text)[0]
			except:
				iframe = re.compile('"http://videomega.tv/iframe.php\?(.+?)"').findall(html)[0] + '&'
				ref = re.compile('ref=(.+?)&').findall(iframe)[0]
	
	url = 'http://videomega.tv/cdn.php?ref='+ref+'&width=638&height=431&val=1'
	iframe_html = requests.get(url,headers=ref_data).text
	url_video = re.compile('<source src="(.+?)"').findall(iframe_html)[0]
	try: url_legendas = re.compile('<track kind="captions" src="(.+?)"').findall(iframe_html)[0]
	except: url_legendas = '-'
	ref_data['Referer'] = url
	return [url_video+headers_str(ref_data),url_legendas]

def addDirPlayer(name,url,mode,iconimage,total,fnart):
	codigo_fonte = abrir_url(url)
	
	try: plot = re.compile('<b>SINOPSE:.+?>(.+?)</p>').findall(codigo_fonte)[0]
	except: 
		try: plot = re.compile('<b>Sinopse:.+?>(.+?)</p>').findall(codigo_fonte)[0]
		except: plot = 'Sem sinopse...'
	plot = h.unescape(plot.decode('utf-8')).encode('utf-8').replace('<span>','')
	
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fnart)
	liz.setInfo( type="Video", infoLabels= { "Title": name,
											 "OriginalTitle": name,
											 "Plot": plot 
											 } )
	cm = []
	cm.append(('Sinopse', 'XBMC.Action(Info)'))
	cm.append(('Download', 'XBMC.RunPlugin(%s?mode=6&url=%s&name=%s)' % (sys.argv[0], urllib.quote_plus(url),name)))
	liz.addContextMenuItems(cm, replaceItems=True)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False,totalItems = total)
	return ok
	


############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'): params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2: param[splitparams[0]]=splitparams[1]
        return param

params=get_params()
url=None
name=None
mode=None
iconimage=None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)

###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################

if mode==None or url==None or len(url)<1:
    print ""
    menus()
	
elif mode==3:
	print ""
	tuga()	
	
elif mode==4:
    print ""
    listar_videos(url)	
	
elif mode==5:
    print ""
    encontrar_fontes(url)
	
elif mode==6:
    print ""
    play(url)
	
	
elif mode==8: 
	print ""
	listar_canais(url)	
	
elif mode==9:
	print ""
	tvbrasil()

elif mode==10:
	selfAddon.openSettings()
	
	
	
xbmcplugin.endOfDirectory(int(sys.argv[1]))