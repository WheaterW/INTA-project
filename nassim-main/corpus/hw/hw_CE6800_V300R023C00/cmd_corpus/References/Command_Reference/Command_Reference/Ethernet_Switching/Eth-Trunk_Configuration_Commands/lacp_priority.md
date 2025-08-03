lacp priority
=============

lacp priority

Function
--------



The **lacp priority** command sets a Link Aggregation Control Protocol (LACP) system priority.

The **undo lacp priority** command restores the default LACP system priority.



The default LACP priority is 32768.


Format
------

**lacp priority** *priority*

**undo lacp priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** *priority* | Specifies an LACP system priority. | The value is an integer ranging from 0 to 65535. The smaller the priority value, the higher the priority. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



LACP system priorities are set to prioritize the device at either end of an Eth-Trunk link. The device with a higher system priority is selected as the Actor, and then active member interfaces are selected according to the configuration of the Eth-Trunk interface on the Actor.If neither of the device at either end of an Eth-Trunk link is configured with a system priority, the devices use the default value 32768. In this case, the Actor is selected based on the system ID. That is, the device with the smaller system ID becomes the Actor. You can run the lacp priority command in the system view to change the Actor of an Eth-Trunk link



**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode.




Example
-------

# Set the LACP system priority to 1.
```
<HUAWEI> system-view
[~HUAWEI] lacp priority 1

```