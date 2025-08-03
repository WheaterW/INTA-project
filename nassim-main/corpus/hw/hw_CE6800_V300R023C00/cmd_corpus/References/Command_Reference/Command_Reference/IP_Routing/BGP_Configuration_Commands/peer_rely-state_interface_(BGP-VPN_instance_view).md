peer rely-state interface (BGP-VPN instance view)
=================================================

peer rely-state interface (BGP-VPN instance view)

Function
--------



The **peer rely-state interface** command configures a BGP peer to track the physical status of a specified physical interface.

The **undo peer rely-state interface** command configures a BGP peer not to track the physical status of a specified physical interface.



By default, the BGP peer is not configured to track the physical status of any physical interface.


Format
------

**peer** *peerIpv4Addr* **rely-state** **interface** { *interface-name* | *localIfType* *localIfNum* }

**undo peer** *peerIpv4Addr* **rely-state** **interface** { *interface-name* | *localIfType* *localIfNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *interface-name* | Specifies the name of an interface. | - |
| *localIfType* | Specifies an interface type. | - |
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

A device sets up BGP peer relationships with some servers in a VLAN through a VLANIF interface. If the physical status of the interface connected to a server goes Down, the BGP peer cannot detect the status change in time, and the BGP peer relationship is disconnected only after a period of time (180s by default). During this period, traffic is lost. To prevent this problem, run the **peer rely-state interface** command to configure the BGP peer to track the physical status of a specified physical interface. The establishment of a BGP peer relationship depends on the physical status of the specified physical interface. If the physical status of the specified physical interface is Up, the BGP peer relationship can be established. If the physical status is Down, the BGP peer relationship is disconnected.

**Precautions**

For BGP peers, after the function of detecting the physical status of a physical interface is enabled, the establishment of a BGP peer relationship depends on the physical status of the detected interface. If the physical status of a specified interface is Down, the BGP peer relationship cannot be established. Therefore, exercise caution when using this function.By default, an interface on a device is a Layer 3 interface. After you run the **peer route-priority-track interface** command to specify an interface, changing the interface type to Layer 2 may affect Layer 3 services. Therefore, exercise caution when changing the interface type.


Example
-------

# Configure a BGP peer to track the physical status of 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vrf1
[*HUAWEI-bgp-instance-vrf1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-vrf1] peer 10.1.1.1 rely-state interface 100GE 1/0/1

```