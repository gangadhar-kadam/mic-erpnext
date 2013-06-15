// ERPNext - web based ERP (http://erpnext.com)
// Copyright (C) 2012 Web Notes Technologies Pvt Ltd
// 
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

/* toolbar settings */

wn.provide('erpnext.toolbar');
erpnext.toolbar.setup = function() {
	// modules 
	erpnext.toolbar.add_modules();
	
	// profile
	$('#toolbar-user').append('<li><a href="#Form/Profile/'+user+'">'
		+wn._("My Settings")+'...</a></li>');

	$('.navbar .pull-right').append('\
		<li><a href="#!messages" title="'+wn._('Unread Messages')
			+'"><span class="navbar-new-comments"></span></a></li>');
  
   var currentdate = new Date(); 
   var weekday=new Array(7);
   var mont=new Array(12);
   weekday[0]="Sunday";
   weekday[1]="Monday";
   weekday[2]="Tuesday";
   weekday[3]="Wednesday";
   weekday[4]="Thursday";
   weekday[5]="Friday";
   weekday[6]="Saturday";
   mont[1]="Jan";
   mont[2]="Feb";
   mont[3]="Mar";
   mont[4]="Apr";
   mont[5]="May";
   mont[6]="Jun";
   mont[7]="Jul";
   mont[8]="Aug";
   mont[9]="Sep";
   mont[10]="Oct";
   mont[11]="Nov";		
   mont[12]="Dec";
   var datetime = "<h style='font-size:19px'>"+currentdate.getDate()+"</h>" + "  "+  mont[(parseInt(currentdate.getMonth())    + 1)]
   + "  " + currentdate.getFullYear() +"<br>"+weekday[currentdate.getDay()]+" , "   
   + currentdate.getHours() + ":"  
   + currentdate.getMinutes() + ":" + currentdate.getSeconds();       
    s=datetime;		
        $('.navbar .pull-right').append('<li><h id="a1" style="color:white;margin-top:35px;font-size:12px"><span>\
                               '+s+'</span></h></li>');
  
	//var myvar=setInterval(function(){calendr()},1000);	
	// help
	$('.navbar .pull-right').prepend('<li class="dropdown">\
		<a class="dropdown-toggle" data-toggle="dropdown" href="#" \
			onclick="return false;">'+wn._('Help')+'<b class="caret"></b></a>\
		<ul class="dropdown-menu" id="toolbar-help">\
		</ul></li>')

	$('#toolbar-help').append('<li><a href="https://erpnext.com/manual" target="_blank">'
		+wn._('Documentation')+'</a></li>')

	$('#toolbar-help').append('<li><a href="http://groups.google.com/group/erpnext-user-forum" target="_blank">'
		+wn._('Forum')+'</a></li>')

	$('#toolbar-help').append('<li><a href="http://www.providesupport.com?messenger=iwebnotes" target="_blank">\
		'+wn._('Live Chat')+'</a></li>')

	erpnext.toolbar.set_new_comments();
}

erpnext.toolbar.add_modules = function() {
	$('<li class="dropdown">\
		<a class="dropdown-toggle" data-toggle="dropdown" href="#"\
			title="'+wn._("Modules")+'"\
			onclick="return false;"><i class="icon-th"></i></a>\
		<ul class="dropdown-menu modules">\
		</ul>\
		</li>').prependTo('.navbar .nav:first');
	
	var modules_list = wn.user.get_desktop_items().sort();
	
	var _get_list_item = function(m) {
		args = {
			module: m,
			module_page: wn.modules[m].link,
			module_label: wn._(wn.modules[m].label || m),
			icon: wn.modules[m].icon
		}
		
		return repl('<li><a href="#!%(module_page)s" \
			data-module="%(module)s"><i class="%(icon)s" style="display: inline-block; \
				width: 21px; margin-top: -2px; margin-left: -7px;"></i>\
			%(module_label)s</a></li>', args);
	}

	// add to dropdown
	$.each(modules_list,function(i, m) {
		if(m!='Setup') {
			$('.navbar .modules').append(_get_list_item(m));			
		}
	})
	
	// setup for system manager
	if(user_roles.indexOf("System Manager")!=-1) {
		$('.navbar .modules').append('<li class="divider">' + _get_list_item("Setup"));
	}
	
}

erpnext.toolbar.set_new_comments = function(new_comments) {
	var navbar_nc = $('.navbar-new-comments');
	if(cint(new_comments)) {
		navbar_nc.addClass('navbar-new-comments-true')
		navbar_nc.text(new_comments);
	} else {
		navbar_nc.removeClass('navbar-new-comments-true');
		navbar_nc.text(0);
	}
}
