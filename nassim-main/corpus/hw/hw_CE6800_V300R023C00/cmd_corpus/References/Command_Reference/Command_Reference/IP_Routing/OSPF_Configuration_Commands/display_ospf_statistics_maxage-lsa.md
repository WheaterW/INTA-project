display ospf statistics maxage-lsa
==================================

display ospf statistics maxage-lsa

Function
--------



The **display ospf statistics maxage-lsa** command displays information about router LSAs that have reached the aging time.




Format
------

**display ospf** [ *process-id* ] **statistics** **maxage-lsa**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process.  If no process ID is specified, information about all OSPF processes is displayed. | The value is an integer that ranges from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about router LSAs that have reached the aging time, run the **display ospf statistics maxage-lsa** command. The command output helps locate the cause of route flapping.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about router LSAs that have reached the aging time.
```
<HUAWEI> display ospf statistics maxage-lsa

          OSPF Process 1 with Router ID 1.1.1.1
                  Statistics of Router-LSAs
          ---------------------------------------------------

                          Area: 0.0.0.0
LinkState ID           MaxAge count        Last Five MaxAge Times
------------------------------------------------------------------
1.1.1.1                           1           2020-07-16 11:26:17

```

**Table 1** Description of the **display ospf statistics maxage-lsa** command output
| Item | Description |
| --- | --- |
| LinkState ID | Link state ID in the LSA header. |
| MaxAge count | Number of times an LSA reached the aging time. |
| Last Five MaxAge Times | Time when the LSA reached the aging time for the last five times. |
| Area | Area whose LSDB information needs to be displayed. |