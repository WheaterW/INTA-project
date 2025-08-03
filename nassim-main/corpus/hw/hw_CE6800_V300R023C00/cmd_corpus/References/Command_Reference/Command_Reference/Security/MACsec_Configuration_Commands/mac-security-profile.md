mac-security-profile
====================

mac-security-profile

Function
--------



The **mac-security-profile** command binds a MACsec profile to an interface.

The **undo mac-security-profile** command unbinds a MACsec profile from an interface.



By default, no MACsec profile is bound to an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-security-profile** *profile-name*

**undo mac-security-profile**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of a profile. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported,can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot be "-" or "--". |



Views
-----

100GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command binds a MACsec profile to an interface.

**Precautions**

This command is supported only on Layer 2 interfaces.



The range of interfaces that support the MACsec function, see the Configuration Precautions for MACsec.




Example
-------

# Create a MACsec profile and bind it to 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] mac-security-profile test

```