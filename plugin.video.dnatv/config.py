import sys
import os
import json
import urllib
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import load_channels
import hashlib
import re
import random
import base64
import server


fanart = 'special://home/addons/plugin.video.dnatv/fanart.jpg'
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addondir    = xbmc.translatePath( addon.getAddonInfo('profile') ) 

opener = urllib.FancyURLopener({})
f = opener.open('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL21hY2JsaXp6YXJkL2RuYXJlcG8vbWFzdGVyL2hhc2gvcGhhc2gudHh0'.decode('base64'))
pu = f.read().decode('base64')

addonset = ['6148523063484D364C793979595863755A326C306148566964584E6C636D4E76626E526C626E5175593239744C32316859324A736158703659584A6B4C32527559584A6C634738766257467A644756794C326868633267766147467A6144457564486830'.decode('hex').decode('base64'), '6148523063484D364C793979595863755A326C306148566964584E6C636D4E76626E526C626E5175593239744C32316859324A736158703659584A6B4C32527559584A6C634738766257467A644756794C326868633267766147467A6144497564486830'.decode('hex').decode('base64'), '6148523063484D364C793979595863755A326C306148566964584E6C636D4E76626E526C626E5175593239744C32316859324A736158703659584A6B4C32527559584A6C634738766257467A644756794C326868633267766147467A61444D7564486830'.decode('hex').decode('base64')]
opener = urllib.FancyURLopener({})
f = opener.open(random.choice(addonset))
temp = f.read()
pm = temp.decode('hex').decode('base64')


def portalConfig(number):

	portal = {};
	
	portal['parental'] = addon.getSetting("parental");
	portal['password'] = addon.getSetting("password");
	
	portal['name'] = addon.getSetting("portal_name_" + number);
	portal['url'] = pu;
	portal['mac'] = configMac(number);
	portal['serial'] = configSerialNumber(number);
		
	return portal;


def configMac(number):
	global go;
	
	custom_mac = ('Y3VzdG9tX21hY18x'.decode('base64'));
	portal_mac = ('cG9ydGFsX21hY18x'.decode('base64'));
	
	if custom_mac != 'true':
		portal_mac = pm;
		
	elif not (custom_mac == 'true' and re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", portal_mac.lower()) != None):
		xbmcgui.Dialog().notification(addonname, 'Custom Mac ' + number + ' is Invalid.', xbmcgui.NOTIFICATION_ERROR );
		portal_mac = '';
		go=False;
		
	return portal_mac;
	
	
def configSerialNumber(number):
	global go;
	
	send_serial = addon.getSetting('send_serial_' + number);
	custom_serial = addon.getSetting('custom_serial_' + number);
	serial_number = addon.getSetting('serial_number_' + number);
	device_id = addon.getSetting('device_id_' + number);
	device_id2 = addon.getSetting('device_id2_' + number);
	signature = addon.getSetting('signature_' + number);

	
	if send_serial != 'true':
		return None;
	
	elif send_serial == 'true' and custom_serial == 'false':
		return {'custom' : False};
		
	elif send_serial == 'true' and custom_serial == 'true':
	
		if serial_number == '' or device_id == '' or device_id2 == '' or signature == '':
			xbmcgui.Dialog().notification(addonname, 'Serial information is invalid.', xbmcgui.NOTIFICATION_ERROR );
			go=False;
			return None;
	
		return {'custom' : True, 'sn' : serial_number, 'device_id' : device_id, 'device_id2' : device_id2, 'signature' : signature};
		
	return None;