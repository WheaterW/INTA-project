radius-server traffic-unit
==========================

radius-server traffic-unit

Function
--------

The **radius-server traffic-unit** command sets the traffic unit used by a RADIUS server.

The **undo radius-server traffic-unit** command restores the default traffic unit used by a RADIUS server.

The default RADIUS traffic unit is byte on the device.



Format
------

**radius-server traffic-unit** { **byte** | **kbyte** | **mbyte** | **gbyte** }

**undo radius-server traffic-unit**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **byte** | Indicates that the traffic unit is byte. | - |
| **kbyte** | Indicates that the traffic unit is kilobyte. | - |
| **mbyte** | Indicates that the traffic unit is megabyte. | - |
| **gbyte** | Indicates that the traffic unit is gigabyte. | - |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

Different RADIUS servers may use different traffic units; therefore, you need to set the traffic unit for each RADIUS server group on the router and the traffic unit must be the same as that on the RADIUS server.



Example
-------

# Set the traffic unit used by a RADIUS server to kilobyte.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] radius-server traffic-unit kbyte

```