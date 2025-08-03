display acl
===========

display acl

Function
--------

The **display acl** command displays information about rules of a specified or all ACLs and packet matching statistics.



Format
------

**display acl** { **name** *acl-name* | **all** }

**display acl** *basic-acl-number*

**display acl** *user-acl-number*

**display acl** *advance-acl-number*

**display acl** *arp-acl-number*

**display acl** *numberLink*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *acl-name* | Specifies the name of an ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter or digit, and cannot contain only digits. |
| **all** | Displays rules and packet matching statistics of all ACLs. | - |
| *basic-acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 2000 to 2999, the number of a basic ACL ranges from 2000 to 2999. |
| *user-acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 5000 to 5999, the number of a user ACL ranges from 5000 to 5999. |
| *advance-acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 3000 to 3999, the number of an advanced ACL ranges from 3000 to 3999. |
| *arp-acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 23000 to 23999, the number of an ARP-based ACL ranges from 23000 to 23999. |
| *numberLink* | Specifies the number of an ACL. | The value is an integer ranging from 4000 to 4999, the number of a Layer 2 ACL ranges from 4000 to 4999. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

You can run the **display acl** command for the following purposes:

* To check details about a configured ACL.
* To check whether an ACL is deleted using the **undo acl** command.
* To check whether an ACL is referenced by a service and packet matching statistics.

**Precautions**

* Before collecting ACL statistics in a certain period, run the **reset acl counter** command to clear historical statistics.
* Rules in an ACL are displayed in ascending order of rule IDs.
* This command can display only the matching status of the control packets processed by the CPU, but cannot display the matching status of the forwarded packets.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display rule information and packet matching statistics of an ACL numbered 2001.
```
<HUAWEI> display acl 2001
Basic ACL 2001, 2 rules
ACL's step is 5
 rule 5 permit source 10.1.1.1 0 (2 times matched)
 rule 10 permit source 10.2.1.1 0 (3 times matched)

```


**Table 1** Description of the
**display acl** command output

| Item | Description |
| --- | --- |
| Basic ACL 2001, 2 rules | Type and number of the ACL and number of rules in the ACL. |
| 2 times matched | Number of times an ACL rule is matched. If this ACL is not referenced for any service, there is no matched times displayed. |
| ACL's step is 5 | ACL's step, which is 5 by default. |
| rule 5 permit source 10.1.1.1 0 | Detailed information about an ACL rule. |