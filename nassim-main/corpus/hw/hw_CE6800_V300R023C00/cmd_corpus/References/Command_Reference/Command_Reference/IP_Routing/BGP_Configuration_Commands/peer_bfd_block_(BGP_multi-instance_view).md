peer bfd block (BGP multi-instance view)
========================================

peer bfd block (BGP multi-instance view)

Function
--------



The **peer bfd block** command prevents a peer from inheriting the BFD function of its peer group.

The **undo peer bfd block** command restores the default configuration.



By default, a peer inherits the BFD function from its peer group.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **bfd** **block**

**undo peer** { *ipv4-address* | *ipv6-address* } **bfd** **block**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **bfd** **block**

**undo peer** *ipv4-address* **bfd** **block**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
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

BFD provides millisecond-level fault detection. It helps BGP to detect faults in neighboring devices or links more quickly, and instructs BGP to recalculate routes for correct packet forwarding. If a peer group is configured with BFD, all members of the peer group will establish BFD sessions. The **peer bfd block** command can be used to prevent a peer from inheriting the BFD function from its peer group.

**Prerequisites**



A BFD session has been established.



**Configuration Impact**



After the **peer bfd block** command is run on a peer, the corresponding BFD session on the peer is deleted. As a result, fast link fault detection cannot be implemented.



**Precautions**



The **peer bfd block** command and the peer bfd enable command are mutually exclusive. After the **peer bfd block** command is run, related BFD sessions are automatically deleted.




Example
-------

# Disable BFD function.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 192.168.1.1 as-number 100
[*HUAWEI-bgp-instance-a] peer 192.168.1.1 bfd block

```