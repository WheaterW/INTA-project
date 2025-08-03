isis authentication-mode (broadcast interface)
==============================================

isis authentication-mode (broadcast interface)

Function
--------



The **isis authentication-mode** command configures an IS-IS broadcast interface to authenticate Hello packets using the specified authentication mode and password.

The **undo isis authentication-mode** command cancels the authentication and deletes the password.



By default, no password is set and no authentication is performed. Configuring authentication is recommended to ensure system security.

It is recommended that you enable authentication and use the HMAC-SHA256 algorithm to improve security, preventing route information from being modified by unauthorized users.




Format
------

**isis authentication-mode** { **simple** { [ **cipher** ] *simple-cipher* | **plain** *simple-plain* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **level-1** | **level-2** ] [ **ip** | **osi** ] [ **send-only** ]

**isis authentication-mode keychain** *keychain-name* [ **level-1** | **level-2** ] [ **send-only** ]

**isis authentication-mode hmac-sha256 key-id** *key-id* { [ **cipher** ] *cipher* | **plain** *plain* } [ **level-1** | **level-2** ] [ **send-only** ]

**undo isis authentication-mode** [ **level-1** | **level-2** ]

**undo isis authentication-mode** { **simple** { **cipher** *simple-cipher* | **plain** *simple-plain* } | **md5** { **cipher** *cipher* | **plain** *plain* } } [ **level-1** | **level-2** ] [ **ip** | **osi** ] [ **send-only** ]

**undo isis authentication-mode keychain** *keychain-name* [ **level-1** | **level-2** ] [ **send-only** ]

**undo isis authentication-mode hmac-sha256 key-id** *key-id* { **cipher** *cipher* | **plain** *plain* } [ **level-1** | **level-2** ] [ **send-only** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **simple** | Indicates the simple authentication.  For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | - |
| **cipher** | Indicates that the password is in ciphertext mode. You can enter a cleartext or ciphertext. When you view the configuration file, the password is displayed in ciphertext. The ciphertext mode is used by default. | - |
| **cipher** *simple-cipher* | Indicates the ciphertext mode. The simple text or ciphertext can be entered. The password in the configuration file is displayed as a ciphertext. MD5 authentication uses the ciphertext mode by default.  A ciphertext password is a character string that is encrypted using a special algorithm. A ciphertext is used for configuration restoration. The parameter value must be the same as the ciphertext in the configuration file. | The value is a string of case-sensitive characters that can be letters or digits. When quotation marks are used around the string, spaces are allowed in the string.  In simple authentication, the value is a string of 1 to 16 characters in the simple text mode or a string of 24 to 128 characters in the ciphertext mode. In MD5 or hmac-sha256 authentication, the value is a string of 1 to 255 characters in the simple text mode or a string of 20 to 432 characters in the ciphertext mode.   * A 24-character ciphertext password configured in an earlier version is also supported in this version. * A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| *cipher* | Specifies a ciphertext password.  A ciphertext password is a character string that is encrypted using a special algorithm. A ciphertext is used for configuration restoration. The parameter value must be the same as the ciphertext in the configuration file. | The value is a string of case-sensitive characters that can be letters or digits.   * In simple authentication, the value is a string of 1 to 16 characters in a simple text, or a string of 24 to 128 characters in a ciphertext. * In md5 or hmac-sha256 authentication, the value is a string of 1 to 255 characters in a simple text, or a string of 20 to 432 characters in a ciphertext. * A 24-character ciphertext password configured in an earlier version is also supported in this version. * A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| *simple-cipher* | Specifies a simple-text or ciphertext password.  A ciphertext password is a character string that is encrypted using a special algorithm. A ciphertext is used for configuration restoration. The parameter value must be the same as the ciphertext in the configuration file. | The value is a string of case-sensitive characters that can be letters or digits.   * In simple authentication, the value is a string of 1 to 16 characters in a simple text, or a string of 24 to 128 characters in a ciphertext. * In md5 or hmac-sha256 authentication, the value is a string of 1 to 255 characters in a simple text, or a string of 20 to 432 characters in a ciphertext. * A 24-character ciphertext password configured in an earlier version is also supported in this version. * A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| *plain* | Specifies a cleartext password. | The value is a string of case-sensitive characters that can be letters or digits.  When the authentication mode is simple, the value is a string of 1 to 16 characters. When the authentication mode is md5 or hmac-sha256, the value is a string of 1 to 255 characters.  The value cannot contain question marks (?) or spaces. However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are used as a part of the password. |
| **plain** | Indicates the simple text mode. Only the simple text can be entered. The password in the configuration file is displayed as a simple text. Simple authentication used the simple text mode by default.  When configuring an authentication password, select the ciphertext mode because the password is saved in the configuration file as a simple text if you select the simple text mode, which has a high risk. To ensure device security, change the password periodically. | - |
| *simple-plain* | Specifies a simple-text password. | The value is a string of case-sensitive characters that can be letters or digits.  When the authentication mode is simple, the value is a string of 1 to 16 characters. When the authentication mode is md5 or hmac-sha256, the value is a string of 1 to 255 characters.  The value cannot contain question marks (?) or spaces. However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are used as a part of the password. |
| **md5** | Indicates that the password is transmitted after being encrypted using HMAC-MD5.  For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended. | - |
| **level-1** | Indicates the Level-1 authentication. | - |
| **level-2** | Indicates the Level-2 authentication.  The level-1 and level-2 parameters are valid only on IS-IS-capable Ethernet interfaces. | - |
| **ip** | Indicates the IP authentication password. This parameter cannot be configured when keychain authentication is used. | - |
| **osi** | Indicates the OSI authentication password. This parameter cannot be configured when keychain authentication is used. | - |
| **send-only** | Encapsulates the Hello packets to be sent with authentication information and ignores checking authentication information carried in received Hello packets. | - |
| **keychain** *keychain-name* | Specifies the keychain that changes with time.  Before configuring this parameter, run the keychain command to create a keychain, and run the key-id, key-string, and algorithm commands to configure the key ID, password, and authentication algorithm for the keychain. Otherwise, the authentication fails.  Keychain authentication supports only HMAC-MD5, HMAC-SHA256, HMAC-SHA384, and HMAC-SHA512 algorithms.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain. | The value is a string of 1 to 47 case-insensitive characters.  The value cannot contain question marks (?) and spaces. However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks are used as a part of the password. |
| **hmac-sha256** | Encapsulates generated packets with the HMAC-SHA256 authentication and a password encrypted using the HMAC-SHA256 algorithm and authenticates received packets. | - |
| **key-id** *key-id* | Specifies the key ID in MD5, HMAC-MD5, or HMAC-SHA256 authentication mode. The key ID must be the same as the key ID on the peer device. | The value is an integer ranging from 0 to 65535. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure network security, you can enable a router to authenticate received packets based on the pre-defined authentication mode or add authentication information to the packets to be sent. Only the packets that are authenticated can be forwarded on the network.The **isis authentication-mode** command enables the local node to discard all the Hello packets with authentication passwords that are different from the one set using this command. You can also enable the device to add the set authentication password to all the Hello packets to be sent.

**Prerequisites**



IS-IS has been enabled on the interface using the **isis enable** command.



**Precautions**



The md5 parameter in this command can be used only after the weak security algorithm/protocol feature package WEAKEA has been installed using the **install feature-software WEAKEA** command.If the keychain password is used, the ip or osi parameter cannot be configured.When a broadcast interface is emulated as a P2P interface through the **isis circuit-type** command or an emulated P2P interface is restored to the broadcast interface through the **undo isis circuit-type** command, the authentication of the IS-IS interface is restored to the default configuration.For broadcast interfaces, if Level-1 or Level-2 authentication is not specified in the command, Level-1-2 authentication is used by default.If MD5 authentication is negotiated for IS-IS and then changed to keychain authentication, IS-IS needs to renegotiate the authentication mode. If keychain authentication is not configured on the peer end, IS-IS services may be affected.




Example
-------

# Set the authentication password using HMAC-SHA256 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206

```