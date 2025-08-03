IPv6 SEND
=========

IPv6 SEND

#### Security Policy Introduction

The IPv6 SEcure Neighbor Discovery (SEND) resolves the security problems that threaten the IPv6 Neighbor Discovery Protocol (NDP).

In the IPv6 protocol suite, ND is significantly important in ensuring availability of neighbors on the local link. As networks rapidly develop, ND is facing growing attacks. To defend against ND, SEND, as an extension of ND, is defined in relevant standards. SEND defines Cryptographically Generated Addresses (CGAs), CGA option, and Rivest Shamir Adleman (RSA) Signature option, which are used to ensure that the sender of an ND message is the owner of the message's source address. SEND also defines Timestamp and Nonce options to prevent replay attacks.

* CGA: contains an IPv6 interface identifier that is generated based on a one-way hash of the public key and associated parameters.
* CGA option: contains information used to verify the sender's CGA, including the public key of the sender. The CGA option is used to check whether the sender of an ND message is the owner of the message's source address.
* RSA signature option: contains the hash value of the sender's public key and the digital signature generated based on the sender's private key and ND messages. The RSA signature option is used to check the integrity of ND messages and authenticity of the sender.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  To use an address that belongs to an authorized node, the attacker must use the public key of the authorized node for encryption. Otherwise, the receiver can detect the attack after checking the CGA option. Even if the attacker obtains the public key of the authorized node, the receiver can still detect the attack after checking the digital signature, which is generated based on the sender's private key.
* Timestamp: a 64-bit unsigned integer field containing a timestamp. The value indicates the number of seconds since January 1, 1970, 00:00 UTC. This option prevents unsolicited notification packets and redirection packets from replaying. The receiver checks whether the timestamp of the recently received packet is the latest.
* Nonce: contains a random number selected by the sender of a solicitation message. The Nonce option prevents replay attacks during packet exchange. For example, during the exchange of NS packets and NA packets, if an NS packet carries the Nonce option, the NA packet, as a response, also carries the Nonce option, allowing the sender to determine whether it is a valid NA packet.

#### Attack Method Introduction

The following table describes the ND attacks that are described in relevant standards:

**Table 1** IPv6 ND attack modes
| Attack Mode | Description |
| --- | --- |
| NS/NA spoofing | An attacker sends an authorized node (host or router) an NS message with a bogus source link-layer address option, or an NA message with a bogus target link-layer address option. Then packets from the authorized node are sent to this link-layer address. |
| Neighbor unreachability detection (NUD) failure | An attacker repeatedly sends forged NA messages in response to an authorized node's NUD NS messages so that the authorized node cannot detect the neighbor unreachability. The consequences of this attack depend on why the neighbor became unreachable and how the authorized node would behave if it knew that the neighbor has become unreachable. |
| Duplicate Address Detection (DAD) attacks | An attacker responds to every DAD attempt made by a host that accesses the network, claiming that the address is already in use. Then the host will never obtain an address. |
| Spoofed Redirect message | An attacker uses the link-local address of the first-hop router to send a Redirect message to an authorized host. The authorized host accepts this message because the host mistakenly considers that the message came from the first-hop router. |
| Replay attacks | An attacker obtains valid messages and replays them. Even if Neighbor Discovery Protocol (NDP) messages are cryptographically protected so that their contents cannot be forged, they are still prone to replay attacks. |
| Bogus address prefix | An attacker sends a bogus RA message specifying that some prefixes are on-link. If a prefix is on-link, a host will not send any packets that contain this prefix to the router. Instead, the host will send NS messages to attempt address resolution, but the NS messages are not responded. As a result, the host is denied services. |
| Malicious last-hop router | An attacker multicasts bogus RA messages or unicasts bogus RA messages in response to multicast RS messages to a host attempting to discover a last-hop router. If the host selects the attacker as its default router, the attacker is able to insert himself as a man-in-the-middle and monitors all messages exchanged between the host and its destination. |



#### Configuration Guide

* Configure an IPv6 CGA address.
  
  Before implementing the IPv6 SEND function on an interface, configure an IPv6 CGA address for the interface so that ND packets sent from this interface carry CGA and RSA options and the peer interface checks the options to determine the authenticity of the sender and integrity of the packets.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**rsa key-pair label**](cmdqueryname=rsa+key-pair+label) *label-name* **modulus** *modulus-bits* command to create an RSA key pair.
  3. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of the interface for which an IPv6 CGA address is to be configured.
  4. Run the [**ipv6 security rsakey-pair**](cmdqueryname=ipv6+security+rsakey-pair) *key-label* command to bind an RSA key pair to the interface.
  5. Run the [**ipv6 security modifier**](cmdqueryname=ipv6+security+modifier) **sec-level** *sec-value* [ *modifier-value* ] command to configure the modifier value and security level.
     
     The modifier value can be set only when the security level is set to 0.
  6. Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } **cga** or [**ipv6 address**](cmdqueryname=ipv6+address) *ipv6-address* **link-local** **cga** [ **tag** *tag-value* ] command to configure an IPv6 CGA address.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the preceding configurations.
* Enable the IPv6 SEND function.
  
  Specify a rate limit for the system to compute or verify the RSA signature in a specified period (1s), the key length that is supported by an interface, and timestamp of ND packets. The received ND packets that do not match these configured parameters are considered invalid.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. (Optional) Run the [**ipv6 nd security rate-limit**](cmdqueryname=ipv6+nd+security+rate-limit) *ratelimit-value* command to set limit for the system to compute or verify the RSA signature in a specified period (1s).
  3. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view.
  4. (Optional) Run the [**ipv6 nd security key-length**](cmdqueryname=ipv6+nd+security+key-length) { **minimum** *keylen-value* | **maximum** *keylen-value* } \* command to configure the key length that is supported by the interface.
  5. (Optional) Run the [**ipv6 nd security timestamp**](cmdqueryname=ipv6+nd+security+timestamp) { **fuzz-factor** *fuzz-value* | **delta** *delta-value* | **drift** *drift-value* } \* command to configure the timestamp of ND packets.
  6. Run the [**ipv6 nd security strict**](cmdqueryname=ipv6+nd+security+strict) command to enable the strict security mode.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the preceding configurations.
* Verify the configuration.
  
  Run the [**display ipv6 security interface**](cmdqueryname=display+ipv6+security+interface) *interface-type* *interface-number* command to check the ND security configurations on the interface.

#### Configuration Suggestion

Note that configuring IPv6 SEND will slow ND entry learning.