#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright 2014 Anonymous
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

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,os,sys,requests,time
h = HTMLParser.HTMLParser()

addon_id = 'plugin.video.tugamovies'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
base_url = 'http://www.tuga-filmes.com/'
fanart = os.path.join(addonfolder,'fanart.jpg')
down_path = selfAddon.getSetting('download-folder')

def CATEGORIES():
	addDir('Em Cartaz',base_url,1,artfolder + 'categorias.png')
	addDir('Destaques','http://www.tuga-filmes.com/category/destaque/',1,artfolder + 'destaques.png')
	addDir('Categorias','-',3,artfolder + 'categorias.png')
	addDir('Brevemente','http://www.tuga-filmes.com/category/brevemente/',8,artfolder + 'brevemente.png')
	addDir('Pesquisar','-',4,artfolder + 'pesquisar.png')
	xbmc.executebuiltin("Container.SetViewMode(500)")

def pesquisa():
	keyb = xbmc.Keyboard('', 'Escreva o parâmetro de pesquisa')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		url = 'http://www.tuga-filmes.com/?s=%s&submit=Search' % str(parametro_pesquisa)
		listar_videos(url)
	
def categorias():
	html = abrir_url(base_url)
	match = re.compile('<li id=".+?" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="(.+?)">(.+?)</a></li>').findall(html)
	
	for url, cat in match:
		if cat.startswith('- Filmes'): continue
		addDir(cat,url,1,artfolder + 'categorias.png')
		xbmc.executebuiltin("Container.SetViewMode(500)")
	
def listar_videos(url):
	codigo_fonte = abrir_url(url)
	url_title = re.compile('<a href="(.+?)" class="thumbnail-wrapper" title="(.+?)">').findall(codigo_fonte)
	img = re.compile('<img.+?src="(.+?)"').findall(codigo_fonte)
	total = len(url_title)
	
	for i in range(0,total):
		titulo = h.unescape(url_title[i][1].decode('utf-8')).encode('utf-8')
		url_v = url_title[i][0]
		
		if selfAddon.getSetting('fanart') == 'true':
			txheaders= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
			tmdbim='http://image.tmdb.org/t/p/'
			#'http://image.tmdb.org/t/p/original'
			#'http://image.tmdb.org/t/p/w500'
			try:
				t = titulo
				request='http://api.themoviedb.org/3/search/movie?api_key=eee9ac1822295afd8dadb555a0cc4ea8&order=asc&query=%s&per_page=1'%(urllib.quote_plus(t))
				response = requests.get(request,headers=txheaders).json()
				fnart = tmdbim + 'w780' + response['results'][0]['backdrop_path']
			except:
				try:
					t = file_name(url2).replace(".html","").replace("-"," ")
					request='http://api.themoviedb.org/3/search/movie?api_key=eee9ac1822295afd8dadb555a0cc4ea8&order=asc&query=%s&per_page=1'%(urllib.quote_plus(t))
					response = requests.get(request,headers=txheaders).json()
					fnart = tmdbim + 'w780' + response['results'][0]['backdrop_path']
				except: 
					try:
						t = file_name(url2).replace(".html","").replace("-"," ")
						t = ''.join(i for i in t if not i.isdigit())
						t = t.replace("(","").replace(")","")
						request='http://api.themoviedb.org/3/search/movie?api_key=eee9ac1822295afd8dadb555a0cc4ea8&order=asc&query=%s&per_page=1'%(urllib.quote_plus(t))
						response = requests.get(request,headers=txheaders).json()
						fnart = tmdbim + 'w780' + response['results'][0]['backdrop_path']
					except:fnart = fanart
		else: fnart = fanart
		addDirPlayer(titulo,url_v,2,img[i],total,fnart)
	
	try: 
		next = re.compile('<a class="nextpostslink" rel="next" href="(.+?)"').findall(codigo_fonte)[0]
		addDir('Próxima página >>',next,1,artfolder + 'proxpagina.png')
	except: pass
	
	xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
	if selfAddon.getSetting('fanart') == 'true': xbmc.executebuiltin("Container.SetViewMode(515)")
	else: xbmc.executebuiltin("Container.SetViewMode(500)")
	
