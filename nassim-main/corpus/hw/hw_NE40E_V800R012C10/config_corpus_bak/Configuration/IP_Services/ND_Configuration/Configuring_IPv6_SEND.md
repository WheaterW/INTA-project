Configuring IPv6 SEND
=====================

The Secure Neighbor Discovery (SEND) protocol is a security extension of the Neighbor Discovery Protocol (NDP) in IPv6.

#### Usage Scenario

In the IPv6 protocol suite, ND is significant in ensuring the availability of neighbors on the local link. However, as network security problems intensify, the security of ND becomes a concern. Standards define several threats to ND security, some of which are described as follows.

**Table 1** IPv6 ND attacks
| Attack Method | Description |
| --- | --- |
| NS/NA spoofing | An attacker sends an authorized node (host or router) either an NS message with a bogus source link-layer address option or an NA message with a bogus target link-layer address option. Packets from the authorized node are then sent to this link-layer address. |
| Neighbor unreachability detection (NUD) failure | An attacker repeatedly sends forged NA messages in response to an authorized node's NUD NS messages so that the authorized node cannot detect neighbor unreachability. The consequences of this attack depend on why the neighbor became unreachable and how the authorized node would behave if it knew that the neighbor has become unreachable. |
| DAD attack | An attacker responds to every DAD attempt made by a host that accesses the network, claiming that the address is already in use. This is performed to ensure that the host will never obtain an address. |
| Spoofed Redirect message | An attacker uses the link-local address of the first-hop router to send a Redirect message to an authorized host. The authorized host accepts this message because it mistakenly considers that the message came from the first-hop router. |
| Replay attack | An attacker obtains valid messages and replays them. Even if NDP messages are protected by signatures or certificates so that their contents cannot be forged, they are still prone to replay attacks. |
| Bogus address prefix | An attacker sends a bogus RA message specifying that some prefixes are on-link. If a prefix is on-link, a host will not send any packets that contain this prefix to the router. Instead, the host will send NS messages to attempt address resolution, but the NS messages are not responded to. As a result, the host is denied services. |
| Malicious last-hop router | An attacker multicasts bogus RA messages, or unicasts them in response to multicast RS messages, to a host attempting to discover a last-hop router. If the host selects the attacker as its default router, the attacker is able to function as a man-in-the-middle and intercept all messages exchanged between the host and its destination. |


To counter these threats, SEND specifies security mechanisms to extend ND. SEND defines cryptographically generated addresses (CGAs), CGA option, and Rivest Shamir Adleman (RSA) Signature option, which are used to ensure that the sender of an ND message is the owner of the message's source address. SEND also defines Timestamp and Nonce options to prevent replay attacks.

* CGA: contains an IPv6 interface identifier that is generated from a one-way hash of the public key and associated parameters.
* CGA option: contains information used to verify the sender's CGA, including the public key of the sender. This option is used to check the validity of source IPv6 addresses carried in ND messages.
* RSA Signature option: contains the hash value of the sender's public key and contains the digital signature generated from the sender's private key and ND messages. This option is used to check the integrity of ND messages and authenticate the identity of the sender.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If an attacker uses an address that belongs to an authorized node, the attacker must use the node's public key for encryption. Otherwise, the receiver can detect the attempted attack after checking the CGA option. Even if the attacker obtains the public key of the authorized node, the receiver can still detect the attempted attack after checking the digital signature, which is generated from the sender's private key.
* Timestamp option: a 64-bit unsigned integer field containing a timestamp. The value indicates the number of seconds since January 1, 1970, 00:00 UTC. This option prevents unsolicited advertisement messages and Redirect messages from being replayed. The receiver is expected to ensure that the timestamp of the recently received message is the latest.
* Nonce option: contains a random number selected by the sender of a solicitation message. This option prevents replay attacks during message exchange. For example, a sender sends an NS message carrying the Nonce option and receives an NA message as a response that also carries the Nonce option; the sender verifies the NA message based on the Nonce option.

#### Pre-configuration Tasks

Before configuring IPv6 SEND, complete the following tasks:

* Configure IPv6 ND.


[Configuring a CGA IPv6 Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0033.html)

To enable IPv6 SEND to protect ND messages that carry CGA and RSA options, configure a CGA IPv6 address on an interface that sends ND messages.

[Enabling IPv6 SEND](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0034.html)

After a rate limit for the system to compute or verify the RSA signature in a specified period (1s), the key length allowed on an interface, and timestamp parameters in ND messages are set, the system considers the received ND messages that do not comply with these settings invalid.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6_cfg_0035.html)

After configuring IPv6 SEND, verify the configuration.