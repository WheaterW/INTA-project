reset arp fast-reply statistics
===============================

reset arp fast-reply statistics

Function
--------



The **reset arp fast-reply statistics** command resets statistics on ARP fast reply packets on the board in a specified slot.




Format
------

**reset arp fast-reply slot** *slot-id* **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Clears statistics on ARP fast reply packets in a specified slot. The slot ID range varies according to the device hardware. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To recollect statistics on ARP fast reply packets on each interface, run the **reset arp fast-reply slot statistics** command to clear existing statistics.


Example
-------

# Reset statistics on ARP fast reply on the board in a specified slot.
```
<HUAWEI> reset arp fast-reply slot 1 statistics

```