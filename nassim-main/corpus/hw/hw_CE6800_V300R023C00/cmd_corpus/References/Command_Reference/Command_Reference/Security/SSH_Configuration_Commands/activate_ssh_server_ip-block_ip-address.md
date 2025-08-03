activate ssh server ip-block ip-address
=======================================

activate ssh server ip-block ip-address

Function
--------



The **activate ssh server ip-block ip-address** command unlocks the IP address of a user that fails the SSH connection authentication.




Format
------

**activate ssh server ip-block ip-address** *ip-address* [ **vpn-instance** *vpn-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a locked IP address. | * For IPv4 address, the value is in the decimal format. * For IPv6 address, the value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-name* | Specifies the name of a VPN to which the locked user belongs. | The value is a string of 1 to 31 case-sensitive characters.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In an SSH connection, if a user enters incorrect passwords for six consecutive times in 5 minutes, the IP address of this user will be blocked for 5 minutes. To unlock the IP address of this user in advance, run the activate ssh server ip-block ip-address command.


Example
-------

# Unlock the IP address 10.1.2.3.
```
<HUAWEI> activate ssh server ip-block ip-address 10.1.2.3

```