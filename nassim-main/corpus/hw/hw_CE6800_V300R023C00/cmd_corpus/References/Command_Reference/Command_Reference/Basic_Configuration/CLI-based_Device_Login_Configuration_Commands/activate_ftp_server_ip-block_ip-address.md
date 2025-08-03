activate ftp server ip-block ip-address
=======================================

activate ftp server ip-block ip-address

Function
--------



The **activate ftp server ip-block ip-address** command unlocks the IP address of a user that fails the FTP authentication.




Format
------

**activate ftp server ip-block ip-address** *ip-address* [ **vpn-instance** *vpn-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a locked ip address. | For IPv4 address, the value is in the decimal format.  For IPv6 address, the value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-name* | Specifies the name of a VPN instance.  The VPN instance specified by vpn-instance <vpn-name> has been configured. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In an FTP connection, if a user enters incorrect passwords for the consecutive times in specified minutes, the IP address of this user will be locked. Run the **ftp server ip-block reactive** command to set lock period. To unlock the IP address of this user in advance, run activate ftp server ip-block ip-address command.


Example
-------

# Unlock the IP address 10.1.2.3.
```
<HUAWEI> activate ftp server ip-block ip-address 10.1.2.3

```