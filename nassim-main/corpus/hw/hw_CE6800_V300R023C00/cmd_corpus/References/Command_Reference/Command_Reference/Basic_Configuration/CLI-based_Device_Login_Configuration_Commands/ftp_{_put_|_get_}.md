ftp { put | get }
=================

ftp { put | get }

Function
--------



The **ftp put** command transfers file to remote FTP server.

The **ftp get** command downloads file from remote FTP server.




Format
------

**ftp put** [ **-a** *source-ip4* | **-i** { *interface-type* *interface-number* | *interface-name* } ] **host-ip** *ip4-address* [ **port** *portnumber* ] [ **vpn-instance** *ipv4-vpn-name* | **public-net** ] **username** *user-name* **sourcefile** *localfilename* [ **destination** *remotefilename* ]

**ftp put ipv6** [ **-a** *source-ip6* ] **host-ip** *ip6-address* [ [ **vpn-instance** *ipv6-vpn-name* ] | **public-net** ] [ **port** *portnumber* ] **username** *user-name* **sourcefile** *localfilename* [ **destination** *remotefilename* ]

**ftp get** [ **-a** *source-ip4* | **-i** { *interface-type* *interface-number* | *interface-name* } ] **host-ip** *ip4-address* [ **port** *portnumber* ] [ **vpn-instance** *ipv4-vpn-name* | **public-net** ] **username** *user-name* **sourcefile** *remotefilename* [ **destination** *localfilename* ]

**ftp get ipv6** [ **-a** *source-ip6* ] **host-ip** *ip6-address* [ [ **vpn-instance** *ipv6-vpn-name* ] | **public-net** ] [ **port** *portnumber* ] **username** *user-name* **sourcefile** *remotefilename* [ **destination** *localfilename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ip4* | Specifies a source IPv4 address. | The value is a string of 0 to 4294967295 case-sensitive characters, spaces not supported. |
| **-a** *source-ip6* | Specifies an IPv6 source address. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **-i** *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Interface type. | - |
| *interface-number* | Shows the number of interfaces. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **host-ip** | Host ip address. | - |
| *ip4-address* | IPv4 address. | The value is a string of 0 to 4294967295 case-sensitive characters, spaces not supported. |
| **port** *portnumber* | Port number. | The value is a string of 1 to 65535 case-sensitive characters, spaces not supported. |
| **vpn-instance** | Set VPN instance. | - |
| *ipv4-vpn-name* | The name of IPv4 VPN. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **public-net** | Connect in Public Network. | - |
| **username** *user-name* | Specifies a user name. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |
| **sourcefile** | Specify the source file. | - |
| *localfilename* | Specifies the local-file name. | The value is a string of 1 to 128 case-sensitive characters. It cannot contain spaces. |
| **destination** | Specify the destination file. | - |
| *remotefilename* | Remote file name. | The value is a string of 1 to 128 case-sensitive characters. It cannot contain spaces. |
| **ipv6** | IPv6. | - |
| *ip6-address* | IPv6 address. | The value is a string of case-sensitive characters. It cannot contain spaces. |
| *ipv6-vpn-name* | The name of IPv6 VPN. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command is used to put/get the file to/from the IPv4 and IPv6 servers. Users can specify the server parameters required for transfer in the command and the FTP client will connect to the server for the first time and then transfer the file.

**Precautions**

* FTP does not have a secure authentication mode, which poses security risks. SFTP is recommended for networks that have high security requirements.
* This command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.


Example
-------

# Transfer the file sourcefile to the server.
```
<HUAWEI> ftp get -a 10.1.1.10 host-ip 10.1.1.1 username abc sourcefile sample.txt
100% [***********]

```

# Transfer the file to the IPv6 server.
```
<HUAWEI> ftp put ipv6 host-ip 2001:db8:2::2 username root sourcefile 1mb.txt

```