

cur_frm.cscript.refresh = function(doc, cdt, cdn) {
	
	//cur_frm.cscript.dt(doc, cdt, cdn);
}


cur_frm.cscript.doct = function(doc, dt, dn) {
	if(!doc.dt) {
		set_field_options('su1', '');
		//return;
	}
	wn.call({
		method: 'selling.doctype.test_customer.test_customer.get_fields_label',
		args: { doctype: doc.dt,fieldname: doc.doct},
		callback: function(r) {
			//alert(r.message);
			var insert_after_val = null;
			/*doc = locals[doc.doctype][doc.name];
			
			if(doc.su1) {
				
			}*/
			insert_after_val = doc.su1;
			set_field_options('su1', r.message, insert_after_val);
		}
	});
}
cur_frm.cscript.su1=function(doc,cdt,cdn)
{
	msgprint(doc.su1);
}
