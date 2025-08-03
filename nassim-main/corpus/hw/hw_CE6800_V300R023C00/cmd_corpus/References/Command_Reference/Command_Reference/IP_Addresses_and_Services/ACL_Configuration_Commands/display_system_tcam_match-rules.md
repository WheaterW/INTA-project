display system tcam match-rules
===============================

display system tcam match-rules

Function
--------



The **display system tcam match-rules** command displays matched entries.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display system tcam match-rules slot** *slot-id* [ [ **ingress** | **egress** | **group** *group-id* ] | [ **delay-time** *time-value* ] ] \*

**display system tcam match-rules slot** *slot-id* [ [ **chip** *chip-id* ] | [ **ingress** | **egress** | **group** *group-id* ] ] \*

For CE6885-LL (low latency mode):

**display system tcam match-rules slot** *slot-id* [ [ **chip** *chip-id* ] | [ **ingress** | **group** *group-id* ] ] \*

**display system tcam match-rules slot** *slot-id* [ [ **ingress** | **group** *group-id* ] | [ **delay-time** *time-value* ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ingress** | Specifies the inbound direction. | - |
| **egress** | Specifies the outbound direction.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **group** *group-id* | Specifies a group ID. | The value is an integer ranging from 1 to 4294967295. |
| **delay-time** *time-value* | Specifies the time delay. | The value is an integer ranging from 1 to 10. |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **chip** *chip-id* | Specifies the chip ID. | The value is an integer. It must be the ID of an available chip. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to view matched entries. If ingress, egress, group group-id, delay-time time-value, and chip chip-id are not specified, all matched entries on a device are displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display matched entries on a device.
```
<HUAWEI> system-view
[HUAWEI] display system tcam match-rules slot 1
--------------------------------------------------------------
ServiceID    ChipID Stage       GroupID  EntryID         HitNum
--------------------------------------------------------------
      216         0 Ingress          67      555         157562
--------------------------------------------------------------
Total: 1

```

**Table 1** Description of the **display system tcam match-rules** command output
| Item | Description |
| --- | --- |
| ServiceID | Displays the service ID. |
| ChipID | Chip ID. |
| Stage | Direction (Pre-Ingress, Ingress, or Egress). |
| GroupID | Group ID. |
| EntryID | Matched entry ID. |
| HitNum | Number of matched packets. |
| Total | Total number of matched rules. |