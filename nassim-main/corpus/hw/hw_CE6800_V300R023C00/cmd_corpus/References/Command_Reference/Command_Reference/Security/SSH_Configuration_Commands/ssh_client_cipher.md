ssh client cipher
=================

ssh client cipher

Function
--------



The **ssh client cipher** command configures encryption algorithms on an SSH client.

The **undo ssh client cipher** command restores the default encryption algorithms on an SSH client.



The default situation is as follows:

* When the device starts with zero configuration, the SSH client supports these encryption algorithms: AES256\_GCM, AES128\_GCM, AES256\_CTR, AES192\_CTR, and AES128\_CTR.
* When the device loads the configuration file for startup, and the ssh client cipher command configuration does not exist in the configuration file, the SSH client supports encryption algorithms: AES128\_CTR, AES256\_CTR, AES192\_CTR, AES128\_GCM and AES256\_GCM.


Format
------

**ssh client cipher** { **des\_cbc** | **3des\_cbc** | **aes128\_cbc** | **aes256\_cbc** | **aes128\_ctr** | **aes256\_ctr** | **arcfour128** | **arcfour256** | **aes192\_cbc** | **aes128\_gcm** | **aes256\_gcm** | **aes192\_ctr** | **sm4\_cbc** | **sm4\_gcm** } \*

**undo ssh client cipher**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **des\_cbc** | Specifies a DES encryption algorithm in CBC mode. | - |
| **3des\_cbc** | Specifies a 3DES encryption algorithm in CBC mode. | - |
| **aes128\_cbc** | Specifies an AES128 encryption algorithm in CBC mode. | - |
| **aes256\_cbc** | Specifies an AES256 encryption algorithm in CBC mode. | - |
| **aes128\_ctr** | Specifies the AES128 encryption algorithm in CTR mode. | - |
| **aes256\_ctr** | Specifies the AES256 encryption algorithm in CTR mode. | - |
| **arcfour128** | Specifies the Arcfour128 encryption algorithm. | - |
| **arcfour256** | Specifies the Arcfour256 encryption algorithm. | - |
| **aes192\_cbc** | Specifies an AES192 encryption algorithm in CBC mode. | - |
| **aes128\_gcm** | Specifies an AES128 encryption algorithm in GCM mode. | - |
| **aes256\_gcm** | Specifies an AES256 encryption algorithm in GCM mode. | - |
| **aes192\_ctr** | Specifies the AES192 encryption algorithm in CTR mode. | - |
| **sm4\_cbc** | Specifies the SM4 encryption algorithm in CBC mode. | - |
| **sm4\_gcm** | Specifies a GCM SM4 encryption algorithm. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure encryption algorithms on an SSH client, run the **ssh client cipher** command. The SSH client and server negotiate encryption algorithms for the packets exchanged between them. During negotiation, the client sends its encryption algorithms to the server. After comparing the received encryption algorithms with local ones, the server selects the first matching encryption algorithm received for packet transmission. If no matching encryption algorithm is found, the negotiation fails.

**Precautions**

* To ensure high security, you are advised to use the following encryption algorithms: aes128\_ctr, aes256\_ctr, aes192\_ctr, aes128\_gcm, and aes256\_gcm.
* This command takes effect for both IPv4 and IPv6 SSH clients.
* The des\_cbc, 3des\_cbc, aes128\_cbc, aes256\_cbc, arcfour128, arcfour256, aes192\_cbc, and sm4\_cbc parameters can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed by running the **install feature-software WEAKEA** command.


Example
-------

# Configure encryption algorithms in aes256\_ctr mode on an SSH client.
```
<HUAWEI> system-view
[~HUAWEI] ssh client cipher aes256_ctr

```