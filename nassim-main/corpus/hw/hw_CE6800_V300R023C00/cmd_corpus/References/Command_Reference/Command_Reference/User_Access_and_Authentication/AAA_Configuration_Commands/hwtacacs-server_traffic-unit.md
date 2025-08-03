hwtacacs-server traffic-unit
============================

hwtacacs-server traffic-unit

Function
--------

The **hwtacacs-server traffic-unit** command sets the traffic unit used by an HWTACACS server.

The **undo hwtacacs-server traffic-unit** command restores the default traffic unit used by the HWTACACS server.

By default, the traffic unit is byte on the device.



Format
------

**hwtacacs-server traffic-unit** { **byte** | **kbyte** | **mbyte** | **gbyte** }

**undo hwtacacs-server traffic-unit**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **byte** | Indicates that the traffic unit is byte. | - |
| **kbyte** | Indicates that the traffic unit is KByte. | - |
| **mbyte** | Indicates that the traffic unit is MByte. | - |
| **gbyte** | Indicates that the traffic unit is GByte. | - |




Views
-----

HWTACACS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

Different HWTACACS servers may use different traffic units; therefore, you need to set the traffic unit for each HWTACACS server group on the device and the traffic unit must be the same as that on the HWTACACS server.

**Precautions**

You can modify this configuration only when the HWTACACS server template is not in use.



Example
-------

# Set the traffic unit used by an HWTACACS server to KByte.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template template1
[*HUAWEI-hwtacacs-template1] hwtacacs-server traffic-unit kbyte

```