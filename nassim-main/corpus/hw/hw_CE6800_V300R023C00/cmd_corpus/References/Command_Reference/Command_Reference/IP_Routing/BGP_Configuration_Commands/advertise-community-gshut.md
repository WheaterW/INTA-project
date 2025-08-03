advertise-community-gshut
=========================

advertise-community-gshut

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

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To advertise the g-shut community attribute of the address family level to EBGP/IBGP peers, run this command. After this command is run, the system advertises routes with the g-shut community attribute to neighbors with the g-shut community attribute enabled, instructing the neighbors to switch traffic to other paths.




Example
-------

# Advertise the g-shut community attribute in an address family.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] advertise-community-gshut ibgp

```