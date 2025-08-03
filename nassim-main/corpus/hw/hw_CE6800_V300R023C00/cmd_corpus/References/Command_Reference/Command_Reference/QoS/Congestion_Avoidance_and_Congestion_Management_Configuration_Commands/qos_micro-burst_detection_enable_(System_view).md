qos micro-burst detection enable (System view)
==============================================

qos micro-burst detection enable (System view)

Function
--------



The **qos micro-burst detection enable** command enables microburst detection.

The **undo qos micro-burst detection enable** command disables microburst detection.



By default, microburst detection is disabled on a device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**qos micro-burst detection** [ **enhanced** ] **enable**

**undo qos micro-burst detection** [ **enhanced** ] **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enhanced** | Enables microburst detection in enhanced mode.  If this parameter is not specified, microburst detection is enabled in default mode. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To detect microbursts on an outbound interface, you must enable microburst detection on a switch and interfaces. This helps locate packet loss caused by microbursts.In default microburst detection mode, the packet sampling interval is 5 ms. In enhanced microburst detection mode, the packet sampling interval is 1 ms.

**Precautions**



Before enabling microburst detection on an interface, you must enable microburst detection in the slot where the interface resides.When the default microburst detection mode is used on a device, microburst detection can be enabled on multiple interfaces of the device. When the enhanced microburst detection mode is used on a device, microburst detection can be enabled on only one interface of the device.To change the microburst detection mode, you must delete the existing microburst detection configuration on the device first.




Example
-------

# Enable microburst detection in default mode on the device.
```
<HUAWEI> system-view
[~HUAWEI] qos micro-burst detection enable

```