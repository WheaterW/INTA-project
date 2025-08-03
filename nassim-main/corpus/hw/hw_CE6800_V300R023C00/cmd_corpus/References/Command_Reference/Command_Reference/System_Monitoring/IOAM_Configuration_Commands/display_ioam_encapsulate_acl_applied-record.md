display ioam encapsulate acl applied-record
===========================================

display ioam encapsulate acl applied-record

Function
--------



The **display ioam encapsulate acl applied-record** command displays the ACL status of IOAM encapsulated nodes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display ioam encapsulate acl applied-record slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is an integer or a character string. You can enter a question mark (?) and select a value from the displayed value range. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check the delivery status of ACLs bound to IOAM encapsulation nodes on a device in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the delivery status of the ACL rule bound to an IOAM encapsulation node.
```
<HUAWEI> display ioam encapsulate acl applied-record slot 1
Total records : 4
----------------------------------------------------------------------
ACL Number/Name                  Type         Rule   Count State
----------------------------------------------------------------------
3000                             IPv4           15       1 Success
3000                             IPv4           20       1 Success
ioam_acl                         IPv6            5       1 Success
ioam_acl                         IPv6           10      -- Failed(3)
----------------------------------------------------------------------
Fail reason:
(3): Insufficient ACL resources.

```

**Table 1** Description of the **display ioam encapsulate acl applied-record** command output
| Item | Description |
| --- | --- |
| Total records | Total number of queried ACL records. |
| ACL Number/Name | ACL number or name. |
| Rule | ACL Rule Index. |
| Count | Number of hardware ACL entries that are actually delivered.  -- indicates that no hardware ACL entry is delivered. |
| State | ACL rule delivery status.  --: indicates that the ACL rule is not delivered.  Success: indicates that the delivery is successful.  Failed(n): indicates that the delivery fails, and n indicates the sequence number of the failure cause. |
| Fail reason | Reason why an ACL rule fails to be delivered.  (1): This ACL rule contains unsupported match conditions. (The referenced ACL rule contains packet matching fields not supported by the device.).  (2): The numbers of ACL rules exceed the limit. (The number of ACL rules to be delivered exceeds the upper limit of IOAM-encapsulated ACLs.).  (3): Insufficient ACL resources. (The ACL resources on the device are insufficient.).  (4): The internal error. (An internal error occurs. You are advised to contact technical support personnel.). |
| TYPE | ACL type. |