group (BGP-VPN instance view)
=============================

group (BGP-VPN instance view)

Function
--------



The **group** command creates a peer group.

The **undo group** command deletes a peer group.



By default, no peer group is created.


Format
------

**group** *group-name* { **internal** | **external** }

**group** *group-name*

**undo group** *group-name* [ **internal** | **external** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **internal** | Creates an IBGP peer group. | - |
| **external** | Creates an EBGP peer group. | - |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A peer group consists of peers with the same routing policies. After a peer is added to a peer group, it inherits the configurations of this peer group. When the configurations of the peer group are changed, the configurations of these peers are changed accordingly.On a large-scale BGP network, there are a large number of peers, many of which require the same policy. In such a case, you can run the group command to create a peer group, configure the policy for the peer group, and then add peers to the group, which simplifies configurations.


Example
-------

# Create an EBGP peer group named ex and set its AS number to 500.1.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-vpn1] group ex external
[*HUAWEI-bgp-vpn1] peer ex as-number 500.1

```

# Create an IBGP peer group named in.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group in internal

```