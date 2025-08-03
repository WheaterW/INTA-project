Configuring a BMR
=================

This section describes how to configure a basic mapping rule (BMR). Configure BMR rules on the BRAS to instruct the BRAS to assign IPv6 and IPv4 addresses to MAP-CEs.

#### Context

BMR parameters are configured using multiple commands in an instance. In addition to the IPv4 prefix and length of a MAP domain, the IPv6 prefix and length, and EA length, PSID offset can also be configured. The PSID offset can be used to reserve ports for public IP addresses.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map rule**](cmdqueryname=map+rule) *rule-name*
   
   
   
   The MAP rule view is displayed.
3. Run [**rule-prefix**](cmdqueryname=rule-prefix) *ipv6âprefix* **prefix-length** *v6prefix-length* **ipv4âprefix** *ipv4âprefix* **prefix-length** *v4prefix-length* [ **vpn-instance** *vpn-instance-name* ] **ea-length** *ea-length* [ **psid-offset** *offset-length* ]
   
   
   
   The device is enabled to verify and encapsulate MAP packets.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) A unique IPv6 address must be set in each BMR. The IPv6 addresses of BMRs cannot be identical.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.