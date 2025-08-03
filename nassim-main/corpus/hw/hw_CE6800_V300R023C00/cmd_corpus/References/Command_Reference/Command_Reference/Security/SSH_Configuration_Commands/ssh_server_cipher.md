ssh server cipher
=================

ssh server cipher

Function
--------



The **ssh server cipher** command configures encryption algorithms on an SSH server.

The **undo ssh server cipher** command restores the default encryption algorithms on the SSH server.



By default:

* When the device starts with no configuration, the SSH server uses the AES256\_GCM, AES128\_GCM, AES256\_CTR, AES192\_CTR or AES128\_CTR encryption algorithm.
* If the device starts with a loaded configuration file and the configuration file does not contain the ssh server cipher configuration, the SSH server uses AES128\_CTR, AES256\_CTR, AES192\_CTR, AES128\_GCM, and AES256\_GCM encryption algorithms.


Format
------

**ssh server cipher** { **des\_cbc** | **3des\_cbc** | **aes128\_cbc** | **aes192\_cbc** | **aes256\_cbc** | **aes128\_ctr** | **aes256\_ctr** | **arcfour128** | **arcfour256** | **blowfish\_cbc** | **aes128\_gcm** | **aes256\_gcm** | **aes192\_ctr** | **sm4\_cbc** | **sm4\_gcm** } \*

**undo ssh server cipher**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **des\_cbc** | Specifies a DES encryption algorithm in CBC mode. | - |
| **3des\_cbc** | Specifies a 3DES encryption algorithm in CBC mode. | - |
| **aes128\_cbc** | Specifies an AES128 encryption algorithm in CBC mode. | - |
| **aes192\_cbc** | Specifies an AES192 encryption algorithm in CBC mode. | - |
| **aes256\_cbc** | Specifies an AES256 encryption algorithm in CBC mode. | - |
| **aes128\_ctr** | Specifies the AES128 encryption algorithm in CTR mode. | - |
| **aes256\_ctr** | Specifies the AES256 encryption algorithm in CTR mode. | - |
| **arcfour128** | Specifies the Arcfour128 encryption algorithm. | - |
| **arcfour256** | Specifies the Arcfour256 encryption algorithm. | - |
| **blowfish\_cbc** | Specifies the Blowfish encryption algorithm in CBC mode. | - |
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

To configure encryption algorithms on an SSH server, run the **ssh server cipher** command. The SSH client and server negotiate encryption algorithms for the packets exchanged between them. During negotiation, the client sends the specified encryption algorithms to the server. After comparing the received encryption algorithms with the local ones, the server selects the first matching encryption algorithm received for packet transmission. If no matching encryption algorithm is found, the negotiation fails.

**Precautions**

* To ensure high security, you are advised to use the following encryption algorithms: aes128\_ctr, aes256\_ctr, aes192\_ctr, aes128\_gcm, and aes256\_gcm.
* This command applies to both IPv4 and IPv6 SSH clients.
* The des\_cbc, 3des\_cbc, aes128\_cbc, aes256\_cbc, arcfour128, arcfour256, blowfish\_cbc, aes192\_cbc, and sm4\_cbc parameters can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed by running the **install feature-software WEAKEA** command.


Example
-------

# Configure the encryption algorithms in aes256\_ctr mode.
```
<HUAWEI> system-view
[~HUAWEI] ssh server cipher aes256_ctr

```