peer description(BGP multi-instance view)
=========================================

peer description(BGP multi-instance view)

Function
--------



The **peer description** command configures a description for a peer.

The **undo peer description** command deletes the description of a peer.



By default, no description is configured for a peer.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **description** *description-text*

**undo peer** { *ipv4-address* | *ipv6-address* } **description**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **description** *description-text*

**undo peer** *ipv4-address* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description-text* | Specifies a description. | The value is a string of 1 to 255 characters. Letters, digits, and spaces are supported. |
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

The peer description can be used to configure a description for a peer, which facilitates management of peers or peer groups. The description records information about the peer, such as the VPN instance to which the peer belongs, and devices that establish peer relationships with the peer.

**Implementation Procedure**

The description configured by using the **peer description** command for a peer is displayed from the first non-space character.

**Configuration Impact**

If the command is run multiple times to configure a description for a peer, the latest configuration overwrites the previous one.

**Follow-up Procedure**

Run the display bgp peer verbose command to view the description of a peer configured using the **peer description** command.


Example
-------

# Configure a description for a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 description ISP1

```