def listar_cartaz(url):
	codigo_fonte = abrir_url(url)
	url_title = re.compile('<a href="(.+?)" class="thumbnail-wrapper" title="(.+?)">').findall(codigo_fonte)
	img = re.compile('<img.+?src="(.+?)"').findall(codigo_fonte)
	total = len(url_title)
	
	for i in range(0,total):
		titulo = h.unescape(url_title[i][1].decode('utf-8')).encode('utf-8')
		url_v = url_title[i][0]
		
		if selfAddon.getSetting('fanart') == 'true':
			txheaders= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
			tmdbim='http://image.tmdb.org/t/p/'
			#'http://image.tmdb.org/t/p/original'
			#'http://image.tmdb.org/t/p/w500'
			try:
				t = titulo
				request='http://api.themoviedb.org/3/search/movie?api_key=eee9ac1822295afd8dadb555a0cc4ea8&order=asc&query=%s&per_page=1'%(urllib.quote_plus(t))
				response = requests.get(request,headers=txheaders).json()
				fnart = tmdbim + 'w780' + response['results'][0]['backdrop_path']
			except:
				try:
					t = file_name(url2).replace(".html","").replace("-"," ")
					request='http://api.themoviedb.org/3/search/movie?api_key=eee9ac1822295afd8dadb555a0cc4ea8&order=asc&query=%s&per_page=1'%(urllib.quote_plus(t))
					response = requests.get(request,headers=txheaders).json()
					fnart = tmdbim + 'w780' + response['results'][0]['backdrop_path']
				except: 
					try:
						t = file_name(url2).replace(".html","").replace("-"," ")
						t = ''.join(i for i in t if not i.isdigit())
						t = t.replace("(","").replace(")","")
						request='http://api.themoviedb.org/3/search/movie?api_key=eee9ac1822295afd8dadb555a0cc4ea8&order=asc&query=%s&per_page=1'%(urllib.quote_plus(t))
						response = requests.get(request,headers=txheaders).json()
						fnart = tmdbim + 'w780' + response['results'][0]['backdrop_path']
					except:fnart = fanart
		else: fnart = fanart
		addDirPlayer(titulo,url_v,7,img[i],total,fnart)
	
	try: 
		next = re.compile('<a class="nextpostslink" rel="next" href="(.+?)"').findall(codigo_fonte)[0]
		addDir('Próxima página >>',next,1,artfolder + 'proxpagina.png')
	except: pass
	
	xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
	if selfAddon.getSetting('fanart') == 'true': xbmc.executebuiltin("Container.SetViewMode(515)")
	else: xbmc.executebuiltin("Container.SetViewMode(500)")
	
def player(name,url,iconimage):
	mensagemprogresso = xbmcgui.DialogProgress()
	mensagemprogresso.create('TvBoxAlex', 'A resolver link','Por favor aguarde...')
	mensagemprogresso.update(33)
	try:
		url, legendas = videomega_resolver(url)
	except:
		dialog = xbmcgui.Dialog()
		dialog.ok(" Erro:", " Impossível abrir vídeo! ")
		return
	mensagemprogresso.update(100)
	mensagemprogresso.close()
	listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	listitem.setPath(url)
	listitem.setProperty('mimetype', 'video/x-msvideo')
	listitem.setProperty('IsPlayable', 'true')
	try:
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(url,listitem)
		while not xbmcPlayer.isPlaying(): xbmc.sleep(500)
		if selfAddon.getSetting('subs') == 'true' and legendas != '-': xbmcPlayer.setSubtitles(legendas)
	except:
		dialog = xbmcgui.Dialog()
		dialog.ok(" Erro:", " Impossível abrir vídeo! ")

def cartaz(name,url,iconimage):
	mensagemprogresso = xbmcgui.DialogProgress()
	mensagemprogresso.create('TvBoxAlex', 'A resolver link','Por favor aguarde...')
	mensagemprogresso.update(33)
	try:
		url, legendas = videomega_resolver(url)
	except:
		dialog = xbmcgui.Dialog()
		dialog.ok("TV BOX ALEX", "[COLOR white]                             BREVEMENTE PARA VISUALIZAÇÃO                             [/COLOR] [COLOR blue]                             MOVIES DA TV BOX ALEX.[/COLOR]")
		return
	mensagemprogresso.update(100)
	mensagemprogresso.close()
	listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	listitem.setPath(url)
	listitem.setProperty('mimetype', 'video/x-msvideo')
	listitem.setProperty('IsPlayable', 'true')
	try:
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(url,listitem)
		while not xbmcPlayer.isPlaying(): xbmc.sleep(500)
		if selfAddon.getSetting('subs') == 'true' and legendas != '-': xbmcPlayer.setSubtitles(legendas)
	except:
		dialog = xbmcgui.Dialog()
		dialog.ok("TV BOX ALEX", "[COLOR white]                             BREVEMENTE PARA VISUALIZAÇÃO                             [/COLOR] [COLOR blue]                             MOVIES DA TV BOX ALEX.[/COLOR]")
		
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
	
