batch-shutdown
==============

batch-shutdown

Function
--------



The **batch-shutdown** command shuts down BFD sessions in batches so that the sessions enter the AdminDown state.

The **undo batch-shutdown** command starts BFD sessions in batches.



By default, all BFD sessions are started.


Format
------

**batch-shutdown** { **all** | **ip** }

**undo batch-shutdown** { **all** | **ip** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Shuts down all BFD sessions in batches. | - |
| **ip** | Shuts down BFD sessions of the IP link type in batches. | - |



Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a large number of BFD sessions flap, frequent link switchovers are performed. As a result, service forwarding is affected. If the **undo bfd** command is run to disable BFD to restore services, a large number of BFD configurations are lost. As a result, flapping fault locating becomes difficult. To resolve this issue, run the **batch-shutdown** command to shut down BFD sessions in batches.The **batch-shutdown** command takes effect on static BFD sessions and static self-negotiated BFD sessions. This command issues the **shutdown** commands in a batch for these types of BFD sessions. A **shutdown** command instance is generated in the view of each BFD session.

**Configuration Impact**

After the **batch-shutdown** command is run, all static BFD sessions and static auto BFD sessions or static BFD sessions and static auto BFD sessions of a specified link type enter the AdminDown state.

**Precautions**

The batch-shutdown and **shutdown** commands have the same result for a BFD session. For example, after running the **batch-shutdown all** command to shut down all BFD sessions, you can run the **undo shutdown** command to start a specified BFD session.


Example
-------

# Shut down all BFD sessions in batches.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] batch-shutdown all

```