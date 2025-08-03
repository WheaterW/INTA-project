mka keyserver priority
======================

mka keyserver priority

Function
--------



The **mka keyserver priority** command configures the MKA key server priority.

The **undo mka keyserver priority** command restores the default MKA key server priority.



By default, the MKA key server priority is 16.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mka keyserver priority** *priority*

**undo mka keyserver priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the MKA key server priority. A smaller value indicates a higher priority. | The value is an integer that ranges from 0 to 255. The default value is 16. |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When MACsec is used to encrypt and decrypt data packets, the interface on the local device and that on the remote device must use the same security key to establish an MKA session. The key is generated and distributed by the key server. Therefore, you need to configure the key server priority on the interfaces of both devices. A smaller value indicates a higher priority. The device with a higher priority is elected as the key server.If the two interfaces have the same key server priority, the device with a smaller SCI value is elected as the key server. An SCI consists of the MAC address of an interface and the last two bytes of the interface index.

**Precautions**

When the device is connected to a non-Huawei device and MACsec is configured on both devices, the MKA key server priorities on both devices cannot be set to 255 at the same time.


Example
-------

# Set the MKA key server priority to 2 in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] mka keyserver priority 2

```