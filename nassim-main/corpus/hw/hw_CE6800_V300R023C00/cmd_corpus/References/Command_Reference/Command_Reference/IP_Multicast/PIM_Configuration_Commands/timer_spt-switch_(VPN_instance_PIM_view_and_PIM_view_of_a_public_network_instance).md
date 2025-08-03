timer spt-switch (VPN instance PIM view/PIM view of a public network instance)
==============================================================================

timer spt-switch (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **timer spt-switch** command sets the interval for checking whether the rate at which multicast data is transmitted exceeds the threshold that can trigger data switching from a rendezvous point tree (RPT) to a shortest path tree (SPT).

The **undo timer spt-switch** command restores the default value.



By default, the interval is 15 seconds.


Format
------

**timer spt-switch** *interval*

**undo timer spt-switch**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Interval for checking whether the rate at which multicast data is transmitted exceeds the threshold that can trigger data switching from an RPT to an SPT. | The value is an integer that ranges from 15 to 65535, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **multicast routing-enable** command is run in the public network instance view or VPN instance view.Before using the **timer spt-switch** command, you must use the **spt-switch-threshold** command to set the rate threshold that can trigger data switching from an RPT to an SPT. Otherwise, running the **timer spt-switch** command is meaningless.

**Configuration Impact**

If the **timer spt-switch** command is run several times, the latest configuration overrides the previous one.

**Precautions**

In an MVPN S-PMSI scenario, if the number of multicast entries in the VPN instance is more than 16K and less than 32K, run the **timer spt-switch** command to set the interval to 120 seconds.


Example
-------

# In the public network instance, set the interval for checking whether the rate at which multicast data is transmitted exceeds the threshold that can trigger data switching from an RPT to an SPT to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] timer spt-switch 30

```