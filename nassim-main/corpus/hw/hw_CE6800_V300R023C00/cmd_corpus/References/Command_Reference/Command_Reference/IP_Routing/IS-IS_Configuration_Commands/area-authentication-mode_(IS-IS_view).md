area-authentication-mode (IS-IS view)
=====================================

area-authentication-mode (IS-IS view)

Function
--------



The **area-authentication-mode** command enables an IS-IS device to authenticate received Level-1 packets (LSPs and SNPs) based on the pre-defined authentication mode and password and to add authentication information to the Level-1 packets to be sent.

The **undo area-authentication-mode** command disables the function.

It is recommended that you enable authentication and use the HMAC-SHA256 algorithm to improve security, preventing route information from being modified by unauthorized users.



By default, the system neither encapsulates the generated Level-1 routing packets with authentication information nor authenticates received Level-1 routing packets. Configuring area authentication is recommended to ensure system security.


Format
------

**area-authentication-mode** { **simple** { **plain** *simple-plain* | [ **cipher** ] *simple-cipher* } | **md5** { **plain** *plain* | [ **cipher** ] *cipher* } } [ **ip** | **osi** ] [ [ **snp-packet** { **send-only** | **authentication-avoid** } ] | **all-send-only** ]

**area-authentication-mode keychain** *keychain-name* [ [ **snp-packet** { **send-only** | **authentication-avoid** } ] | **all-send-only** ]

**area-authentication-mode hmac-sha256 key-id** *key-id* { **plain** *plain* | [ **cipher** ] *cipher* } [ [ **snp-packet** { **send-only** | **authentication-avoid** } ] | **all-send-only** ]

