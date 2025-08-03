display bridge-domain statistics
================================

display bridge-domain statistics

Function
--------



The **display bridge-domain statistics** command displays statistics about packets transmitted in a bridge domain (BD).



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bridge-domain** *bd-id* **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bd-id* | Specifies a BD number. | The value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check traffic statistics of a BD when monitoring it, run the **display bridge-domain statistics** command. The command output helps locate faults.

**Prerequisites**

To ensure that the **display bridge-domain statistics** command displays valid statistics entries, you must have performed the following operations before running the **display bridge-domain statistics** command:

* A bridge domain has been created using the **bridge-domain** command in the system view.
* Packet statistics in a bridge domain have been collected using the **statistic enable** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display packet statistics in bridge domain 10.
```
<HUAWEI> display bridge-domain 10 statistics
-------------------------------------------------------------------------------------------
Item                     Packets                       Bytes     Packets/s          Bytes/s
-------------------------------------------------------------------------------------------
Inbound                         0                          0             0                0
Outbound                        0                          0             0                0
-------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display bridge-domain statistics** command output
| Item | Description |
| --- | --- |
| Item | Inbound or outbound. |
| Packets | Packet numbers. |
| Bytes | Bytes. |
| Packets/s | Packets per second. |
| Bytes/s | Bytes per second. |