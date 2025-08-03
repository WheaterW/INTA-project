display system resource mode
============================

display system resource mode

Function
--------



The **display system resource mode** command displays the configured resource mode and effective resource mode.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display system resource mode**


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

To view the resource mode that takes effect, run this command. The command output contains the configured resource mode and the resource mode that takes effect.The options are as follows:

* standard: default mode
* large-mac: large MAC address table mode
* large-route: large routing table mode
* user-defined: user-defined mode
* balance: balance mode
* large-multicast: large multicast mode
* large-flow: large flow table mode
* large-user: large user table mode

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the effective system resource mode.
```
<HUAWEI> display system resource mode
-------------------------------------------------
Current configuration:
standard

Effective configuration:
standard
-------------------------------------------------

```

**Table 1** Description of the **display system resource mode** command output
| Item | Description |
| --- | --- |
| Current configuration | Current resource mode. |
| Effective configuration | Effective resource mode. |