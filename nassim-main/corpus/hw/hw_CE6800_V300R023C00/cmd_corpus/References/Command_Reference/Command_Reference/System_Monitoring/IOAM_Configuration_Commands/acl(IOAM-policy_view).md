acl(IOAM-policy view)
=====================

acl(IOAM-policy view)

Function
--------



The **acl** command binds an ACL rule in the IOAM policy view.

The **undo acl** command unbinds an ACL rule in the IOAM policy view.



By default, no IOAM ACL rule is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**acl** { *acl-num* | *acl-name* }

**undo acl** { *acl-num* | *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-num* | Specifies the advanced ACL number. | The value is an integer ranging from 3000 to 3999. |
| *acl-name* | Specifies the advanced ACL name. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. The value starts with a letter or digit but cannot contain only digits. (Only advanced ACLs are supported.) |



Views
-----

IOAM-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an IOAM network, to make the encapsulation action configured in the IOAM policy view take effect, you need to configure an IOAM ACL rule in the IOAM policy view. Only the packets that match the IOAM ACL rule are encapsulated with IOAM packets.

**Prerequisites**

Create an advanced ACL and configure rules.


Example
-------

# Specify the packet matching rule as ACL 3046 in the IOAM policy view.
```
<HUAWEI> system-view
[~HUAWEI] acl 3046
[*HUAWEI-acl4-advance-3046] rule permit tcp
[*HUAWEI-acl4-advance-3046] quit
[*HUAWEI] ioam
[*HUAWEI-ioam] profile default
[*HUAWEI-ioam-profile-default] policy 1
[*HUAWEI-ioam-profile-default-policy-1] acl 3046

```