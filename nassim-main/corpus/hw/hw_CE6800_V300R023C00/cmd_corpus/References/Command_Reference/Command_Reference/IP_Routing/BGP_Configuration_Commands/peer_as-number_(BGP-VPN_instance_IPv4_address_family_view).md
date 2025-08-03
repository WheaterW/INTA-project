peer as-number (BGP-VPN instance IPv4 address family view)
==========================================================

peer as-number (BGP-VPN instance IPv4 address family view)

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

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer as-number** command to create a specified peer relationship and specify the AS number of the peer.

**Precautions**

If the peer group to which a peer belongs is not configured with an AS number or the peer is not added to any peer group, deleting the AS number of the peer resets the peer relationship.Running the **undo peer** *ipv4-address*or **undo peer** *ipv6-address*command deletes all configurations related to the peer. Therefore, exercise caution when running this command.After the YANG management mode is enabled for a BGP VPN instance using the **bgp yang-mode enable** command, the **peer as-number** command cannot be configured. To configure a peer, run the **peer as-number** command in the BGP-VPN instance view and the **peer enable** command in the BGP-VPN instance IPv4 address family view to enable the peer.If the YANG management mode is disabled for a BGP VPN instance, the **peer as-number** command can be configured.


Example
-------

# Set the AS number to 100 for the peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 as-number 100

```