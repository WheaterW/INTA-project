peer as-number (BGP-VPN instance view)
======================================

peer as-number (BGP-VPN instance view)

Function
--------



The **peer as-number** command creates a peer and configures an AS number for the peer.

The **undo peer** command deletes a specified peer.



By default, no BGP peer is configured, and no AS number is specified for a peer or peer group.


Format
------

**peer** *ipv4-address* **as-number** *as-number*

**undo peer** *ipv4-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *as-number* | Specifies a destination AS number. | For an AS number in integer format, the value ranges from 1 to 4294967295.  For an AS number in dotted notation, it is in the format of x.y, in which x and y are integers, with x ranging from 1 to 65535 and y ranging from 0 to 65535. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer as-number** command to create a specified peer relationship and specify the AS number of the peer.

**Precautions**

A peer group has been created using the **group** *group-name*{ **external** | **internal** } command.

* If the **group** *group-name***external** command is run, the AS number of the EBGP peer group specified in the **peer as-number** command must be different from the local AS number.
* If the **group** *group-name***internal** command is run, the AS number of the IBGP peer group is the same as the local AS number by default. Therefore, no extra configuration is required.

If the peer group to which a peer belongs is not configured with an AS number or the peer is not added to any peer group, deleting the AS number of the peer resets the peer relationship.Running the **undo peer** *ipv4-address*or **undo peer** *ipv6-address*command deletes all configurations related to the peer. Therefore, exercise caution when running this command.


Example
-------

# Set the AS number to 100 for IPv4 peer 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.1 as-number 100

```