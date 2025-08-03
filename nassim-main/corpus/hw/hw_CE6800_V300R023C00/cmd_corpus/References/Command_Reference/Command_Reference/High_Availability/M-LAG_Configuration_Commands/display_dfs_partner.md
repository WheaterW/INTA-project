display dfs partner
===================

display dfs partner

Function
--------



The **display dfs partner** command displays the PID, status and other information about the external components interacting with the DFS module.




Format
------

**display dfs partner**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display dfs partner** command can be used to check the PID, status, and other information about the external components interacting with the DFS module, facilitating fault locating and handling.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the PID, status, and other information about the external components interacting with the DFS module.
```
<HUAWEI> display dfs partner
------------------------------------------------------------------------------
DfsCID     ComType  PeerID     HA status   Consumer status   Producer status
------------------------------------------------------------------------------
0x81de0457 IFM      0x7a0409   AVAILABLE   READY             RUNNING
0x81de0457 FES      0x6a040e   AVAILABLE   -                 REALSEND
0x81de0457 DEVM     0xfa0002   AVAILABLE   READY             -
0x81de0457 SOCK     0x6503f8   AVAILABLE   RUN_ALONE         -
0x81de0457 ARP      0x7703f4   AVAILABLE   READY             READY
0x81de0457 ND       0x7303f5   AVAILABLE   READY             READY
0x81de0457 VBST     0x7a0410   AVAILABLE   READY             RUNNING
------------------------------------------------------------------------------

```

**Table 1** Description of the **display dfs partner** command output
| Item | Description |
| --- | --- |
| DfsCID | DFS component ID. |
| ComType | Component type. |
| PeerID | CID of the pipe used by DFS. |
| HA status | HA status of the component. |
| Consumer status | Consumer status. |
| Producer status | Producer status. |