display fwm smart-link statistics
=================================

display fwm smart-link statistics

Function
--------



The **display fwm smart-link statistics** command displays collected statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display fwm smart-link statistics** { *ifName* | *ifType* *ifNum* } **slot** *slotId*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ifName* | Specifies a port name. | The value is a string of case-sensitive characters. It cannot contain spaces. |
| *ifType* | Specifies a port type. | The value is an integer. |
| *ifNum* | Specifies the index of a port. | The value is a string of case-sensitive characters. It cannot contain spaces. |
| **slot** *slotId* | Specifies a slot ID. | The value varies according to the device. You can enter a question mark (?) and select a value as prompted. |



Views
-----

All views (excluding the AAA domain view)


Default Level
-------------

3: Management level


Usage Guidelines
----------------

This command displays the number of Smart Link interfaces that go down, filtered number of interfaces that go down, number of interface down errors, number of sent data threads when the interface is down, number of received, filtered, and error flush packets, number of sent data threads, and number of successful switchovers.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display Smart Link statistics on an interface.
```
<HUAWEI> display fwm smart-link statistics 10GE1/0/1 slot 1
Interface                : 10GE1/0/1
Port Down Cnt            : 1
Port Down TrunkMem       : 0
Port Down Err            : 0
Port Down Sent           : 1
Flush Rcv Cnt            : 0
Flush Rcv Disabled       : 0
Flush Rcv Err            : 0
Flush Rcv Sent           : 0
Port Fast Switch         : 1

```

**Table 1** Description of the **display fwm smart-link statistics** command output
| Item | Description |
| --- | --- |
| Interface | Name of an interface. |
| Port Down Cnt | Number of times the interface enters the Down state. |
| Port Down TrunkMem | Number of filtered interface down events. The number increases when the trunk member interface that is configured with Smart Link groups or receives Smart Link packets is shut down. |
| Port Down Err | Number of interface down errors. |
| Port Down Sent | Number of DATA threads sent when the interface is in the Down state. |
| Port Fast Switch | Number of Smart Link fast switching times on an interface. |
| Flush Rcv Cnt | Number of Flush packets received on an interface. |
| Flush Rcv Disabled | Number of Flush packets filtered on an interface. The value increases when the interface receives Flush packets but is not enabled to receive Flush packets. |
| Flush Rcv Err | Number of errors reported when Flush packets are received. |
| Flush Rcv Sent | Number of data threads sent when flush packets are received. |