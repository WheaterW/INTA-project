display dfs-group m-lag check stp
=================================

display dfs-group m-lag check stp

Function
--------



The **display dfs-group m-lag check stp** command checks whether the STP configurations on both ends in the M-LAG are consistent.




Format
------

**display dfs-group** *dfs-group-id* **m-lag** **check** **stp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dfs-group-id* | Specifies the ID of a DFS group. | The value is 1. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

When V-STP is configured in M-LAG networking, you can run this command to check whether the STP configurations on both ends in the M-LAG are consistent. If parameters are inconsistent, the calculation results on both ends may be different. As a result, network forwarding fails or network flapping occurs. Determine and modify the configurations to ensure that the STP configurations on both ends are consistent.

**Precautions**



An M-LAG in VBST mode does not support STP configuration check or commands used to check STP configurations.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Check whether the STP configurations on both ends of the M-LAG are consistent.
```
<HUAWEI> display dfs-group 1 m-lag check stp
*                   : This option must be kept consistent on the local and remote ends.
                      Local     Remote    Result
*Protocol Status    : Enabled   Enabled   OK
 Priority           : 32768     32768     OK
*Foward Delay (s)   : 15        15        OK
*Hello Time (s)     : 2         2         OK
*Max Age (s)        : 20        20        OK

```

**Table 1** Description of the **display dfs-group m-lag check stp** command output
| Item | Description |
| --- | --- |
| \* | Parameter that must be consistent on both ends. |
| Local | Local end. |
| Remote | Remote end. |
| Result | Whether the results on both ends are consistent.  â¢OK: The results on both ends are consistent.  â¢Fail: The results on both ends are inconsistent.  â¢-: The results on both ends are inconsistent. To prevent network flapping when faults occur, you are advised to use consistent parameters at both ends. |
| Priority | Priority of the device in the specified spanning tree. |
| Protocol Status | STP status:  â¢Enabled.  â¢Disabled. |
| Foward Delay (s) | Value of the Forward Delay timer, in seconds. |
| Hello Time (s) | Value of the Hello Timer, in seconds. |
| Max Age (s) | Value of the Max Age Timer, in seconds. |