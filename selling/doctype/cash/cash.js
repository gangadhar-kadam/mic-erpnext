

cur_frm.cscript.refresh = function(doc, cdt, cdn) {
	
	//cur_frm.cscript.dt(doc, cdt, cdn);
}


cur_frm.cscript.onload = function(doc, dt, dn) {
	//alert(doc.br);
        if(!doc.dt) {
                //alert("!doc.dt");
		set_field_options('br', '');
		//return;
	}
	wn.call({
		method: 'selling.doctype.cash.cash.get_fields_label',
		args: { doctype: doc.dt,fieldname: doc.doct},
		callback: function(r) {
			alert(r.message);
			var insert_after_val = null;
			/*doc = locals[doc.doctype][doc.name];
			
			if(doc.su1) {
				
			}*/
			insert_after_val = doc.br;
			set_field_options('br', r.message, insert_after_val);
		}
	});
}

