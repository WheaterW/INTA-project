display fwm m-lag synchronization connectivity statistics
=========================================================

display fwm m-lag synchronization connectivity statistics

Function
--------



The **display fwm m-lag synchronization connectivity statistics** command displays statistics about connectivity synchronization packets exchanged between the devices paired into a DFS group.




Format
------

**display fwm m-lag synchronization connectivity statistics** [ **slot** *slotid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotid* | Specifies the slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display fwm m-lag synchronization connectivity statistics** command is used to query statistics about connectivity synchronization packets exchanged between the devices paired into a DFS group, including the number of packets that are successfully sent and fail to be sent, and the number of packets that are successfully received and fail to be received. The command output helps maintain and check whether the connectivity mechanism between the devices paired into a DFS group is correct.

**Precautions**

* Connectivity check is not supported in virtual peer-link scenarios.
* If the peer device does not support detection based on peer-link member interfaces, the local device displays only the slot status and statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about connectivity synchronization packets exchanged between the devices paired into a DFS group.
```
<HUAWEI> display fwm m-lag synchronization connectivity statistics
Slot 1:
Interface       : 100GE1/0/1
Current Status  : Failed
Send success    : 0
Send fail       : 0
Receive success : 0
Receive fail    : 0

Interface       : 100GE1/0/2
Current Status  : Success
Send success    : 0
Send fail       : 0
Receive success : 0
Receive fail    : 0

```

**Table 1** Description of the **display fwm m-lag synchronization connectivity statistics** command output
| Item | Description |
| --- | --- |
| Interface | Name of a peer-link member interface.  If -- is displayed, it indicates the status and statistics of the slot. |
| Current Status | Current status of fast channel detection.   * Failed: The current status of fast channel detection is failed. * Success: The current status of fast channel detection is successful. |
| Send success | Statistics on packets that are successfully sent. |
| Send fail | Statistics on packets that fail to be sent. |
| Receive success | Statistics on packets that are successfully received. |
| Receive fail | Statistics on packets that fail to be received. |
| Slot | Slot number. |