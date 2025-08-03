lacp m-lag system-id
====================

lacp m-lag system-id

Function
--------



The **lacp m-lag system-id** command configures a Link Aggregation Control Protocol (LACP) system ID for a member Eth-Trunk interface in an M-LAG (LACP M-LAG system ID for short).

The **undo lacp m-lag system-id** command restores the default LACP M-LAG system ID.



By default, the LACP M-LAG system ID in the system view is the system bridge MAC address.


Format
------

**lacp m-lag system-id** *mac-address*

**undo lacp m-lag system-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **system-id** *mac-address* | Specifies an LACP M-LAG system ID.  A smaller system ID indicates a higher priority. | The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number, such as 00e0 or fc01. If an H contains less than four hexadecimal digits, 0s are padded ahead. For example, if an H is e0, it is equal to 00e0.  An LACP system ID cannot be all 0s.  If the value is all Fs, the LACP system ID is restored to the default. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an M-LAG consists of Eth-Trunk interfaces working in LACP mode, each member Eth-Trunk interface and the connected peer Eth-Trunk interface use LACP M-LAG system priorities to determine the priority of the device at either end of the Eth-Trunk link. The device with the higher priority functions as the LACP Actor and determines which member interfaces in its Eth-Trunk interface are active based on the interface priorities. The other device selects the member interfaces connected to the active member interfaces on the Actor as active member interfaces. If a member Eth-Trunk interface in an M-LAG has the same LACP system priority as its connected Eth-Trunk interface, run the **lacp m-lag system-id** command to configure an LACP M-LAG system ID. In this situation, LACP system IDs are used to determine the priority of the device at either end of the Eth-Trunk link. The device with the higher priority then selects active member interfaces in its Eth-Trunk interface, and the other device selects the interconnected member interfaces to be active member interfaces.

**Precautions**

The LACP M-LAG system IDs of member Eth-Trunk interfaces on the two devices where M-LAG is deployed do not need to be configured. The devices can automatically negotiate the LACP M-LAG system IDs. If the LACP M-LAG system IDs need to be configured, the LACP M-LAG system IDs of member Eth-Trunk interfaces on the two devices must be the same.The LACP M-LAG system ID configured in the system view takes effect on all Eth-Trunk interfaces. The LACP M-LAG system ID configured in the Eth-Trunk interface view takes effect only on the Eth-Trunk interface. If this command is configured in the system view and in the view of the specified Eth-Trunk interface, the configuration in the Eth-Trunk interface view takes effect.When multiple M-LAGs are configured on the same device, different member Eth-Trunk interfaces can have different LACP M-LAG system IDs. In this case, you need to configure the LACP M-LAG system ID in the Eth-Trunk interface view.The LACP M-LAG system ID applies to an M-LAG consisting of Eth-Trunk interfaces in LACP mode, whereas the LACP system ID applies to Eth-Trunk interfaces in LACP mode. The LACP system ID is fixed (system bridge MAC address) and cannot be changed through configuration.


Example
-------

# Configure the LACP M-LAG system ID in the system view as 00E0-FC00-0000.
```
<HUAWEI> system-view
[~HUAWEI] lacp m-lag system-id 00e0-fc00-0000

```