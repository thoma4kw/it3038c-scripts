function getIP{
		(get-netipaddress).ipv4address | Select-String "192*"
}

$IP = getIP
$User = $env:Username
$ver = $host.version
$LEAD = $(hostname)
$DATE = $(date)

$BODY = "This machine's IP is $IP. User is $User. Hostname is $LEAD.
Powershell $ver. Today's Date is $DATE."