dhcp snooping alarm threshold(system view)
==========================================

dhcp snooping alarm threshold(system view)

Function
--------



The **dhcp snooping alarm threshold** command sets the alarm threshold for the number of DHCP messages discarded by DHCP snooping.

The **undo dhcp snooping alarm threshold** command restores the default alarm threshold.



By default, the global alarm threshold for the number of messages discarded by DHCP snooping is 100.


Format
------

**dhcp snooping alarm threshold** *threshold*

**undo dhcp snooping alarm threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold* | Specifies the alarm threshold for the number of DHCP messages discarded by DHCP snooping. | The value is an integer in the range from 1 to 1000. The default value is 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the alarm function for discarded DHCP messages is enabled, you can run the **dhcp snooping alarm threshold** command to set the alarm threshold for the number of discarded DHCP messages.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

If you run this command in the system view, the command takes effect on all the interfaces of the device.If the alarm threshold for the number of DHCP messages discarded by DHCP snooping is configured in the system view, an alarm is generated when the number of all types of DHCP messages discarded by DHCP snooping reaches the threshold.To ensure that alarms can be reported, run the **snmp-agent trap enable feature-name dhcp** command to enable the DHCP module to report alarms. You can run the **display snmp-agent trap feature-name dhcp all** command to check whether the alarm reporting function of the DHCP module is enabled.


Example
-------

# Set the global alarm threshold for the number of messages discarded by DHCP snooping to 200.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] dhcp snooping alarm threshold 200

```