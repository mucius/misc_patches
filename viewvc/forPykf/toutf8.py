import pykf
import cgi

def toutf8(txt):
  """pykf.guess cannot guess utf-8 string (wrong to sjis)"""
  if not txt:
    return txt
  import sys
  c = pykf.guess(txt)
  if c is pykf.JIS:
    try:
      u = unicode(txt, 'iso2022_jp')
    except:
      return txt
    return u.encode('utf-8')
  for enc in ['utf-8', 'euc_jp', 'shift_jis']:
    try:
      u = unicode(txt, enc)
      return u.encode('utf-8')
    except UnicodeError:
      pass
  return txt

def escape(txt):
  return cgi.escape( toutf8(txt))
