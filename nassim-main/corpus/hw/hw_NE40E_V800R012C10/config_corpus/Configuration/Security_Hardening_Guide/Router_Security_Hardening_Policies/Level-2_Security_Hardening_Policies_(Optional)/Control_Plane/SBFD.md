SBFD
====

This section describes the security policies, attack methods, and configuration and maintenance methods and suggestions for SBFD.

#### Security Policy

* SBFD helps improve system security through configurable negotiation packet authentication. You can configure negotiation packet authentication for an SBFD session in SBFD for IP, SBFD for LSP/tunnel, SBFD for SR-MPLS TE Policy, and SBFD for SRv6 TE Policy scenarios.
* The authentication mode, **key-id** field, and authentication password need to be configured only on the SBFD initiator.
  
  + *key-id* is an integer ranging from 1 to 255.
  + The authentication password is a string of 1 to 20 characters in cleartext or a string of 20 to 148 characters in ciphertext.
* After negotiation packet authentication is configured, the A flag in the SBFD packet header is set to 1, and the 28-byte authentication field is added to the payload.
* An SBFD initiator decapsulates a packet. If the A flag in the packet header is different from the local one, the initiator discards the packet. If they are the same, the initiator checks whether the authentication field is the same as the local configuration. If they are different, the authentication field is considered incorrect.
* The SBFD reflector cannot authenticate packets.
* An authentication password can be configured in cleartext or ciphertext mode. In both modes, the password is displayed in ciphertext in the configuration file.

#### Attack Methods

An attacker forges SBFD packets and sends them to a target.


#### Configuration and Maintenance Methods

In the SBFD view, configure SBFD negotiation packet authentication based on the service scenario.

* To configure negotiation packet authentication for a multi-hop SBFD session for IPv6, run the [**sbfd**](cmdqueryname=sbfd) **multi-hop** **peer-ipv6** *ipv6-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command.
* To configure negotiation packet authentication for an SBFD for LSP/tunnel session, run the [**sbfd**](cmdqueryname=sbfd) **lsp-tunnel** **peer-ip** *ip-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command.
* To configure negotiation packet authentication for an SBFD for SR-MPLS TE Policy segment list session, run the [**sbfd**](cmdqueryname=sbfd) **sr-te-policy segment-list endpoint** *endpoint-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command.
* To configure negotiation packet authentication for an SBFD for SRv6 TE Policy segment list session, run the [**sbfd**](cmdqueryname=sbfd) **srv6-te-policy segment-list endpoint** *endpoint-address* **authentication-mode** **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** command.

#### Configuration and Maintenance Suggestions

Enable SBFD negotiation packet authentication on a network requiring high security.


#### Verifying the Security Hardening Result

Run the [**display current-configuration configuration bfd**](cmdqueryname=display+current-configuration+configuration+bfd) command to check the SBFD configuration.