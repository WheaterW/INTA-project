Configuring a CGA IPv6 Address
==============================

Configuring a CGA IPv6 Address

#### Context

To enable IPv6 SEND to protect ND messages that carry CGA and RSA options, configure a CGA IPv6 address on an interface that sends ND messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an RSA key pair.
   
   
   ```
   [rsa key-pair label](cmdqueryname=rsa+key-pair+label) label-name modulus modulus-bits
   ```
3. Enter the view of the interface on which a CGA IPv6 address needs to be configured.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
5. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
6. Bind the RSA key pair to the interface.
   
   
   ```
   [ipv6 security rsakey-pair](cmdqueryname=ipv6+security+rsakey-pair) key-label
   ```
7. Configure a modifier value and security level for a CGA address.
   
   
   ```
   [ipv6 security modifier](cmdqueryname=ipv6+security+modifier) sec-level sec-value [ modifier-value ]
   ```
   
   You can manually configure a modifier value only when the security level of a CGA address is 0.
8. Configure a CGA IPv6 address.
   
   
   
   **Table 1** Configuring a CGA IPv6 address
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a CGA IPv6 global unicast address. | [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } **cga** [ **tag** *tag-value* ] | After the command is run, a CGA IPv6 global unicast address is generated. |
   | Configure a CGA IPv6 link-local address. | [**ipv6 address**](cmdqueryname=ipv6+address) *ipv6-address* **link-local** **cga** [ **tag** *tag-value* ] | Link-local addresses are used for the communication between nodes on the same local link in ND or stateless address autoconfiguration. The packets with link-local addresses being the source or destination addresses are not forwarded to other links, that is, link-local addresses are valid only on local links. |
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```