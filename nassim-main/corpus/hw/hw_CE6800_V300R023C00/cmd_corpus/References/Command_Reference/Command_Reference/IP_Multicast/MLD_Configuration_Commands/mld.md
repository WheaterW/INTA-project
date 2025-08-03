mld
===

mld

Function
--------



The **mld** command displays the MLD view.

The **undo mld** command deletes the MLD view and all the configurations in the MLD view.



By default, no MLD view is not created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld**

**mld vpn-instance** *instance-name*

**undo mld**

**undo mld vpn-instance** *instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Global parameters related to MLD must be configured in the MLD view.


Example
-------

# Enter the MLD view.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld]

```