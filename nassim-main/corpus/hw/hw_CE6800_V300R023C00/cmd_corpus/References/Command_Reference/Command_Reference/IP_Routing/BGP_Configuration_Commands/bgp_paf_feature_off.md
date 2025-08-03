bgp paf feature off
===================

bgp paf feature off

Function
--------



The **bgp paf feature off** command disables the PAF restriction for a specified BGP feature.

The **undo bgp paf feature off** command enables the PAF restriction for a specified BGP feature.



By default, the PAF restriction for each BGP feature is enabled.


Format
------

**bgp paf feature** *featureName* **off**

**undo bgp paf feature** *featureName* **off**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *featureName* | Specifies a feature name. | The value is of the enumerated type:  route-num-all-peer: feature indicating whether the number of routes received from all peers in a BGP address family exceeds the upper limit. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The feature indicating whether the number of routes received from all peers in a BGP address family exceeds the upper limit can be restricted by the PAF. With the PAF restriction, if the number of received routes exceeds 80% of the upper limit, a threshold alarm is generated. If the number exceeds the upper limit, a threshold-crossing alarm is generated, and the excess routes are discarded. To enable the local device to continue to receive routes even after the number exceeds the upper limit, run the **bgp paf feature off** command to disable the PAF restriction for this feature.

**Precautions**

If the number of routes on a device has exceeded the upper limit, the discarded excess routes cannot be restored automatically after the PAF restriction is disabled. To address this issue, run the **refresh bgp** command.


Example
-------

# Disable the PAF restriction for the feature indicating whether the number of routes received from all peers in a BGP address family exceeds the upper limit.
```
<HUAWEI> system-view
[~HUAWEI] bgp paf feature route-num-all-peer off
Warning: This operation will cause the system to be out of PAF protection. [Y/N]:y

```