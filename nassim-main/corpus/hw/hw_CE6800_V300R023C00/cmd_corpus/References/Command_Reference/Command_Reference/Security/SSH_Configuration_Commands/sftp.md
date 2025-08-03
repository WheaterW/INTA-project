sftp
====

sftp

Function
--------



The **sftp** command enables the system to log in to another device from the current device through SFTP.




Format
------

**sftp** [ **-a** *source-ip-address* ] [ **-force-receive-pubkey** ] *host-ip-address* [ *port-number* ] [ [ **prefer\_kex** { *prefer\_kex* } ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ] \*

**sftp ipv6** [ **-force-receive-pubkey** ] [ **-a** *source-ipv6-address* ] *host-ipv6-address* [ [ [ **-vpn-instance** *vpn-instance-name* ] | **public-net** ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] | [ *port-number* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ] \*

**sftp -i** { *interface-name* | *interface-type* *interface-number* } [ **-force-receive-pubkey** ] *host-ip-address* [ *port-number* ] [ [ **prefer\_kex** { *prefer\_kex* } ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ipv6-address* | Specifies the SFTP source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **-a** *source-ip-address* | Specifies the SFTP source IP address. | The value is in dotted decimal notation. |
| **-force-receive-pubkey** | Indicates that a server forcibly receives public key authentication. | - |
| *host-ip-address* | Specifies the IP address of remote system. | The value is in dotted decimal notation. |
| *port-number* | Specifies the port number of the SSH server. | The value is an integer ranging from 1 to 65535. The default value is 22, which is a standard SFTP port number. |
| **prefer\_kex** *prefer\_kex* | Specifies the preferred algorithm for key exchange. | The preferred key exchange algorithms supported depend on the algorithm type configured using the ssh client key-exchange command. |
| **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* | Specifies the preferred encryption algorithm for packets from the client to the server. | Encryption algorithms supported depend on the ssh client cipher command settings. |
| **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* | Specifies the preferred encryption algorithm for packets from the server to the client. | Encryption algorithms supported depend on the ssh client cipher command settings. |
| **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* | Specifies the preferred HMAC algorithm for packets from the client to the server. | The preferred HMAC algorithms supported depend on the HMAC algorithm type configured using the ssh client hmac command. |
| **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* | Specifies the preferred HMAC algorithm for packets from the server to the client. | The preferred HMAC algorithms supported depend on the HMAC algorithm type configured using the ssh client hmac command. |
| **prefer\_ctos\_compress** | Specifies the preferred compression algorithm for packets from the server to the client. Currently, it can only be zlib. | The default algorithm is none. |
| **zlib** | Specifies the preferred compression algorithm for packets is zlib. | - |
| **prefer\_stoc\_compress** | Specifies the preferred compression algorithm for packets from a client to the server. Currently, it can only be zlib. | - |
| **public-net** | Indicates that the SFTP server resides on a public network. | - |
| **-vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **-ki** *interval* | Specifies an interval at which keepalive packets are sent if no data is received. | The value is an integer ranging from 1 to 3600, in seconds. |
| **-kc** *count* | Specifies the maximum number of times that a server does not respond to keepalive packets. | The value is an integer ranging from 1 to 30. |
| **identity-key** *identity-key-type* | Specifies the public key for server authentication. | Currently, RSA\_SHA2\_512, RSA\_SHA2\_256, RSA, DSA, and ECC are supported. The default public key algorithms are RSA\_SHA2\_512 and RSA\_SHA2\_256.  To ensure high security, do not use the RSA algorithm whose length is less than 3072 bits. Use the more secure RSA SHA2-512 or RSA SHA2-256 authentication algorithm. |
| **user-identity-key** *user-key* | Specifies the public key for user authentication. | Currently, RSA\_SHA2\_512, RSA\_SHA2\_256, RSA, DSA, and ECC are supported. The default public key algorithms are RSA\_SHA2\_512 and RSA\_SHA2\_256.  To ensure high security, do not use the RSA algorithm whose length is less than 3072 bits. Use the more secure RSA SHA2-512 or RSA SHA2-256 authentication algorithm. |
| **ipv6** | Specifies the IPv6 SFTP. | - |
| *host-ipv6-address* | Specifies the IPv6 address of remote system. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **-oi** | Specifies the source interface for the IPv6 client, including the type and number of the interface. If no IPv6 address is configured for the source interface, the connection cannot be set up. | - |
| *interface-type* *interface-number* | Specifies the source interface for the client, including the type and number of the interface. | - |
| **-i** *interface-name* | Specifies the name of the egress interface to the remote SFTP server. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

SFTP is short for SSH FTP, which is a secure FTP protocol. SFTP is established over SSH and enables remote users to securely log in to a device for file management and transfer. This ensures data transmission security. In addition, the device provides the SFTP client function so that you can log in to a remote SSH server from the device to securely transfer files.When the SFTP server or its connection to a client fails, the client must detect the fault in time and release the connection. To achieve this goal, before a client logs in to the server through SFTP, configure an interval at which keepalive packets are sent if no data is received and the maximum number of times that the server does not respond. If the client does not receive any data within the specified interval, it sends a keepalive packet to the server. If the maximum number of times that the server does not respond exceeds the specified value, the client tears down the connection.

**Prerequisites**

The VPN instance to be specified in this command has been created using the **ip vpn-instance** command.The SFTP service has been enabled on the SSH server using the **sftp server enable** command.

**Precautions**

* If the SSH server monitors port number 22, you may not specify the port number for SSH login.
* If command execution fails due to ACLs on the SFTP client or the TCP connection fails, the system prompts an error message indicating that the connection to the server fails.
* If no source IP address or source interface is specified, the system uses the source IP address or source interface specified in the **sftp client-source** command.
* If a source IP address or source interface is specified, the system does not use the source IP address or source interface specified in the **sftp client-source** command.
* If a source IP address has been specified and VPN instance name is not specified, the system uses the global VPN if any and the public VPN when no global VPN is available.

Example
-------

# Connect to a remote SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance ssh
[*HUAWEI-vpn-instance-ssh] quit
[*HUAWEI] sftp -a 10.1.1.1 10.2.2.2 1025 -vpn-instance ssh
Trying 10.2.2.2...
Press CTRL+K to abort
Connected to 10.2.2.2...
Please input the username: client001
Enter password:

```

# Connect to a remote IPv6 SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] sftp ipv6 2001:db8:1::1 1025
Trying 2001:db8:1::1...
Press CTRL+K to abort
Connected to 2001:db8:1::1...
Please input the username: client001
Enter password:

```