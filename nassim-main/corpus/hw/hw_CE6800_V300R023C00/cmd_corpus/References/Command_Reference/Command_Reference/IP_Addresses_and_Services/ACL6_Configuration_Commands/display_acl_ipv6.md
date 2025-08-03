display acl ipv6
================

display acl ipv6

Function
--------

The **display acl ipv6** command can view information about the rules of a specified ACL6 or of all ACL6s and packet matching statistics.



Format
------

**display acl ipv6** { **name** *acl6-name* | **all** }

**display acl ipv6** *basic-acl6-number*

**display acl ipv6** *advance-acl6-number*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *acl6-name* | Specifies the name of an ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **all** | Displays information about all ACL6s. | - |
| *basic-acl6-number* | Specifies the number of an ACL6. | The value is an integer ranging from 2000 to 2999. The number of a basic ACL6 ranges from 2000 to 2999. |
| *advance-acl6-number* | Specifies the number of an ACL6. | The value is an integer ranging from 3000 to 3999. The number of an advanced ACL6 ranges from 3000 to 3999. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

You can run the **display acl ipv6** command for the following purposes:

* To check details about a configured ACL6.
* To check whether an ACL6 is deleted using the **undo acl ipv6** command.
* To check whether an ACL6 is referenced by a service and packet matching statistics.

**Prerequisites**

Historical statistics have been cleared using the **reset acl ipv6 counter** command.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display rule information and packet matching statistics of an ACL6 numbered 2200.
```
<HUAWEI> display acl ipv6 2200
Basic IPv6 ACL 2200, 1 rule
IPv6 ACL's step is 5
 rule 5 permit source 2001:DB8::/64 (0 times matched)

```


**Table 1** Description of the
**display acl ipv6** command output

| Item | Description |
| --- | --- |
| Basic IPv6 ACL 2200, 1 rule | Type and number of the ACL6 and number of rules in the ACL6. |
| IPv6 ACL's step is 5 | ACL6 step, which is 5 in this example. |
| rule 5 permit source 2001:DB8::/64 | Detailed information about an ACL6 rule. |
| 0 times matched | Number of times an ACL6 rule is matched. |