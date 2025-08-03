vpn-instance-capability simple
==============================

vpn-instance-capability simple

Function
--------



The **vpn-instance-capability simple** command configures the device to directly calculate routes without detecting routing loops.

The **undo vpn-instance-capability** command sets the DN bit in the LSAs to be advertised and enables the device to check the DN bit in received summary LSAs. It also enables the device to check the DN bit and route tag in received ASE LSAs and NSSA LSAs to prevent routing loops.



By default, the routing loop detection is enabled.


Format
------

**vpn-instance-capability simple**

**undo vpn-instance-capability**


Parameters
----------

None

Views
-----

OSPFv3 view,OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **vpn-instance-capability simple** command takes effect only for the OSPF or OSPFv3 processes bound to a VPN instance.


Example
-------

# Disable routing loop detection for OSPF.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] vpn-target 3:3 export-extcommunity
[*HUAWEI-vpn-instance-vrf1-af-ipv4] vpn-target 4:4 import-extcommunity
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] ospf 100 vpn-instance vrf1
[*HUAWEI-ospf-100] vpn-instance-capability simple

```

# Disable OSPFv3 routing loop detection.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv6-family
[*HUAWEI-vpn-instance-huawei-af-ipv6] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ospfv3 100 vpn-instance huawei
[*HUAWEI-ospfv3-100] vpn-instance-capability simple

```