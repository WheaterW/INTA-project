statistics enable (VLANIF interface view)
=========================================

statistics enable (VLANIF interface view)

Function
--------



The **statistics enable** command enables the traffic statistics function on a VLANIF interface.

The **undo statistics enable** command disables the traffic statistics function on a VLANIF interface.



By default, the traffic statistics function is disabled on a VLANIF interface.


Format
------

**statistics** { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ]

**undo statistics** { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Enables traffic statistics collection on IPv4 packets. | - |
| **ipv6** | Enables traffic statistics collection on IPv6 packets. | - |
| **inbound** | Enables traffic statistics collection in the inbound direction of an interface. | - |
| **outbound** | Enables traffic statistics collection in the outbound direction of an interface. | - |



Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To check the network status or locate network faults, you can use the statistics enable command to enable the traffic statistics function on VLANIF interfaces. The device then collects traffic statistics on the VLANIF interfaces.

**Precautions**

* If the inbound and outbound parameters are not specified, traffic statistics collection is enabled in the inbound and outbound directions of a VLANIF interface.
* After you run the **undo statistics enable** command on a VLANIF interface, the device stops collecting traffic statistics on the VLANIF interface, and the collected traffic statistics are deleted.
* The device uses ACL resources when collecting traffic statistics. If the traffic statistics function is enabled on too many VLANIF interfaces, other services may fail to obtain ACL resources.
* Traffic statistics on VLANIF interfaces is unavailable for error packets.
* On the VLANIF interface enabled with the traffic statistics function, the packets such as ping packets sent from the device cannot be counted.
* The traffic statistics function on VLANIF interfaces is unavailable for MPLS packets.
* After enabling the traffic statistics function in a VLANIF, you can use the **display interface vlanif** command to view traffic statistics in the VLANIF.
* A higher number of VLANIF interfaces configured with the traffic statistics function leads to higher CPU usage.


Example
-------

# Enable the traffic statistics function for IPv4 and IPv6 traffic on the VLANIF interface.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWE-vlan100]
[~HUAWEI] interface vlanif 100
[*HUAWEI-Vlanif100] statistics ipv4 enable
[*HUAWEI-Vlanif100] statistics ipv6 enable

```