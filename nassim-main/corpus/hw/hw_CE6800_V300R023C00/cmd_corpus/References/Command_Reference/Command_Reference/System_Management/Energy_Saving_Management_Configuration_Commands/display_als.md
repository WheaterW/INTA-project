display als
===========

display als

Function
--------



The **display als** command displays ALS configuration.




Format
------

**display als interface** { *interface-name* | *interface-type* *interface-number* }

**display als all**

**display als slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of characters. You can enter a question mark (?) and select a value from the displayed value range. |
| *interface-type* | Specifies the type of an interface. | The value is a string of characters. You can enter a question mark (?) and select a value from the displayed value range. |
| *interface-number* | Specifies an interface number. | The value is a string of characters. You can enter a question mark (?) and select a value from the displayed value range. |
| **all** | Displays ALS configuration on all interfaces. | - |
| **slot** *slot-id* | Displays ALS configuration on interfaces with a specified slot ID. | The value is a string of characters. You can enter a question mark (?) and select a value from the displayed value range. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,User view,System view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display als command displays ALS configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays ALS configuration on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] display als interface 10GE 1/0/1
--------------------------------------------------------------------------
Interface ALS Status Laser Status  Restart Mode  Interval(s)  Width(s)                                                                         
--------------------------------------------------------------------------
10GE1/0/1  Disable     Off          Auto          100          2                                                                                
---------------------------------------------------------------------------

```

**Table 1** Description of the **display als** command output
| Item | Description |
| --- | --- |
| Interface | Interface type and number. |
| ALS Status | Whether ALS is enabled:  Enable: enabled.  Disable: disabled.  For details about the command, see als enable. |
| Laser Status | Whether the laser is On:   * Off: The laser is Off. * On: The laser is On.   When the interface status is Down, the Laser Status field displays Off. |
| Restart Mode | ALS restart modes:   * Auto: automatic restart mode. * Manual: manual restart mode.   For details about the command, see als restart mode. |
| Interval(s) | ALS pulse interval, expressed in seconds. For details, see als restart pulse interval pulse-interval. |
| Width(s) | ALS pulse width, expressed in seconds. The ALS pulse width is set using the als restart pulse width pulse-width command. |