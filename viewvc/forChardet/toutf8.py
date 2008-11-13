import chardet

def toutf8(txt):
  if not txt:
    return txt
  c = chardet.detect( txt)
  try:
    u = unicode( txt, c['encoding'])
    return u.encode('utf-8')
  except UnicodeError:
    pass
  except TypeError:
    pass
  return txt
