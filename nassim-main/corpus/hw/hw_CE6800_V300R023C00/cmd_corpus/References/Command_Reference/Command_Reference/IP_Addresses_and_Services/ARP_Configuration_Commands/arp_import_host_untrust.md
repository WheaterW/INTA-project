arp import host untrust
=======================

arp import host untrust

Function
--------



The **arp import host untrust** command enables a forwarder to generate ARP entries based on the OpenFlow table delivered by the Agile Controller-DCN (AC-DCN controller).

The **undo arp import host** command disables a forwarder from generating ARP entries based on the OpenFlow table delivered by the AC-DCN controller.



By default, a forwarder does not generate ARP entries based on the OpenFlow table delivered by the AC-DCN controller.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp import host untrust**

**undo arp import host** [ **untrust** ]


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

Whether a forwarder generates ARP entries based on the OpenFlow table delivered by the AC-DCN controller is determined by user configuration. To enable a forwarder to generate ARP entries based on the OpenFlow table delivered by the AC-DCN controller, run the arp import host untrust command.

* If the information in the OpenFlow table is consistent with the dynamic ARP entries on the forwarder, the forwarder changes the type of the dynamic ARP entries to OpenFlow.ARP entries of the OpenFlow type are similar to static ARP entries, the forwarder does not age out the ARP entries of the OpenFlow type.
* If the information in the OpenFlow table is inconsistent with the dynamic ARP entries on the forwarder, the forwarder trusts the learned dynamic ARP entries, instead of generating new ARP entries based on the OpenFlow table.
* If dynamic ARP entries do not exist on the forwarder, the forwarder simply generates ARP entries of the OpenFlow type based on the OpenFlow table.


Example
-------

# On interface VBDIF 10, configure a forwarder to generate ARP entries based on the OpenFlow table delivered by the AC-DCN controller.
```
<HUAWEI> system-view
[~HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] arp import host untrust

```