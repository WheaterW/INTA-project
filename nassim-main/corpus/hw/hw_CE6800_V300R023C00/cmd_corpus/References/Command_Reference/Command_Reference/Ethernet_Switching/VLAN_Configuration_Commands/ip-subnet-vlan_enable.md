ip-subnet-vlan enable
=====================

ip-subnet-vlan enable

Function
--------



The **ip-subnet-vlan enable** command enables IP subnet-based VLAN classification.

The **undo ip-subnet-vlan enable** command disables IP subnet-based VLAN classification.



By default, no IP subnet-based VLAN is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip-subnet-vlan enable**

**undo ip-subnet-vlan enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

IP subnet-based VLAN division is also called network layer-based VLAN division.Network layer-based VLAN division greatly reduces the workload of manual configurations and allows users to easily join a VLAN, move from one VLAN to another VLAN, or leave a VLAN.IP subnet-based VLAN division is applicable to networks that have traveling users and require simple management.

**Prerequisites**



The ip-subnet-vlan enable command can be run only on Layer 2 interfaces. If the interface is a Layer 3 interface, run the **portswitch** command to change the interface from Layer 3 mode to Layer 2 mode.



**Configuration Impact**

After a Layer 2 device receives untagged packets, it determines the VLANs to which the packets belong based on the packets' source IP addresses and then sends the packets to correct VLANs.

**Precautions**

The IP subnet or the IP address associated with a VLAN cannot be a multicast network segment or multicast address.


Example
-------

# Enable VLAN classification based on sub-net addresses.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] undo shutdown
[*HUAWEI-100GE1/0/1] ip-subnet-vlan enable

```