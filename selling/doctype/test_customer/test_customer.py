# For license information, please see license.txt

from __future__ import unicode_literals
import webnotes
from webnotes.utils import cint, cstr
msgprint = webnotes.msgprint
sql = webnotes.conn.sql

class DocType:
	def __init__(self, d, dl):
		self.doc, self.doclist = d, dl

        def on_update(self):
                if self.doc.ll2!='Unverified':
		  resa=sql("select role from tabUserRole where parent='"+webnotes.session['user']+"'")
		  as1=resa and resa[0][0] or ''
		  if as1=='Operator':
		    self.doc.ll2='Unverified'
		    self.doc.save()


	def get_detail(self):
		res1=sql("select permlevel from `tabDocField` where fieldname='ad1'")
		s=res1 and res1[0][0] or ''
		msgprint(res1[0][0])
		if (s==1):
		  res2=sql("select permlevel from `tabDocField` where fieldname='ad2'")
		  s1=res2 and res2[0][0] or ''
		  if (s1==1):
		    res3=sql("select permlevel from `tabDocField` where fieldname='ad3'")
		    s2=res3 and res3[0][0] or ''
		    if (s2==1):
		      return "hi"
		    else:
		      a1=sql("update `tabDocField` set permlevel=1 where parent='Test Customer' and fieldname='ad3'")
		  else:
		    a2=sql("update `tabDocField` set permlevel=1 where parent='Test Customer' and fieldname='ad2'")		
		else:
		  a3=sql("update `tabDocField` set permlevel=1 where parent='Test Customer' and fieldname='ad1'")

	def get_detail1(self):
		b1=sql("update `tabDocField` set permlevel=3 where parent='Test Customer' and fieldname='ad1'")
		b2=sql("update `tabDocField` set permlevel=4 where parent='Test Customer' and fieldname='ad2'")
		b3=sql("update `tabDocField` set permlevel=5 where parent='Test Customer' and fieldname='ad3'")
		self.doc.save()

	def get_detail2(self):
		c1=sql("select ad1,ad2,ad3 from `tabTest Customer` where name='"+self.doc.name+"'")
		c2=c1 and c1[0][0] or ''
		c3=c1 and c1[0][1] or ''
		c4=c1 and c1[0][2] or ''
		if(c2!='None'):
		  k1=sql("update `tabDocField` set permlevel=1 where parent='Test Customer' and fieldname='ad1'")
		if(c3!='None'):
		  k2=sql("update `tabDocField` set permlevel=1 where parent='Test Customer' and fieldname='ad2'")
@webnotes.whitelist()
def get_fields_label(dt=None, form=1):
		fieldname = webnotes.form_dict.get('fieldname')
		w1=sql("select sub from `tabData Table` where mast='"+fieldname+"'")
		s1=[]
		s=1
		d1=''
		for d in w1:
		  d1=d[0]	
		  s1.append(d1)
		#msgprint(s1)
		k=cstr(s1).replace("u'","")
		k1=cstr(k).replace("'","")
		k2=cstr(k1).replace("[","")
		k3=cstr(k2).replace("]","")
		a=cstr(k3).replace(',','\n')
		#msgprint(k3)
		return cstr("\n"+cstr(a))

