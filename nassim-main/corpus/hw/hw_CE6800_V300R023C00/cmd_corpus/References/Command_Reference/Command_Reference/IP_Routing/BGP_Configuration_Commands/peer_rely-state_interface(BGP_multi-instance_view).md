peer rely-state interface(BGP multi-instance view)
==================================================

peer rely-state interface(BGP multi-instance view)

Function
--------



The **peer rely-state interface** command configures a BGP peer to track the physical status of a specified physical interface.

The **undo peer rely-state interface** command configures a BGP peer not to track the physical status of a specified physical interface.



By default, the BGP peer is not configured to track the physical status of any physical interface.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **rely-state** **interface** { *interface-name* | *localIfType* *localIfNum* }

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **rely-state** **interface** { *interface-name* | *localIfType* *localIfNum* }

For CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **rely-state** **interface** { *interface-name* | *localIfType* *localIfNum* }

**undo peer** *peerIpv4Addr* **rely-state** **interface** { *interface-name* | *localIfType* *localIfNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | - |
| *localIfType* | Specifies an interface type. | - |
| *localIfNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **peer** *peerIpv4Addr* | Specifies an IPv4 peer address to be displayed. | The value is in dotted decimal notation. |
| **peer** *peerIpv6Addr* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A device sets up BGP peer relationships with some servers in a VLAN through a VLANIF interface. If the physical status of the interface connected to a server goes Down, the BGP peer cannot detect the status change in time, and the BGP peer relationship is disconnected only after a period of time (180s by default). During this period, traffic is lost. To prevent this problem, run the **peer rely-state interface** command to enable a BGP peer to monitor the physical status of a specified physical interface. After the command is run, the BGP peer relationship is established only when the physical status of the physical interface is Up. If the physical status of a specified physical interface is Down, the peer relationship is disconnected.

**Precautions**

For BGP peers, after the function of detecting the physical status of a physical interface is enabled, the establishment of a BGP peer relationship depends on the physical status of the detected interface. If the physical status of a specified interface is Down, the BGP peer relationship cannot be established. Therefore, exercise caution when using this function.By default, an interface on a device is a Layer 3 interface. After you run the **peer route-priority-track interface** command to specify an interface, changing the interface type to Layer 2 may affect Layer 3 services. Therefore, exercise caution when changing the interface type.


Example
-------

# Configure an IPv6 peer to track the status of 100GE 1/0/1.
```
[~HUAWEI] bgp 100 instance a
[~HUAWEI-bgp-instance-a] peer 2001:db8:1::1 as-number 100
[~HUAWEI-bgp-instance-a] peer 2001:db8:1::1 rely-state interface 100GE 1/0/1

```