advertise-community-gshut(BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)
==============================================================================================================

advertise-community-gshut(BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)

Function
--------



The **advertise-community-gshut** command advertises the g-shut community attribute of the address family level.

The **undo advertise-community-gshut** command deletes the g-shut community attribute of an address family.



By default, a device is disabled from advertising the g-shut community attribute.


Format
------

**advertise-community-gshut**

**advertise-community-gshut** { **ibgp** | **ebgp** }

**undo advertise-community-gshut**

**undo advertise-community-gshut** { **ibgp** | **ebgp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ibgp** | Advertises routes with the g-shut community attribute to all IBGP peers. | - |
| **ebgp** | Advertises routes with the g-shut community attribute to all EBGP peers. | - |



Views
-----

BGP-VPN instance IPv4 address family view,BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To advertise the g-shut community attribute of the address family level to EBGP/IBGP peers, run this command. After this command is run, the system advertises routes with the g-shut community attribute to neighbors with the g-shut community attribute enabled, instructing the neighbors to switch traffic to other paths.


Example
-------

# Enable BGP to advertise the g-shut community attribute in the BGP-VPN instance IPv6 address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] advertise-community-gshut ibgp

```

# Enable BGP to advertise the g-shut community attribute in the BGP-VPN instance IPv4 address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] advertise-community-gshut ibgp

```