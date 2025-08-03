peer keychain (VPN instance MSDP view/MSDP view of a public network instance)
=============================================================================

peer keychain (VPN instance MSDP view/MSDP view of a public network instance)

Function
--------



The **peer keychain** command applies a keychain to a Multicast Source Discovery Protocol (MSDP) peer, so that the peer can use this keychain to authenticate TCP connection setup and MSDP message exchange requests.

The **undo peer keychain** command cancels keychain authentication for an MSDP peer.



By default, keychain authentication is not configured for an MSDP peer. Configuring keychain authentication is recommended to improve system security.


Format
------

**peer** *peer-address* **keychain** *keychain-name*

**undo peer** *peer-address* **keychain**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The value is in dotted decimal notation. |
| *keychain-name* | Specifies the name of a keychain. | The value must be a keychain-name parameter value specified in the keychain command. The value is a string of 1 to 47 characters. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve system security, run the peer **keychain** command to apply a keychain to an MSDP peer, so that the peer can use this keychain to authenticate TCP connection setup and MSDP message exchange requests. Keychain implements higher MSDP peer authentication security than the message-digest algorithm 5 (MD5).

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.MSDP peers have been configured.A keychain name has been specified using the keychain-name parameter in the **keychain** command. Otherwise, a TCP connection cannot be set up.

**Configuration Impact**

If the peer **keychain** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

You must configure keychain authentication on both MSDP peers. Encryption algorithms and passwords configured for keychain authentication on both MSDP peers must be the same; otherwise, the TCP connection cannot be set up between MSDP peers and MSDP messages cannot be transmitted.The MD5 encryption algorithm has low security and poses security risks. You are advised to use the MSDP keychain encryption algorithm.To ensure high security, do not use the MD5 algorithm.MSDP MD5 authentication and MSDP keychain authentication are mutually exclusive.


Example
-------

# In the public network instance, apply the keychain named huawei to the MSDP peer 1.1.1.2.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 1.1.1.2 connect-interface LoopBack 1
[*HUAWEI-msdp] peer 1.1.1.2 keychain Huawei

```