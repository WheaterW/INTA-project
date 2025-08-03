reset drop-event flow-cache
===========================

reset drop-event flow-cache

Function
--------



The **reset drop-event flow-cache** command clears the packet loss visualization flow table.




Format
------

**reset drop-event flow-cache** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID of a card. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the reset drop-event flow-cache command to delete detailed information from the packet loss visualization flow table locally and report the flow entries to the collector.


Example
-------

# Clear the packet loss visualization flow table.
```
<HUAWEI> reset drop-event flow-cache

```