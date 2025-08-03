sftp client-transfile
=====================

sftp client-transfile

Function
--------



The **sftp client-transfile** command uploads files from an SFTP client to an SFTP server or downloads files from an SFTP server to an SFTP client.




Format
------

**sftp client-transfile get ipv6** [ **-a** *source-ipv6-address* ] **host-ip** *host-ipv6* [ **-oi** { *interface-type* *interface-number* | *interface-name* } ] [ *port* ] [ [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **identity-key** *identity-key-type* ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **-ki** *interval* ] | [ **-kc** *count* ] ] \* **username** *user-name* **password** *password* **sourcefile** *destination* [ **destination** *source-file* ]

**sftp client-transfile get** [ **-a** *source-address* | **-i** { *interface-type* *interface-number* | *interface-name* } ] **host-ip** *host-ipv4* [ *port* ] [ [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **identity-key** *identity-key-type* ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **-ki** *interval* ] | [ **-kc** *count* ] ] \* **username** *user-name* **password** *password* **sourcefile** *destination* [ **destination** *source-file* ]

**sftp client-transfile put ipv6** [ **-a** *source-ipv6-address* ] **host-ip** *host-ipv6* [ **-oi** { *interface-type* *interface-number* | *interface-name* } ] [ *port* ] [ [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **identity-key** *identity-key-type* ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **-ki** *interval* ] | [ **-kc** *count* ] ] \* **username** *user-name* **password** *password* **sourcefile** *source-file* [ **destination** *destination* ]

