peer as-number (BGP-VPN instance IPv6 address family view) (group)
==================================================================

peer as-number (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer as-number** command configures an AS number for a specified peer group.

The **undo peer as-number** command deletes the AS number of a specified peer group.



By default, no BGP peer is configured, and no AS number is specified for a peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **as-number** *as-number*

**undo peer** *group-name* **as-number**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *as-number* | Specifies an AS number. | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer as-number** command to create a specified peer relationship and specify the AS number of the peer.

**Precautions**

If the peer group to which a peer belongs is not configured with an AS number or the peer is not added to any peer group, deleting the AS number of the peer resets the peer relationship.Running the **undo peer ipv4-address** or **undo peer ipv6-address** command deletes all configurations related to the peer. Therefore, exercise caution when running this command.After the YANG management mode is enabled for a BGP VPN instance using the **bgp yang-mode enable** command, the **peer as-number** command cannot be configured. To configure a peer, run the **peer as-number** command in the BGP-VPN instance view and the **peer enable** command in the BGP-VPN instance IPv6 address family view to enable the peer.If the YANG management mode is disabled for a BGP VPN instance, the **peer as-number** command can be configured.


Example
-------

# Set the AS number to 200 for a peer group named test.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] group test external
[*HUAWEI-bgp-6-vpna] peer test as-number 200

```