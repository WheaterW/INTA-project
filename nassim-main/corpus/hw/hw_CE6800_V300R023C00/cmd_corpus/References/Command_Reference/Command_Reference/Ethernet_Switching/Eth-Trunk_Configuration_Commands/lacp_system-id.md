lacp system-id
==============

lacp system-id

Function
--------



The **lacp system-id** command configures an LACP system ID for an Eth-Trunk interface.

The **undo lacp system-id** command restores the default LACP system ID of an Eth-Trunk interface.



By default, an LACP system ID of an Eth-Trunk interface is the system bridge MAC address.


Format
------

**lacp system-id** *mac-address*

**undo lacp system-id**

**undo lacp system-id** *mac-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **system-id** *mac-address* | Specifies the LACP system ID of an Eth-Trunk interface. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. An LACP system ID cannot be all 0s.  If the value is all Fs, the LACP system ID is restored to the default. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When devices are connected through Eth-Trunk interfaces in LACP mode, the device with a higher LACP system priority functions as the LACP Actor. The other device then selects active member interfaces based on the interface priorities of the LACP Actor. If the two connected devices have the same LACP system priority, the LACP system IDs determine the device priorities. To configure an LACP system ID, run the **lacp system-id** command. The device with a higher priority then becomes the LACP Actor. The other device then selects active member interfaces based on the interface priorities of the LACP Actor.When Eth-Trunk interfaces in static LACP mode are associated with the same VRRP group, you must run the **lacp system-id** command to configure the same LACP system ID for the Eth-Trunk interfaces so that the VRRP group takes effect.




Example
-------

# Set the LACP system ID to 00e0-fc12-3456 for an Eth-Trunk interface view.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 10
[*HUAWEI-Eth-Trunk10] mode lacp-static
[*HUAWEI-Eth-Trunk10] lacp system-id 00e0-fc12-3456

```