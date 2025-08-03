stub (OSPF area view)
=====================

stub (OSPF area view)

Function
--------



The **stub** command configures an area as a stub area.

The **undo stub** command cancels the configuration.



By default, no area is configured as a stub area.


Format
------

**stub** [ **no-summary** | { **default-route-advertise** **backbone-peer-ignore** } ] \*

**undo stub**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **no-summary** | Prevents the ABR from sending Summary LSAs to the stub area. | - |
| **default-route-advertise** | Controls the default route's advertisement. | - |
| **backbone-peer-ignore** | Prevents the ABR from checking the neighbor status. | - |



Views
-----

OSPF area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

There are two stub area-related commands: stub and default-cost (OSPF). If you want to configure one area as a stub area, run the stub command on all devices in the area.The default-cost (OSPF) command is used to specify the cost of the default summary route that the ABR sends to the stub area. The command takes effect only when it is run on an ABR.On an ABR, you can configure no-summary in the stub command to prevent Type 3 LSAs from entering the stub area to which the ABR connects.If default-route-advertise and backbone-peer-ignore are configured in the command, the ABR is prevented from checking the neighbor status when it generates a default Type 3 LSA and advertises it to the stub area.


Example
-------

# Configure OSPF area 1 as a stub area.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] area 1
[*HUAWEI-ospf-100-area-0.0.0.1] stub no-summary default-route-advertise backbone-peer-ignore

```