rip authentication-mode
=======================

rip authentication-mode

Function
--------



The **rip authentication-mode** command configures an authentication mode and associated parameters for RIP-2.

The **undo rip authentication-mode** command deletes the configured authentication mode.



By default, authentication for RIP-2 is disabled on an interface. Configuring authentication is recommended to ensure system security.


Format
------

**rip authentication-mode simple** { [ **cipher** ] *password-key* | **plain** *plain-text* }

**rip authentication-mode md5 nonstandard** { [ **cipher** ] *password-key* | **plain** *plain-text* } *key-id*

**rip authentication-mode md5 usual** { [ **cipher** ] *password-key* | **plain** *plain-text* }

**rip authentication-mode hmac-sha256** { [ **cipher** ] *password-key* | **plain** *plain-text* } *key-id*

**rip authentication-mode sm3** { [ **cipher** ] *password-key* | **plain** *plain-text* } *key-id*

**undo rip authentication-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cipher** | Indicates that the authentication text is encrypted. | - |
| *password-key* | Specifies the password and the ID of the key when MD5 authentication is used. | The value is a string of case-sensitive characters that can be letters or digits.  A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **plain** | Indicates that the authentication text is not encrypted.  When configuring an authentication password, select the ciphertext mode. If you select simpletext mode, the password is saved in simple text in the configuration files, which has a high risk. To ensure device security, change the password periodically. | - |
| *plain-text* | Indicates the keyword for simple authentication. | The value is a string of case-sensitive characters that can be letters or digits.  A password cannot contain a question mark (?), but can contain spaces if surrounded by double quotation marks (""). In this case, the double quotation marks are part of the password. |
| **md5** | Indicates the Message Digest version 5 (MD5) authentication mode. For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended. | - |
| **nonstandard** | Indicates that the packet for MD5 ciphertext authentication is in the nonstandard format (IETF standard). | - |
| *key-id* | Specifies the ciphertext authentication identifier. | The value is an integer ranging from 0 to 255. |
| **usual** | Indicates the standard (proprietary standard) packet format. | - |
| **hmac-sha256** | Indicates Hash Message Authentication Code (HMAC) for Secure Hash Algorithm 256 (SHA256). | - |
| **sm3** | Indicates SM3-based authentication. | - |
| **simple** | Indicates simple authentication.  For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure network security, you can enable a device to authenticate received packets based on specified rules or add authentication information to the packets to be sent. Only the packets that are authenticated can be forwarded on the network.After the **rip authentication-mode** command is run, the device discards the RIP packets whose authentication passwords are different from the interface authentication password set using this command; in addition, the device inserts the set authentication password into all the RIP packets to be sent by the interface.

**Precautions**

For security purposes, MD5 is not recommended. If MD5 is required, run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol feature package WEAKEA first.


Example
-------

# Set the authentication mode to HMAC-SHA256, and key ID to 200.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip authentication-mode hmac-sha256 cipher YsHsjx_202206 200

```