display erps statistics
=======================

display erps statistics

Function
--------



The **display erps statistics** command displays statistics about sent and received ring auto protection switching (R-APS) protocol data units (PDUs) on the ports that have been added to ERPS rings.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display erps** [ **ring** *ring-id* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ring** *ring-id* | Specifies the ID of an ERPS ring. | The value is an integer ranging from 1 to 255. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To monitor the network running status and maintain devices on a Layer 2 network running ERPS, run the **display erps statistics** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about sent and received R-APS PDUs on the ports that have been added to ERPS rings.
```
<HUAWEI> display erps statistics
- -------------------------------------------------------------------------------
Ring Port            RX/TX       SF       NR     NRRB       FS       MS    EVENT
- -------------------------------------------------------------------------------
   1 Eth-Trunk1      RX           0        0      552        0        0        0
   1 Eth-Trunk1      TX           0       68        0      326        0        6
   1 100GE1/0/1         RX           0        6      552        0        0        0
   1 100GE1/0/1         TX           4       63        0      326        0        6
  10 100GE1/0/2         RX           0        1        0        0        0        0
  10 100GE1/0/2         TX           4       74        0        0        0        0

```

# Display statistics about sent and received R-APS PDUs on the ports that have been added to ERPS ring 2.
```
<HUAWEI> display erps ring 2 statistics
- -------------------------------------------------------------------------------
Ring  Port           RX/TX       SF       NR     NRRB       FS       MS    EVENT
- -------------------------------------------------------------------------------
   2  100GE1/0/1       RX           0        1        0        0        0        0
   2  100GE1/0/1       TX           4       74        0        0        0        0

```

**Table 1** Description of the **display erps statistics** command output
| Item | Description |
| --- | --- |
| Ring | ID of the ERPS ring. |
| Port | Port that is added to the ERPS ring. |
| RX/TX | R-APS PDU forwarding direction:   * RX: R-APS PDUs are received. * TX: R-APS PDUs are sent. |
| SF | Statistics about R-APS (SF) messages. |
| NR | Statistics about R-APS (NR) messages. |
| NRRB | Statistics about R-APS (NR, RB) messages. |
| FS | Statistics about R-APS (FS) messages. |
| MS | Statistics about R-APS (MS) messages. |
| EVENT | In a multi-ring scenario, when an intersecting node on a major ring detects a sub-ring topology change, the intersecting node notifies other nodes on the major ring of the topology change. |