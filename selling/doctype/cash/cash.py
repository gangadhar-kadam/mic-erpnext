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
		
@webnotes.whitelist()
def get_fields_label(dt=None, form=1):
                #if(self.doc.name):
                # return self.doc.br
                res=webnotes.conn.convert_to_listssql("select name from tabCustomer where category='Branch' or category='Representative'"))
                s1=[]
                msgprint(w1)
                i=0
                d1=''
                for name in w1:
                  s1.append(res[i])
                  i=i+1
                msgprint(s1)
                return s1
                k=cstr(s1).replace("u'","")
                k1=cstr(k).replace("'","")
                k2=cstr(k1).replace("[","")
                k3=cstr(k2).replace("]","")
                #a=cstr(k3).replace(',','\n')
		bw=cstr(k3).replace('  ','')
                c=cstr(bw).replace('(','')
                b=cstr(c).replace('\n','')
                l=cstr(b).replace(')','')
                d=cstr(l).replace(',, ','\n')
                e=cstr(d).replace(',','')
                f=cstr(e).replace('UMESH ANAND','UMESH (ANAND)')
                g=cstr(f).replace('B.M. MALLAPPA','\nB.M. MALLAPPA')                
                #msgprint(g)
                return g

