refresh bgp evpn (IPv6)
=======================

refresh bgp evpn (IPv6)

Function
--------



The **refresh bgp evpn** command configures soft reset for BGP EVPN connections.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**refresh bgp evpn** *peer-address* { **import** | **export** }

**refresh bgp instance** *bgpName* **evpn** *peer-address* { **import** | **export** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the IPv6 address of a peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **import** | Triggers an inbound soft reset. | - |
| **export** | Triggers an inbound soft reset. | - |
| **instance** *bgpName* | Displays BGP routes of a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the peer supports route-refresh, you can run the **refresh bgp evpn** command to soft reset the BGP EVPN connection. BGP EVPN soft reset can refresh the EVPN routing table and apply new filtering policies without tearing down the BGP connection.

**Prerequisites**

Configuring BGP soft reset requires that the peers support the route-refresh capability.

**Precautions**

Assume that a device supports route-refresh and is configured with the **peer keep-all-routes** command. After the **refresh bgp** command is run on the device, the device does not refresh its routing table.


Example
-------

# Softly reset specified BGP EVPN connection in the inbound direction so that new configurations can take effect.
```
<HUAWEI> refresh bgp evpn 2001:db8:1::1 import

```