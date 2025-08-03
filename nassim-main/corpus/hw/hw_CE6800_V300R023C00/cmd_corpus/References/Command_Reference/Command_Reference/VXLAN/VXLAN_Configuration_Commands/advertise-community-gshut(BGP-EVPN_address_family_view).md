advertise-community-gshut(BGP-EVPN address family view)
=======================================================

advertise-community-gshut(BGP-EVPN address family view)

Function
--------



The **advertise-community-gshut** command advertises the g-shut community attribute of the address family level.

The **undo advertise-community-gshut** command deletes the g-shut community attribute of an address family.



By default, a device is disabled from advertising the g-shut community attribute.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To advertise the g-shut community attribute of the address family level to EBGP/IBGP peers, run this command. After this command is run, the system advertises routes with the g-shut community attribute to neighbors with the g-shut community attribute enabled, instructing the neighbors to switch traffic to other paths.


Example
-------

# Enable BGP to advertise the g-shut community attribute in the BGP-EVPN address family.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] advertise-community-gshut ibgp

```