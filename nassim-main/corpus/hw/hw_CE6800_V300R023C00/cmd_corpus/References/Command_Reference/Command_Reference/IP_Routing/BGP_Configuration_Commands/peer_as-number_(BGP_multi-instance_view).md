peer as-number (BGP multi-instance view)
========================================

peer as-number (BGP multi-instance view)

Function
--------



The **peer as-number** command creates a peer and configures an AS number for the peer.

The **undo peer** command deletes a specified peer.



By default, no BGP peer is configured, and no AS number is specified for a peer or peer group.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **as-number** *as-number*

**undo peer** { *ipv4-address* | *ipv6-address* }

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **as-number** *as-number*

**undo peer** *ipv4-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-number* | Specifies a destination AS number. | For an AS number in integer format, the value ranges from 1 to 4294967295.  For an AS number in dotted notation, it is in the format of x.y, in which x and y are integers, with x ranging from 1 to 65535 and y ranging from 0 to 65535. |
| **peer** *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **peer** *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **peer as-number** command to create a specified peer relationship and specify the AS number of the peer.

**Precautions**

If the peer group to which a peer belongs is not configured with an AS number or the peer is not added to any peer group, deleting the AS number of the peer resets the peer relationship.Running the **undo peer** *ipv4-address*or **undo peer** *ipv6-address*command deletes all configurations related to the peer. Therefore, exercise caution when running this command.After the YANG management mode is enabled for a BGP VPN instance using the **bgp yang-mode enable** command, the **peer as-number** command cannot be configured. To configure a peer, run the **peer as-number** command in the BGP multi-instance VPN instance view and run the **peer enable** command in the BGP multi-instance view to enable the peer.If the YANG management mode is disabled for a BGP VPN instance, the **peer as-number** command can be configured.


Example
-------

# Set the AS number to 100 for IPv4 peer 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 100

```