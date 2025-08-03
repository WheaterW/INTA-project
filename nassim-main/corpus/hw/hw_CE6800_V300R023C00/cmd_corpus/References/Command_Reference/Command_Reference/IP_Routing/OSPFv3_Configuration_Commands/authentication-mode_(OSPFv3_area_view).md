authentication-mode (OSPFv3 area view)
======================================

authentication-mode (OSPFv3 area view)

Function
--------



The **authentication-mode** command configures an authentication mode and a password for an OSPFv3 area.

The **undo authentication-mode** command deletes the authentication mode and password configured for an OSPFv3 area.



By default, no authentication mode is configured for an OSPFv3 area.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**authentication-mode** { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *PlainText* | [ **cipher** ] *CipherText* }

**authentication-mode** { **keychain** *Keychain-Name* }

**undo authentication-mode** { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId*

**undo authentication-mode** { **keychain** *Keychain-Name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hmac-sha256** | Configures HMAC-SHA256 authentication. | - |
| **hmac-sm3** | Sets the HMAC-SM3 authentication mode. | - |
| **key-id** *KeyId* | Specifies the key ID in MD5, HMAC-MD5, or HMAC-SHA256 authentication mode. The key ID must be the same as the key ID on the peer device. | The value is an integer ranging from 1 to 65535. |
| **plain** *PlainText* | Specifies simple authentication. You can only type in simple passwords, and the passwords are displayed in simple mode in the configuration file.   * The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters. * For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | The value is a string of 1 to 255 characters.  The value cannot contain question marks (?) or spaces. However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are used as a part of the password. |
| **cipher** *CipherText* | Specifies the cipher authentication. You can type in simple or ciphertext passwords, and the passwords are displayed in ciphertext in the configuration file. | The value can be a string of 1 to 255 characters for a simpletext and 20 to 432 characters for a ciphertext.  A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **keychain** *Keychain-Name* | Specifies the keychain authentication mode.  Before configuring keychain authentication, run the keychain command to configure a keychain, the key-id command to configure a key ID, the key-string command to configure a password, and the algorithm command to configure an algorithm. Otherwise, OSPFv3 authentication fails.  Currently, OSPFv3 supports only HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512 algorithms.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain. | The value is a string of 1 to 47 case-insensitive characters.  The value cannot contain question marks (?) and spaces However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks at both ends of the password are used as a part of the password. |



Views
-----

OSPFv3 area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Attacks based on TCP/IP networks are increasing. Due to the defects of TCP/IP and the inappropriate implementation process, the impact of network attacks is increasing. In particular, attacks on network devices will cause network crash or unavailability. Authentication can be configured to improve OSPFv3 network security.

**Precautions**

* You are advised to configure an authentication mode. Otherwise, the system may be insecure.
* When area authentication is used, the authentication modes and passwords configured on the interfaces of all devices in an area must be the same.
* The priority of area authentication is lower than that of interface authentication.
* To configure interface authentication, run the **ospfv3 authentication-mode** command.


Example
-------

# Configure HMAC-SHA256 authentication for OSPFv3 area 0.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] area 0
[*HUAWEI-ospfv3-100-area-0.0.0.0] authentication-mode hmac-sha256 key-id 10 cipher YsHsjx_202206

```