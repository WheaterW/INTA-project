peer keychain (BGP-VPN instance view)
=====================================

peer keychain (BGP-VPN instance view)

Function
--------



The **peer keychain** command configures the Keychain authentication for establishing the TCP connection between BGP peers.

The **undo peer keychain** command deletes the Keychain authentication.



By default, the Keychain authentication is not performed during TCP connection establishment between peers.


Format
------

**peer** *ipv4-address* **keychain** *keychain-name*

**undo peer** *ipv4-address* **keychain**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
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

# Configure keychain authentication named keychain\_1 for the peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] keychain keychain_1 mode periodic daily
[*HUAWEI-keychain-keychain_1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 keychain keychain_1

```