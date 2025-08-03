shutdown (BGP multi-instance view)
==================================

shutdown (BGP multi-instance view)

Function
--------



The **shutdown** command terminates all sessions between a device and its BGP peers.

The **undo shutdown** command restores all sessions between a device and its BGP peers.



By default, the function of terminating all sessions between a device and its BGP peers is disabled.


Format
------

**shutdown**

**undo shutdown**


Parameters
----------

None

Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Running this command causes all BGP peers unable to establish sessions. Exercise caution when using this command.During the system upgrade, or maintenance, you can run the **shutdown** command to terminate all sessions between a device and its BGP peers to prevent possible BGP route flapping from affecting the network. After the system upgrade, or maintenance, run the undo **shutdown** command to restore the sessions. If a large number of BGP sessions exist, terminating BGP sessions one by one using the **peer ignore** command is inefficient. Running the **shutdown** command in the BGP view terminates all BGP sessions at one time.Although BGP sessions take effect only after you run the commit command in two-phase validation mode, the **shutdown** command is necessary in the following situations:

* The two-phase validation mode is changed to the immediate validation mode.
* Some configurations have been committed.
* The script files are used for the upgrade or maintenance.

Example
-------

# Terminate all sessions between the device and its BGP peers.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] shutdown

```