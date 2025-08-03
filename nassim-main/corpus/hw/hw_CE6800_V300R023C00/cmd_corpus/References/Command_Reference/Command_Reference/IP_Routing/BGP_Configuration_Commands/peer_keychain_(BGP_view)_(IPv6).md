peer keychain (BGP view) (IPv6)
===============================

peer keychain (BGP view) (IPv6)

Function
--------



The **peer keychain** command configures the Keychain authentication for establishing the TCP connection between BGP peers.

The **undo peer keychain** command deletes the Keychain authentication.



By default, the Keychain authentication is not performed during TCP connection establishment between peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **keychain** *keychain-name*

**undo peer** *ipv6-address* **keychain**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The address is in the format of X:X:X:X:X:X:X:X. |
| *keychain-name* | Specifies the name of the Keychain authentication.  Before configuring this parameter, run the keychain command to create a keychain. Then, run the key-id, key-string, and algorithm commands to configure a key ID, a password, and an authentication algorithm for this keychain. Otherwise, the authentication will fail, and the BGP peer relationship fails to be established.  If the dependent keychain is deleted, the neighbor relationship may be interrupted. Therefore, exercise caution when deleting the keychain. | The value is a string of 1 to 47 case-insensitive characters. The characters do not include question marks (?) or spaces. However, when double quotation marks (") are used around the string, spaces are allowed in the string. |



Views
-----

BGP view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 keychain keychain_1

```