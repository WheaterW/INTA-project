reserved for vxlan bypass
=========================

reserved for vxlan bypass

Function
--------



The **reserved for vxlan bypass** command configures the IPv4 address of the VLANIF interface for a peer-link interface as a dedicated address for the bypass VXLAN tunnel.

The **undo reserved for vxlan bypass** command restores the default configuration.



By default, the IPv4 address of the VLANIF interface for a peer-link interface is not specified as a dedicated address for the bypass VXLAN tunnel, and a consistency check is performed to determine whether the VLANIF interface addresses on the M-LAG master and backup devices are the same.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reserved for vxlan bypass**

**undo reserved for vxlan bypass**


Parameters
----------

None

Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a scenario where a server is dual-homed to a VXLAN network through an M-LAG, a static bypass VXLAN tunnel must be configured between the M-LAG member devices to divert service traffic to the peer-link.If the \*\*consistency-check enable mode \*\* command is run on M-LAG member devices to enable M-LAG configuration consistency check, the VLANIF interfaces configurations on the peer-link interfaces of the master and backup M-LAG member devices are checked. If the configurations are inconsistent, an alarm is reported.If you run this command to specify the IPV4 address of the VLANIF interface for a peer-link interface to be used only by the bypass VXLAN tunnel, the check criteria for VLANIF interface configuration consistency change accordingly. Specifically, if the IPV4 address and MAC address of the corresponding VLANIF interfaces on the M-LAG master and backup devices are the same, an alarm is reported.


Example
-------

# Configure the IPv4 address of VLANIF 100 as a dedicated address for the bypass VXLAN tunnel.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[*HUAWEI] interface Vlanif 100
[*HUAWEI-Vlanif100] reserved for vxlan bypass

```