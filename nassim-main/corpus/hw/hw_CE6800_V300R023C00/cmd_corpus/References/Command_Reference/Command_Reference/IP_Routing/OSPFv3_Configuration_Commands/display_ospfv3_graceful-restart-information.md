display ospfv3 graceful-restart-information
===========================================

display ospfv3 graceful-restart-information

Function
--------



The **display ospfv3 graceful-restart-information** command displays the status of OSPFv3 GR.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **graceful-restart-information**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the status of OSPFv3 GR, run the display ospfv3 graceful-restart-information command. If no process ID is specified, the brief information about all OSPFv3 processes is displayed in an ascending order.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the OSPFv3 GR status.
```
<HUAWEI> display ospfv3 graceful-restart-information
OSPFv3 Router with ID (0.0.0.0) (Process 1)

  Helper capability                : enabled
  Helper support                   : planned and un-planned, strict lsa check
  Max Grace-Period Configured      : 1800 Sec
  Last Helper-exit Reason          : none

```

**Table 1** Description of the **display ospfv3 graceful-restart-information** command output
| Item | Description |
| --- | --- |
| Helper capability | Whether OSPFv3 GR Helper is enabled:   * enabled. * disabled. |
| Helper support | Helper GR configuration:   * planned: indicates that only the planned GR is supported. * un-planned: indicates that only the un-planned GR is supported. * strict lsa check: indicates that the Helper supports the strict external LSA check. |
| Max Grace-Period Configured | GR period. |
| Last Helper-exit Reason | Reason why the Helper exited from GR last time:   * none: indicates that the Router never enters the Helper mode since it starts. * successful: indicates that the Helper successfully exits from GR. * topology change: indicates that the network topology changes. * interface id change: indicates that the interface ID changes. * grace period exp: indicates that GR period expires. * hold timer expire: indicates that the hold timer expires. * interface address deleted: indicates that the interface address is deleted. |