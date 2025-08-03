default-cost
============

default-cost

Function
--------



The **default-cost** command sets the cost of the Type 3 default routes that OSPF sends to a Stub area.

The **undo default-cost** command restores the default setting.



By default, the cost of the Type 3 default routes that OSPF sends to a Stub area is 1.


Format
------

**default-cost** *costvalue*

**undo default-cost**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *costvalue* | Specifies the cost of the Type 3 default routes that OSPF sends to a Stub area. | The value ranges from 0 to 16777214. |



Views
-----

OSPF area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Configuring the cost of a default route can control OSPF route selection result, improving network flexibility.This command is applicable only to the ABRs connected to a Stub area.

**Prerequisites**

A default route exists in the local routing table.


Example
-------

# Set area 1 as a Stub area, and set the cost of the Type 3 default routes to be sent to this Stub area to 20.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] area 1
[*HUAWEI-ospf-100-area-0.0.0.1] stub
[*HUAWEI-ospf-100-area-0.0.0.1] default-cost 20

```