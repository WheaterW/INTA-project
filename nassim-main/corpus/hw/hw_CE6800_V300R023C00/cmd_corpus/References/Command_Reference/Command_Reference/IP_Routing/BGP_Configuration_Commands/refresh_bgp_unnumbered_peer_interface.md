refresh bgp unnumbered peer interface
=====================================

refresh bgp unnumbered peer interface

Function
--------



The **refresh bgp unnumbered peer interface** command softly resets a BGP unnumbered peer connection.

The **refresh bgp ipv6 unnumbered peer interface** command softly resets a BGP IPv6 unnumbered peer connection.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**refresh bgp unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } { **export** | **import** }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**refresh bgp ipv6 unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } { **export** | **import** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | - |
| *IfType* | Specifies the type of an interface. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **export** | Triggers outbound soft resetting. | - |
| **import** | Triggers inbound soft resetting. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a device's peer supports route-refresh, the **refresh bgp unnumbered peer interface** command can be used on the device to softly reset the BGP unnumbered peer connection with the peer. BGP soft resetting can be used to refresh the BGP routing table and apply new routing policies, without closing any BGP peer connection.

**Prerequisites**

Configuring BGP soft resetting requires that the peers support the route-refresh capability.

**Precautions**

Assume that a device supports route-refresh and is configured with the **peer keep-all-routes** command. After the **refresh bgp** command is run on the device, the device does not refresh its routing table.


Example
-------

# Perform a soft reset on unnumbered peer connections in the inbound direction on an interface to make new configurations take effect.
```
<HUAWEI> refresh bgp unnumbered peer interface 100GE 1/0/8 import

```