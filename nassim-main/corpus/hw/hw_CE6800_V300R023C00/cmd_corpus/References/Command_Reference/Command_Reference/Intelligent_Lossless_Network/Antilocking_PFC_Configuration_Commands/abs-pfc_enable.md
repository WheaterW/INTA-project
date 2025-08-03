abs-pfc enable
==============

abs-pfc enable

Function
--------



The **abs-pfc enable** command applies an antilocking PFC profile to an interface.

The **undo abs-pfc enable** command deletes the antilocking PFC profile applied to an interface.



By default, no antilocking PFC profile is applied to an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6885-SAN.



Format
------

**abs-pfc enable** *profile-name*

**undo abs-pfc enable** *profile-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of an antilocking PFC profile. | The antilocking PFC profile must exist. |



Views
-----

100GE interface view,200GE interface view,25GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Antilocking PFC is a type of PFC technology that enables a device to periodically scan the buffer usage of priority queues on an interface, and then send PFC frames to the upstream device to control the period during which the upstream device stops sending traffic. This allows the device to constantly adjust when traffic is being sent or paused. After specifying a priority queue in an antilocking PFC profile, you need to run this command to enable antilocking PFC on an interface.

**Precautions**

* The abs-pfc enable and dcb pfc enable commands are mutually exclusive on the same interface.
* Antilocking PFC takes effect only after the **long-distance mode** command is run to enable the long-distance detection mode and a detection success message is returned.
* In scenarios such as device upgrade and restart, long-distance detection may fail. As a result, antilocking PFC becomes invalid. In this case, you can run the **start long-distance detect** command to manually send detection packets.
* An antilocking PFC profile can be bound only when it has priority queue configuration.
* Antilocking PFC can be enabled for a maximum of 20 queues on the device.

Example
-------

# Apply the antilocking PFC profile to 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] abs-pfc enable myabspfc

```