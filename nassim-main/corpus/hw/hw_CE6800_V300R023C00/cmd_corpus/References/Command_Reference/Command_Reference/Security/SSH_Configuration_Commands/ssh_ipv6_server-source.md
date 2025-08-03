ssh ipv6 server-source
======================

ssh ipv6 server-source

Function
--------



The **ssh ipv6 server-source** command specifies a source IPv6 address for an SSH server.

The **undo ssh ipv6 server-source** command cancels the specified source IPv6 address for an SSH server.



By default, no source interface or source IPv6 address is specified for an SSH server.


Format
------

**ssh ipv6 server-source -a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ]

**ssh ipv6 server-source all-interface**

**undo ssh ipv6 server-source -a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ]

**undo ssh ipv6 server-source all-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-vpn-instance** *vpn-instance-name* | Specifies the VPN instance of an SSH server. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-interface** | Indicates that any interface having an IP address configured can be used as the source interface of an SSH server. | - |
| **-a** *ipv6-address* | Specifies the source IPv6 address of an SSH server. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The SSH server receives login requests from all interfaces and addresses, leading to low system security. To improve system security, you can run this command to specify the source interface or IPv6 source address of the SSH server so that only authorized users can log in to the server.

**Prerequisites**

If the source interface of the SSH server is a logical interface, the logical interface must have been created. Otherwise, the command cannot be executed successfully.Before specifying a VPN instance for an SSH server, ensure that a VPN has been created. Otherwise, the command cannot be executed successfully.

**Configuration Impact**

After the source interface or IPv6 source address of the SSH server is specified, the system allows only SFTP, STelnet, SCP, and SNETCONF users to log in to the server through the specified source interface or IPv6 source address, and SFTP, STelnet, SCP, and SNETCONF users who log in through other interfaces will be rejected. However, the SFTP, STelnet, SCP, and SNETCONF users who have logged in to the server are not affected.

**Precautions**

* After you specify the source interface or IPv6 source address of the SSH server, ensure that the SFTP, STelnet, SCP, and SNETCONF users can communicate with the specified source interface at Layer 3 so that authorized SFTP, STelnet, SCP, and SNETCONF users can successfully log in to the SSH server.
* The configuration takes effect upon the next login. The system will prompt you to determine whether to continue the operation.
* If the specified source interface is bound to a VPN instance, the SSH server is bound to the VPN instance.
* If the specified source interface is bound to the VPN instance vpn1 and the VPN instance vpn2 is configured using the ssh ipv6 server-source -a ipv6-address [ -vpn-instance vpn-instance-name ] command, the VPN instance vpn1 bound to the source interface is used for IPv4 users, and the VPN instance vpn2 configured using the **ssh ipv6 server-source** command is used for IPv6 users.
* After a bound VPN instance is deleted, the VPN configuration specified using the ssh server-source command will not be cleared but does not take effect. In this case, the SSH server uses a public IP address. If you configure the VPN instance with the same name again, the VPN function is restored.
* After the bound source interface is deleted, the interface configuration in this command is not deleted, but the function does not take effect. After the source interface with the same name is configured again, the function is restored.
* For an IPv6 SSH server, you can run the ssh ipv6 server-source -a ipv6-address [ -vpn-instance vpn-instance-name ] command to configure a user to log in to the server through a specified IPv6 source address.
* If both the **ssh ipv6 server-source -a** and **ssh ipv6 server-source all-interface** commands are run, the interface specified in the **ssh ipv6 server-source -a** command is preferentially used as the source interface of the ssh server. If the specified source interface fails to be used for login, the system selects an interface from other valid interfaces for login.


Example
-------

# Set the source IPv6 address of the SSH server to 2001:db8::1 and the VPN instance name to vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ssh ipv6 server-source -a 2001:db8::1 -vpn-instance vpn1
Warning: SSH server source configuration will take effect in the next login. Do you want to continue? [Y/N]:y

```