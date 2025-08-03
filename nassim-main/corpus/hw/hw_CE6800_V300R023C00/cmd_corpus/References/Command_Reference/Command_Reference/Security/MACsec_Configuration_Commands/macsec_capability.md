macsec capability
=================

macsec capability

Function
--------



The **macsec capability** command configures the MACsec capability value.



By default, the MACsec capability value is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**macsec capability** *capability-value*

**undo macsec capability**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **capability** *capability-value* | Specifies the MACsec capability value. | The value is an integer that ranges from 2 to 3. |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MACsec capability table:2: Integrity and confidentiality check is supported. Encryption can be performed only from the packet header.3: Integrity and confidentiality check is supported. Encryption can start from the packet header, offset 30 bytes, and offset 50 bytes.If the peer device supports only MACsec capability 2, change the MACsec capability of the device to be the same as that of the peer device.

**Precautions**

If the MACsec capability is set to 2, setting the MACsec encryption offset to 30 or 50 using the **macsec confidentiality-offset** command does not take effect. In this case, the MACsec encryption offset is always 0.


Example
-------

# Set the capability value to 2 in the MACsec profile test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] macsec capability 2

```