mka timer sak-life
==================

mka timer sak-life

Function
--------



The **mka timer sak-life** command sets the Secure Association Key (SAK) timeout period.

The **undo mka timer sak-life** command restores the default SAK timeout period.



By default, the SAK timeout period is 3600 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mka timer sak-life** *life-time*

**undo mka timer sak-life**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *life-time* | Specifies the SAK timeout period. | The value is an integer that ranges from 60 to 604800, in seconds. The default value is 3600 seconds. |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When MACsec is used for secure communication, an SAK is used to encrypt and decrypt data packets. To ensure the security of data packets, an SAK needs to be replaced when the number of data packets encrypted using the SAK reaches a certain value or the time for using the SAK exceeds a certain period.

**Precautions**

When the number of data packets encrypted using the SAK reaches a certain value or the time for using the SAK exceeds a certain period, the key server generates and distributes a new SAK. Before a new SAK is used, data packets are encrypted and decrypted using the original SAK.If the local end is not the key server, the SAK timeout period advertised by the key server is used. If the local end is the key server, the locally configured SAK timeout period is used, and the local end advertises the SAK timeout period to the remote end.


Example
-------

# Set the SAK timeout period to 3000 seconds in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] mka timer sak-life 3000

```