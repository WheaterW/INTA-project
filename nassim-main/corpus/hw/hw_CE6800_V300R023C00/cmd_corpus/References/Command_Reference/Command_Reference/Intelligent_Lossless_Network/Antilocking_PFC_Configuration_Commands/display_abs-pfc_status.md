display abs-pfc status
======================

display abs-pfc status

Function
--------



The **display abs-pfc status** command displays the configuration and status of antilocking PFC.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6885-SAN and CE8850-SAN.



Format
------

**display abs-pfc status** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-num* | Specifies the type and number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **interface** *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the configuration and status of antilocking PFC.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of antilocking PFC on an interface. (CE6860-SAN and CE8850-SAN)
```
<HUAWEI> display abs-pfc status interface 100GE 1/0/1
Current buffer optimization mode: Enhanced-long-distance
-----------------------------------------------------------------------------------------------
Interface         Queue         Status         RTT(us)        Threshold(KB)         Speed(Gbps)
-----------------------------------------------------------------------------------------------
100GE1/0/1            3         Enable             397                    0                 100
-----------------------------------------------------------------------------------------------

```

# Display the configuration of antilocking PFC on an interface. (CE6885-SAN)
```
<HUAWEI> display abs-pfc status interface 100GE 1/0/1
-----------------------------------------------------------------------------------------------
Interface         Queue         Status         RTT(us)        Threshold(KB)         Speed(Gbps)
-----------------------------------------------------------------------------------------------
100GE1/0/1            3         Enable             397                    0                 100
-----------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display abs-pfc status** command output
| Item | Description |
| --- | --- |
| Current buffer optimization mode | Current buffer optimization mode:   * Default: indicates that the plane buffer optimization mode is not configured or the configured plane buffer optimization mode does not take effect. * Long-distance: indicates that the plane buffer optimization mode that has taken effect is the long-distance mode. * Enhanced-long-distance: indicates that the plane buffer optimization mode that has taken effect is the enhanced long-distance mode. |
| Interface | Name of the interface on which antilocking PFC is enabled. |
| Queue | Index of the queue for which antilocking PFC is enabled. |
| Status | Status (enabled or disabled) of antilocking PFC. |
| RTT(us) | Round-trip delay between the local and peer devices. |
| Threshold(KB) | Buffer threshold for antilocking PFC to take effect. |
| Speed(Gbps) | Rate of an interface. |