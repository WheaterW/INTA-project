display dfs-group consistency-check packet configuration
========================================================

display dfs-group consistency-check packet configuration

Function
--------



The **display dfs-group consistency-check packet configuration** command displays the status of configuration consistency check at both ends of an M-LAG.




Format
------

**display dfs-group consistency-check packet configuration**


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

You can run the **display dfs-group consistency-check packet configuration** command to check the configuration of packet receiving and sending for M-LAG consistency check on the local device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of packet receiving and sending for M-LAG consistency check.
```
<HUAWEI> display dfs-group consistency-check packet configuration
--------------------------------------------------------------------------------
Receive : Enable
Send    : Enable
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display dfs-group consistency-check packet configuration** command output
| Item | Description |
| --- | --- |
| Receive | Status of packet receiving on the local end of an M-LAG:  Enable.  Disable. |
| Send | Status of packet sending on the local end of an M-LAG:  Enable.  Disable. |