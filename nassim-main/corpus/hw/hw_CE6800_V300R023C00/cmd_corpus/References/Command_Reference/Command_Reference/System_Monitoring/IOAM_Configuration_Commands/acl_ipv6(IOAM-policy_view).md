acl ipv6(IOAM-policy view)
==========================

acl ipv6(IOAM-policy view)

Function
--------



The **acl ipv6** command binds an IPv6 ACL rule in the IOAM policy view.

The **undo acl ipv6** command unbinds an IPv6 ACL rule in the IOAM policy view.



By default, no IOAM IPv6 ACL rule is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**acl ipv6** { *acl-num* | *acl-name* }

**undo acl ipv6** { *acl-num* | *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-num* | Specifies the advanced ACL number. | The value is an integer ranging from 3000 to 3999. |
| *acl-name* | Specifies the advanced ACL name. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. The value starts with a letter or digit but cannot contain only digits. |



Views
-----

IOAM-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To make the encapsulation action configured in the IOAM policy view take effect, you need to configure an IOAM ACL rule in the IOAM policy view. Only the packets that match the rule can be encapsulated.

**Prerequisites**

Create an advanced IPv6 ACL and configure rules.


Example
-------

# Specify the packet matching rule as ACL IPv6 3046 in the IOAM policy view.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3046
[*HUAWEI-acl6-advance-3046] rule permit tcp
[*HUAWEI-acl6-advance-3046] quit
[*HUAWEI] ioam
[*HUAWEI-ioam] profile default
[*HUAWEI-ioam-profile-default] policy 1
[*HUAWEI-ioam-profile-default-policy-1] acl ipv6 3046

```