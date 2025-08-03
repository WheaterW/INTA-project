description (ERPS ring view)
============================

description (ERPS ring view)

Function
--------



The **description** command configures a description for an ERPS ring.

The **undo description** command restores the default description of an ERPS ring.



By default, the description of an ERPS ring is the ERPS ring name, such as Ring 1.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies a description for an ERPS ring. | The value is a string of 1 to 80 case-sensitive characters. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a device running ERPS, you can run the **description** command to configure a description for an ERPS ring, such as an ERPS ring ID. Configuring the description for an ERPS ring facilitates further maintenance of the ERPS ring.

**Precautions**

After being configured in the ERPS ring view, the **description** command takes effect only on the local device.


Example
-------

# Configure the description huawei Ring 1 for the ERPS ring 10 on the device.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 10
[*HUAWEI-erps-ring10] description huawei Ring 1

```