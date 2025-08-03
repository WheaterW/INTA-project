peer password (VPN instance MSDP view/MSDP view of a public network instance)
=============================================================================

peer password (VPN instance MSDP view/MSDP view of a public network instance)

Function
--------



The **peer password** command configures message-digest algorithm 5 (MD5) authentication for establishing a TCP connection between Multicast Source Discovery Protocol (MSDP) peers and transmitting MSDP messages.

The **undo peer password** command cancels MD5 authentication for an MSDP peer.



By default, MD5 authentication is not configured for an MSDP peer.


Format
------

**peer** *peer-address* **password** **simple** *simple-password*

**peer** *peer-address* **password** **cipher** *cipher-password*

**undo peer** *peer-address* **password**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The value is in dotted decimal notation. |
| **simple** *simple-password* | Specifies a password in simple mode.  For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | The value is a string of 1 to 255 case-sensitive characters, without spaces.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| **cipher** *cipher-password* | Specifies a password in ciphertext mode. | In the case of a plain text, the value is a string of 1 to 255 case-sensitive characters, without spaces. In the case of a cipher text password, the value is a string of 20 to 432 case-sensitive characters, without spaces.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enhance the security of TCP connections between MSDP peers, run the **peer password** command to configure MD5 authentication.The MD5 encryption algorithm has low security and has security risks. You are advised to use the MSDP Keychain encryption algorithm.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.MSDP peers have been configured.

**Configuration Impact**

If this command is run more than once, the latest configuration overrides the previous one.

**Precautions**

MSDP peers must be configured with the same authentication password; otherwise, the TCP connection cannot be set up and MSDP messages cannot be exchanged. The plaintext mode can be configured on ane end, with the ciphertext mode on the other end.MSDP MD5 authentication and MSDP keychain authentication are mutually exclusive. This command can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed using the **install feature-software WEAKEA** command.The **peer password** command can be used only after the weak security algorithm function is enabled. If the weak security algorithm function has been disabled, an error message will be displayed when you configure the weak security algorithm. To enable the weak security algorithm function, run the **undo crypto weak-algorithm disable** command.


Example
-------

# In the public network instance, configure MD5 authentication for the MSDP peer 1.1.1.1 and set the password to YsHsjx\_202206 in cipher text.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 1.1.1.1 connect-interface LoopBack 1
[*HUAWEI-msdp] peer 1.1.1.1 password cipher YsHsjx_202206

```