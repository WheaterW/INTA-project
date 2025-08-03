display ifit policy acl applied-record
======================================

display ifit policy acl applied-record

Function
--------



The **display ifit policy acl applied-record** command displays the ACL delivery status of the IFIT policy.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ifit policy** { **all** | **name** *policy-name* } **acl** **applied-record** **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all policies. | - |
| **name** *policy-name* | Specifies the name of a traffic policy. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the ACL delivery status of the IFIT policy on the device in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the delivery status of an ACL in an IFIT policy.
```
<HUAWEI> display ifit policy name huawei acl applied-record slot 1
Slot          : 1
TotalRecords  : 6
PolicyName    : huawei
Interface     : -
----------------------------------------------------------------------------------------------
Protocol     AclNumber       AclName                                     RuleId     State     
----------------------------------------------------------------------------------------------
IPv4              3001       -                                                5     Success   
IPv4              3001       -                                               10     Success   
IPv4              3000       abcd                                             5     Success   
IPv4              3000       abcd                                            10     Success   
IPv4                 -       abcd2                                            5     Success   
IPv4                 -       abcd2                                           10     Success   
----------------------------------------------------------------------------------------------
Fail reason:
   1 -- Insufficient resources
   2 -- Unsupported information
   3 -- Reaches the upper limit (256)

```

# Display the delivery status of all ACLs in an IFIT policy.
```
<HUAWEI> display ifit policy all acl applied-record slot 1
Slot          : 1
TotalRecords  : 6
PolicyName    : huawei
Interface     : -
----------------------------------------------------------------------------------------------
Protocol     AclNumber       AclName                                     RuleId     State     
----------------------------------------------------------------------------------------------
IPv4              3001       -                                                5     Success   
IPv4              3001       -                                               10     Success   
IPv4              3000       abcd                                             5     Success   
IPv4              3000       abcd                                            10     Success   
IPv4                 -       abcd2                                            5     Success   
IPv4                 -       abcd2                                           10     Success   
----------------------------------------------------------------------------------------------
Slot          : 1
TotalRecords  : 6
PolicyName    : huawei2
Interface     : 100GE1/0/1
----------------------------------------------------------------------------------------------
Protocol     AclNumber       AclName                                     RuleId     State     
----------------------------------------------------------------------------------------------
IPv4              3001       -                                                5     Success   
IPv4              3001       -                                               10     Success   
IPv4              3000       abcd                                             5     Success   
IPv4              3000       abcd                                            10     Success   
IPv4                 -       abcd2                                            5     Success   
IPv4                 -       abcd2                                           10     Success   
----------------------------------------------------------------------------------------------
Fail reason:
   1 -- Insufficient resources
   2 -- Unsupported information
   3 -- Reaches the upper limit (256)

```

**Table 1** Description of the **display ifit policy acl applied-record** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| TotalRecords | Total count of records. |
| PolicyName | Policy name. |
| Interface | Number of the port to which the IFIT policy is applied. If the IFIT policy is applied globally, a hyphen (-) is displayed. |
| Protocol | Protocol type. |
| AclNumber | Advanced ACL ID. |
| AclName | ACL ID. |
| RuleId | Rule ID. |
| State | ACL delivery status. |
| Fail reason | Possible cause of the ACL delivery failure for the IFIT policy. |