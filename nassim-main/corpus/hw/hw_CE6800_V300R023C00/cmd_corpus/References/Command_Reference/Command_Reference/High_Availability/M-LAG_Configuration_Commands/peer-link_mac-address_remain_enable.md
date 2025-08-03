peer-link mac-address remain enable
===================================

peer-link mac-address remain enable

Function
--------



The **peer-link mac-address remain enable** command configures an M-LAG device not to trigger the local or peer M-LAG device to delete the corresponding MAC address on the peer-link interface under certain conditions.

The **undo peer-link mac-address remain enable** command configures an M-LAG device to trigger the local or peer M-LAG device to delete the corresponding MAC address on the peer-link interface under certain conditions.



By default, the M-LAG device does not trigger the local or peer M-LAG device to delete the corresponding MAC address on the peer-link interface under certain conditions.


Format
------

**peer-link mac-address remain enable** { **unpaired-port** | **paired-port** }

**undo peer-link mac-address remain enable** { **unpaired-port** | **paired-port** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unpaired-port** | Indicates that the M-LAG device does not trigger the peer M-LAG device to delete the corresponding MAC address on the peer-link interface when an M-LAG single-homing interface fails. | - |
| **paired-port** | Indicates that the M-LAG device does not trigger the local M-LAG device to delete the corresponding MAC address on the peer-link interface when an M-LAG single-homing interface is changed to a dual-homing interface. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG scenario, you can configure an M-LAG device not to trigger the local or peer M-LAG device to delete the corresponding MAC address on the peer-link interface under the following conditions:When an M-LAG single-homing interface is changed to a dual-homing interface and there are a large number of M-LAG interfaces on the entire network, you can configure the **peer-link mac-address remain enable paired-port** command to prevent a large amount of flooding traffic from affecting device performance.When an access device is single-homed to the M-LAG, the outbound interface of the MAC address entry on the peer M-LAG device to the M-LAG member interface is the peer-link interface. By default, if the M-LAG member interface fails, the peer M-LAG device is triggered to delete MAC addresses on the peer-link interface in batches. If the M-LAG member interface alternates between Up and Down states, the peer M-LAG device is repeatedly triggered to delete MAC addresses on the peer-link interface in batches, causing broadcast traffic flooding. By default, an M-LAG device does not trigger the peer M-LAG device to delete the corresponding MAC address on the peer-link interface when a device is single-homed to the M-LAG and the connected M-LAG member interface is Down.


Example
-------

# Configure an M-LAG device not to trigger the peer M-LAG device to delete the corresponding MAC address on the peer-link interface when a device is single-homed to the M-LAG and the connected M-LAG member interface is Down.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] undo peer-link mac-address remain enable unpaired-port

```