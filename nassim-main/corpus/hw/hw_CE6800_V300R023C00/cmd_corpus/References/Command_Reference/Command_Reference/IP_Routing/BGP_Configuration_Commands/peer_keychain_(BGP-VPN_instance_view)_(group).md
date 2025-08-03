peer keychain (BGP-VPN instance view) (group)
=============================================

peer keychain (BGP-VPN instance view) (group)

Function
--------



The **peer keychain** command configures the Keychain authentication for establishing the TCP connection between BGP peers.

The **undo peer keychain** command deletes the Keychain authentication.



By default, the Keychain authentication is not performed during TCP connection establishment between peers.


Format
------

**peer** *group-name* **keychain** *keychain-name*

**undo peer** *group-name* **keychain**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *keychain-name* | Specifies the name of the Keychain authentication.  Before configuring this parameter, run the keychain command to create a keychain. Then, run the key-id, key-string, and algorithm commands to configure a key ID, a password, and an authentication algorithm for this keychain. Otherwise, the authentication will fail, and the BGP peer relationship fails to be established.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain. | The value is a string of 1 to 47 case-insensitive characters. The characters do not include question marks (?) or spaces. However, when double quotation marks (") are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Configuring Keychain authentication improves the security of the TCP connection. You must configure Keychain authentication specified for TCP-based applications on both BGP peers. Note that encryption algorithms and passwords configured for the Keychain authentication on both peers must be the same; otherwise, the TCP connection cannot be set up between BGP peers and BGP messages cannot be transmitted.

**Prerequisites**

Before configuring the BGP Keychain authentication, a Keychain in accordance with the configured keychain-name must be configured first.

**Precautions**

The peer keychain command and the peer password command are mutually exclusive.


Example
-------

# Configure keychain authentication named keychain\_1 for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] keychain keychain_1 mode periodic daily
[*HUAWEI-keychain-keychain_1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test
[*HUAWEI-bgp-instance-vpn1] peer test keychain keychain_1

```