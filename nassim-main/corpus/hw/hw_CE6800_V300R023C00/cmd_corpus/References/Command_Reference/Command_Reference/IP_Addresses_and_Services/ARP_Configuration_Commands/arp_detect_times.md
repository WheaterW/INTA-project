arp detect times
================

arp detect times

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

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view,Management interface view


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

# Set the aging probe times to 5 for dynamic ARP entries on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp detect times 5

```