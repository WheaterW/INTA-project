peer rely-state interface (BGP view)
====================================

peer rely-state interface (BGP view)

Function
--------



The **peer rely-state interface** command configures a BGP peer to track the physical status of a specified physical interface.

The **undo peer rely-state interface** command configures a BGP peer not to track the physical status of a specified physical interface.



By default, the BGP peer is not configured to track the physical status of any physical interface.


Format
------

**peer** *ipv4-address* **rely-state** **interface** { *interface-name* | *interface-type* *interface-number* }

**undo peer** *ipv4-address* **rely-state** **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *interface-name* | Specifies an interface name. | - |
| *interface-type* | Specifies the type of an interface. | -  -  - |
| *interface-number* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



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

# Configure a public network BGP IPv4 peer to track the physical status of 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp] peer 10.1.1.2 rely-state interface 100GE 1/0/1

```