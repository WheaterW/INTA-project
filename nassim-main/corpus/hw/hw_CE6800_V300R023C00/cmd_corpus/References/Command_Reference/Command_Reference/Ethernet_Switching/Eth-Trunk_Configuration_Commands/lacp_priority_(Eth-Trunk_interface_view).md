lacp priority (Eth-Trunk interface view)
========================================

lacp priority (Eth-Trunk interface view)

Function
--------



The **lacp priority** command sets the LACP system priority for an Eth-trunk interface.

The **undo lacp priority** command restores the default LACP system priority of an Eth-Trunk interface.



The default LACP priority is 32768.


Format
------

**lacp priority** *priority*

**undo lacp priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** *priority* | Specifies the LACP system priority of the current Eth-Trunk interface. | The value is an integer ranging from 0 to 65535. The smaller the priority value, the higher the priority. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To change the Actor of an Eth-Trunk, run this command in the Eth-Trunk view.LACP system priorities are set to prioritize the devices at both ends of an Eth-Trunk. The device with a higher system priority is selected as the Actor, and then active member interfaces are selected according to the configuration of the Eth-Trunk interface on the Actor.The system priority configured in the Eth-Trunk view is preferentially used as the Eth-Trunk system priority. If the system priority is not configured in the Eth-Trunk interface view, the global system priority is used.If neither of the devices at the two ends of an Eth-Trunk is configured with the system priority, the devices adopt the default value 32768. In this case, the Actor is selected according to the system ID. That is, the device with the smaller system ID becomes the Actor.



**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode.




Example
-------

# Set the LACP priority to 1.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 10
[*HUAWEI-Eth-Trunk10] mode lacp-static
[*HUAWEI-Eth-Trunk10] lacp priority 1

```