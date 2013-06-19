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
                if self.doc.se2!='Unverified':
		  resa=sql("select role from tabUserRole where parent='"+webnotes.session['user']+"'")
		  as1=resa and resa[0][0] or ''
		  if as1=='Operator':
		    self.doc.se2='Unverified'
		    self.doc.save()
		
	def get_d(self):
		res1=sql("select address,conatact_person,tel_no,cell_no,fax,email_id from tabCustomer where name='"+self.doc.name1+"'")
		
		self.doc.address=res1 and res1[0][0] or ''
		self.doc.cp=res1 and res1[0][1] or ''
		self.doc.tel_no=res1 and res1[0][2] or ''
		self.doc.cell=res1 and res1[0][3] or ''
		self.doc.fax=res1 and res1[0][4] or ''
		self.doc.e_id=res1 and res1[0][5] or ''
		ret={
			'address':res1 and res1[0][0] or '',
			'cp':res1 and res1[0][1] or '',
			'tel_no':res1 and res1[0][2] or '',
			'cell':res1 and res1[0][3] or '',    
			'fax':res1 and res1[0][4] or '',
			'e_id':res1 and res1[0][5] or ''
		}
		return ret
		

