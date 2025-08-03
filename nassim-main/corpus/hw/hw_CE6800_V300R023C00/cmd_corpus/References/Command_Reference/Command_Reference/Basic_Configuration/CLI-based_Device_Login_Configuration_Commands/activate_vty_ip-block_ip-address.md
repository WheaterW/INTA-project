activate vty ip-block ip-address
================================

activate vty ip-block ip-address

Function
--------



The **activate vty ip-block ip-address** command unlocks the IP address that fails to be authenticated in a Telnet connection.




Format
------

**activate vty ip-block ip-address** *ip-address* [ **vpnname** *vpn-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the locked IPv4 address. | The options are as follows:   * For an IPv4 address, the value is in dotted decimal notation. * For an IPv6 address, the value is a 32-bit hexadecimal number in the format of X:X:X:X:X:X:X:X. |
| **vpnname** *vpn-name* | Specifies the name of the VPN where the locked client belongs to. | The value is a string of 1 to 31 case-sensitive characters. :  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In the telnet connection, if a user enters incorrect passwords for six consecutive times in 5 minutes, the IP address of this user is locked for 5 minutes. To unlock the IP address of this user in advance, run the activate vty ip-block ip-address command.


Example
-------

# Unlock the IP address 10.1.2.3.
```
<HUAWEI> activate vty ip-block ip-address 10.1.2.3

```