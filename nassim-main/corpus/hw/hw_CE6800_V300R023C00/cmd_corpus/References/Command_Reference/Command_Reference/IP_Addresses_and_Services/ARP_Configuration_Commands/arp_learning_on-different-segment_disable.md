arp learning on-different-segment disable
=========================================

arp learning on-different-segment disable

Function
--------



The **arp learning on-different-segment disable** command disables the function of learning ARP entries on different network segments.

The **undo arp learning on-different-segment disable** command enables the function of learning ARP entries on different network segments.



By default, the function of learning ARP entries on different network segments is enabled.


Format
------

**arp learning on-different-segment disable**

**undo arp learning on-different-segment disable**


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



By default, the main physical interface of a device supports the function of learning ARP entries of IP addresses on different network segments, and the routed ARP proxy can access devices on different network segments. This function is by default disabled on logical interfaces and Layer 3 sub-interfaces. The process of learning ARP entries of IP addresses on different network segments is as follows: A device sends an ARP broadcast request packet on the network segment. Upon receipt of the ARP response packet by the routed ARP proxy, the device learns ARP entries, instead of checking the source IP address in the ARP response packets.This, however, may pose the device to risks. For example, if a network attacker on the same network segment sends a large number of ARP request packets based on a false source IP address, ARP entries of the device may be used up.To ensure service access and network security, run the **arp learning on-different-segment disable** command to disable the function of learning ARP entries on different network segments.



**Configuration Impact**



After the **arp learning on-different-segment disable** command is run, the device cannot learn ARP entries of the IP addresses on different network segments. However, the ARP entries of the IP addresses on different network segments that have learned before this configuration are still valid until the aging period of ARP entries ends.




Example
-------

# Disable the function of learning ARP entries on different network segments.
```
<HUAWEI> system-view
[~HUAWEI] arp learning on-different-segment disable

```