authentication-mode (OSPF area view)
====================================

authentication-mode (OSPF area view)

Function
--------



The **authentication-mode** command configures an authentication mode and a password for an OSPF area.

The **undo authentication-mode** command cancels the configuration.



By default, authentication is not configured for an OSPF area. Configuring authentication is recommended to ensure system security.


Format
------

**authentication-mode simple** [ **plain** *SPlainText* | [ **cipher** ] *SCipherText* ]

**authentication-mode** { **md5** | **hmac-md5** | **hmac-sha256** } [ *KeyID* { **plain** *MPlainText* | [ **cipher** ] *MCipherText* } ]

**authentication-mode keychain** *Keychain-Name*

**undo authentication-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **plain** *SPlainText* | Specifies the simple password authentication key. Only a simple password can be entered. The password is displayed in plaintext when you view the configuration file.  Description:  When configuring an authentication password, you are advised to select the ciphertext mode because a simple password is saved in the configuration file in plaintext mode, which has high security risks. To ensure device security, change the password periodically. | The value is a character string.   * In simple mode, the value is a string of 1 to 8 characters.   Description:  The value cannot contain question marks (?) or spaces. However, if double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are part of the password.  In simple authentication mode, the cipher type is used by default. |
| **cipher** | Specifies the ciphertext mode. You can enter a cleartext or a ciphertext, but the password is displayed in ciphertext in the configuration file. | By default, cipher takes effect for MD5, HMAC-MD5, or HMAC-SHA256 authentication. |
| *SCipherText* | Specifies a ciphertext password. | The value is a character string.   * In simple mode, a simple password is a string of 1 to 8 characters, and a ciphertext password is a string of 24 to 128 characters.   Description:  The value cannot contain question marks (?) or spaces but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **md5** | Indicates MD5 authentication.  For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended. | - |
| **hmac-md5** | Indicates HMAC-MD5 authentication.  For the sake of security, using the HMAC-SHA256 algorithm rather than the HMAC-MD5 algorithm is recommended. | - |
| **hmac-sha256** | Indicates HMAC SHA256 ciphertext authentication. | - |
| *KeyID* | This object indicates the key ID for ciphertext authentication on an interface. The key ID must be the same as that on the peer end. | The value is an integer ranging from 1 to 255. |
| *MPlainText* | Specifies a plaintext password. | The value is a character string.   * In md5, hmac-md5, or hmac-sha256 mode, the value is a string of 1 to 255 characters.   Description:  The value cannot contain question marks (?) or spaces but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| *MCipherText* | Specifies a ciphertext password. | The value is a character string.   * In md5, hmac-md5, or hmac-sha256 mode, the value is a string of 1 to 255 plaintext characters or a string of 20 to 432 ciphertext characters.   Description:  The value cannot contain question marks (?) or spaces but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **keychain** | Specifies the keychain authentication mode.  Before configuring keychain authentication, run the keychain command to create a keychain, the key-id command to configure a key ID, the key-string command to configure a password, and the algorithm command to configure an algorithm. Otherwise, OSPF authentication fails.  Currently, OSPF supports MD5, SHA-1, SHA-256, SM3, HMAC-MD5, HMAC-SHA1-12, HMAC-SHA1-20, HMAC-SHA256, HMAC-SHA384, and HMAC-SHA512 algorithms.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain.  To ensure high security, using the HMAC-SHA256 algorithm instead of the SHA-1 and MD5 algorithms is recommended. | - |
| *Keychain-Name* | Specifies the name of a keychain. | The value is a string of 1 to 47 case-insensitive characters.  The value cannot contain question marks (?) and spaces However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks at both ends of the password are used as a part of the password. |
| **simple** | Sets the simple authentication mode.  By default, the simple authentication mode is cipher.  To prevent high security risks, you are advised to select the ciphertext mode. To ensure device security, change the password periodically. | - |



Views
-----

OSPF area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPF authentication can be configured to improve network security and meet high security demands. When area authentication is used, interfaces on all devices in an area must have the same area authentication mode and the password.

**Precautions**



The priority of area authentication is lower than that of interface authentication. The priority of interface authentication is set using the **ospf authentication-mode** command.For security purposes, md5 and hmac-md5 are not recommended. If they must be used, run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol feature package WEAKEA first.




Example
-------

# Configure HMAC SHA256 authentication for OSPF area 0.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] area 0
[*HUAWEI-ospf-100-area-0.0.0.0] authentication-mode hmac-sha256 1 cipher YsHsjx_202206

```