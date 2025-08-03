lacp m-lag system-id (Eth-Trunk interface view)
===============================================

lacp m-lag system-id (Eth-Trunk interface view)

Function
--------



The **lacp m-lag system-id** command configures a Link Aggregation Control Protocol (LACP) system ID (LACP M-LAG system ID for short) for an M-LAG member Eth-Trunk interface.

The **undo lacp m-lag system-id** command resets the LACP M-LAG system ID.



By default, no default LACP M-LAG system ID exists in the Eth-Trunk interface view.


Format
------

**lacp m-lag system-id** *mac-address*

**undo lacp m-lag system-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **system-id** *mac-address* | Specifies an LACP M-LAG system ID.  A smaller system ID indicates a higher priority. | The value is in the format of H-H-H. Each H is a 4-digit hexadecimal number, such as 00e0 and fc01. If you enter less than four digits, 0s are added before the entered digits. For example, if you enter e0, 00e0 is displayed.  The LACP system ID cannot be all 0s.  If the value is all Fs, the LACP system ID is reset. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an M-LAG consists of Eth-Trunk interfaces working in LACP mode, each member Eth-Trunk interface and the connected peer Eth-Trunk interface use LACP M-LAG system priorities to determine the priority of the device at either end of the Eth-Trunk link. The device with the higher priority functions as the LACP Actor and determines which member interfaces in its Eth-Trunk interface are active based on the interface priorities. The other device selects the member interfaces connected to the active member interfaces on the Actor as active member interfaces. If a member Eth-Trunk interface in an M-LAG has the same LACP system priority as its connected Eth-Trunk interface, run the **lacp m-lag system-id** command to configure an LACP M-LAG system ID. In this situation, LACP system IDs are used to determine the priority of the device at either end of the Eth-Trunk link. The device with the higher priority then selects active member interfaces in its Eth-Trunk interface, and the other device selects the interconnected member interfaces to be active member interfaces.

**Prerequisites**

The working mode of an Eth-Trunk interface has been set to the static LACP mode using the **mode lacp-static** command in the Eth-Trunk interface view or the dynamic LACP mode using the mode lacp-dynamic command.

**Precautions**

The LACP M-LAG system IDs of member Eth-Trunk interfaces on the two devices where M-LAG is deployed do not need to be configured. The devices can automatically negotiate the LACP M-LAG system IDs. If the LACP M-LAG system IDs need to be configured, the LACP M-LAG system IDs of member Eth-Trunk interfaces on the two devices must be the same.The LACP M-LAG system ID configured in the system view takes effect on all Eth-Trunk interfaces. The LACP M-LAG system ID configured in the Eth-Trunk interface view takes effect only on the Eth-Trunk interface. If this command is configured in the system view and in the view of the specified Eth-Trunk interface, the configuration in the Eth-Trunk interface view takes effect.When multiple M-LAGs are configured on a device, different member Eth-Trunk interfaces can have different LACP M-LAG system IDs. In this case, you need to configure the LACP M-LAG system ID in the Eth-Trunk interface view.The LACP M-LAG system ID applies to an M-LAG consisting of Eth-Trunk interfaces in LACP mode. The LACP system ID applies to Eth-Trunk interfaces in LACP mode. The LACP system ID is fixed (MAC address of the device's Ethernet interface) and cannot be changed through configuration.


Example
-------

# Configure the LACP M-LAG system ID as xxxx-xxxx-xxxx in the Eth-Trunk interface view.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 10
[*HUAWEI-Eth-Trunk10] mode lacp-static
[*HUAWEI-Eth-Trunk10] lacp m-lag system-id xxxx-xxxx-xxxx

```