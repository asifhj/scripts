#!/usr/bin/tclsh 
#!/usr/bin/expect

set timeout 1
set cmd {uname -a}

spawn -noecho telnet 127.0.0.1
expect_after eof { exit 0 }

set timeout 60

expect "login:"
send "abacus\r"
expect "Password: "
send "12qwaszx\r"
expect "$"

foreach a [list "ls -l" "ps" "df" "free"] {
    #sleep 3
	send "$a\n"
	expect "$"
}



send "$cmd\r"
expect "$"

send "ls\r"
expect "$"


set i 1
while { $i>0 } {
	set value [expr floor( rand() * 600) + 1]
	sleep 2
	send "$value\r"
	expect "$value: command not found\r"
}
send "logout\r"
expect "(.*)"
expect eof
