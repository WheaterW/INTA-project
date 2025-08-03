abs-pfc priority enable
=======================

abs-pfc priority enable

Function
--------



The **abs-pfc priority enable** command enables dragonfly antilocking PFC for interface queues in a dragonfly profile.

The **undo abs-pfc priority enable** command disables dragonfly antilocking PFC for interface queues in a dragonfly profile.



By default, dragonfly antilocking PFC is disabled for interface queues in a dragonfly profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**abs-pfc priority** { *prioritynumber* } &<1-3> **enable** [ **threshold** *threshold-value* ]

**undo abs-pfc priority** { *prioritynumber* } &<1-3> **enable** [ **threshold** *threshold-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *prioritynumber* | Specifies the index of a queue for which dragonfly antilocking PFC is enabled. | The value is an integer ranging from 0 to 5. |
| **threshold** *threshold-value* | Specifies the buffer threshold for dragonfly antilocking PFC to take effect. | The value is an integer that ranges from 0 to 512. The unit is KB and the default value is 0. |



Views
-----

Dragonfly-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a lossless network with direct connections, you can run this command to enable dragonfly antilocking PFC for interface queues in a dragonfly profile.

**Precautions**

* If dragonfly antilocking PFC is enabled in the dragonfly profile, dragonfly antilocking PFC is enabled on the interface where the adaptive routing function is enabled.
* If dragonfly antilocking PFC is enabled in the dragonfly profile and adaptive routing is enabled on an interface, you need to run the **qos hpc enhanced** command to ensure that packets in queues 6 and 7 are not discarded.
* If dragonfly antilocking PFC is enabled in the dragonfly profile, the bandwidths of the interfaces enabled with the adaptive routing function on the device must be the same.
* Dragonfly antilocking PFC can be enabled for a maximum of three queues on an interface.
* The total number of queues for which dragonfly antilocking PFC is enabled on all interfaces of a device cannot exceed 90.
* PFC and dragonfly antilocking PFC cannot be enabled on the same interface at the same time.
* Antilocking PFC and dragonfly antilocking PFC cannot be enabled on the same interface at the same time.
* On an interface, dragonfly antilocking PFC for priority queue 1 and differentiated flow scheduling for any queue cannot be enabled at the same time.
* Dragonfly antilocking PFC and differentiated flow scheduling cannot be enabled for queues of the same priority on the same interface at the same time.
* If dragonfly deadlock prevention has been enabled for a queue of a certain priority, you need to disable this function for the queue before disabling dragonfly antilocking PFC for the queue.
* If PFC or antilocking PFC has been enabled on an interface, PFC resources on the interface will be occupied. To release PFC resources on the interface, disable PFC or antilocking PFC on the interface and restart the device.
* Currently, the device supports PFC or antilocking PFC on a maximum of 127 interfaces. If the number of interfaces on which PFC or antilocking PFC has been enabled exceeds 127, disable delivered configurations to reduce the number of interfaces on which PFC or antilocking PFC has been enabled, and restart the device, so that the number of interfaces enabled with PFC or antilocking PFC can be increased.

Example
-------

# Enable dragonfly antilocking PFC for interface queues in the default dragonfly profile.
```
<HUAWEI> system-view
[~HUAWEI] dragonfly profile default
[~HUAWEI-dragonfly-profile-default] abs-pfc priority 2 3 4 enable threshold 10

```