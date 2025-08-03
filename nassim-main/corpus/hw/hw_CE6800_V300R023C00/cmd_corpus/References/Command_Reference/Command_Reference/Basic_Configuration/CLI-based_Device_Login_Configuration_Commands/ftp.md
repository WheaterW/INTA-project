ftp
===

ftp

Function
--------



The **ftp** command sets up a control connection with a remote FTP server using an IPv4 or IPv6 address and displays the FTP client view.




Format
------

**ftp** [ **-a** *source-ip-address* | **-i** { *interface-type* *interface-number* | *interface-name* } ] *host-ip* [ *port-number* ] [ **vpn-instance** *vpn-instance-name* | **public-net** ]

**ftp**

**ftp ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ [ **vpn-instance** *ipv6-vpn-instance-name* ] | **public-net** ] **-oi** { *interface-type* *interface-number* | *interface-name* } [ *port-number* ]

**ftp ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ [ **vpn-instance** *ipv6-vpn-instance-name* ] | **public-net** ] [ *port-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ip-address* | Specifies the IPv4 address of the FTP client.  The IP address must have been configured on the device. You are advised to configure an IP address for the loopback interface and use this IP address as the source IP address of the FTP connection.  On an IPv4 network, the source IP address specified in this command takes precedence over that specified in the ftp client source command. If you run the ftp client source command to specify a source IP address and then run this command to specify a source IP address, the source IP address specified in this command is used for communication.  The source IP address specified in the ftp client source command is valid for all FTP connections. The source IP address specified in this command is valid only for the current FTP connection. | The value is in dotted decimal notation. |
| **-i** *interface-name* | Specifies the source interface name for the FTP client. | - |
| *interface-type* | Specifies the source interface type for the FTP client. | - |
| *interface-number* | Specifies the source interface number for the FTP client. | - |
| *host-ip* | Specifies the IP address of the remote FTP server or the host with a specific name.  To view the mapping between the IPv4 address and host name, run the display dns dynamic-host or display ip host command. | The value is a string case-sensitive characters. It cannot contain spaces. |
| *port-number* | Specifies the listening port number of the FTP server.  By default, the listening port number of a Telnet server is 21. You can directly log in to the device without specifying the port number. Attackers may access the default listening port, consuming bandwidth, deteriorating server performance, and causing authorized users unable to access the server. You can run the ftp command to change the listening port number of the Telnet server. After that, attackers do not know the new listening port number, preventing attackers from accessing the listening port. | Port number is an integer that is 21 or ranges from 1025 to 65535. By default, the port number is 21. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the FTP server belongs.  Before specifying vpn-instance <vpn-instance-name>, ensure that a VPN instance has been configured. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **public-net** | Specifies the public network where the FTP server resides.  If you have run the set net-manager vpn-instance command to configure the default VPN instance used for an NMS to manage devices and want to use FTP to access a public network server, you must specify this parameter. | - |
| **ipv6** *host-ipv6-address* | Specifies the IPv6 address of the remote IPv6 FTP server or the host with a specific name. | The value is a string case-sensitive characters. It cannot contain spaces. |
| *source-ip6* | Specifies an IPv6 address for the FTP client.  An IP address that has been configured on the device is used as the IPv6 address. It is recommended that an IP address be configured on the loopback interface and then used as the source IP address of the FTP connection.  On an IPv6 network, the source IP address specified using the ftp command takes precedence over the source IP address specified using the ftp ipv6 client-source command. If the ftp command is run after a source IP address has been specified using the ftp ipv6 client-source command, the source IP address specified using the ftp command is used for communication.  The source IP address specified using the ftp ipv6 client-source command is available for all FTP connections; the source IP address specified using the ftp command is available only for the current FTP connection. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *ipv6-vpn-instance-name* | Specifies the name of an IPv6 VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **-oi** | Specifies the source interface for the IPv6 FTP client, including the type and number of the interface. The IPv6 address configured in this interface view is the source IPv6 address of the packet. If no IPv6 address is configured for the source interface, the FTP connection cannot be set up.  Setting the loopback interface as the source IPv6 address is recommended. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

An FTP client can access an FTP server after establishing a connection with the FTP server. The ftp command can be used to establish an FTP connection between the FTP client and FTP server.

**Prerequisites**

An FTP connection can establish if the following conditions are met:

* FTP server function on a device is enabled by executing the **ftp server enable** command on the FTP server to allow FTP users to log in.
* The FTP server and FTP client are routable.

**Configuration Impact**

After logging in to the FTP server from the FTP client, you can remotely manage files on the FTP server.

**Follow-up Procedure**

If the number of users allowed to log in to the FTP server reaches the maximum, new authorized users cannot log in to the FTP server. To ensure that new authorized users can successfully log in to the FTP server, users who have completed the FTP function need to disconnect the FTP connection in time. Perform any of the following steps in the FTP client view as required:

* Run the **bye** or **quit** command to terminate the connection with the FTP server and return to the user view.
* Run the **close** or **disconnect** command to terminate the connection with the FTP server and terminate the FTP session. The FTP client view is still displayed.

**Precautions**

* After executing the **FTP** command, the system prompts you to enter the user name and password for logging in to the FTP server. You can log in to the FTP server and enter the FTP client view only after the correct user name and password is entered.
* If no parameter is specified in the **FTP** command then the FTP view is displayed and the connection with the FTP server is not established.
* FTP lacks a secure authentication mode. If high security is required, SFTP is recommended.
* This command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.


Example
-------

# Establish FTP connection with the remote server.
```
<HUAWEI> ftp 1.1.1.1
Trying 1.1.1.1 ...
Press CTRL + K to abort
Connected to 1.1.1.1.
220 VRPV8 FTP service ready.
User(1.1.1.1:(none)):root
331 Password required for root.
Password:
230 Logged on

```

# Establish FTP connection with a remote server with source IP address.
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] ip address 1.1.1.1 24
[*HUAWEI-LoopBack0] quit
[*HUAWEI] ftp client source -a 1.1.1.1
[*HUAWEI] quit
<HUAWEI> ftp -a 1.1.1.1 1.1.1.1 10000
Trying 1.1.1.1 ...
Press CTRL + K to abort
Connected to 1.1.1.1.
220 VRPV8 FTP service ready.
User(1.1.1.1:(none)):root
331 Password required for root.
Password:
230 Logged on

```

# Establish FTP connection with a remote server with VPN.
```
<HUAWEI> ftp 2.2.2.2 vpn-instance vpn1
Trying 2.2.2.2 ...
Press CTRL + K to abort
Connected to 2.2.2.2.
220 (vsFTPd 2.3.2)
User(2.2.2.2:(none)):root
331 Please specify the password.
Password:
230 Logged on

```

# Set up the connection to the remote IPv6 FTP server of which the address is FE80::2E0:27FF:FE35:8342 (link-local address generated automatically by the interface of the remote IPv6 FTP server).
```
<HUAWEI> ftp ipv6 FE80::2E0:27FF:FE35:8342 -oi 100GE 1/0/1
Trying fe80::2e0:27ff:fe35:8342
Press CTRL+K to abort
Connected to FE80::2E0:27FF:FE35:8342.
220 FTP service ready.
User(FE80::2E0:27FF:FE35:8342:(none)):root
331 Password required for root.
Enter password:
230 Logged on

```