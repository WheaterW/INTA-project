dhcp relay trust option82
=========================

dhcp relay trust option82

Function
--------



The **dhcp relay trust option82** command enables Option 82 on the DHCP relay agent.

The **undo dhcp relay trust option82** command disables Option 82 on the DHCP relay agent.



By default, Option 82 is enabled on the DHCP relay agent.


Format
------

**dhcp relay trust option82**

**undo dhcp relay trust option82**


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

This command is used on the DHCP relay agent to enable the Option 82 function. After receiving a DHCP packet that carries the Option 82 field but the giaddr field of the packet is 0, the DHCP relay agent processes the packet by default. Using the **undo dhcp relay trust option82** command, the DHCP relay agent discards the packet.

**Prerequisites**

DHCP has been enabled globally by using the **dhcp enable** command.


Example
-------

# Disable Option 82 trusted of the DHCP relay agent.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] undo dhcp relay trust option82

```