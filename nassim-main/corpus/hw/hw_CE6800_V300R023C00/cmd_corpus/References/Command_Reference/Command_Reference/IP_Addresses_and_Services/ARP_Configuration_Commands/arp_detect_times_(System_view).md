arp detect times (System view)
==============================

arp detect times (System view)

Function
--------



The **arp detect times** command sets the aging probe times of dynamic ARP entries.

The **undo arp detect times** command restores the default setting.



By default, the aging probe times of dynamic ARP entries is 3.


Format
------

**arp detect times** *times-value*

**undo arp detect times** [ *times-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *times-value* | Specifies the aging probe times of dynamic ARP entries. | The value is an integer ranging from 0 to 10. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **arp detect times** command sets the aging probe times of dynamic ARP entries to reduce address resolution errors. Before aging a dynamic ARP entry, the system performs ARP probe. If the system does not receive any response after the number of probe times reaches the upper limit, the system deletes the ARP entry.



**Precautions**



If times-value is set to 0, dynamic ARP entries are aged directly without being probed. You are advised not to set times-value to 0. Otherwise, ARP entry update is affected, which causes service traffic forwarding failures.




Example
-------

# Set the aging probe times to 5 for dynamic ARP entries.
```
<HUAWEI> system-view
[~HUAWEI] arp detect times 5

```