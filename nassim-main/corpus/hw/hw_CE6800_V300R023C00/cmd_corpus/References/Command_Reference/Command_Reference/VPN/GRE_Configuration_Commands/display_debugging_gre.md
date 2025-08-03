display debugging gre
=====================

display debugging gre

Function
--------



The **display debugging gre** command displays information about the enabled GRE debugging functions.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display debugging gre**


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

To view information about the enabled GRE debugging functions when a large amount of information is output, run the **display debugging gre** command. Based on the command output, you can disable some unnecessary debugging functions to minimize the debugging information output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the enabled debugging functions.
```
<HUAWEI> display debugging gre
GRE packet debugging switch is on
GRE keepalive debugging switch is on

```

**Table 1** Description of the **display debugging gre** command output
| Item | Description |
| --- | --- |
| GRE packet debugging switch is on | The debugging function has been enabled for GRE packets. |
| GRE keepalive debugging switch is on | The debugging function has been enabled for the GRE Keepalive function. |