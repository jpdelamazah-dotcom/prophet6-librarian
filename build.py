# Copia la app desde la fuente y le agrega lo necesario para instalarla como app.
import sys
src=open(sys.argv[1]).read()
head='''<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#17181A">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Prophet-6">
<link rel="apple-touch-icon" href="icon-192.png">
<link rel="icon" href="icon-192.png">
<script>if("serviceWorker" in navigator&&location.protocol==="https:") navigator.serviceWorker.register("sw.js").catch(()=>{});</script>
'''
i=src.index("<style>"); open("index.html","w").write(src[:i]+head+src[i:])
