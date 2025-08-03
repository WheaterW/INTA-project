dhcp server trust option82
==========================

dhcp server trust option82

Function
--------

The **dhcp server trust option82** command enables Option 82 on the DHCP server.

The **undo dhcp server trust option82** command disables Option 82 on the DHCP server.

By default, the DHCP server trusts Option 82.



Format
------

**dhcp server trust option82**

**undo dhcp server trust option82**



Parameters
----------

None


Views
-----

System view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command is used on the DHCP server to enable the Option 82 function. After receiving a DHCP packet that carries the Option 82 field but the giaddr is 0, the DHCP server processes the packet by default. Using the **undo dhcp server trust option82** command, the DHCP server discards the packet.

**Prerequisites**

DHCP has been enabled globally by using the **dhcp enable** command.



Example
-------

# Disable Option 82 of the DHCP server.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] undo dhcp server trust option82

```