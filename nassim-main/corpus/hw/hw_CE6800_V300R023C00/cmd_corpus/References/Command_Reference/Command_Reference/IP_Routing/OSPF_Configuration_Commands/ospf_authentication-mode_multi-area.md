ospf authentication-mode multi-area
===================================

ospf authentication-mode multi-area

Function
--------



The **ospf authentication-mode multi-area** command configures an authentication mode for a multi-area adjacency interface.

The **ospf authentication-mode multi-area null** command configures null authentication for a multi-area adjacency interface.

The **undo ospf authentication-mode multi-area** command deletes the authentication mode configured for a multi-area adjacency interface.



By default, a multi-area adjacency interface does not authenticate OSPF packets.


Format
------

**ospf authentication-mode simple** [ **plain** *plain-text* | [ **cipher** ] *cipher-text* ] **multi-area** { *area-id* | *area-id-ipv4* }

**ospf authentication-mode** { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ] **multi-area** { *area-id* | *area-id-ipv4* }

**ospf authentication-mode null multi-area** { *area-id* | *area-id-ipv4* }

**ospf authentication-mode keychain** *keychain-name* **multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf authentication-mode multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **plain** | Indicates the cleartext authentication.  When configuring an authentication password, select the ciphertext mode because the password is saved in configuration files in cleartext if you select cleartext mode, which has a high risk. To ensure device security, change the password periodically. | By default, cipher takes effect for simple authentication. |
| *plain-text* | Specifies a plaintext password. | The value is a string of characters.   * In simple mode, the value is a string of 1 to 8 characters. * In md5, hmac-md5, or hmac-sha256 mode, the value is a string of 1 to 255 characters.   A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **cipher** | Indicates the cipher mode. | In MD5/HMAC-MD5 authentication mode, if this parameter is not specified, the password is in cipher text by default. |
| *cipher-text* | Specifies a ciphertext password. | The value is a string of characters.   * For simple authentication, a plaintext is 1 to 8 characters, and a ciphertext is 24 to 128 characters. * For MD5, HMAC-MD5, or HMAC-SHA256 authentication, a plaintext is 1 to 255 characters, and a ciphertext is 20 to 432 characters.   A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| *area-id* | Specifies the ID of an OSPF area. | The value can be a decimal integer ranging from 0 to 4294967295 or in the format of an IP address. |
| *area-id-ipv4* | Specifies the ID of an OSPF area, in the format of an IP address. | The value is in the format X.X.X.X, where each X represents a value from 0 to 255 |
| **md5** | Indicates MD5 authentication.  Configuring HMAC-SHA256 rather than MD5 is recommended for the sake of security. | The string $@$@ is particularly used to distinguish the target-version password from the source-version password during an upgrade. Therefore, do not start and end an MD5 authentication password with $@$@. |
| **hmac-md5** | Indicates HMAC-MD5 authentication.  Configuring HMAC-SHA256 rather than HMAC-MD5 is recommended for the sake of security. | - |
| **hmac-sha256** | Indicates HMAC-SHA256 ciphertext authentication. | - |
| *key-id* | Specifies a key ID for authentication, which must be the same as the one configured at the other end. | The value is an integer ranging from 1 to 255. |
| **null** | Indicates the null authentication mode. | - |
| **keychain** | Specifies the keychain authentication mode.  Before configuring this parameter, run the keychain command to create a keychain, and run the key-id, key-string, and algorithm commands to configure a key ID, a password, and an authentication algorithm for the keychain. Otherwise, OSPF authentication fails.  Currently, OSPF supports the MD5, SHA-1, SHA-256, SM3, HMAC-MD5, HMAC-SHA1-12, HMAC-SHA1-20, HMAC-SHA256, HMAC-SHA384, and HMAC-SHA512 algorithms. | - |
| *keychain-name* | Specifies a keychain name. | The value is a string of 1 to 47 case-insensitive characters.  The value cannot contain question marks (?) and spaces However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks at both ends of the password are used as a part of the password. |
| **simple** | Sets the simple authentication mode.  To prevent high security risks, you are advised to select the ciphertext mode. To ensure device security, change the password periodically. | * The length of a simple password ranges from 1 to 8. * A ciphertext password is a string of 24 to 128 characters.   By default, the simple authentication mode is cipher. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Due to inherent defects and flawed implementation of the TCP/IP protocol suite, there are an increasing number of attacks, which poses greater threats on TCP/IP networks than ever before. The attacks on network devices may lead to network failures. To configure an authentication mode and a password for an OSPF interface to improve OSPF network security, run the ospf authentication-mode command.

**Prerequisites**

Run the **ospf enable multi-area** command first.

**Configuration Impact**

Interface authentication is used to set authentication mode and password used between neighboring devices. It takes precedence over area authentication.

**Precautions**

Null indicates an authentication mode, which does not mean that no authentication is configured.Interfaces on the same network segment must be configured with the same authentication mode and password.For security purposes, md5 and hmac-md5 are not recommended. If they must be used, run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol feature package WEAKEA first.


Example
-------

# Configure HMAC-SHA256 authentication on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 0
[*HUAWEI-ospf-1-area-0.0.0.0] quit
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] quit
[*HUAWEI-ospf-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0
[*HUAWEI-100GE1/0/1] ospf enable multi-area 1
[*HUAWEI-100GE1/0/1] ospf authentication-mode hmac-sha256 1 cipher YsHsjx_202206 multi-area 1

```