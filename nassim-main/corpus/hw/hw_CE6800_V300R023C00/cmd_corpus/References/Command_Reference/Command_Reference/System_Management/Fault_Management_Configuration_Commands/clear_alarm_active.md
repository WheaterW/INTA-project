clear alarm active
==================

clear alarm active

Function
--------



The **clear alarm active** command clears active alarms.




Format
------

**clear alarm active sequence-number** *sequence-number*

**clear alarm active all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sequence-number** *sequence-number* | Specifies the sequence number of an alarm. | The value is an integer ranging from 1 to 4294967295. |
| **all** | Clears all alarms. | - |



Views
-----

Alarm management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To quickly clear an alarm generated for a fault that is rectified, run this command. You can run the **display alarm active** command to view the alarms of the current device.

**Configuration Impact**

If a fault persists but the alarm triggered by this fault is cleared, the alarm of the same type will no longer be sent to the NMS.

**Follow-up Procedure**

Run the **display alarm active** command to verify that the alarm is cleared successfully.

**Precautions**

After the **clear alarm active all** command is run, the device sends the hwAlarmClearedReportTrap event to the NMS. This trap contains two parameters: number of cleared active alarms and SN list of cleared active alarm.

* If the number of cleared active alarms is less than or equal to 15, the SN list of cleared active alarms carries the SNs of all cleared alarms. After receiving the trap, the NMS clears the active alarm based on the alarm SN.
* If the number of cleared active alarms is greater than 15, the SN list of cleared active alarms is empty and the SNs of cleared alarms are not carried. After receiving the trap, the NMS automatically synchronizes alarms to the device to clear all active alarms on the NMS.

Example
-------

# Clear an active alarm with a specified index.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] clear alarm active sequence-number 1

```

# Clear all active alarms in the system.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] clear alarm active all

```