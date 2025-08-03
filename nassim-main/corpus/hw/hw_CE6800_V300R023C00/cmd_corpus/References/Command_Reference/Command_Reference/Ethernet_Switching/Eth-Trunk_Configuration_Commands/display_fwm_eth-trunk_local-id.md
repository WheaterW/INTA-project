display fwm eth-trunk local-id
==============================

display fwm eth-trunk local-id

Function
--------



The **display fwm eth-trunk local-id** command displays Eth-Trunk ID information in the forwarding and control planes.




Format
------

**display fwm eth-trunk** *trunk-id* **local-id** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk. | The value is an integer in the range from 0 to 1023. |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 15 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After an Eth-Trunk interface is successfully configured, you can run the command to view the configuration of the Eth-Trunk interface, you can run the display fwm eth-trunk local-id command to check Eth-Trunk ID information in the forwarding and control planes. The command output helps analyze and locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display Eth-Trunk ID information in the forwarding and control planes.
```
<HUAWEI> display fwm eth-trunk 5 local-id
Slot     Control ID     Local ID
----------------------------------------
1                 3            3
----------------------------------------

```

**Table 1** Description of the **display fwm eth-trunk local-id** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Control ID | Eth-Trunk ID in the control plane. |
| Local ID | Eth-Trunk ID in the forwarding plane. |