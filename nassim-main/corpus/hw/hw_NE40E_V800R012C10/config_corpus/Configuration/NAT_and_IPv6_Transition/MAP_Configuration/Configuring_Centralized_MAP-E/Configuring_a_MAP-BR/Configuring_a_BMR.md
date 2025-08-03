Configuring a BMR
=================

This section describes how to configure a basic mapping rule (BMR). A BMR is used to convert user-side IPv6 addresses into IPv4 addresses and network-side IPv4 addresses into IPv6 addresses.

#### Context

BMR parameters are set in an instance. The parameters include the IPv4 prefix and length, IPv6 prefix and length, embedded address length, and PSID offset. The PSID offset is used to reserve ports based on public IP addresses.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map rule**](cmdqueryname=map+rule) *rule-name*
   
   
   
   The MAP rule view is displayed.
3. Run [**rule-prefix**](cmdqueryname=rule-prefix) *ipv6âprefix* **prefix-length** *v6prefix-length* **ipv4âprefix** *ipv4âprefix* **prefix-length** *v4prefix-length* [ **vpn-instance** *vpn-instance-name* ] **ea-length** *ea-length* [ **psid-offset** *offset-length* ]
   
   
   
   Parameters are configured to verify and encapsulate MAP packets.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) A unique IPv6 address must be set in each BMR. The IPv6 addresses of BMRs cannot be identical.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.