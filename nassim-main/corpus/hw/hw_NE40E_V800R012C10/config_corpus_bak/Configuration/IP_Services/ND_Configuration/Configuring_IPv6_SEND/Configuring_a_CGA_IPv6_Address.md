Configuring a CGA IPv6 Address
==============================

To enable IPv6 SEND to protect ND messages that carry CGA and RSA options, configure a CGA IPv6 address on an interface that sends ND messages.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rsa key-pair label**](cmdqueryname=rsa+key-pair+label) *label-name* **modulus** *modulus-bits*
   
   
   
   An RSA key pair is created.
3. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the interface where a CGA IPv6 address needs to be configured is displayed.
4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled.
5. Run [**ipv6 security rsakey-pair**](cmdqueryname=ipv6+security+rsakey-pair) *key-label*
   
   
   
   The RSA key pair is bound to the interface to generate a CGA address.
6. Run [**ipv6 security modifier**](cmdqueryname=ipv6+security+modifier) **sec-level** *sec-value* [ *modifier-value* ]
   
   
   
   A modifier value and security level are configured for the CGA address.
   
   
   
   You can manually configure a modifier value only when the security level of a CGA address is 0.
7. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **cga** [ **tag** *tag-value* ] or [**ipv6 address**](cmdqueryname=ipv6+address) *ipv6-address* **link-local** **cga** [ **tag** *tag-value* ]
   
   
   
   A CGA IPv6 address is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.