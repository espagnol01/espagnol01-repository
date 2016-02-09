# denmark television plugin written by IPTVxtra
# -*- coding: utf-8 -*-

# for more info please visit http://www.iptvxtra.net

import xbmcgui,xbmcplugin 
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty( "Fanart_Image", img )
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)


add_video_item('',{ 'title': '       - - - - - -  TV CHANNELS SWEDEN  - - - - - -'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/icon.png')

add_video_item('http://srv1.iptvxtra.net/xbmc/m3u/schweden.m3u',{ 'title': 'SWEDEN TEST PLAYLIST'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/icon.png')
add_video_item('https://svt10-lh.akamaihd.net/i/svt10_0@77505/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': 'SVT 1 (SE)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/svt1.png')
add_video_item('https://svt12-lh.akamaihd.net/i/svt12_0@77507/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': 'SVT 2 (SE)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/svt2.png')
add_video_item('https://svt13-lh.akamaihd.net/i/svt13_0@77508/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': 'SVT Barnkanalen (SE)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/svtb.png')
add_video_item('https://svt11-lh.akamaihd.net/i/svt11_0@77506/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': 'SVT Kunskapskanalen (SE)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/svtk.png')
add_video_item('http://tv4live-i.akamaihd.net/hls/live/200284/akamaihls2/wifi1500_akamaihls2.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': 'TV 4 (SE)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv4se.png')
add_video_item('rtmp://cdn-kanal10.crossnet.net/kanal10//mpegts.stream',{ 'title': 'TV10 (SE)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv10se.png')
add_video_item('rtmp://stream1.lifestyletv.se/live/livestream3',{ 'title': 'Livestyle TV'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/livstyle.png')

add_video_item('',{ 'title': '       - - - - - -  TV CHANNELS NORWAY  - - - - - -'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/icon.png')

add_video_item('https://nrk1us-f.akamaihd.net/i/nrk1us_0@102847/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 1 (NO)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/nrk1.png')
add_video_item('https://nrk2us-f.akamaihd.net/i/nrk2us_0@107231/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 2 (NO)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/nrk2.png')
add_video_item('https://nrk3us-f.akamaihd.net/i/nrk3us_0@107233/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 3 (NO)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/nrk3.png')
add_video_item('https://nrksuper-lh.akamaihd.net/i/nrksupertvus_0@108447/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK Super (NO)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/nrksuper.png')
add_video_item('https://nrktegnsprak-lh.akamaihd.net/i/nrktegnsprak_0@111177/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK Tegnsprak (NO)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/nrkteg.png')
add_video_item('http://hls.akamai.tv2.no/wzlive/_definst_/amlst:LS3/.smil/playlist.m3u8?DVR|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK Nyheter (NO) - sorry not work'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/nrkny.png')
                
add_video_item('',{ 'title': '       - - - - - -  TV CHANNELS DENMARK  - - - - - -'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/icon.png')

add_video_item('http://dr01-lh.akamaihd.net/i/dr01_0@147054/master.m3u8?b=100-2000|X-Forwarded-For=77.66.34.57',{ 'title': 'DR 1 (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/dr1.png')
add_video_item('http://dr02-lh.akamaihd.net/i/dr02_0@147055/master.m3u8?b=100-2000|X-Forwarded-For=77.66.34.57',{ 'title': 'DR 2 (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/dr2.png')
add_video_item('http://dr03-lh.akamaihd.net/i/dr03_0@147056/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DK 3 (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/dr3.png')
add_video_item('http://dr04-lh.akamaihd.net/i/dr04_0@147057/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DR K (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/drk.png')
add_video_item('http://dr05-lh.akamaihd.net/i/dr05_0@147058/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DR Ramasjang (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/drrs.png')
add_video_item('http://dr06-lh.akamaihd.net/i/dr06_0@147059/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DK Ultra (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/dru.png')
# add_video_item('rtmp://ftflash.arkena.dk/webtvftlivefl/ playpath=mp4:live.mp4 pageUrl=http://www.ft.dk/webTV/TV_kanalen_folketinget.aspx live=1',{ 'title': 'Folketinget (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/folk.png')
# add_video_item('http://lswb-de-08.servers.octoshape.net:1935/live/kanalsport_1000k/playlist.m3u8',{ 'title': 'KanalSport.dk (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/dksport.png')
add_video_item('rtmp://livestream2.fynskemedier.dk:1935/live/_definst_/tv2fyn_1000 live=1',{ 'title': 'TV2 Fyn (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv2dk.png')
add_video_item('rtmp://livestream2.fynskemedier.dk:1935/live/_definst_/tv2lorry_1000 live=1',{ 'title': 'TV2 Lorry (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv2dk.png')
add_video_item('rtmp://livestream2.fynskemedier.dk:1935/live/_definst_/tvsyd_1000 live=1',{ 'title': 'TV2 Syd (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv2dk.png')
add_video_item('rtmp://live.tvmidtvest.dk/tvmv/live live=1',{ 'title': 'TV2 Midtvest (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv2dk.png')
add_video_item('rtmp://livestream2.fynskemedier.dk:1935/live/_definst_/tv2nord-plus_1000 live=1',{ 'title': 'TV2 Nord (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv2dk.png')
add_video_item('http://tv2east.live-s.cdn.bitgravity.com/cdn-live-c1/_definst_/tv2east/live/feed01/playlist.m3u8|X-Forwarded-For=77.66.34.57',{ 'title': 'TV2 East (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv2dk.png')
add_video_item('rtmp://livestream2.fynskemedier.dk:1935/live/_definst_/tv2oj-plus_1000 live=1',{ 'title': 'TV2 OJ (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv2dk.png')
add_video_item('rtmp://itv08.digizuite.dk/tv2b/ch1 live=1',{ 'title': 'TV2 Bornholm (DK)'},img='http://srv1.iptvxtra.net/xbmc/senderlogos_dk/tv2dk.png')

xbmcplugin.endOfDirectory(plugin_handle)





















