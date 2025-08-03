vlink-peer
==========

vlink-peer

Function
--------



The **vlink-peer** command creates and configures a virtual link.

The **undo vlink-peer** command deletes the virtual link or restores the default setting.



By default, no virtual link is configured.


Format
------

**vlink-peer** *router-id* [ **hello** *hello-interval* | **retransmit** *retransmit-interval* | **trans-delay** *trans-delay-interval* | **dead** *dead-interval* | **smart-discover** | [ **simple** [ **plain** *SPlainText* | [ **cipher** ] *SCipherText* ] | { **hmac-sha256** | **md5** | **hmac-md5** } [ *key-id* { **plain** *MPlainText* | [ **cipher** ] *MCipherText* } ] | **authentication-null** | **keychain** *keychain-name* ] ] \*

**undo vlink-peer** *router-id*

**undo vlink-peer** *router-id* { **hello** | **retransmit** | **trans-delay** | **dead** | **simple** | **hmac-sha256** | **md5** | **hmac-md5** | **authentication-null** | **keychain** | **smart-discover** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *router-id* | Specifies the router ID of a virtual link neighbor. | The value is in dotted decimal notation. |
| **hello** *hello-interval* | Specifies the interval at which Hello packets are sent on an interface.  This value must be equal to hello-interval value of the Device that sets up the virtual link through the interface. | The value is an integer ranging from 1 to 65535 seconds. The default value is 10 seconds. |
| **retransmit** *retransmit-interval* | Specifies the interval at which LSAs are retransmitted. | The value is an integer ranging from 1 to 3600, in seconds. The default value is 5 seconds. |
| **trans-delay** *trans-delay-interval* | Specifies the delay in sendingLSAs on an interface. | The value is an integer ranging from 1 to 3600, in seconds. The default value is 1 second. |
| **dead** *dead-interval* | Specifies the dead interval.  This value must be equal to dead-interval of the Device that sets up a virtual link through the interface. In addition, the value must be at least 4 times of hello-interval. | The value is an integer ranging from 1 to 235926000, in seconds. The default value is 40 seconds. |
| **smart-discover** | Enables the device to proactively send Hello packets. | - |
| **simple** | Indicates the simple authentication mode.   * The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters. * For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | - |
| **plain** | Indicates the plaintext authentication. You can only type in the plaintext, and it is displayed as a plaintext in the configuration file. When configuring an authentication password, select the ciphertext mode because the password is saved as a plaintext in the configuration file if you select the plaintext mode, which has a high risk. In addition, to ensure device security, change the password periodically. | - |
| *SPlainText* | Specifies a plaintext password. | The value is a string of characters.   * In simple mode, the value is a string of 1 to 8 characters. * In md5, hmac-md5 or hmac-sha256 mode, the value is a string of 1 to 255 characters.   Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| **cipher** | Indicates the cipher authentication.  You can type in a simpletext or ciphertext, but it is displayed as the ciphertext in the configuration file. | - |
| *SCipherText* | Specifies a ciphertext. | The value is a string of characters.   * For simple authentication, a simpletext is 1 to 8 characters, and a ciphertext password is 24 to 128 characters. * For MD5, HMAC-MD5, or HMAC-SHA256 authentication, a simpletext is 1 to 255 characters, and a ciphertext password is 20 to 432characters.   Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| **hmac-sha256** | Indicates the HMAC-SHA256 authentication mode.  By default, the hmac-sha256 authentication mode is cipher. | - |
| **md5** | Indicates the MD5 authentication mode.  By default, the md5 authentication mode is cipher. For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended. | - |
| **hmac-md5** | Indicates the HMAC-MD5 authentication mode.  By default, the hmac-md5 authentication mode is cipher. For the sake of security, using the HMAC-SHA256 algorithm rather than the HMAC-MD5 algorithm is recommended. | - |
| *key-id* | Specifies a key ID for ciphertext authentication.  The key ID must be consistent with that of the peer. | The value is an integer ranging from 1 to 255. |
| *MPlainText* | Specifies a plaintext password. | The value is a string of characters.   * In simple mode, the value is a string of 1 to 8 characters. * In md5, hmac-md5 or hmac-sha256 mode, the value is a string of 1 to 255 characters.   Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| *MCipherText* | Specifies a ciphertext. | The value is a string of characters.   * For simple authentication, a simpletext is 1 to 8 characters, and a ciphertext password is 24 to 128 characters. * For MD5, HMAC-MD5, or HMAC-SHA256 authentication, a simpletext is 1 to 255 characters, and a ciphertext password is 20 to 432characters.   Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| **authentication-null** | Sets the null authentication mode. | - |
| **keychain** | Indicates the keychain authentication.  Before configuring this parameter, run the keychain command to create a keychain. Then, run the key-id, key-string, and algorithm commands to configure a key ID, a password, and an authentication algorithm for this keychain. Otherwise, the OSPF authentication fails.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain. | - |
| *keychain-name* | Specifies the name of a keychain. | The value is a string of 1 to 47 case-insensitive characters. The characters do not include question marks (?) or spaces. However, when double quotation marks (") are used around the string, spaces are allowed in the string. |



Views
-----

OSPF area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After OSPF is divided into different areas, OSPF routes between non-backbone areas are updated by route exchange with the backbone area. Therefore, OSPF requires that all non-backbone areas keep connected to the backbone area and devices within the backbone area also keep connected. In real-world scenarios, however, these requirements cannot be met due to various limitations. Configuring OSPF virtual links can solve the problem.

**Configuration Impact**

Establish virtual links between the non-backbone areas and the backbone area, and between devices within the backbone area to ensure connectivity in an OSPF network.

**Follow-up Procedure**

Different vendors may use different MTUs as default settings. To ensure consistency, run the **undo ospf mtu-enable** command to set the default MTU to 0 when DD packets are sent on an OSPF interface.If the MTU of DD packets is configured, the neighbor relationship will be reestablished.

**Precautions**

The md5 and hmac-md5 parameters in this command can be used only after the weak security algorithm/protocol feature package has been installed using the **install feature-software WEAKEA** command.The default parameter values are recommended when a virtual link is configured; however, you can modify the parameter values as needed. Suggested parameter configurations are as follows:

* The smaller the hello value, the faster the device detects network changes and the more network resources are consumed.
* If the retransmit parameter is set too small, unnecessary LSAs may be retransmitted. Setting the parameter to a large value is recommended on a low-speed network.
* The authentication mode of the virtual link must be the same as that of the backbone area.The virtual link function does not apply to DCN processes.


Example
-------

# Configure a virtual link with the peer Router ID 1.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] area 2
[*HUAWEI-ospf-100-area-0.0.0.2] vlink-peer 1.1.1.1

```