display stp topology-change
===========================

display stp topology-change

Function
--------



The **display stp topology-change** command displays statistics about Multiple Spanning Tree Protocol (MSTP) topology changes.




Format
------

**display stp** [ **instance** *instance-id* ] **topology-change**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Displays statistics about the topology changes of a specified STP instance.  If instance instance-id is not specified, statistics about the topology changes of a Common and Internal Spanning Tree (CIST) instance are displayed. | The value is an integer ranging from 0 to 4094, Value 0 indicates CIST. |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a Layer 2 network running MSTP, a device clears ARP entries and MAC entries after receiving TC BPDUs. If a device receives too many TC BPDUs, the device will frequently clear ARP entries and MAC entries, causing high CPU usage. As a result, network traffic is unstable.You can run the display stp topology-change command to display statistics about MSTP topology changes. If the statistics increase, network flapping occurs.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about MSTP topology changes.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] display stp topology-change
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

**Table 1** Description of the **display stp topology-change** command output
| Item | Description |
| --- | --- |
| Number of Topology Changes | Total number of topology changes since MSTP initialization. |
| Number of generated topologychange traps | Total number of generated TC traps. |
| Time since last Topology Change | Time past since the last topology changed. |
| Topology Change initiator(detected) | Interface that triggers a topology change because the interface status changes to Detected. |
| Topology Change initiator(notified) | Interface that triggers a topology change after receiving a TC BPDU. |
| Topology Change last received from | Source bridge MAC address contained in a TC BPDU. |
| number of suppressed topologychange traps | number of suppressed topologychange traps. |