ipv4-family vpn-target
======================

ipv4-family vpn-target

Function
--------



The **ipv4-family vpn-target** command enables the BGP VPN-Target address family and displays the address family view.

The **undo ipv4-family vpn-target** command deletes the configurations in the BGP VPN-Target address family.



By default, the BGP VPN-Target address family is disabled.


Format
------

**ipv4-family vpn-target**

**undo ipv4-family vpn-target**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to enable the BGP VPN-Target address family and enter the BGP VPN-Target address family view. The BGP VPN-Target address family is used to configure VPN ORF.




Example
-------

# Enter the BGP VPN-Target address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target]

```