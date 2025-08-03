if-match protocol
=================

if-match protocol

Function
--------



The **if-match protocol** command configures a protocol-based filtering rule to match routes of a specified protocol.

The **undo if-match protocol** command deletes a protocol-based filtering rule.



By default, no protocol-based filtering rule is configured.


Format
------

**if-match protocol** { **direct** | **static** | **isis** | **bgp** | **ospf** | **rip** | **ospfv3** | **ripng** } \*

**undo if-match protocol**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **direct** | Matches direct routes. | - |
| **static** | Matches static routes. | - |
| **isis** | Matches IS-IS routes. | - |
| **bgp** | Matches BGP routes. | - |
| **ospf** | Matches OSPF routes. | - |
| **rip** | Matches RIP routes. | - |
| **ospfv3** | Matches OSPFv3 routes. | - |
| **ripng** | Matches RIPng routes. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To match routes of a specified protocol, run the **if-match protocol** command.




Example
-------

# Configure a filtering rule to match direct, static, and OSPF routes.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match protocol direct static ospf

```