display dfs-group m-lag up-delay
================================

display dfs-group m-lag up-delay

Function
--------



The **display dfs-group m-lag up-delay** command displays the remaining time in the delay for all M-LAG member interfaces in a DFS group to automatically go Up.




Format
------

**display dfs-group** *dfs-group-id* **m-lag** **up-delay**


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

You can run the display dfs-group m-lag up-delay command to check the remaining time in the delay for all M-LAG member interfaces to automatically go Up. This command takes effect only in fault recovery scenarios and scenarios where M-LAG member interfaces change to Error-Down state.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the remaining time in the delay for all M-LAG member interfaces in DFS group 1 to automatically go Up.
```
<HUAWEI> display dfs-group 1 m-lag up-delay
M-Lag ID    Interface       Port State      Error-Down        Recovery Countdown         
--------------------------------------------------------------------------------         
       1    Eth-Trunk 2     Down            Yes                              150         
       2    Eth-Trunk 24    Down            Yes                              180

```

**Table 1** Description of the **display dfs-group m-lag up-delay** command output
| Item | Description |
| --- | --- |
| M-Lag ID | Bound M-LAG ID. |
| Interface | Corresponding user-side Eth-Trunk. |
| Port State | Actual physical status of the interface.  Down.  Up. |
| Error-Down | Whether the interface changes to Error-Down state.  Yes.  No. |
| Recovery Countdown | Recovery time countdown, which is updated every second. |