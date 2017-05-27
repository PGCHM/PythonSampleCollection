import urllib
import urllib2
import sys

uri = 'http://qamonitor/qacommon/CrLookup.aspx'
cr = sys.argv[1]

#the http headers are useful to simulate a particular browser (some sites deny
#access to non-browsers (bots, etc.)
#also needed to pass the content type. 
headers = {
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# we group the form fields and their values in a list (any
# iterable, actually) of name-value tuples.  This helps
# with clarity and also makes it easy to later encoding of them.

formFields = (
   # the viewstate is actualy 800+ characters in length! I truncated it
   # for this sample code.  It can be lifted from the first page
   # obtained from the site.  It may be ok to hardcode this value, or
   # it may have to be refreshed each time / each day, by essentially
   # running an extra page request and parse, for this specific value.
   (r'__VSTATE', r'7TzretNIlrZiKb7EOB3AQE ... ...2qd6g5xD8CGXm5EftXtNPt+H8B'),

   # following are more of these ASP form fields
   (r'cr',cr)
   ## (r'__VIEWSTATE', r'')
   ## (r'__EVENTVALIDATION', r'/wEWDwL+raDpAgKnpt8nAs3q+pQOAs3q/pQOAs3qgpUOAs3qhpUOAoPE36ANAve684YCAoOs79EIAoOs89EIAoOs99EIAoOs39EIAoOs49EIAoOs09EIAoSs99EI6IQ74SEV9n4XbtWm1rEbB6Ic3/M=')
)

# these have to be encoded    
encodedFields = urllib.urlencode(formFields)

req = urllib2.Request(uri, encodedFields, headers)
f= urllib2.urlopen(req)     #that's the actual call to the http site.

# *** here would normally be the in-memory parsing of f 
#     contents, but instead I store this to file
#     this is useful during design, allowing to have a
#     sample of what is to be parsed in a text editor, for analysis.

try:
  fout = open('CRs\'+cr+'.htm', 'w')
except:
  print('Could not open output file\n')

fout.writelines(f.readlines())
fout.close()
