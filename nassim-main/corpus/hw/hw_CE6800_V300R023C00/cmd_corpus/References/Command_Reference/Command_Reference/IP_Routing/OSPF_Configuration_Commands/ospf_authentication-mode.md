ospf authentication-mode
========================

ospf authentication-mode

Function
--------



The **ospf authentication-mode** command sets the authentication mode and password used between neighboring nodes.

The **ospf authentication-mode null** command configures the null authentication mode on an interface.

The **undo ospf authentication-mode** command deletes the authentication mode from an interface.



By default, an interface does not authenticate OSPF packets.


Format
------

**ospf authentication-mode simple** [ **plain** *plain-text* | [ **cipher** ] *cipher-text* ]

**ospf authentication-mode** { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ]

**ospf authentication-mode null**

**ospf authentication-mode keychain** *keychain-name*

**undo ospf authentication-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **plain** | Indicates the cleartext authentication.  When configuring an authentication password, select the ciphertext mode because the password is saved in configuration files in cleartext if you select cleartext mode, which has a high risk. To ensure device security, change the password periodically. | By default, cipher takes effect for simple authentication. |
| *plain-text* | Specifies a plaintext password. | The value is a string of characters.   * When simple is configured, plain-text is a string of 1 to 8 characters. * When md5, hmac-md5 or hmac-sha256 is configured, plain-text is a string of 1 to 255 characters.   A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **cipher** | Indicates the cipher mode. | In MD5/HMAC-MD5 authentication mode, if this parameter is not specified, the password is in cipher text by default. |
| *cipher-text* | Specifies a ciphertext. | The value is a string of characters.   * In simple mode, a simple password is a string of 1 to 8 characters, and a ciphertext password is a string of 24 to 128 characters. * In md5, hmac-md5 or hmac-sha256 mode, if the value is a string of 1 to 255 characters, the password is a plaintext; if the value is a string of 20 to 432 characters, the password is a ciphertext password.   The value cannot contain question marks (?) or spaces. However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are used as a part of the password. |
| **md5** | Indicates MD5 authentication.  For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended. | Because $@$@ is used to distinguish old and new passwords in an upgrade, an MD5 authentication password must not start and end with $@$@. |
| **hmac-md5** | Indicates HMAC-MD5 authentication.  For the sake of security, using the HMAC-SHA256 algorithm rather than the HMAC-MD5 algorithm is recommended. | - |
| **hmac-sha256** | Indicates HMAC SHA256 ciphertext authentication. | - |
| *key-id* | This object indicates the key ID for ciphertext authentication on an interface. The key ID must be the same as that on the peer end. | The value is an integer ranging from 1 to 255. |
| **null** | Indicates null authentication. | - |
| **keychain** | Configures keychain authentication.  Before configuring keychain authentication, run the keychain command to create a keychain, the key-id command to configure a key ID, the key-string command to configure a password, and the algorithm command to configure an algorithm. Otherwise, OSPF authentication fails.  Currently, OSPF supports MD5, SHA-1, SHA-256, SM3, HMAC-MD5, HMAC-SHA1-12, HMAC-SHA1-20, HMAC-SHA256, HMAC-SHA384, and HMAC-SHA512 algorithms.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain.  To ensure high security, using the HMAC-SHA256 algorithm instead of the SHA-1 and MD5 algorithms is recommended. | - |
| *keychain-name* | Specifies the name of a keychain. | The value is a string of 1 to 47 case-insensitive characters.  The value cannot contain question marks (?) and spaces However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks at both ends of the password are used as a part of the password. |
| **simple** | Sets the simple authentication mode.  By default, the cipher type is used in simple authentication.   * The length of a simple password ranges from 1 to 8 characters. * A ciphertext password is a string of 24 to 128 characters. * To prevent high security risks, you are advised to select the ciphertext mode. To ensure device security, change the password periodically. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Due to inherent defects and flawed implementation of the TCP/IP protocol suite, there are an increasing number of attacks, which poses greater threats on TCP/IP networks than ever before. The attacks on network devices may lead to network failures. To configure an authentication mode and a password for an OSPF interface to improve OSPF network security, run the ospf authentication-mode command.

**Configuration Impact**



Interface authentication is used to set authentication mode and password used between neighboring devices. It takes precedence over area authentication. If both interface authentication and area authentication are configured, the authentication succeeds as long as the interface authentication succeeds. If authentication is configured on an interface, OSPFv3 neighbor relationships can be established on the interface as long as interface authentication succeeds, regardless of the area authentication configuration or whether area authentication is configured.



**Precautions**

Null indicates an authentication mode, which does not mean that no authentication is configured.Interfaces on the same network segment must be configured with the same authentication mode and password.For security purposes, md5 and hmac-md5 are not recommended. If they must be used, run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol feature package WEAKEA first.


Example
-------

# Set the authentication mode and password used between neighboring nodes.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf authentication-mode hmac-sha256 1 cipher YsHsjx_202206

```