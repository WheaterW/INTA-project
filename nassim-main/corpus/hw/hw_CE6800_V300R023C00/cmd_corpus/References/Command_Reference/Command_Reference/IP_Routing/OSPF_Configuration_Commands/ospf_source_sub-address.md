ospf source sub-address
=======================

ospf source sub-address

Function
--------



The **ospf source sub-address** command specifies a secondary IP address as the source IP address on a broadcast network.

The **undo ospf source sub-address** command cancels the configuration.



By default, a primary IP address is used as the source IP address to establish an OSPF neighbor relationship on a broadcast network.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospf source sub-address** *ipv4-address*

**undo ospf source sub-address** [ *ipv4-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies a secondary IP address as the source IP address. | The value is in dotted decimal notation. |



Views
-----

VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To specify a secondary IP address as the source IP address on a broadcast network, run the **ospf source sub-address** command. After the configuration, the secondary IP address will be used to establish OSPF neighbor relationships.In an M-LAG scenario, VLANIF interfaces of M-LAG devices have the same primary IP address. To establish OSPF neighbor relationships between M-LAG devices and between M-LAG devices and user-side access devices, you need to configure different secondary IP addresses for the master and backup M-LAG devices and specify the secondary IP addresses as the source IP addresses, this address is used to establish an OSPF neighbor relationship.

**Precautions**

The **ospf source sub-address** command takes effect only on broadcast networks, and does not take effect if the network type is P2P, NBMA, or P2MP.In addition, the **ospf source sub-address** command does not take effect if the primary IP address of the configured interface is unnumbered.


Example
-------

# Specify the secondary IP address 1.1.1.1 as the source IP address on a broadcast network.
```
<HUAWEI> system-view
[~HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] ospf source sub-address 1.1.1.1

```