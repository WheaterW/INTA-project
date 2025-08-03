display stp topology-change (All views)
=======================================

display stp topology-change (All views)

Function
--------



The **display stp topology-change** command displays statistics about MSTP topology changes.




Format
------

**display stp** [ **instance** *instance-id* ] **topology-change**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Displays statistics about the topology changes of a specified STP instance.  If instance <instanceId> is not specified, statistics about the topology changes of a CIST instance are displayed. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



On a Layer 2 network running MSTP, a device clears ARP entries and MAC entries after receiving TC BPDUs. If a device receives too many TC BPDUs, the device will frequently clear ARP entries and MAC entries, causing high CPU usage. As a result, network traffic is unstable.You can run the display stp topology-change command to display statistics about MSTP topology changes. If the statistics increase, network flapping occurs.



**Precautions**



If you run this command in the MSTP process view without specifying an MSTP process, information about the MSTP process in this view is displayed by default. If you run this command in other views without specifying the ID of an MSTP process, information about MSTP process 0 is displayed by default. If you specify the ID of an MSTP process, information about the MSTP process with the specified ID is displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about MSTP topology changes.
```
<HUAWEI> display stp topology-change
CIST topology change information
   Number of topology changes             :5
   Time since last topology change        :0 days 0h:23m:19s
   Topology change initiator(detected)    :100GE1/0/1
   Topology Change last received from     :00e0-fc12-3456
   Number of generated topologychange traps :   5
   Number of suppressed topologychange traps:   3

 MSTI 1 topology change information
   Number of topology changes             :5
   Time since last topology change        :0 days 0h:23m:19s
   Topology change initiator(detected)    :100GE1/0/2
   Number of generated topologychange traps :   5
   Number of suppressed topologychange traps:   3

 MSTI 2 topology change information
   Number of topology changes             :5
   Time since last topology change        :0 days 0h:23m:19s
   Topology change initiator(notified)    :100GE1/0/3
   Number of generated topologychange traps :   5
   Number of suppressed topologychange traps:   3

 MSTI 3 topology change information
   Number of topology changes             :5
   Time since last topology change        :0 days 0h:23m:19s

```

**Table 1** Description of the **display stp topology-change (All views)** command output
| Item | Description |
| --- | --- |
| Number of Topology Changes | Total number of topology changes since MSTP initialization. |
| Number of generated topologychange traps | Total number of generated TC traps. |
| Number of suppressed topologychange traps | Total number of suppressed topology-change traps. |
| Time since last Topology Change | Time since the last topology change. |
| Topology Change initiator(detected) | Interface that triggers the topology change because the interface status changes to DETECTED after the interface status changes from blocked to unblocked. |
| Topology Change initiator(notified) | Interface that initiates a topology change after receiving a topology change packet. |
| Topology Change last received from | Bridge MAC address of the source of topology change BPDUs. |