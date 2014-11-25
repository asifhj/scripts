#!/usr/bin/tclsh 
#!/usr/bin/expect

set timeout 1
spawn -noecho telnet 10.75.24.1
expect_after eof { exit 0 }

set timeout 60
expect "Password: "
send "cisco\r"
expect "*>"

send "en\r"
expect "Password: "
send "wipro@123\r"
expect "*#"

set i 1
while { $i>0 } {
	#set value [expr floor( rand() * 600) + 1]
	#sleep 2
	#send "$value\r"
	#expect "$value: command not found\r"
	send "config t\r"
	expect "*(config)# "	

	foreach a [list "clear snmp" "logging on" "logging timestamp" "logging history informational" "logging host 10.75.24.3" "logging trap 7" "logging trap debugging" "aaa authentication enable console" "aaa authentication (serial|ssh|enable|telnet|http|secure-http-client) console \S LOCAL" "aaa authentication (serial|ssh|enable|telnet|http|secure-http-client) console LOCAL" "aaa authentication (ssh|enable|telnet|http|secure-http-client) console LOCAL" "aaa-server \S+ host \w+ \S+ timeout 10" "aaa-server \w+ host \w+ \w+ timeout" "aaa-server \w+ host \w+ \w+ timeout" "aaa authorization" "aaa authorization" "aaa authorization" "aaa accounting" "aaa accounting" "aaa accounting" "passwd wipro@123" "password cisco" "no http 10.75.24.32" "no telnet 10.75.24.32" "http 10.75.24.32" "telnet 10.75.24.32" "console timeout 5" "no ssh 10.75.24.31" "ssh 10.75.24.31" "clear banner" "banner exec Exec started be careful with what changes you attempt to make." "banner login Welcome to Fire on wall" "banner motd Have a pleasant Tech day!" "banner ASDM You never know who is watching you" "username firewall password firewall" "enable password wipro@123 encrypted" "snmp-server community test123" "snmp-server host 10.75.24.3" "snmp-server enable traps" "snmp-server host 10.10.1.2 trap community test123" "snmp-server host 10.75.24.5 trap " "snmp-server host 10.75.24.3 community abc123" "snmp-server community private" "snmp-server community private" "snmp-server group qwaszx v3 priv" "snmp-server user abc v3 encrypted abc123" "clock timezone UTC 0" "clock timezone IST 5 30" "clock timezone GMT 5 30" "clock summer-time GMT recurring" "clock summer-time GMT date 10 Oct 2013 10:50 10 Oct 2013 10:50" "clock summer-time GMT recurring 100 1 2013 10:50 10 Oct 2013 10:50" "aaa authentication ssh console cisco LOCAL" "aaa authentication ssh console enable_15 LOCAL" "clear username samm" "clear username firewall" "username samm password goldddddd encrypted privilege 14" "ssh timeout 5" "aaa local authentication attempts max-fail 5" "ssh version 2" "dhcpd domain wipro.com" "http server enable" "logging console 2" "logging console 2" "logging on" "logging facility 23" "logging facility 22" "logging history 6" "logging history informational" "logging host 10.75.24.3" "logging trap 7" "logging trap debugging" "logging timestamp" "flow-export destination" "ntp server 10.75.24.3 key 1 source intf5 prefer" "ntp server 10.75.24.3 key 1 source intf4 prefer" "ntp authenticate" "ntp trusted-key 1" "ntp authentication-key 1 md5 12qwaszx" "ntp server 10.75.24.3 key 1" "timeout conn 00:10:00" "timeout xlate 00:05:20" "ip audit attack action alarm drop" "clear object-group" "object-group service 1 tcp" "exit" "object-group protocol 2" "exit" "object-group network 3" "exit" "show object-group" "clear object-group" "fragment chain 1 outside" "inspect ftp" "ip verify reverse-path interface \w+" "authentication mode eigrp \S+ md5" "console timeout 45" "ssh timeout 34" "aaa local authentication attempts max-fail 10" "logging console 2" "logging console 7" "logging facility 23" "logging facility 22" "logging history 6" "logging history informational" "logging trap 7" "logging trap debugging" "logging console" "no telnet 10.75.24.31" "no telnet 10.75.24.41" "no telnet 10.75.24.51" "telnet 10.75.24.31" "telnet 10.75.24.41" "telnet 10.75.24.51" "console timeout 5" "ssh timeout 10" "aaa local authentication attempts max-fail 5" "ssh version 2" "logging console 2" "logging facility 22" "logging history 6" "no ntp authenticate" "no ntp trusted-key 1" "no ntp server 10.75.24.3" "no ntp authentication-key 1"] {
    set value [expr floor( rand() * 0) + 1]
	sleep $value
	send "$a\n"
	expect "*#"
	}

	send "exit\r"
	expect "*#"
}

send "logout\r"
expect "(.*)"
expect eof

