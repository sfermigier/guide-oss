#!/usr/bin/env python
# coding=utf8


import unicodedata
import re

def slugify(value, separator="-"):
  """ Slugify an unicode string, to make it URL friendly. """
  if not isinstance(value, unicode):
    value = unicode(value)
  value = unicodedata.normalize('NFKD', value)
  value = value.encode('ascii', 'ignore')
  value = value.decode('ascii')
  value = re.sub('[^\w\s-]', ' ', value)
  value = value.strip().lower()
  value = re.sub('[%s\s]+' % separator, separator, value)
  return str(value)


def parse_chapter(s):
  output = []
  lines = s.split("\n")
  title = lines[0]
  output.append(title)
  output.append(len(title) * "=")
  output.append("")

  in_header = False
  version = porteur = site = None

  for line in lines[1:]:
    print (line,)
    if re.match(r"^\s", line):
      title = line[1:]
      output.append("")
      output.append(title)
      output.append(len(title) * "-")
      output.append("")
    else:
      m = re.match(u"^Version étudiée : (.*)", line)
      if m:
        in_header = True
        version = m.group(1)
        continue
      if in_header:
        m =  re.match(u"^Site Internet de la solution : (.*)", line)
        if m:
          site = m.group(1)
          continue
        m =  re.match(u"^Solution portée par (.*)", line)
        if m:
          porteur = m.group(1)
          continue

        in_header = False
        assert version and porteur and site, (version, porteur, site)
        output.append(":Version: %s" % version)
        output.append(":Site: %s" % site)
        output.append(":Porteur: %s" % porteur)
        output.append("")

        version = porteur = site = None

      output.append(line)
      output.append("")
  return "\n".join(output)

def main():
  source = open("orig.txt").read().decode("utf8")
  master = open("master.rst", "wc")

  chapters = source.split("\n---\n")
  chapters = [ chapter.strip() for chapter in chapters ]

  for chapter in chapters:
      lines = chapter.split("\n")
      title = lines[0]
      slug = slugify(title)

      chapter = parse_chapter(chapter)

      open("src/" + slug + ".rst", "wc").write(chapter.encode("utf8") + "\n")

      master.write('.. include:: src/%s.rst\n' % slug)


main()
