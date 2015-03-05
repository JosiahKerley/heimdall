#import nginxparser as nginx

settings = {
	"nginxroot":"/etc/nginx",
	"nginxconf":"/etc/nginx/conf.d",
}

backends = [
	{
		"name":None,
		"url":None,
		"enable":False,
		"whitelist":[None],
		"blacklist":[None],
	},
]


server = {
	"httphost":"$http_host",
	"port":"80",
	"ssl":"",
	"resolver":"127.0.0.1",
	"location":"/",
	"scheme":"$scheme",
	"host":"$host",
	"uri":"$request_uri",
	"auth":'Restricted',
	"authfile":'%s/.htpasswd'%(settings['nginxroot']),
}



configtemplate = '''
server {
 resolver <[resolver]>;
 access_log off;
 listen  [::]:<[port]> <[ssl]>;
 location <[location]> {
   auth_basic '<[auth]>';
   auth_basic_user_file '<[authfile]>';
   proxy_pass <[scheme]>://<[host]><[uri]>;
   proxy_set_header Host <[httphost]>;
   proxy_buffers 256 4k;
   proxy_max_temp_file_size 0k;
 }
}'''




for key in server: configtemplate = configtemplate.replace('<[%s]>'%(key),server[key])






