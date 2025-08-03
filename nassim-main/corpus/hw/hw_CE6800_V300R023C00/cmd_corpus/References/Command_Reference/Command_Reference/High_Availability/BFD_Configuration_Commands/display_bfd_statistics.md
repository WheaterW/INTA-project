display bfd statistics
======================

display bfd statistics

Function
--------



The **display bfd statistics** command displays global BFD statistics.




Format
------

**display bfd statistics**


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

To view global BFD statistics, such as the number of current BFD sessions, run the display bfd statistics command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display global BFD statistics.
```
<HUAWEI> display bfd statistics
Total Up/Down Session Number : 0/1
Total Up/Down Main Session Number : 0/0
Total Up/Down Sub Session Number  : 0/0
Current Session Number       :
  Static Session             : 1            Dynamic Session        : 0
  STATIC_AUTO Session        : 0            IP Session             : 1
  VXLAN Session              : 0
--------------------------------------------------------------------------------
PAF/LCS Name                       Maxnum         Minnum         Create
--------------------------------------------------------------------------------
BFD_CFG_NUM                          2048              1              1
BFD_IO_SESSION_NUM                    500              1              -
--------------------------------------------------------------------------------
Current Total Used Discriminator Num               : 1
--------------------------------------------------------------------------------
BFD Global Information :
--------------------------------------------------------------------------------
System Session Delay Up Timer                      : OFF
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bfd statistics** command output
| Item | Description |
| --- | --- |
| Total Up/Down Session Number | Total number of current BFD sessions in the Up or Down state. |
| Total Up/Down Main Session Number | Total number of current main BFD sessions in the Up or Down state. |
| Total Up/Down Sub Session Number | Total number of current sub BFD sessions in the Up or Down state. |
| Current Total Used Discriminator Num | Number of discriminators that are currently used. |
| Current Session Number | Number of current BFD sessions.   * Static session: number of static BFD sessions. * Dynamic session: number of dynamic BFD sessions. * Static\_Auto session: number of BFD sessions with automatically negotiated discriminators. * IP session: number of current BFD sessions for IP. * VXLAN session: number of current BFD sessions for VXLAN. |
| Static session | Number of static BFD sessions. |
| Dynamic session | Number of dynamic BFD sessions. |
| STATIC\_AUTO session | Number of BFD sessions with automatically negotiated discriminators. |
| IP Session | Number of current BFD sessions for IP. |
| PAF/LCS Name | PAF/License name.   * BFD\_CFG\_NUM: maximum number of BFD sessions that can be created globally. * BFD\_IO\_SESSION\_NUM: maximum number of BFD sessions that can be created in each slot.   The value range varies according to the product type. |
| Maxnum | Maximum value defined in the license file. |
| Minnum | Minimum value defined in the license file. |
| Create | Actual number of created BFD sessions. |
| BFD Global Information | Other information about BFD sessions. |
| System Session Delay Up Timer | status of the current system delay Up timer, including:   * OFF: indicates that the system is in the normal state. * Xs: indicates that after X seconds, the system recovers, and the BFD session can become Up. |
| VXLAN Session | Number of current BFD sessions for VXLAN. |