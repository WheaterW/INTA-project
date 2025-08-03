peer rely-state interface (BGP-VPN instance view)(IPv6)
=======================================================

peer rely-state interface (BGP-VPN instance view)(IPv6)

Function
--------



The **peer rely-state interface** command configures a BGP peer to track the physical status of a specified physical interface.

The **undo peer rely-state interface** command configures a BGP peer not to track the physical status of a specified physical interface.



By default, a BGP peer is disabled from detecting the physical status of a specified physical interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **rely-state** **interface** { *interface-name* | *localIfType* *localIfNum* }

**undo peer** *peerIpv6Addr* **rely-state** **interface** { *interface-name* | *localIfType* *localIfNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is in dotted decimal notation. |
| *interface-name* | Specifies the name of an interface. | - |
| *localIfNum* | Specifies an interface number. | - |



Views
-----

BGP-VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A device sets up BGP peer relationships with some servers in a VLAN through a VLANIF interface. If the physical status of the interface connected to a server goes Down, the BGP peer cannot detect the status change in time, and the BGP peer relationship is disconnected only after a period of time (180s by default). During this period, traffic is lost. To prevent this problem, run the **peer rely-state interface** command to enable a BGP peer to monitor the physical status of a specified physical interface. After the command is run, the BGP peer relationship is established only when the physical status of the physical interface is Up. If the physical status of a specified physical interface is Down, the peer relationship is disconnected.

**Precautions**

For BGP peers, after the function of detecting the physical status of a physical interface is enabled, the establishment of a BGP peer relationship depends on the physical status of the detected interface. If the physical status of a specified interface is Down, the BGP peer relationship cannot be established. Therefore, exercise caution when using this function.By default, an interface on a device is a Layer 3 interface. After you run the **peer rely-state interface** command to specify an interface, changing the interface type to Layer 2 may affect Layer 3 services. Therefore, exercise caution when changing the interface type.


Example
-------

# Configure a BGP peer to track the physical status of 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-instance-vpna] peer 2001:db8:1::1 as-number 100
[*HUAWEI-bgp-instance-vpna] peer 2001:db8:1::1 rely-state interface 100GE 1/0/1

```