**sftp client-transfile put** [ **-a** *source-address* | **-i** { *interface-type* *interface-number* | *interface-name* } ] **host-ip** *host-ipv4* [ *port* ] [ [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **identity-key** *identity-key-type* ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **-ki** *interval* ] | [ **-kc** *count* ] ] \* **username** *user-name* **password** *password* **sourcefile** *source-file* [ **destination** *destination* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-address* | Specifies the source address of an SFTP client. | The value is in dotted decimal notation. |
| **-a** *source-ipv6-address* | Specifies the source ipv6 address of an SFTP client. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **host-ip** *host-ipv4* | Specifies the IPv4 address or host name of an SFTP server. | The value is a string of case-sensitive characters, spaces not supported. |
| **host-ip** *host-ipv6* | Specifies the IPv6 address or host name of an SFTP server. | The value is a string of case-sensitive characters without spaces. |
| **-oi** | Specifies the source IPv6 interface of an SFTP client. | - |
| *interface-type* *interface-number* | Specifies the source IPv6 interface of an SFTP client.  If host-ipv6 is a link-local IPv6 address, you must specify the interface name corresponding to the link-local address. If host-ipv6 is not a link-local IPv6 address, no interface name is required. | - |
| *port* | Specifies the monitoring port number of an SSH server.  You can log in to the server from the SFTP client without the need of specifying the monitoring port number only when the monitoring port number of the server is 22. Otherwise, the monitoring port number must be specified. | The value is an integer ranging from 1 to 65535. The default value is 22, which is a standard SFTP port number. |
| **public-net** | Indicates that the SFTP server resides on a public network. | - |
| **-vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. This means that the SFTP server resides on a private network. | The value is a string of 1 to 31 case-sensitive characters without spaces.  If spaces are used, the string must start and end with double quotation marks ("). |
| **prefer\_kex** *prefer\_kex* | Specifies the preferred algorithm for key exchange. | Preferred algorithms for key exchange supported depend on the ssh client key-exchange command settings. |
| **identity-key** *identity-key-type* | Specifies a public key algorithm for the server authentication. | Currently, RSA\_SHA2\_512, RSA\_SHA2\_256, RSA, DSA, and ECC are supported. The default public key algorithms are RSA\_SHA2\_512 and RSA\_SHA2\_256.  To ensure high security, do not use the RSA algorithm whose length is less than 3072 bits. Use the more secure RSA SHA2-512 or RSA SHA2-256 authentication algorithm. |
| **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* | Specifies the preferred encryption algorithm for packets from the client to the server. | Encryption algorithms supported depend on the ssh client cipher command settings. |
| **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* | Specifies the preferred encryption algorithm for packets from the server to the client. | Encryption algorithms supported depend on the ssh client cipher command settings. |
| **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* | Specifies the preferred HMAC algorithm for packets from the client to the server. | The preferred HMAC algorithms supported depend on the HMAC algorithm type configured using the ssh client hmac command. |
| **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* | Specifies the preferred HMAC algorithm for packets from the server to the client. | The preferred HMAC algorithms supported depend on the HMAC algorithm type configured using the ssh client hmac command. |
| **-ki** *interval* | Specifies an interval at which keepalive packets are sent if no data is received. | The value is an integer ranging from 1 to 3600, in seconds. The default value is 60. |
| **-kc** *count* | Specifies the maximum number of times that a server does not respond to keepalive packets. | The value is an integer ranging from 1 to 30. The default value is 5. |
| **username** *user-name* | Specifies the user name for an SFTP connection. | The value is a string of 1 to 255 case-sensitive characters without spaces.  If spaces are used, the string must start and end with double quotation marks ("). |
| **password** *password* | Specifies the password for an SFTP connection. | The value is a string of 1 to 128 case-sensitive characters without spaces.  If spaces are used, the string must start and end with double quotation marks ("). |
| **sourcefile** *source-file* | Specifies the absolute path of the source file to be uploaded or downloaded. | The value is a string of 1 to 256 case-insensitive characters without spaces. The file name is a string of 1 to 128 characters. |
| **destination** *destination* | Specifies the absolute path of the destination file to be uploaded or downloaded.  If destination is not specified, the destination file name is the same as the source file name. | The value is a string of 1 to 256 case-insensitive characters without spaces. The file name is a string of 1 to 128. |
| **get** | Downloads files from an SFTP server. | - |
| **-i** | Specifies the source interface of an SFTP client. | - |
| **put** | Uploads files to an SFTP server. | - |
| **ipv6** | Specifies an IPv6 SFTP server. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To upload files from an SFTP client to an SFTP server or download files from an SFTP server to an SFTP client, run the **sftp client-transfile** command. This command can be run only on an SFTP client.Before you run the **sftp** command to transfer files, enter the user name and password. You can transfer files only when the authentication succeeds. The **sftp client-transfile** command supports one-click file transfer, so that a file can be transferred after you run the command.

**Prerequisites**

Before you run the **sftp client-transfile** command to connect to an SFTP server, ensure that the following requirements are met:

* The route between the SSH client and server is reachable. If the server does not use a standard port number, the port number configured on the server must be obtained.
* The IP address of the SSH server and the information about the SSH user used for login are obtained.
* The SFTP service is enabled on the server, the service types configured for the server contain SFTP, and password authentication is configured for the SSH user.

**Configuration Impact**

After a connection is established between an SFTP client and an SFTP server, they start to communicate.

**Precautions**

* If command execution fails due to ACL configuration on the SFTP client or the TCP connection fails, the system displays an error message indicating that the connection to the server fails.
* When the connection between the server and the client fails, the client must detect the fault in time and proactively tears down the connection. To achieve this, before the client logs in to the server through SFTP, configure an interval at which keepalive packets are sent if no data is received and the maximum number of times that the server does not respond. If the client does not receive any data within the specified interval, it sends a keepalive packet to the server. If the maximum number of times that the server does not respond exceeds the specified value, the client proactively tears down the connection.
* If a source interface is specified using the -i interface-type interface-number parameter, the -vpn-instance vpn-instance-name parameter cannot be set then.
* This command is used to connect to the server and transfer files. Password authentication is required for login.

Example
-------

# Log in to the SFTP server whose IPv6 address is 2001:db8::1 in ECC authentication mode and upload the sample.txt file to the SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] ssh client publickey ecc
Warning: Insecure public key algorithms (ecc) are enabled. Disabling them is recommended.
[*HUAWEI] sftp client-transfile put ipv6 host-ip 2001:db8::1 identity-key ecc username huawei password YsHsjx_202206 sourcefile sample.txt

```

# Log in to the SFTP server at 10.1.1.4 in ECC authentication mode and download the source file sample.txt to the SFTP client.
```
<HUAWEI> system-view
[~HUAWEI] ssh client publickey ecc
Warning: Insecure public key algorithms (ecc) are enabled. Disabling them is recommended.
[*HUAWEI] sftp client-transfile get host-ip 10.1.1.4 identity-key ecc username huawei password YsHsjx_202206 sourcefile sample.txt

```

# Download the source file sample.txt from the server at 10.1.1.3 to the SFTP client. Set the interval at which keepalive packets are sent if no data is received and the maximum number of times that the server does not respond to 10 and 4, respectively.
```
<HUAWEI> system-view
[~HUAWEI] sftp client-transfile get host-ip 10.1.1.3 -ki 10 -kc 4 username huawei password YsHsjx_202206 sourcefile sample.txt

```

# Download the source file sample.txt from the server at 10.1.1.2 to the SFTP client.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance ssh
[*HUAWEI-vpn-instance-ssh] ipv4-family
[*HUAWEI-vpn-instance-ssh-af-ipv4] quit
[*HUAWEI-vpn-instance-ssh] quit
[*HUAWEI] sftp client-transfile get host-ip 10.1.1.2 1025 -vpn-instance ssh username huawei password YsHsjx_202206 sourcefile sample.txt

```