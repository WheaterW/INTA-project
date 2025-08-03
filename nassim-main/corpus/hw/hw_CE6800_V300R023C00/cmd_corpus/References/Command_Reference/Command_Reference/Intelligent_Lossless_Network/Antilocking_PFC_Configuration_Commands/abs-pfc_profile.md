abs-pfc profile
===============

abs-pfc profile

Function
--------



The **abs-pfc profile** command creates an antilocking PFC profile and displays the antilocking PFC profile view, or displays the view of an existing antilocking PFC profile.

The **undo abs-pfc profile** command deletes an antilocking PFC profile.



By default, no antilocking PFC profile is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6885-SAN.



Format
------

**abs-pfc profile** *profile-name*

**undo abs-pfc profile** [ *profile-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of an antilocking PFC profile. | The value is a string of 1 to 31 case-sensitive characters. It can contain letters, digits, hyphens (-), and underscores (\_), but cannot start with an underscore (\_) or contain spaces or the following characters: | > $\* ^.  When an antilocking PFC profile is applied, if the configured profile name conflicts with the command keyword, the command keyword preferentially takes effect. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Antilocking PFC is a type of PFC technology that enables a device to periodically scan the buffer usage of priority queues on an interface, and then send PFC frames to the upstream device to control the period during which the upstream device stops sending traffic. This allows the device to constantly adjust when traffic is being sent or paused. You can run this command to create an antilocking PFC profile and enter its view.

**Precautions**

* If an antilocking PFC profile has been applied to an interface, you need to delete the application of the profile in the interface view before deleting the profile.
* A maximum of two antilocking PFC profiles can be configured globally.

Example
-------

# Create an antilocking PFC profile.
```
<HUAWEI> system-view
[~HUAWEI] abs-pfc profile myabspfc
[*HUAWEI-abs-pfc-myabspfc]

```