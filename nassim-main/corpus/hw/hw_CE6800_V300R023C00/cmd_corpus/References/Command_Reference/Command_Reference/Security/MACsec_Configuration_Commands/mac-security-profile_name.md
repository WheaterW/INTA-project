mac-security-profile name
=========================

mac-security-profile name

Function
--------



The **mac-security-profile name** command creates a MACsec profile and displays the MACsec profile view.

The **undo mac-security-profile name** command deletes a MACsec profile.



By default, there is no default MACsec profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-security-profile name** *profile-name*

**undo mac-security-profile name** *profile-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of a profile. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported, can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot be "-" or "--". |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command creates a MACsec profile and displays the MACsec profile view.


Example
-------

# Create a MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test]

```