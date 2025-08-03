bfd authentication-mode
=======================

bfd authentication-mode

Function
--------



The **bfd authentication-mode** command enables negotiation authentication for a BFD session with a specified peer IP address and configures authentication information.

The **undo bfd** command disables negotiation authentication for a BFD session with a specified peer IP address.



By default, negotiation authentication is disabled for a BFD session. You are advised to configure BFD negotiation authentication to reduce security risks.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**bfd single-hop peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet**

**bfd multi-hop peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet**

**undo bfd single-hop peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ]

**undo bfd multi-hop peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**bfd single-hop peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet**

**bfd multi-hop peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet**

**undo bfd single-hop peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ]

**undo bfd multi-hop peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **met-sha1** | Specifies the M-SHA1 algorithm. | - |
| **key-id** *key-id-value* | Specifies the key ID. | The value is an integer ranging from 1 to 255. |
| **cipher** *cipher-text* | Specifies the encryption password. | The value is a string of case-sensitive characters, spaces not supported.   * If a plaintext authentication password is entered, the value is a string of 1 to 20 characters. * A ciphertext authentication password is a string of 20 to 148 characters. |
| **nego-packet** | Authenticates BFD negotiation packets. | - |
| **single-hop** | Specifies the BFD for IP single-hop session type. | - |
| **peer-ipv6** *ipv6-address* | Specifies the peer IPv6 address of the BFD sessions with negotiation authentication.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **multi-hop** | Specifies the BFD for IP multi-hop session type. | - |
| **peer-ip** *ip-address* | Specifies the peer IPv4 address of the BFD sessions with negotiation authentication. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-name* | Specifies the name of a VPN instance for the BFD sessions with negotiation authentication. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When configuring negotiation authentication for BFD sessions, you need to select different commands according to the type of the target BFD sessions.

* bfd single-hop authentication-modeEnable negotiation authentication for a BFD for IP single-hop session with the specified peer IP address on the network and configure the key ID and encryption password.
* bfd multi-hop authentication-modeEnable negotiation authentication for a BFD for IP multi-hop session with the specified peer IP address on the network and configure the key ID and encryption password.

**Prerequisites**

BFD has been enabled globally using the **bfd** command.

**Precautions**

* The peer device must be configured with the same algorithm (met-sha1) and key (key-id key-id-value) as the local device to ensure that BFD sessions can be authenticated and go Up after negotiation.
* BFD negotiation authentication information is configured based on the peer IP address.


Example
-------

# Configure negotiation packet authentication for a single-hop BFD session with the peer IP address 10.1.1.1 and key-id set to 1 and cipher password set to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] bfd single-hop peer-ip 10.1.1.1 authentication-mode met-sha1 key-id 1 cipher YsHsjx_202206 nego-packet

```