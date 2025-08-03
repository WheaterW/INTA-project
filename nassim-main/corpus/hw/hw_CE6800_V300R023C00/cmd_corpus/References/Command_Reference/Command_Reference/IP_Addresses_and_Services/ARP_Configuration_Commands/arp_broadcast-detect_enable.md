arp broadcast-detect enable
===========================

arp broadcast-detect enable

Function
--------



The **arp broadcast-detect enable** command enables ARP broadcast probe implemented when a VXLAN tunnel or Layer 2 sub-interface goes Down.

The **undo arp broadcast-detect enable** command restores the default configuration.



By default, ARP broadcast probe is disabled when a VXLAN tunnel or Layer 2 sub-interface goes Down.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp broadcast-detect enable**

**undo arp broadcast-detect enable**


Parameters
----------

None

Views
-----

VBDIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the VXLAN tunnel or Layer 2 sub-interface on the local device is down, the ARP entries learned from the VXLAN tunnel or Layer 2 sub-interface are deleted. As a result, traffic cannot be forwarded. By default, the device triggers ARP Miss messages through traffic forwarding to relearn ARP entries. To enable the device to quickly learn ARP entries, enable ARP broadcast probe on the VBDIF interface.For example, in a distributed VXLAN gateway scenario, if a Layer 2 sub-interface on a device is down and ARP broadcast probe is enabled, the device broadcasts ARP request packets based on the ARP entries learned by the Layer 2 sub-interface to relearn ARP entries.

**Configuration Impact**

After the arp broadcast-detect enable command is run, ARP broadcast probe is initiated for dynamic ARP entries learned on the local VXLAN tunnel or Layer 2 sub-interface that goes from Up to Down.


Example
-------

# On VBDIF 10, enable ARP broadcast probe implemented when a VXLAN tunnel or Layer 2 sub-interface goes Down.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] arp broadcast-detect enable

```