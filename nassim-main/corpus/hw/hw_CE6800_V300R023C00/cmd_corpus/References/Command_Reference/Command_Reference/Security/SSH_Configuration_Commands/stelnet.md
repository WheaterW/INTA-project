stelnet
=======

stelnet

Function
--------



The **stelnet** command enables the system to log in to another device from the current device through STelnet.




Format
------

**stelnet ipv6** [ **-a** *source-ipv6-address* ] [ **-force-receive-pubkey** ] *host-ipv6-address* [ [ **public-net** | **-vpn-instance** *vpn-instance-name* ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] | [ *server-port* ] | [ **prefer\_kex** *prefer\_kex* ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ] \*

**stelnet -i** { *interface-name* | *interface-type* *interface-number* } [ **-force-receive-pubkey** ] *host-ip-address* [ *server-port* ] [ [ **prefer\_kex** *prefer\_kex* ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ] \*

**stelnet** [ **-a** *source-ip-address* ] [ **-force-receive-pubkey** ] *host-ip-address* [ *server-port* ] [ [ **prefer\_kex** *prefer\_kex* ] | [ **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* ] | [ **prefer\_ctos\_compress** **zlib** ] | [ **prefer\_stoc\_compress** **zlib** ] | [ **-vpn-instance** *vpn-instance-name* ] | [ **-ki** *interval* ] | [ **-kc** *count* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ipv6-address* | Specifies the source IPv6 address of STelnet. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **-a** *source-ip-address* | Specifies the source IP address of STelnet. | The value is in dotted decimal notation. |
| **-force-receive-pubkey** | Indicates that a server forcibly receives public key authentication. | - |
| *host-ipv6-address* | Specifies the IP address or host name of the remote system (IPv6-based STelnet server). | The value is a string of case-sensitive characters. It cannot contain spaces. |
| **public-net** | Specifies the public network where the SSH server resides.  If you have run the set net-manager vpn-instance command to configure the default VPN instance used for an NMS to manage devices and want to use SSH to access a public network server, you must specify this parameter. | - |
| **-vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **-oi** | Specifies the source interface for the IPv6 client. The IPv6 address configured in this interface view is the source IPv6 address of outbound packets. If no IPv6 address is configured for the source interface, the connection cannot be set up. | - |
| *interface-type* *interface-number* | Specifies the source interface for the client, including the type and number of the interface. | - |
| *server-port* | Specifies the port number of the SSH server. | The value is an integer ranging from 1 to 65535. The default port number is 22. |
| **prefer\_kex** *prefer\_kex* | Specifies the preferred algorithm for key exchange. | The options are as follows:   * dh\_group1\_sha1 * dh\_group\_exchange\_sha1 * sm2\_kep * dh-group-exchange-sha256 * ecdh-sha2-nistp256 * ecdh-sha2-nistp384 * ecdh-sha2-nistp521 * dh\_group14\_sha1 * dh\_group16\_sha512 * curve25519\_sha256 |
| **prefer\_ctos\_cipher** *prefer\_ctos\_cipher* | Specifies the preferred encryption algorithm for packets from the client to the server. | Encryption algorithms supported depend on the ssh client cipher command settings. |
| **prefer\_stoc\_cipher** *prefer\_stoc\_cipher* | Specifies the preferred encryption algorithm for packets from the server to the client. | Encryption algorithms supported depend on the ssh client cipher command settings. |
| **prefer\_ctos\_hmac** *prefer\_ctos\_hmac* | Specifies the preferred HMAC algorithm for packets from the client to the server. | The preferred HMAC algorithms supported depend on the HMAC algorithm type configured using the ssh client hmac command. |
| **prefer\_stoc\_hmac** *prefer\_stoc\_hmac* | Specifies the preferred HMAC algorithm for packets from the server to the client. | The preferred HMAC algorithms supported depend on the HMAC algorithm type configured using the ssh client hmac command. |
| **prefer\_ctos\_compress** | Specifies the preferred compression algorithm for packets from the server to the client. Only the ZLIB algorithm is supported. | - |
| **zlib** | Specifies the preferred compression algorithm is ZLIB. | - |
| **prefer\_stoc\_compress** | Specifies the preferred compression algorithm for packets from a client to the server. Only the ZLIB algorithm is supported. | - |
| **-ki** *interval* | Specifies an interval at which keepalive packets are sent if no data is received. | The value is an integer in the range of 1 to 3600, in seconds. |
| **-kc** *count* | Specifies the maximum number of times that a server does not respond to keepalive packets. | The value is an integer ranging from 1 to 30. |
| **identity-key** *identity-key-type* | Specifies the public key for server authentication. | Specifies the public key for server authentication, which depends on the type configured using the ssh client publickey command. |
| **user-identity-key** *user-key* | Specifies the public key for user authentication. | Specifies the public key for user authentication, which depends on the type configured using the ssh client publickey command. |
| **-i** | Specifies the egress interface corresponding to the link-local address or host name. | - |
| *host-ip-address* | Specifies the IP address or host name of the remote system (IPv4-based STelnet server). | The value is a string of 0 to 4294967295 case-sensitive characters, spaces not supported. |
| **ipv6** | Indicates login to another device from the current device through IPv6 STelnet. | - |



Views
-----

User view,System view


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

* Logins by using Telnet bring security risks because Telnet does not provide any secure authentication mechanism and data is transmitted by using TCP in plain text. Compared with Telnet, SSH guarantees secure file transfer on a traditional insecure network by authenticating clients and encrypting data in bidirectional mode. The SSH protocol supports STelnet. You can run this command to use STelnet to log in to another device from the current device.
* STelnet is a secure Telnet service. SSH users can use the STelnet service in the same way as the Telnet service.
* When the STelnet server or its connection to a client fails, the client must detect the fault in time and release the connection. To achieve this goal, before a client logs in to the server through STelnet, configure an interval at which keepalive packets are sent if no data is received and the maximum number of times that the server does not respond. If the client does not receive any data within the specified interval, it sends a keepalive packet to the server. If the maximum number of times that the server does not respond exceeds the specified value, the client tears down the connection.

**Prerequisites**



The VPN instance to be specified in this command has been configured.The STelnet service has been enabled on the SSH server using the **stelnet server enable** command.



**Precautions**

* If the SSH server monitors port number 22, you may not specify the port number for SSH login.
* A secure algorithm is required to ensure high security. The STelnet client and the gateway NE in a DCN plug-and-play scenario must support the AES128\_CTR, AES256\_CTR, AES192\_CTR, AES128\_GCM, or AES256\_GCM algorithm.
* You must run the **ssh client first-time enable** command on the STelnet client to enable first login for the SSH client.
* To ensure compatibility after an upgrade, the **stelnet** command can be run in the system view.


Example
-------

# Connect to the STelnet server at remote location with IPv6 address.
```
<HUAWEI> stelnet ipv6 2001:db8:1::1 1025 prefer_kex dh-group1 prefer-ctos-cipher aes128 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1 -vpn-instance vpn01
Trying 2001:db8:1::1...
Press CTRL+K to abort
Connected to 2001:db8:1::1...
Please input the username: client001
Enter password:
Info: The number of current VTY users on line is 1.
      The current login time is 2011-10-18 10:54:33.

```

# Connect to a remote IPv6 STelnet server.
```
<HUAWEI> stelnet ipv6 2001:db8:1::1 1025 prefer_kex dh-group1 prefer-ctos-cipher aes128 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1 -vpn-instance vpn01
Trying 2001:db8:1::1...
Press CTRL+K to abort
Connected to 2001:db8:1::1...
Please input the username: client001
Enter password:

```

# Connect to a remote STelnet server.
```
<HUAWEI> stelnet -a 10.1.1.1 10.164.39.120 prefer_kex dh-group1 prefer-ctos-cipher aes128 prefer-stoc-cipher aes128 prefer-ctos-hmac sha1 prefer-stoc-hmac sha1 -vpn-instance vpn01 -ki 2 -kc 4
Trying 10.164.39.120...
Press CTRL+K to abort
Connected to 10.164.39.120...
Please input the username: client001
Enter password:

```

# Connect to the STelnet server at remote location.
```
<HUAWEI> stelnet -a 10.1.1.1 10.164.39.120 prefer_kex dh_exchange_group prefer_ctos_cipher aes128 prefer_stoc_cipher aes128 prefer_ctos_hmac sha1 prefer_stoc_hmac sha1 -vpn-instance vpn01 -ki 2 -kc 4
Trying 10.164.39.120...
Press CTRL+K to abort
Connected to 10.164.39.120...
Please input the username: client001
Enter password:
Info: The number of current VTY users on line is 1.
      The current login time is 2015-10-18 10:52:13.

```