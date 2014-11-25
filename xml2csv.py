'''from xmlutils.xml2csv import xml2csv

converter = xml2csv("sample.xml", "sample.csv", encoding="utf-8")
converter.convert(tag="row")

from xml.dom.minidom import parseString, parse

dom = parseString(<row Id="1" PostTypeId="1" AcceptedAnswerId="509" CreationDate="2009-04-30T06:49:01.807" Score="15" ViewCount="1981" Body="&lt;p&gt;Our nightly full (and periodic differential) backups are becoming quite large, due mostly to the amount of indexes on our tables; roughly half the backup size is comprised of indexes.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;We're using the &lt;strong&gt;Simple&lt;/strong&gt; recovery model for our backups.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Is there any way, through using &lt;code&gt;FileGroups&lt;/code&gt; or some other file-partitioning method, to &lt;strong&gt;exclude&lt;/strong&gt; indexes from the backups?&lt;/p&gt;&#xA;&#xA;&lt;p&gt;It would be nice if this could be extended to full-text catalogs, as well.&lt;/p&gt;&#xA;" OwnerUserId="3" LastEditorUserId="919" LastEditDate="2009-05-04T02:11:16.667" LastActivityDate="2009-05-10T15:22:39.707" Title="How to exclude indexes from backups in SQL Server 2008" Tags="&lt;sql-server&gt;&lt;backup&gt;&lt;sql-server-2008&gt;&lt;indexes&gt;" AnswerCount="3" CommentCount="0" FavoriteCount="3" />)
hreflist= [elt.getAttribute("Score") for elt in dom.getElementsByTagName('row')  if elt.getAttribute("Id")=="1"]
for href in hreflist:
    print(href)'''

from bs4 import BeautifulSoup
import json
import sys

count = 0
line_number = 0
a = 0
q = 0
fo_p = open("progress.log", "wb")
with open("Posts.xml") as questions:
    for que_line in questions:
		que_soup = BeautifulSoup(que_line)
		que_tag = que_soup.row		
		try:
			if que_tag.get('parentid'):
				a = a + 1
			else:
				if line_number>250182 and line_number<=300000:
					que_tag['domain']="serverfault.com"			
					ans_soup = BeautifulSoup(open("Posts.xml"))			
					answers = []
					i = 0
					q = q + 1
					for answer in ans_soup.find_all(parentid=que_tag['id']):						
						answers.append(answer.attrs)				
						i = i + 1				
					que_tag['answers'] = answers			
					#print que_tag.attrs
					#newDictionary=json.loads(str(que_tag))
					#
					print json.dumps(que_tag.attrs)
					print ","
		except:
			e = sys.exc_info()[0]
   			#write_to_page("<p>Error: %s</p>" % e )
   			fo = open("error.log", "ab")
			fo.write( "\n%s" % e)
			fo.write("\nQuestions: "+str(q)+"\tAnswers: "+str(a)+"\tLineNumber: "+str(line_number))
			# Close opend file
			fo.close()			
			print e
		line_number = line_number + 1
		#if count==1:
		#	break   
		#count = count + 1 		
		fo_p.write("\nQuestions: "+str(q)+"\tAnswers: "+str(a)+"\tLineNumber: "+str(line_number))
fo_p.close()			
print "\n\tQuestions: "+str(q)
print "\tAnswers: "+str(a)
print "\tTotal: "+str(line_number)
			
