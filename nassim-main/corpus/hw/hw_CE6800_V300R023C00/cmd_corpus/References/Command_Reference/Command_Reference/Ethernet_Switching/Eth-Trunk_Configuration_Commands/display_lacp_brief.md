display lacp brief
==================

display lacp brief

Function
--------



The **display lacp brief** command displays brief Link Aggregation Control Protocol (LACP) information, including the LACP system priority and system ID.




Format
------

**display lacp brief**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

LACP system priorities or IDs determine which Eth-Trunk interface in static LACP mode at either end of an Eth-Trunk link can function as the Actor.

* The two Eth-Trunk interfaces first compare their LACP system priorities. The one with a smaller LACP system priority is selected as the Actor.The default LACP system priority is 32768. It can be changed using the **lacp priority** command.
* If the two Eth-Trunk interfaces have the same LACP system priority, they compare their system IDs. The one with a smaller system ID is selected as the Actor.The default LACP system ID is the MAC address of an devices Ethernet interface.The **display eth-trunk** command can be used to check the LACP system priority and system ID only after an Eth-Trunk interface working in static LACP mode is configured, causing inconvenience in network planning. To facilitate network planning, you can run the **display lacp brief** command to check the LACP system priority and system ID when no Eth-Trunk interface working in static LACP mode is configured.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief LACP information.
```
<HUAWEI> display lacp brief
System Priority:32768
System ID      :00e0-fc12-3457

```

**Table 1** Description of the **display lacp brief** command output
| Item | Description |
| --- | --- |
| System Priority | LACP system priority, which can be changed using the lacp priority command. |
| System ID | LACP system ID, which is fixed at the MAC address of an Ethernet interface on the device's main control board. |