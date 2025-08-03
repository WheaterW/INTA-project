rip authentication-mode md5
===========================

rip authentication-mode md5

Function
--------



The **rip authentication-mode md5** command sets the authentication mode to MD5 authentication mode for RIP-2.

The **undo rip authentication-mode md5** command deletes the configured authentication mode.



By default, authentication for RIP-2 is disabled on an interface. Configuring authentication is recommended to ensure system security.


Format
------

**rip authentication-mode md5 nonstandard keychain** *keychain-name*

**undo rip authentication-mode md5 nonstandard keychain**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **md5** | Indicates the Message Digest version 5 (MD5) authentication mode.  For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended. | - |
| **nonstandard** | Indicates that the packet for MD5 ciphertext authentication is in the nonstandard format (IETF standard). | - |
| **keychain** *keychain-name* | Specifies the key linked list authentication mode.  Before configuring this parameter, run the keychain command to create a keychain. Then, run the key-id, key-string, and algorithm commands to configure a key ID, a password, and an authentication algorithm for this keychain. Otherwise, the authentication will fail.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain. | The value is a string of 1 to 47 case-insensitive characters.  The value cannot contain question marks (?) and spaces However, when double quotation marks are used around the password, spaces are allowed in the password. In this case, the double quotation marks at both ends of the password are used as a part of the password. |



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

The md5 parameter in this command can be used only after the weak security algorithm/protocol feature package WEAKEA has been installed by running the **install feature-software WEAKEA** command.


Example
-------

# Set MD5 authentication in the usual format.
```
<HUAWEI> install feature-software WEAKEA
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip authentication-mode md5 nonstandard keychain YsHsjx_202206

```