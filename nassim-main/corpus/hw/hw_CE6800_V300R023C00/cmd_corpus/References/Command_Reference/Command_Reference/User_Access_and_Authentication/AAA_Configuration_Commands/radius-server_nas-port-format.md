radius-server nas-port-format
=============================

radius-server nas-port-format

Function
--------

The **radius-server nas-port-format** command sets the format of the NAS port attribute.

The **undo radius-server nas-port-format** command restores the default format of the NAS port attribute.

By default, the new NAS port format is used.



Format
------

**radius-server nas-port-format** { **new** | **old** }

**undo radius-server nas-port-format**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **new** | Uses the new format of an NAS port. The new format of the NAS port attribute is slot number (8 bits) + subslot number (4 bits) + port number (8 bits) + VLAN ID (12 bits). | - |
| **old** | Uses the old format of an NAS port. The old format of the NAS port attribute is slot number (12 bits) + port number (8 bits) + VLAN ID (12 bits). | - |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The NAS port format affects the information about the physical port. The NAS port format can be used by the RADIUS server to process services, such as binding the user name and port. This attribute is developed by Huawei, which is used to ensure connectivity and service cooperation among Huawei devices.

**Precautions**

The difference between the two NAS port formats lies in the physical ports connected to Ethernet access users.

* The new format of the NAS port attribute is slot number (8 bits) + subslot number (4 bits) + port number (8 bits) + VLAN ID (12 bits).
* The old format of the NAS port attribute is slot number (12 bits) + port number (8 bits) + VLAN ID (12 bits).The format of the NAS port attribute for Asymmetric Digital Subscriber Line (ADSL) access users is slot number (4 bits) + subslot number (2 bits) + port number (2 bits) + VPI (8 bits) + VCI (16 bits). This format is not affected by the command.


Example
-------

# Set the format of the NAS port attribute to new.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] radius-server nas-port-format new

```