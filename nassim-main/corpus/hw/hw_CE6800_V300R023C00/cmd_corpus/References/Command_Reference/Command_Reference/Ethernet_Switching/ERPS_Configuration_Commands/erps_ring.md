erps ring
=========

erps ring

Function
--------



The **erps ring** command creates an ERPS ring and displays the view of the ERPS ring, or displays the view of a specific ERPS ring.

The **undo erps ring** command deletes the created ERPS ring.



By default, no ERPS ring is created on the device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**erps ring** *ring-id*

**undo erps ring** *ring-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ring-id* | Specifies the ID of an ERPS ring. | The value is an integer ranging from 1 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Ethernet Ring Protection Switching (ERPS) is a standard protocol issued by the ITU-T to prevent loops on ring networks. ERPS provides carrier-class reliability with a fast convergence speed. ERPS takes effect on a ring network if all devices on a ring network support it.

* If ERPS needs to be enabled on a device, run the **erps ring** command to create an ERPS ring and enter the ERPS ring view.
* After entering the ERPS ring view, you can configure parameters such as a control VLAN and an ERP instance for the ERPS ring.

**Precautions**

If an ERPS ring needs to be deleted, ensure that no interfaces are added to the ERPS ring. If any interface is added to the ERPS ring, a message is displayed when the ERPS ring is being deleted. In this case, run the **undo erps ring** command in the interface view or the **undo port** command in the ERPS ring view to remove the interface. and run the **undo erps ring** command to delete the ERPS ring.


Example
-------

# Create ERPS ring 1.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 1

```