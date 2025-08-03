display stp vlan topology-change
================================

display stp vlan topology-change

Function
--------



The **display stp vlan topology-change** command displays the statistics about topology changes.




Format
------

**display stp vlan** [ *vlan-id* ] **topology-change**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays statistics on topology changes in a specified VLAN.  If vlan vlan-id is not specified, statistics on topology changes in all VLANs are displayed. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

On a Layer 2 network running VBST, a device clears ARP entries and MAC entries after receiving topology change packets. If a device receives too many topology change packets, the device will frequently clear ARP entries and MAC entries, causing high CPU usage. As a result, network traffic is unstable.The **display stp vlan topology-change** command can be used to display the statistics about topology changes. If the statistics increase, network flapping occurs.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on topology changes in VLAN 5 when VBST is running.
```
<HUAWEI> display stp vlan 5 topology-change
VLAN 5 topology change information:
--------------------------------------------------------------
Number of topology changes           : 2
Topology change initiator(notified)  : Eth-Trunk1
Time since last topology change      : 0 days 0h:0m:34s
Topology change last received from   : 00e0-fc12-3456
--------------------------------------------------------------

```

**Table 1** Description of the **display stp vlan topology-change** command output
| Item | Description |
| --- | --- |
| Number of topology changes | Total number of topology changes since initialization. |
| Topology change initiator(notified) | Interface that initiates a topology change after receiving a topology change packet. |
| Topology change last received from | Source bridge MAC address contained in a topology change packet. |
| Time since last topology change | Time since the last topology change. |