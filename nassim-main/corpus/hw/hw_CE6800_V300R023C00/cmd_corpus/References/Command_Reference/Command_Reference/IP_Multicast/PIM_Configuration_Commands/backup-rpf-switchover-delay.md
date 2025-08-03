backup-rpf-switchover-delay
===========================

backup-rpf-switchover-delay

Function
--------



The **backup-rpf-switchover-delay interval** command delays forwarding entry generation on new interfaces connected to backup upstream devices in PIM FRR scenarios.

The **undo backup-rpf-switchover-delay interval** command restores the default configuration.



By default, forwarding entry generation is not delayed on new interfaces connected to backup upstream devices in PIM FRR scenarios.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**backup-rpf-switchover-delay interval** *hold-time* [ **policy** { *acl-number* | **acl-name** *acl-name* } ]

**undo backup-rpf-switchover-delay** [ **interval** *hold-time* [ **policy** { *acl-number* | **acl-name** *acl-name* } ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hold-time* | Allows new interfaces connected to backup upstream devices to generate forwarding entries only after the specified delay expires. | The value is an integer ranging from 1 to 300, in seconds. |
| **policy** | Indicates a matching policy for multicast entries. | - |
| *acl-number* | Specifies an ACL number. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies an ACL number. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In IGP ECMP-based or non-ECMP-based PIM FRR scenarios, IGP route changes will trigger frequent PIM backup inbound interface switchovers, causing frequent master/backup forwarding entry switchovers on the forwarding plane. As a result, the rapid convergence function of PIM FRR is adversely affected. To resolve this issue, run the **backup-rpf-switchover-delay interval** command to delay forwarding entry generation on new interfaces connected to backup upstream devices.


Example
-------

# Set a delay in generating forwarding entries on new interfaces connected to backup upstream devices.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] backup-rpf-switchover-delay interval 300

```