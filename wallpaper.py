from time import gmtime, strftime
from xml.dom import minidom
import ctypes, urllib.request, os

url = strftime("http://commons.wikimedia.org/w/api.php?action=expandtemplates&text={{Potd/%Y-%m-%d}}&format=xml", gmtime())

f = urllib.request.urlopen(url)

dom = minidom.parse(f)
expandtemplates = dom.getElementsByTagName("expandtemplates")

filename = str(expandtemplates[0].firstChild.nodeValue)
filename = filename.replace(" ", "_")

screenWidth = ctypes.windll.user32.GetSystemMetrics(0)

fApi = urllib.request.urlopen("http://commons.wikimedia.org/w/api.php?titles=Image:" + filename.replace(" ", "%20") + "&action=query&prop=imageinfo&iiprop=url&format=xml")
#print(fApi.read())

fDom = minidom.parse(fApi)

fullUrl = fDom.getElementsByTagName("ii")[0].attributes["url"].nodeValue

print(fullUrl)

localFileUrl = "backgroundwallpaper" + fullUrl[fullUrl.rindex('.'):len(fullUrl)]

print(localFileUrl)

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19"

u = urllib.request.urlopen(urllib.request.Request(fullUrl, headers={'User-Agent': user_agent}))

bytes = u.read()
print("Download file")

localFile = open(localFileUrl, "wb")
localFile.write(bytes)
localFile.close();

print("Written to file")

user32 = ctypes.windll.user32

SPI_SETDESKWALLPAPER = 20

fullLocalFileUrl = os.getcwd() + "\\" + localFileUrl;

user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, fullLocalFileUrl, 0)

print("Set wallpaper to " + fullLocalFileUrl)