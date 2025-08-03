peer ignore (BGP multi-instance view) (group)
=============================================

peer ignore (BGP multi-instance view) (group)

Function
--------



The **peer ignore** command prevents a BGP device from establishing a session with a peer group.

The **undo peer ignore** command cancels the configuration.



By default, a BGP device is allowed to establish a session with a BGP peer group.


Format
------

**peer** *group-name* **ignore**

**undo peer** *group-name* **ignore**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a peer session needs to be interrupted temporarily and a large number of configurations exist on the peer, you can run the **peer ignore** command to reduce the reconfiguration workload. For example, if the peer relationship is frequently established due to the upgrade or link adjustment of the peer end within a period of time, you can run this command on the stable end to temporarily interrupt the BGP peer relationship to prevent frequent route or peer relationship flapping.You can run this command to terminate the session with a specified peer group and clear all related routing information. For a peer group, this means that a large number of sessions with the peers are terminated suddenly.



**Configuration Impact**



After a BGP session is successfully established, running the **peer ignore** command interrupts the BGP session. The interrupted BGP session cannot be established again, and the status of the corresponding BGP peer relationship is displayed as Idle.




Example
-------

# Prohibit a device from establishing any session with the peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instanc a
[*HUAWEI-bgp-instance-a] group test
[*HUAWEI-bgp-instance-a] peer test ignore

```