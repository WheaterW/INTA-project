filter-policy
=============

filter-policy

Function
--------



The **filter-policy** command configures a device to filter received MAC routes. MAC duplication suppression is not performed for MAC addresses in the filter policy.

The **undo filter-policy** command disables a device from filtering received MAC routes.



By default, the advertised or received MAC routes are not filtered.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**filter-policy** { *acl-number* | **acl-name** *acl-name-value* }

**undo filter-policy** { *acl-number* | **acl-name** *acl-name-value* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer in the range from 4000 to 4999. |
| **acl-name** *acl-name-value* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value starts with a letter or digit but cannot contain only digits. The ACL type must be link. |



Views
-----

BD-EVPN mac-duplication view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **filter-policy** command is used to configure a MAC address whitelist. MAC duplication is not suppressed for MAC addresses in the whitelist.When configured filtering conditions are used for a named ACL, only the configurations specified by source and time-range take effect.

**Prerequisites**

An ACL has been configured to set filtering rules.

**Configuration Impact**

If the **filter-policy** command is run more than once for the same EVPN instance, the latest configuration overrides the previous one.


Example
-------

# Use the ACL named mac to filter EVPN MAC routes.
```
<HUAWEI> system-view
[~HUAWEI] acl name mac link
[*HUAWEI-acl-L2-mac] quit
[*HUAWEI] bridge-domain 1
[*HUAWEI-bd1] evpn
[*HUAWEI-bd1-evpn] mac-duplication
[*HUAWEI-bd1-evpn-mac-dup] filter-policy acl-name mac

```