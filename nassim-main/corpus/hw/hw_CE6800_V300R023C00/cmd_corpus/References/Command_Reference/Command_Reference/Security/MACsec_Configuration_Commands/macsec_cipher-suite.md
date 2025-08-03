macsec cipher-suite
===================

macsec cipher-suite

Function
--------



The **macsec cipher-suite** command configures an encryption algorithm for MACsec data packets.



By default, the encryption algorithms supported by different devices vary. The actually used algorithm is automatically negotiated by the devices at both ends in descending order of encryption strength.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K:

**macsec cipher-suite** { **gcm-aes-128** | **gcm-aes-256** | **gcm-aes-xpn-128** | **gcm-aes-xpn-256** } \*

**undo macsec cipher-suite** [ **gcm-aes-128** | **gcm-aes-256** | **gcm-aes-xpn-128** | **gcm-aes-xpn-256** ] \*

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**macsec cipher-suite** { **gcm-aes-128** | **gcm-aes-256** | **gcm-aes-xpn-128** | **gcm-aes-xpn-256** | **gcm-sm4-128** | **gcm-sm4-xpn-128** } \*

**undo macsec cipher-suite** [ **gcm-aes-128** | **gcm-aes-256** | **gcm-aes-xpn-128** | **gcm-aes-xpn-256** | **gcm-sm4-128** | **gcm-sm4-xpn-128** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **gcm-aes-128** | Sets the encryption algorithm for MACsec data packets to GCM-AES-128. | - |
| **gcm-aes-256** | Sets the encryption algorithm for MACsec data packets to GCM-AES-256. | - |
| **gcm-aes-xpn-128** | Sets the encryption algorithm for MACsec data packets to GCM-AES-XPN-128. | - |
| **gcm-aes-xpn-256** | Sets the encryption algorithm for MACsec data packets to GCM-AES-XPN-256. | - |
| **gcm-sm4-128** | Sets the encryption algorithm for MACsec data packets to GCM-SM4-128.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **gcm-sm4-xpn-128** | Sets the encryption algorithm for MACsec data packets to GCM-SM4-XPN-128.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The encryption strength of the MACsec data packet encryption algorithm is GCM-AES-XPN-256 > GCM-AES-XPN-128 > GCM-AES-256 > GCM-AES-128, GCM-SM4-XPN-128 > GCM-SM4-128 in descending order. You can run this command to specify multiple encryption algorithms. The algorithms to be used are automatically negotiated by the devices at both ends in descending order of encryption strength.

**Precautions**

* If the encryption algorithm for MACsec data packets is set to GCM-AES-XPN-128 or GCM-AES-XPN-256, the MACsec encryption offset is always 0.
* When a Huawei device connects to a Cisco Catalyst switch running a version earlier than 16.3.6, only one encryption algorithm can be configured on the Huawei device, and the encryption algorithm must be the same as that configured on the Cisco device. When a Huawei device connects to a Cisco Catalyst switch running 16.3.6 or a later version, if the peer device does not support encryption algorithm negotiation, the Huawei device functions as a key server and uses the encryption algorithm with the weakest encryption strength to connect to the peer device. Multiple encryption algorithms can be configured on Huawei devices. The encryption algorithm with the weakest encryption strength must be the same as the effective algorithm configured on Cisco devices.
* If an encryption algorithm needs to be specified when Huawei devices are interconnected, ensure that the encryption algorithms configured on both ends are the same. Otherwise, the negotiation may fail.
* If the encryption algorithm GCM-SM4-128 is used, the switch can interwork only with Huawei CE switches that support encryption algorithms approved by the State Cryptography Administration.


Example
-------

# # Set the data packet encryption algorithm to GCM-AES-XPN-256 in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] macsec cipher-suite gcm-aes-xpn-256

```