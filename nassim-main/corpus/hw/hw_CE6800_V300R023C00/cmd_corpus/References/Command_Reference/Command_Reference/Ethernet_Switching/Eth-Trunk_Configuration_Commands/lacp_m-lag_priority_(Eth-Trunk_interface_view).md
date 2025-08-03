lacp m-lag priority (Eth-Trunk interface view)
==============================================

lacp m-lag priority (Eth-Trunk interface view)

Function
--------



The **lacp m-lag priority** command configures a Link Aggregation Control Protocol (LACP) priority for a member Eth-Trunk interface in an M-LAG (LACP M-LAG system priority for short).

The **undo lacp m-lag priority** command restores the default LACP M-LAG system priority.



By default,no default LACP M-LAG system priority exists in the Eth-Trunk interface view.


Format
------

**lacp m-lag priority** *priority*

**undo lacp m-lag priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** *priority* | Specifies an LACP M-LAG system priority. A smaller value indicates a higher priority. | The value is an integer ranging from 0 to 65535. The smaller the LACP priority value, the higher the priority. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an M-LAG consists of Eth-Trunk interfaces working in LACP mode, each member Eth-Trunk interface and the connected peer Eth-Trunk interface use LACP M-LAG system priorities to determine the priority of the device at either end of the Eth-Trunk link. The device with the higher priority functions as the LACP Actor and determines which member interfaces in its Eth-Trunk interface are active based on the interface priorities. The other device selects the member interfaces connected to the active member interfaces on the Actor as active member interfaces.

You can run the **lacp m-lag priority** command to configure the LACP priority of the member Eth-Trunk interface in the M-LAG. In this situation, LACP priorities determine the priorities of devices on both ends of the Eth-Trunk link, and the device with the higher priority selects active member interfaces in its Eth-Trunk interface based on interface priorities.

**Prerequisites**

The working mode of an Eth-Trunk interface has been set to the static LACP mode using the **mode lacp-static** command in the Eth-Trunk interface view or the dynamic LACP mode using the mode lacp-dynamic command.

**Precautions**

The member Eth-Trunk interfaces in an M-LAG must have the same LACP M-LAG system priority.The LACP M-LAG system priority configured in the system view takes effect on all Eth-Trunk interfaces. The LACP M-LAG system priority configured in the Eth-Trunk interface view takes effect only on the Eth-Trunk interface. If the **lacp m-lag priority** command is configured both in the system view and the Eth-Trunk interface view, the LACP M-LAG system priority configured in the Eth-Trunk interface view takes precedence.If multiple MC-LAGs are configured on a device, member Eth-Trunk interfaces in different MC-LAGs may have different LACP M-LAG system priorities. In this situation, run the **lacp m-lag priority** command in the Eth-Trunk interface view to configure the LACP M-LAG system priority.The LACP M-LAG system priority applies to the M-LAG consisting of Eth-Trunk interfaces working in LACP mode and is configured using the **lacp m-lag priority** command, while the LACP system priority applies to the Eth-Trunk interfaces working in LACP mode and is configured using the **lacp priority** command.If the LACP M-LAG system priority and LACP system priority are both configured, after an Eth-Trunk interface working in LACP mode is added to an M-LAG, only the LACP M-LAG system priority takes effect for the Eth-Trunk interface.


Example
-------

# Configure the LACP M-LAG system priority as 10 in the Eth-Trunk interface view.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 10
[*HUAWEI-Eth-Trunk10] mode lacp-static
[*HUAWEI-Eth-Trunk10] lacp m-lag priority 10

```