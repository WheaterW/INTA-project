peer rely-state interface (BGP view) (IPv6)
===========================================

peer rely-state interface (BGP view) (IPv6)

Function
--------



The **peer rely-state interface** command configures a BGP peer to track the physical status of a specified physical interface.

The **undo peer rely-state interface** command configures a BGP peer not to track the physical status of a specified physical interface.



By default, the BGP peer is not configured to track the physical status of any physical interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **rely-state** **interface** { *interface-name* | *interface-type* *interface-number* }

**undo peer** *ipv6-address* **rely-state** **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The address is in the format of X:X:X:X:X:X:X:X. |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies an interface type. | -  -  - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

BGP view


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

# Configure a public network BGP IPv6 peer to track the physical status of 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 rely-state interface 100GE 1/0/1

```