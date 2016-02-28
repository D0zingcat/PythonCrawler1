# coding:utf-8
import urllib, os


# The amount of records in total
totalRecord = 111

# The main domain
domain = 'http://www.liaoxuefeng.com'          

# The storage path
path = os.getcwd() + "\\" + r'html\\'    

# The "Meta" data of a HTML file keeping the contents of '<head>' and '<body>' such information 
data_input = open(r'meta.html', 'r')
head = data_input.read()

# To get the index URLs
f = urllib.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
home = f.read()
f.close()

# remove all the spaces and enters to get URL more easily
geturl = home.replace("\n", "")
geturl = geturl.replace(" ", "")

# The URL links with other characters
list = geturl.split(r'em;"><ahref="')[1:totalRecord]

# The first Page
list.insert(0, '/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000">')

for li in list:
    url = li.split(r'">')[0]

    # Merge the URL
    url = domain + url              
    f = urllib.urlopen(url)
    html = f.read()

    # To name the files
    title = html.split("<title>")[1]
    title = title.split(" - 廖雪峰的官方网站</title>")[0]

    # To decode 
    title = title.decode('utf-8').replace("/", " ")
    
#     # To get the body content
    html = html.split('<div class="x-content" style="width:100%">')[1].split(r'<div id="x-wiki-prev-next')[0]
    
    
    html = html.replace(r'src="', 'src="' + domain)
    print "The %d(th) record has be taken down." % (list.index(li) + 1)

#     # Make Up complete html files using the meta template
    html = head + "<title>%s</title>" % title.encode('utf-8') + html+"</body></html>"

#     # Save files to local drive
    output = open(path + "%d_" % (list.index(li) + 1) + title + '.html', 'w')
    output.write(html)
    output.close()

# Print statistics in total
print "Here are %d records in total" % len(list)