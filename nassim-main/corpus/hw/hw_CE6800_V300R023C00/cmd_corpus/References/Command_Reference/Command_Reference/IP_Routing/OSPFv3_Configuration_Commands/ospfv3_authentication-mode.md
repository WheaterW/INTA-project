ospfv3 authentication-mode
==========================

ospfv3 authentication-mode

Function
--------



The **ospfv3 authentication-mode** command configures an authentication mode and a password for an OSPFv3 interface.

The **undo ospfv3 authentication-mode** command deletes the authentication mode and password configured for an OSPFv3 interface.



By default, no authentication mode or password is configured for any OSPFv3 interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 authentication-mode** { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* { **plain** *plainText* | [ **cipher** ] *cipherText* } [ **instance** *instanceId* ]

**ospfv3 authentication-mode** { **keychain** *keychain-Name* } [ **instance** *instanceId* ]

**undo ospfv3 authentication-mode** { **hmac-sha256** | **hmac-sm3** } **key-id** *KeyId* [ **plain** *plainText* | **cipher** *cipherText* ] [ **instance** *instanceId* ]

**undo ospfv3 authentication-mode** { **keychain** *keychain-Name* } [ **instance** *instanceId* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hmac-sha256** | Configures the HMAC-SHA256 authentication mode. | - |
| **hmac-sm3** | Sets the HMAC-SM3 authentication mode. | - |
| **key-id** *KeyId* | This object indicates the key ID for ciphertext authentication on an interface. The key ID must be the same as that on the peer end. | The value is an integer ranging from 1 to 65535. |
| **plain** *plainText* | Specifies simple authentication. You can only type in simple passwords, and the passwords are displayed in simple mode in the configuration file.   * The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters. * For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | The value is a string of 1 to 255 characters. A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **cipher** *cipherText* | Specifies the ciphertext mode. You can enter a cleartext or a ciphertext, but the password is displayed in ciphertext in the configuration file. | The value can be a string of 1 to 255 characters for a simpletext and 20 to 432 characters for a ciphertext.  A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **instance** *instanceId* | Specifies the ID of the instance to which an interface belongs. | The value is an integer that ranges from 0 to 255. The default value is <b>0</b>. |
| **keychain** *keychain-Name* | Specifies the keychain authentication mode.  Before configuring keychain authentication, run the keychain command to configure a keychain, the key-id command to configure a key ID, the key-string command to configure a password, and the algorithm command to configure an algorithm. Otherwise, OSPFv3 authentication fails.  Currently, OSPFv3 supports only HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512 algorithms.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain. | The value is a string of 1 to 47 case-insensitive characters.  The value cannot contain question marks (?) and spaces However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks at both ends of the password are used as a part of the password. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Due to inherent defects and flawed implementation of the TCP/IP protocol suite, there are an increasing number of attacks, which poses greater threats on TCP/IP networks than ever before. The attacks on network devices may lead to network failures. To configure an authentication mode and a password for an OSPFv3 interface to improve OSPFv3 network security, run the ospfv3 **authentication-mode** command.

**Precautions**



OSPFv3 interface authentication takes precedence over OSPFv3 area authentication. If both interface authentication and area authentication are configured, the authentication succeeds as long as the interface authentication succeeds. If authentication is configured on an interface, OSPFv3 neighbor relationships can be established on the interface as long as interface authentication succeeds, regardless of the area authentication configuration or whether area authentication is configured.To configure OSPFv3 area authentication, run the **authentication-mode** command.




Example
-------

# Configure OSPFv3 HMAC-SHA256 authentication on the interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 authentication-mode hmac-sha256 key-id 10 cipher YsHsjx_202206

```