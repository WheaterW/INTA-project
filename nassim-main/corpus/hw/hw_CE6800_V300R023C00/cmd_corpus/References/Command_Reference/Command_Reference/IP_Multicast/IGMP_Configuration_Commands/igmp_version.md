igmp version
============

igmp version

Function
--------



The **igmp version** command configures an IGMP version on an interface.

The **undo igmp version** command restores the default setting.



By default, an interface runs IGMPv2.


Format
------

**igmp version** *VersionValue*

**undo igmp version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *VersionValue* | Specifies an IGMP version to be run on an interface. | The value can be 1, 2, or 3.   * 1:IGMPv1 * 2:IGMPv2 * 3:IGMPv3 |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Router interfaces on a subnet must run the same IGMP version. Otherwise, they cannot communicate.An IGMP version cannot automatically change to another version.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Configure IGMPv1 on VLANIF 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp version 1

```