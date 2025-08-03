zone
====

zone

Function
--------



The **zone** command creates an iNOF customized zone and displays the zone view, or directly displays the view of an existing customized zone.

The **undo zone** command deletes a customized zone from an iNOF system.



By default, no iNOF customized zone is created, and a default zone exists on the device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**zone** *zone-name*

**undo zone** *zone-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *zone-name* | Specifies the name of an iNOF customized zone. | The value is a string of 1 to 63 case-sensitive characters. |



Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A device in an iNOF system can manage hosts connected to the system through zones. By default, the device has a default zone that cannot be deleted. You can run this command to configure a customized zone.

**Precautions**

* You can configure a maximum of 16000 zones (excluding the default zone) in the iNOF system.
* In versions earlier than V300R023C00, an iNOF zone name can contain a maximum of 31 bytes. In V300R023C00 and later versions, an iNOF zone name can contain a maximum of 63 bytes. When the reflector DeviceA running V300R023C00 or a later version and the reflector DeviceB running a version earlier than V300R023C00 coexist on an iNOF network and if the iNOF zone name of DeviceA is longer than 31 bytes, DeviceB cannot receive zone information synchronized from DeviceA. To ensure correct synchronization of zone information, ensure that the lengths of iNOF zone names supported by devices on the iNOF network are the same or the length of an iNOF zone name does not exceed 31 bytes.

Example
-------

# Create a customized zone named test and enter the zone view.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] zone test
[*HUAWEI-ai-service-inof-zone-test]

```