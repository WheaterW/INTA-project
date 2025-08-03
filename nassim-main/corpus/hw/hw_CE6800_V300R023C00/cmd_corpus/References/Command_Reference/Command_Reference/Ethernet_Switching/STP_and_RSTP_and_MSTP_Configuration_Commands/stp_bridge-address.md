stp bridge-address
==================

stp bridge-address

Function
--------



The **stp bridge-address** command configures a bridge MAC address used by the device to calculate the spanning tree.

The **undo stp bridge-address** command restores the default configuration.



By default, a device uses its MAC address as the bridge MAC address to calculate the spanning tree.


Format
------

**stp bridge-address** *mac-address*

**undo stp bridge-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a bridge MAC address used by the device to calculate the spanning tree. | The value is in the H-H-H format. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In some special applications, two devices must simulate one root bridge. Specifically, the bridge IDs of BPDUs sent by both devices must be the same. However, because each device has a unique MAC address, the bridge IDs of devices are different. To configure the same bridge MAC address for the two devices, run the **stp bridge-address** command.



**Follow-up Procedure**



Configure the same spanning tree protocol parameters, such as the same device priority and timer, on the devices, so that the two devices can simulate the same root bridge.



**Precautions**



A bridge MAC address identifies a device. If different devices send packets with the same bridge MAC address, other devices consider the received packets to be sent by the same device. Therefore, exercise caution when running the **stp bridge-address** command.




Example
-------

# Configure the bridge MAC address used by the device to calculate the spanning tree as 00e0-fc12-3456.
```
<HUAWEI> system-view
[~HUAWEI] stp bridge-address 00e0-fc12-3456

```