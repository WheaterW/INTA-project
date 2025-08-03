group unnumbered
================

group unnumbered

Function
--------



The **group unnumbered** command creates an unnumbered peer group.

The **undo group unnumbered** command restores the default setting.



By default, no unnumbered peer group is created.


Format
------

**group** *peerGroupName* **unnumbered** { **internal** | **external** }

**group** *peerGroupName* **unnumbered**

**undo group** *peerGroupName* **unnumbered** [ **internal** | **external** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **internal** | Specifies an IBGP unnumbered peer group. | - |
| **external** | Specifies an EBGP unnumbered peer group. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



An unnumbered peer group is a group of peers that have the same policies. When a peer is added to a peer group, the peer obtains the same configuration as the peer group. The peers in a peer group can inherit the configurations of the peer group. When the configurations of the peer group change, the configurations of members in the peer group change accordingly.During network deployment based on the BGP unnumbered feature, unnumbered group configurations can be inherited to manage peers.




Example
-------

# Create an IBGP unnumbered peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test unnumbered internal

```

# Create an EBGP unnumbered peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test unnumbered external

```