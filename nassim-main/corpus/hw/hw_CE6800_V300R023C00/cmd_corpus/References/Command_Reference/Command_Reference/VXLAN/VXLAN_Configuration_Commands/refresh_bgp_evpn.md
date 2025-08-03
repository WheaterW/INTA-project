refresh bgp evpn
================

refresh bgp evpn

Function
--------



The **refresh bgp evpn** command soft resets connections in the BGP EVPN address family.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**refresh bgp** [ **instance** *instance-name* ] **evpn** { **all** | *peer-address* | **group** *group-name* } { **import** | **export** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies a BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **all** | Softly resets all BGP EVPN connections. | - |
| *peer-address* | Specifies a BGP EVPN peer IP address. | The value is in dotted decimal notation. |
| **group** *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **import** | Triggers an inbound soft reset. | - |
| **export** | Triggers an inbound soft reset. | - |



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

The route-refresh function has been enabled for BGP EVPN peers.

**Precautions**

Assume that a device supports route-refresh and is configured with the **peer keep-all-routes** command. After the **refresh bgp** command is run on the device, the device does not refresh its routing table.


Example
-------

# Softly reset all BGP EVPN connections in the inbound direction so that new configurations can take effect.
```
<HUAWEI> refresh bgp evpn all import

```