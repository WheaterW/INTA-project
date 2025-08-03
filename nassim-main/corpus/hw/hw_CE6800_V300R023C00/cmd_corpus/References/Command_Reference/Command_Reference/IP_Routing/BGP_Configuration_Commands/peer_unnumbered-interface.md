peer unnumbered-interface
=========================

peer unnumbered-interface

Function
--------



The **peer unnumbered-interface** command specifies an outbound interface for an unnumbered peer group.

The **undo peer unnumbered-interface** command restores the default configuration.



By default, no outbound interface is specified for an unnumbered peer group.


Format
------

**peer** *peerGroupName* **unnumbered-interface** { *interface-name* | *IfType* *IFNum* }

**undo peer** *peerGroupName* **unnumbered-interface** { *interface-name* | *IfType* *IFNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *interface-name* | Specifies an interface name. | - |
| *IfType* | Specifies the type of an interface. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



As the BGP network topology becomes increasingly complex, IP address resources are insufficient, a large number of peer relationships are established, and the configurations are more and more complex. BGP Unnumbered is a port multiplexing technology that saves IP address resources and automatically discovers and establishes peer relationships. You can run the **peer unnumbered-interface** command to configure an outbound interface for an unnumbered peer group. After this command is run, the IPv6 link-local address of the outbound interface and the advertisement protocol are used to automatically discover peers and establish BGP sessions with the peers, implementing IPv4 and IPv6 route distribution.



**Prerequisites**



A peer group has been created using the **group unnumbered** command.



**Precautions**



For the outbound interface of an unumbered peer group, no IP address needs to be configured by default. The IPv6 link-local address of the outbound interface is used to establish a peer relationship.However, in IPv4 scenarios, if no IP address is configured, traffic cannot be forwarded. In this case, you need to configure the interface to borrow the IP address of another interface using the **ip address unnumbered interface** command.It is recommended that the hold time be set based on the total number of BGP peers in each address family. As the number of peers increases, increase the minimum hold time accordingly. Adjust the hold time according to "Mapping Between the Total Number of BGP Peers in Each Address Family and the Recommended Minimum Hold Time" in the usage guide of the **peer timer** command.By default, an interface on a device is a Layer 3 interface. After you run the **peer unnumbered-interface** command to specify an interface, changing the interface type to Layer 2 may affect Layer 3 services. Therefore, exercise caution when changing the interface type.




Example
-------

# Specify an outbound interface for the unnumbered peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group a unnumbered
[*HUAWEI-bgp] peer a unnumbered-interface 100GE1/0/1

```