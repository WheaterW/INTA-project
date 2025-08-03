rpf-prune-delay
===============

rpf-prune-delay

Function
--------



The **rpf-prune-delay** command sets a delay in sending Prune messages to upstream devices, so that Prune messages are not sent immediately when a PIM-SM SPT or PIM-SSM route change occurs.

The **undo rpf-prune-delay** command restores the default configuration.



By default, no delay is set in sending Prune messages to upstream devices.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rpf-prune-delay** *delay-time* [ **policy** { *acl-number* | **acl-name** *acl-name* } ]

**undo rpf-prune-delay** [ *delay-time* [ **policy** { *acl-number* | **acl-name** *acl-name* } ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-time* | Sets a delay in sending Prune messages to upstream devices. | The value is an integer ranging from 1 to 300, in seconds. |
| **policy** | Indicates a matching policy for multicast entries to be pruned. | - |
| *acl-number* | Specifies an ACL number. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies an ACL number. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In IGP ECMP-based or non-ECMP-based PIM FRR scenarios, IGP route changes will trigger frequent PIM inbound interface switchovers, causing frequent master/backup forwarding entry switchovers on the forwarding plane. As a result, the rapid convergence function of PIM FRR is adversely affected. To resolve this issue, run the **rpf-prune-delay** command to set a delay in sending Prune messages to upstream devices.


Example
-------

# Set the delay in sending Prune messages to upstream devices to 210s.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] rpf-prune-delay 210

```