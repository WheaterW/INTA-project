mac-address learning disable
============================

mac-address learning disable

Function
--------



The **mac-address learning disable** command disables MAC address learning.

The **undo mac-address learning disable** command restores MAC address learning.



By default, MAC address learning is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-address learning disable**

**undo mac-address learning disable**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a fixed network, you can disable MAC address learning in a VLAN or on an interface to save MAC address entries.After MAC address learning is disabled using the **mac-address learning disable** command, the device does not learn new MAC addresses from the specified bridge domain (BD).When MAC address learning is enabled, the device parses the source MAC address of an Ethernet frame received from a neighboring device and adds a new entry to the MAC address entry based on the source MAC address and the interface that receives the Ethernet frame. When receiving an Ethernet frame destined for the MAC address, the device searches the MAC address entry for the correct outbound interface to prevent broadcast.


Example
-------

# Disable MAC address learning in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] mac-address learning disable

```