def file_name(path):
	import ntpath
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)
	

def headers_str(headers):
	start = True
	headers_str = ''
	for k,v in headers.items():
		if start:
			headers_str += '|'+urllib.quote_plus(k)+'='+urllib.quote_plus(v)
			start = False
		else: headers_str += '&'+urllib.quote_plus(k)+'='+urllib.quote_plus(v)
	return headers_str
	
def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

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
	
def download(name,url):
	if down_path == '':
		dialog = xbmcgui.Dialog()
		dialog.ok(" Erro:", "Por favor defina a pasta de Download!")
		selfAddon.openSettings()
		return
	name = re.sub('[^-a-zA-Z0-9_.()\\\/ ]+', '',name) + '.mp4'
	mypath=os.path.join(down_path,name)
	if os.path.isfile(mypath) is True:
		dialog = xbmcgui.Dialog()
		dialog.ok('Erro','Já existe um ficheiro com o mesmo nome')
		return
			  
	url, legendas = videomega_resolver(url)
	headers = {}
	hh = url.split('|')[1].split('&')
	for h in hh:
		k = urllib.unquote_plus(h.split('=')[0])
		v = urllib.unquote_plus(h.split('=')[1])
		headers[k] = v
		
	url = url.split('|')[0]
	httpDownload(url, mypath, headers, dialogdown)
	
def httpDownload(url, filename, headers=None, reporthook=None,postData=None):
	dp = xbmcgui.DialogProgress()
	dp.create('Download')
	try:
		if headers==None:
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.99 Safari/535.1'}
		reqObj = urllib2.Request(url, postData, headers)
		fp = urllib2.urlopen(reqObj)
		headers = fp.info()

		tfp = open(filename, 'wb')
		result = filename, headers
		bs = 1024*8
		size = -1
		read = 0
		blocknum = 0
		start_time = time.time()
		if reporthook:
			if "content-length" in headers:
				size = int(headers["Content-Length"])
			reporthook(blocknum, bs, size, dp, start_time)

		while 1:
			block = fp.read(bs)
			if block == "": break
			read += len(block)
			tfp.write(block)
			blocknum += 1
			if reporthook:
				reporthook(blocknum, bs, size, dp, start_time)

		fp.close()
		tfp.close()
		del fp
		del tfp
	except:
		while os.path.exists(filename): 
			try: os.remove(filename); break 
			except: pass
	dp.close()

def dialogdown(numblocks, blocksize, filesize, dp, start_time):
      try:
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB de %.02f MB' % (currently_downloaded, total) 
            e = ' (%.0f Kb/s) ' % kbps_speed 
            tempo = 'Tempo estimado:' + ' %02d:%02d' % divmod(eta, 60) 
            dp.update(percent, mbs + e,tempo)
      except: 
            percent = 100 
            dp.update(percent) 
      if dp.iscanceled(): 
            dp.close()
            raise StopDownloading('Stopped Downloading')

class StopDownloading(Exception):
      def __init__(self, value): self.value = value 
      def __str__(self): return repr(self.value)
	
def addLink(name,url,iconimage,total=1):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', addonfolder + '/fanart.jpg')
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,totalItems=total)
	return ok

def addDir(name,url,mode,iconimage,pasta = True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', addonfolder + '/fanart.jpg')
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
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

if mode==None or url==None or len(url)<1: CATEGORIES()
elif mode==1: listar_videos(url)
elif mode==2: player(name,url,iconimage)
elif mode==3: categorias()
elif mode==4: pesquisa()
elif mode==5: selfAddon.openSettings()
elif mode==6: download(name,url)
elif mode==7: cartaz(name,url,iconimage)
elif mode==8: listar_cartaz(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))