dual-active detection hold-time
===============================

dual-active detection hold-time

Function
--------



The **dual-active detection hold-time** command sets the DAD delay during M-LAG heartbeat recovery.

The **undo dual-active detection hold-time** command restores the default DAD delay during M-LAG heartbeat recovery.



By default, the DAD delay upon M-LAG heartbeat recovery is 3 seconds.


Format
------

**dual-active detection hold-time** *holdtime*

**undo dual-active detection hold-time** *holdtime*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *holdtime* | DAD delay during M-LAG heartbeat recovery. | The value is an integer ranging from 100 to 10000, in milliseconds. The default value is 3000 ms. |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the peer-link fails but the DAD heartbeat status is normal, DAD acceleration is triggered immediately and three DAD packets are separately sent at an interval of 200 ms. As a result, exceptions occur in the following scenario:

* Secondary M-LAG fault scenario: After an interface on the standby device enters the Error-Down state due to a peer-link fault, the active device fails. In this case, the interface in the Error-Down state on the standby device goes up and forwards traffic. After the active device restarts, if the heartbeat of the active device recovers before the peer-link interface recovers, the peer-link is faulty but the DAD heartbeat status is normal, triggering DAD acceleration. As a result, the interface on the standby device enters the Error-Down state.

To solve the preceding problem, if the DAD heartbeat status recovers when the peer-link is faulty, three DAD packets are sent at an interval of 200 ms after the DAD delay (3s by default). This prevents DAD acceleration from being incorrectly triggered, so that interfaces on the standby switch do not mistakenly enter the Error-Down state.

**Precautions**



If the system software is upgraded from an earlier version to V300R023C00, the default value of the hold-time parameter changes to 10 seconds after the DB/CFG upgrade.




Example
-------

# Set the DAD delay during M-LAG heartbeat recovery.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] dual-active detection hold-time 100

```