dcb abs-pfc queue enable
========================

dcb abs-pfc queue enable

Function
--------



The **dcb abs-pfc queue enable** command enables antilocking PFC for queues on an interface.

The **undo dcb abs-pfc queue enable** command disables antilocking PFC for queues on an interface.



By default, this function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN and CE8850-SAN.



Format
------

**dcb abs-pfc queue** *first-queue-index* [ *second-queue-index* ] **enable** [ **threshold** *threshold-value* ]

**undo dcb abs-pfc queue** *first-queue-index* [ *second-queue-index* ] **enable** [ **threshold** *threshold-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *first-queue-index* | Specifies the index of the first queue for which antilocking PFC is to be enabled. | The value is an integer ranging from 0 to 5. |
| *second-queue-index* | Specifies the index of the second queue for which antilocking PFC is to be enabled. | The value is an integer ranging from 0 to 5. |
| **threshold** *threshold-value* | Specifies the buffer threshold for antilocking PFC to take effect. | The value is an integer that ranges from 0 to 512. The unit is KB and the default value is 0. |



Views
-----

100GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If lossless services on the live network have a long communication distance, for example, in a long-distance DCI scenario, you can run this command to enable antilocking PFC for interface queues.

**Precautions**

* For the CE6860-SAN: The antilocking PFC function can be enabled on 25GE interfaces 1 to 48, 50GE interfaces 1 to 48, 100GE interfaces 1 to 8, 200GE interfaces 2, 4, 6, and 8, and interfaces split from 100GE interfaces 2, 4, 6, and 8.For the CE8850-SAN: The antilocking PFC function can be enabled on 100GE interfaces 1 to 8 and interfaces split from them.
* The **dcb abs-pfc queue enable** and **dcb pfc enable** commands are mutually exclusive on the same interface.
* Antilocking PFC takes effect only when the following conditions are met: (1) The **buffer optimization mode enhanced-long-distance** command has been run to set the plane buffer optimization mode to enhanced long-distance mode, and the setting has taken effect upon a device restart. (2) The **long-distance mode** command has been run to enable the long-distance detection mode, and a detection success message has been returned.
* Antilocking PFC can take effect only on antilocking PFC-capable interfaces specified by the Interface that can be enabled with ABS PFC field of the **display buffer optimization configuration** command output.
* In scenarios such as device upgrade and restart, long-distance detection may fail. As a result, antilocking PFC becomes invalid. In this case, you can run the **start long-distance detect** command to manually send detection packets.
* In a priority queue of an interface, antilocking PFC is mutually exclusive with differentiated flow scheduling.
* On an interface, antilocking PFC for priority queue 1 is mutually exclusive with differentiated flow scheduling for any queue.
* If PFC or antilocking PFC has been enabled on an interface, PFC resources on the interface will be occupied. To release PFC resources on the interface, disable PFC or antilocking PFC on the interface and restart the device.
* Currently, PFC or antilocking PFC can be enabled on a maximum of 127 interfaces. If the number of interfaces on which PFC or antilocking PFC has been enabled exceeds 127, disable the delivered configuration to reduce the number of interfaces on which PFC or antilocking PFC has been enabled, and restart the device before you can enable PFC or antilocking PFC on more interfaces.
* Antilocking PFC can be enabled for a maximum of 20 queues on the device.

Example
-------

# Enable antilocking PFC on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] dcb abs-pfc queue 3 enable threshold 0

```