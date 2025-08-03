BFD
===

This section describes the security policies, attack methods, and configuration and maintenance methods and suggestions for BFD.

#### Security Policy

* BFD helps improve system security through configurable negotiation packet authentication. You can configure negotiation packet authentication for a static multicast BFD session, single-hop BFD session for IP, multi-hop BFD session for IP, BFD for LSP proactive session, or BFD for LSP passive session.
* The same authentication mode, **key-id** field, authentication password, and authentication timeout period must be configured on a sender and receiver.
  
  + *key-id* is an integer ranging from 1 to 255.
  + The authentication password is a string of 1 to 20 characters in cleartext or a string of 20 to 148 characters in ciphertext.
  + The authentication timeout period ranges from 1 to 10000, in seconds.
* After negotiation packet authentication is configured, the A flag in the BFD packet header is set to 1, and the 28-byte authentication field is added to the payload.
* A receiver decapsulates a packet. If the A flag in the packet header is different from the local one, the receiver discards the packet. If they are the same, the receiver checks whether the authentication field is the same as the local configuration. If they are different, the authentication field is considered incorrect.
* An authentication password can be configured in cleartext or ciphertext mode. In both modes, the password is displayed in ciphertext in the configuration file.

#### Attack Methods

An attacker forges BFD packets and sends them to a target.


#### Configuration and Maintenance Methods

* Configure authentication in the BFD session view. Only static multicast BFD sessions and multicast auto sessions are supported.
  
  To configure BFD session authentication, run the [**authentication-mode**](cmdqueryname=authentication-mode) **met-sha1** **key-id** *key-id-value* **cipher** *cipher-text* **nego-packet** [ **enhanced** ] [ **timeout-interval**  < *interval-value* >] command.
  
  In a specific access scenario, for example, when a multicast BFD session is associated with the protocol status of an interface, configure authentication for the BFD session on the interface. BFD negotiation can succeed, the BFD-associated protocol status of the interface can be activated, and users can access the device through this interface only when the BFD authentication information on both ends is consistent.
* In the BFD view, you can configure negotiation packet authentication for a single-hop BFD for IP session, BFD for LSP proactive session, BFD for LSP passive session, or multi-hop BFD for IP session.
  + To configure negotiation packet authentication for a single-hop BFD session for IPv4, run the **[**bfd**](cmdqueryname=bfd) **single-hop peer-ip**** *ip-address* [ ****vpn-instance**** **vpn-name** ] **[**authentication-mode**](cmdqueryname=authentication-mode)** ****met-sha1********key-id**** **key-id-value******cipher**** **cipher-text** ****nego-packet**** command.
  + To configure negotiation packet authentication for a single-hop BFD session for IPv6, run the **[**bfd**](cmdqueryname=bfd) **single-hop peer-ipv6**** *ipv6-address* [ ****vpn-instance*****vpn-name*] **[**authentication-mode**](cmdqueryname=authentication-mode)******met-sha1********key-id**** **key-id-value******cipher******cipher-text** ****nego-packet**** command.
  + To configure negotiation packet authentication for a multi-hop BFD session for IPv4, run the **[**bfd**](cmdqueryname=bfd) **multi-hop peer-ip**** **ip-address** [ **[**vpn-instance**](cmdqueryname=vpn-instance)** **vpn-name** ] **[**authentication-mode**](cmdqueryname=authentication-mode)** ****met-sha1********key-id**** **key-id-value** ****cipher**** **cipher-text** ****nego-packet**** command.
  + To configure negotiation packet authentication for a multi-hop BFD session for IPv6, run the **[**bfd**](cmdqueryname=bfd) **multi-hop peer-ipv6**** *i*pv6-address** [ ****vpn-instance**** **vpn-name** ] **[**authentication-mode**](cmdqueryname=authentication-mode)** ****met-sha1********key-id**** **key-id-value** ****cipher**** **cipher-text** ****nego-packet**** command.
  + To configure negotiation packet authentication for a BFD for LSP passive session, run the **[**bfd**](cmdqueryname=bfd) **mpls-passive peer-ip**** *i*p-address** **[**authentication-mode**](cmdqueryname=authentication-mode)** ****met-sha1********key-id**** **key-id-value** ****cipher**** **cipher-text** **[**nego-packet**](cmdqueryname=nego-packet)** command.
  + To configure negotiation packet authentication for a BFD for LSP proactive session, run the **[**bfd**](cmdqueryname=bfd) **lsp-tunnel peer-ip**** **ip-address** **[**authentication-mode**](cmdqueryname=authentication-mode)** ****met-sha1********key-id**** **key-id-value** ****cipher**** **cipher-text** ****nego-packet**** command.

#### Configuration and Maintenance Suggestions

Enable BFD negotiation packet authentication on a network requiring high security.


#### Verifying the Security Hardening Result

Run the [**display current-configuration configuration bfd**](cmdqueryname=display+current-configuration+configuration+bfd) command to check the BFD configuration.