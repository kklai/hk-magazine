# "http://download.hk-magazine.com/pdf/hkmagazine/HKMagazine_1099.pdf"
# "http://download.hk-magazine.com/pdf/hkmagazine/HKMagazine_1165.pdf"

import urllib2


def download_file(download_url):
    try:
        response = urllib2.urlopen(download_url)
        filename = str.split(download_url, "/")[5]
        file = open(filename, 'w')
        file.write(response.read())
        file.close()
        print("Completed")
    except urllib2.HTTPError, err:
        print("Failed: " + download_url)


for x in xrange(1099, 1166):
  print(x)
  download_file("http://download.hk-magazine.com/pdf/hkmagazine/HKMagazine_" + str(x) + ".pdf")