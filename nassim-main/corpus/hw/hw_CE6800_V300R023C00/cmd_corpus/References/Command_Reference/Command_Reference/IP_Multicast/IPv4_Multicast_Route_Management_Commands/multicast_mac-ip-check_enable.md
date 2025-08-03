multicast mac-ip-check enable
=============================

multicast mac-ip-check enable

Function
--------



The **multicast mac-ip-check enable** command enables the consistency check between the destination MAC address and destination IP address of multicast packets.

The **undo multicast mac-ip-check enable** command disables the consistency check between the destination MAC address and destination IP address of multicast packets.



By default, the device does not check the consistency between the destination MAC address and destination IP address of multicast packets.


Format
------

**multicast mac-ip-check enable**

**undo multicast mac-ip-check enable**


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

For multicast packets, there is a mapping between MAC addresses and IP addresses. The last 23 bits of the MAC address of an IPv4 multicast packet must be the same as those of the IP address.You can run this command to check the consistency between multicast MAC addresses and IP addresses and discard packets with inconsistent multicast MAC addresses and IP addresses.

**Precautions**



If the mapping between the MAC address and destination IP address of a multicast packet is incorrect, the packet is discarded.




Example
-------

# Enable the consistency check between the destination MAC address and destination IP address of multicast packets.
```
<HUAWEI> system-view
[~HUAWEI] multicast mac-ip-check enable

```