**undo area-authentication-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **simple** | Indicates the simple authentication.  For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | - |
| **plain** | Indicates the simple text mode. Only the simple text can be entered. The password in the configuration file is displayed as a simple text. Simple authentication used the simple text mode by default.  When configuring an authentication password, select the ciphertext mode because the password is saved in the configuration file as a simple text if you select the simple text mode, which has a high risk. To ensure device security, change the password periodically. | - |
| *plain* | Specifies a cleartext password. | 1. The value is a string of case-sensitive characters, which can be letters or digits.   When the authentication mode is simple, the value is a string of 1 to 16 characters. When the authentication mode is MD5 or HMAC-SHA256, the value is a string of 1 to 255 characters.  The value cannot contain question marks (?) or spaces. However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are used as a part of the password. |
| *simple-plain* | Specifies a simple-text password. | The value is a string of case-sensitive characters that can be letters or digits.   * In simple authentication, the value is a string of 1 to 16 characters. * In MD5 or HMAC-SHA256 authentication, the value is a string of 1 to 255 characters.   A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are a part of the password. |
| **cipher** | Indicates that the password is in ciphertext mode. You can enter a cleartext or ciphertext. When you view the configuration file, the password is displayed in ciphertext. The ciphertext mode is used by default. | - |
| **cipher** *simple-cipher* | Indicates the ciphertext mode. The simple text or ciphertext can be entered. The password in the configuration file is displayed as a ciphertext. MD5 authentication uses the ciphertext mode by default.  A ciphertext password is a character string that is encrypted using a special algorithm. A ciphertext is used for configuration restoration. The parameter value must be the same as the ciphertext in the configuration file. | The value is a string of case-sensitive characters that can be letters or digits.  In simple authentication, the value is a string of 1 to 16 characters in plain text or a string of 24 to 128 characters in cipher text. In md5 or hmac-sha256 authentication, the value is a string of 1 to 255 characters in plain text or a string of 20 to 432 characters in cipher text.  A 24-character ciphertext password configured in an earlier version is also supported in this version.  The value cannot contain question marks (?) or spaces. However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are used as a part of the password. |
| *cipher* | Specifies a ciphertext password.  A ciphertext password is a character string that is encrypted using a special algorithm. A ciphertext is used for configuration restoration. The parameter value must be the same as the ciphertext in the configuration file. | The value is a string of case-sensitive characters that can be letters or digits. When double quotation marks are used around the string, spaces are allowed in the string.   * In simple authentication, the value is a string of 1 to 16 characters in plain text or a string of 24 to 128 characters in cipher text. * When the authentication mode is MD5 or HMAC-SHA256, the value is a string of 1 to 255 characters in plain text or a string of 20 to 432 characters in cipher text. * If a 24-character ciphertext password can be configured in the source version, the target version is compatible with the source version. * The value cannot contain question marks (?) or spaces. However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are used as a part of the password. |
| *simple-cipher* | Specifies a simple-text or ciphertext password.  A ciphertext password is a character string that is encrypted using a special algorithm. A ciphertext is used for configuration restoration. The parameter value must be the same as the ciphertext in the configuration file. | The value is a string of case-sensitive characters that can be letters or digits When quotation marks are used around the string, spaces are allowed in the string.   * In simple authentication, the value is a string of 1 to 16 characters in a simple text, or a string of 24 to 128 characters in a ciphertext. * In MD5 or HMAC-SHA256 authentication, the value is a string of 1 to 255 characters in a simple text, or a string of 20 to 432 characters in a ciphertext.   A 24-character ciphertext password configured in an earlier version is also supported in this version.  A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are a part of the password. |
| **md5** | Indicates that the password is transmitted after being encrypted using HMAC-MD5.  For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended. | - |
| **ip** | Indicates the IP authentication password. This parameter is not specified in most cases. | - |
| **osi** | Indicates the OSI authentication password. By default, the OSI authentication password is specified. | - |
| **snp-packet** | Enables the device to authenticate SNPs. | - |
| **send-only** | Encapsulates generated LSPs and SNPs with authentication information and authenticates received LSPs instead of the SNPs. | - |
| **authentication-avoid** | Prevents the device from encapsulating the generated SNP packets with authentication information and authenticating received SNPs. After the parameter is configured, the device encapsulates only the generated LSPs with authentication information and authenticates received LSPs. | - |
| **all-send-only** | Encapsulates authentication information in generated LSPs and SNPs but does not check authentication information in the received LSPs or SNPs. | - |
| **keychain** *keychain-name* | Specifies the keychain that changes with time.  Before configuring keychain authentication, run the keychain command to create a keychain, the key-id command to configure a key ID, the key-string command to configure a password, and the algorithm command to configure an algorithm. Otherwise, the authentication fails.  Keychain authentication supports only HMAC-MD5, SM3, HMAC-SHA256, HMAC-SHA384, and HMAC-SHA512 algorithms. If any other algorithm is used, authentication fails.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain. | The value is a string of 1 to 47 characters. When quotation marks are used around the string, spaces are allowed in the string.  A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are a part of the password. |
| **hmac-sha256** | Encapsulates generated packets with the HMAC-SHA256 authentication and a password encrypted using the HMAC-SHA256 algorithm and authenticates received packets. | - |
| **key-id** *key-id* | Specifies the key ID in MD5, HMAC-MD5, or HMAC-SHA256 authentication mode. The key ID must be the same as the key ID on the peer device. | The value is an integer ranging from 0 to 65535. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure network security, you can enable a router to authenticate received packets based on the pre-defined authentication mode or add authentication information to the packets to be sent. Only the packets that are authenticated can be forwarded on the network.The **area-authentication-mode** command is valid only on Level-1 or Level-1-2 routers, and it is for all topologies in an IS-IS process.

**Configuration Impact**

After the **area-authentication-mode** command is run, newly received Level-1 LSPs and SNPs that fail to be authenticated are discarded. All Level-1 LSPs in the local LSDB that fail to be authenticated are not discarded immediately until the LSPs age out. Therefore, to prevent packets from being lost before authentication is configured on the peer end, you can specify all-send-only when deploying authentication on the network where services have been deployed.The establishment of the Level-1 neighbor relationship is not affected, regardless of whether the packets match the area authentication.

**Precautions**

The md5 parameter in this command can be used only after the weak security algorithm/protocol feature package WEAKEA has been installed using the **install feature-software WEAKEA** command.If the password is set but ip and osi are not specified, the system uses osi by default.If the keychain password is used, the ip or osi parameter cannot be configured.The authentication takes effect only on the end that is configured with authentication. The receive end that is not configured with authentication can still receive the LSP with the authentication password.If MD5 authentication is negotiated for IS-IS and then changed to keychain authentication, IS-IS needs to renegotiate the authentication mode. If keychain authentication is not configured on the peer end, IS-IS services may be affected.


Example
-------

# Set the area authentication mode to keychain and keychain name to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] area-authentication-mode keychain YsHsjx_202206

```

# Set the area authentication password to YsHsjx\_202206 and the authentication algorithm to HMAC-SHA256.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] area-authentication-mode hmac-sha256 key-id 2 YsHsjx_202206

```