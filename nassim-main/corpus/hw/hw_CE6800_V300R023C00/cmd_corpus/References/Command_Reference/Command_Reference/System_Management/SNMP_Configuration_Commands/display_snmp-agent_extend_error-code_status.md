display snmp-agent extend error-code status
===========================================

display snmp-agent extend error-code status

Function
--------



The **display snmp-agent extend error-code status** command displays the status of extended error codes.




Format
------

**display snmp-agent extend error-code status**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If an NMS does not receive extended error codes sent by a device capable of the extended error code function, check whether the extended error code function is enabled on the device. To obtain information about the extended error code function on the device, run the display snmp-agent extend error-code status command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display whether a device is enabled to return extended error codes.
```
<HUAWEI> display snmp-agent extend error-code status
Extend error-code status: enabled

```

**Table 1** Description of the **display snmp-agent extend error-code status** command output
| Item | Description |
| --- | --- |
| Extend error-code status | Status of the return of extended error codes:   * enabled. * disabled. |