advertise-community-gshut(BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)
====================================================================================================

advertise-community-gshut(BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)

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

BGP-IPv4 unicast address family view,BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To advertise the g-shut community attribute of the address family level to EBGP/IBGP peers, run this command. After this command is run, the system advertises routes with the g-shut community attribute to neighbors with the g-shut community attribute enabled, instructing the neighbors to switch traffic to other paths.


Example
-------

# Enable BGP to advertise the g-shut community attribute in the BGP-IPv6 unicast address family.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] advertise-community-gshut ibgp

```

# Enable BGP to advertise the g-shut community attribute in the BGP-IPv4 unicast address family.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] advertise-community-gshut ibgp

```