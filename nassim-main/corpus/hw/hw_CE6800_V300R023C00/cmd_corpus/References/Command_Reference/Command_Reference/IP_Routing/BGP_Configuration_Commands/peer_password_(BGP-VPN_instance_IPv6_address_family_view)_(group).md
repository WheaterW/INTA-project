peer password (BGP-VPN instance IPv6 address family view) (group)
=================================================================

peer password (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer password** command configures Message Digest 5 (MD5) authentication for BGP messages exchanged between BGP peers during TCP connection establishment.

The **undo peer password** command restores the default configuration.



By default, the BGP device to implement Message Digest 5 (MD5) authentication for BGP messages exchanged during the establishment of a TCP connection with a peer is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **password** **simple** *simple-password*

**peer** *group-name* **password** **cipher** *cipher-password*

**undo peer** *group-name* **password**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **simple** *simple-password* | Specifies a simple text password.  For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | The value is a string of 1 to 255 case-sensitive characters, without spaces.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| **cipher** *cipher-password* | Specifies a cipher text password. | In the case of a plain text, the value is a string of 1 to 255 case-sensitive characters, without spaces. In the case of a cipher text password, the value is a string of 20 to 432 case-sensitive characters, without spaces.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP uses TCP as the transport layer protocol. To improve BGP security, you can perform MD5 authentication when establishing a TCP connection. In MD5 authentication of BGP, only the MD5 authentication password is set for the TCP connection, and the authentication is performed by TCP.A password can be set in plaintext or ciphertext mode. The two modes determine how the password is saved in the configuration file.

* Plaintext: The character string set by the user is directly saved.
* Ciphertext: The character string is encrypted using a special algorithm before it is saved.

**Prerequisites**

The **peer as-number** command has been run to create BGP peers or BGP peer groups.

**Configuration Impact**

BGP MD5 authentication does not authenticate BGP message. It only sets an MD5 authentication password for a TCP connection, and TCP performs authentication. If the authentication fails, no TCP connection is established.

**Precautions**

The MD5 encryption algorithm has low security and has security risks. You are advised to use a more secure encryption algorithm within the encryption algorithm range supported by the protocol.After MD5 is configured on a peer, keychain cannot be configured on the peer.If the passwords configured on both ends of a BGP peer relationship are the same, the BGP peer relationship is not re-established. However, if the interval configured on both ends exceeds the holdtime of the BGP peer session or the passwords configured on both ends are different, the BGP peer relationship is disconnected due to timeout.If authentication is configured for a peer using the **peer password** command, authentication is configured for a peer group using the **peer password** command, and you want to add the peer to the peer group and let the peer inherit the authentication configuratoin form the peer group, it is recommended that you run the **undo peer password** command to delete the configuration of the peer before adding the peer to the peer group using the **peer group** command.


Example
-------

# Configure authentication for the TCP connection between a device and its peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group test
[*HUAWEI-bgp-6-vpn1] peer test password cipher YsHsjx_202206

```