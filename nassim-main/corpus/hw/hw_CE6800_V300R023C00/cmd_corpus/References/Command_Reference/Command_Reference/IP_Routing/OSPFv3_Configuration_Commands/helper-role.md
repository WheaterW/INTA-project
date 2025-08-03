helper-role
===========

helper-role

Function
--------



The **helper-role** command configures the device to support the helper mode.

The **undo helper-role** command disables the helper mode on the device.



By default, the helper mode is disabled on the device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**helper-role** [ { **acl-name** *acl-name* | **acl-number** *acl-number* | **ip-prefix** *ip-prefix-name* } | **max-grace-period** *period* | **planned-only** | **lsa-checking-ignore** ] \*

**undo helper-role** [ { [ **acl-name** [ *acl-name* ] ] | [ **acl-number** [ *acl-number* ] ] | [ **ip-prefix** [ *ip-prefix-name* ] ] } | [ **max-grace-period** [ *period* ] ] | [ **planned-only** ] | [ **lsa-checking-ignore** ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **acl-number** *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **max-grace-period** *period* | Specifies the permitted maximum restart period. | The value is an integer ranging from 1 to 1800, expressed in seconds. The default value is 120 seconds. |
| **planned-only** | Indicates that devices support planned-GR only. By default, devices support planned-GR and unplanned-GR. | - |
| **lsa-checking-ignore** | Indicates that the strict check is not performed on LSAs. By default, devices perform strict check on received LSAs. | - |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Devices cannot use the helper mode during the GR process.When the rule (basic ACL6 view) command is used to configure a filtering rule for a named ACL, only the source address range that is specified in source and the time period that is specified in time-range take effect on the filtering rule.


Example
-------

# Configure a device to support the helper mode.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2001
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] helper-role acl-number 2001 max-grace-period 250 planned-only lsa-checking-ignore

```