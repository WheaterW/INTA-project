display tunnel statistics
=========================

display tunnel statistics

Function
--------



The **display tunnel statistics** command displays statistics information about tunnels.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display tunnel statistics**


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

To view the statistics about different types of tunnels that are already set up, run the **display tunnel statistics** command.


Example
-------

# Display the statistics about different types of tunnels.
```
<HUAWEI> display tunnel statistics
TunnelType                               Number
-----------------------------------------------------------
gre                                      1

```

**Table 1** Description of the **display tunnel statistics** command output
| Item | Description |
| --- | --- |
| TunnelType | Tunnel type:   * gre.   The output of the display tunnel-info tunnel-id command varies according to tunnel types. |
| Number | Number of tunnels. |