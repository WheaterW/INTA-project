display acl hardware statistics
===============================

display acl hardware statistics

Function
--------



The **display acl hardware statistics** command displays statistics about packets matching hardware ACL.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display acl hardware statistics** [ *acl-number* | **name** *acl-name* | **ipv6** [ *acl6-number* | **name** *acl6-name* ] ]

For CE6885-LL (low latency mode):

**display acl hardware statistics** [ *acl-number* | **name** *acl-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of an ACL. | The value is an integer that ranges from 2000 to 2999, 3000 to 3999, 4000 to 4999, 5000 to 5999, or 23000 to 23999. |
| **name** *acl6-name* | Specifies an ACL6 name.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. The value starts with a letter or digit but cannot contain only digits. |
| **name** *acl-name* | Specifies the name of an ACL. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **ipv6** | Specifies an ACL6 number or name.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *acl6-number* | Specifies an ACL6 number.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 2000 to 2999 or an integer ranging from 3000 to 3999. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view statistics about the packets matching hardware ACL, run the **display acl hardware statistics** command.

**Precautions**

The switch can display only the statistics about the packets matching hardware ACL referenced by MQC. In addition, you need to run the **statistics enable** command to enable traffic statistics collection.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about packets matching hardware ACL.
```
<HUAWEI> display acl hardware statistics
Advanced ACL 3000
rule 5 permit ip source 10.1.1.0 0.0.0.255 (550 times matched)
Total 550 times matched.

```

**Table 1** Description of the **display acl hardware statistics** command output
| Item | Description |
| --- | --- |
| Advanced ACL 3000 | An advanced ACL with number 3000. |
| rule 5 permit ip source 10.1.1.0 0.0.0.255 | Details about an ACL rule. |
| Total 550 times matched | Total number of times all ACL rules are matched. |
| 550 times matched | Number of times an ACL rule is matched. |