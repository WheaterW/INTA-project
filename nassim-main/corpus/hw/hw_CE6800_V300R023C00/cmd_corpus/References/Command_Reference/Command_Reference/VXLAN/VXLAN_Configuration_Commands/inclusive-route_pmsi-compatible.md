inclusive-route pmsi-compatible
===============================

inclusive-route pmsi-compatible

Function
--------



The **inclusive-route pmsi-compatible** command enables compatibility with the PMSI attribute for inclusive routes.

The **undo inclusive-route pmsi-compatible** command restores the default configuration.



By default, compatibility with the PMSI attribute of inclusive routes is disabled.


Format
------

**inclusive-route pmsi-compatible**

**undo inclusive-route pmsi-compatible**


Parameters
----------

None

Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When the most significant bit of the Tunnel Type field in the PMSI Tunnel Attribute of a received inclusive route is 1 (composite tunnel bit) and the least significant seven bits are 0x06 (Ingress Replication), all routes contained in the packet are withdrawn according to related standards. After the **inclusive-route pmsi-compatible** command is run, these routes are not withdrawn.




Example
-------

# Enable compatibility with the PMSI attribute of inclusive routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] inclusive-route pmsi-compatible

```