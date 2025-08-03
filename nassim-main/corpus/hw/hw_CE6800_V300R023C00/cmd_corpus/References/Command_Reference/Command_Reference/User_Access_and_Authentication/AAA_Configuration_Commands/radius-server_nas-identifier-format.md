radius-server nas-identifier-format
===================================

radius-server nas-identifier-format

Function
--------

The **radius-server nas-identifier-format** command sets the encapsulation format of the NAS-Identifier attribute.

The **undo radius-server nas-identifier-format** command restores the default encapsulation format of the NAS-Identifier attribute.

By default, the NAS-Identifier attribute encapsulation format is the device's hostname.



Format
------

**radius-server nas-identifier-format** { **hostname** | **vlan-id** }

**undo radius-server nas-identifier-format**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hostname** | Sets the encapsulation format of NAS-Identifier to a device's host name. | - |
| **vlan-id** | Sets the encapsulation format of NAS-Identifier to a user's VLAN ID. | - |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

A RADIUS server uses the NAS-Identifier attributes to identify NASs. The NASs also use the NAS-Identifier attributes carried in the sent RADIUS packets to identify themselves.



Example
-------

# Set the NAS-Identifier encapsulation format to VLAN ID.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] radius-server nas-identifier-format vlan-id

```