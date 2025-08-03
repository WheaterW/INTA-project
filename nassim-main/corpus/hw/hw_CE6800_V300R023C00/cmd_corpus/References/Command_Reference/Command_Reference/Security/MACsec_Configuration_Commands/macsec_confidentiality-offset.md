macsec confidentiality-offset
=============================

macsec confidentiality-offset

Function
--------



The **macsec confidentiality-offset** command configures the MACsec encryption offset.

The **undo macsec confidentiality-offset** command restores the default MACsec encryption offset.



By default, the MACsec encryption offset is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**macsec confidentiality-offset** *offset-value*

**undo macsec confidentiality-offset**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *offset-value* | Specifies the MACsec encryption offset. | The value is 0, 30, or 50, in bytes. |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The MACsec encryption offset indicates from which byte behind the MACsec tag field a data frame is encrypted. For some applications (such as load balancing) that need to identify IPv4/IPv6 headers, packet headers must not be encrypted. In this case, you need to configure the encryption offset.

**Precautions**

If the local end is not the key server, the encryption offset advertised by the key server is used. If the local end is the key server, the locally configured encryption offset is used, and the local end advertises the offset to the remote end.When the encryption algorithm for MACsec data packets is set to GCM-AES-XPN-128 or GCM-AES-XPN-256, the MACsec encryption offset is always 0.


Example
-------

# Set the encryption offset to 30 bytes in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] macsec confidentiality-offset 30

```