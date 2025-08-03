clear ip df
===========

clear ip df

Function
--------



The **clear ip df** command enables a device to forcibly fragment outgoing IP packets on an interface.

The **undo clear ip df** command disables a device from forcibly fragmenting outgoing IP packets on an interface.



By default, a device is disabled from forcibly fragmenting outgoing IP packets on an interface.


Format
------

**clear ip df**

**undo clear ip df**


Parameters
----------

None

Views
-----

Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An IP header contains a Don't Fragment (DF) field, indicating whether an IP packet can be fragmented. If the DF field of an IP packet is set to 1, a device does not fragment the packet. If the size of an IP packet is greater than the MTU of an interface because of a protocol encapsulation, a device discards the packet and sends ICMP error messages, causing data loss. To prevent data loss in this scenario, run the **clear ip df** command to enable the forced fragmentation of IP packets.

**Configuration Impact**

If the function is enabled, the system resets the DF field to 0 and performs fragmentation when the IP packet meets the following requirements:

* DF field in the IP header is 1.
* Size of the packet is larger than the MTU configured on the outbound interface.

**Precautions**

This command takes effect only for the IP packets sent by the CPU, but not for the packets forwarded by the CPU.


Example
-------

# Enable forcible fragmentation for outgoing IP packets on VLANIF 100.
```
<HUAWEI> system-view
[~HUAWEI] interface vlanif 100
[~HUAWEI-Vlanif100] clear ip df

```