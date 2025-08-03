(Optional) Allocating IP Addresses Based on Option 60
=====================================================

When there is no relay device between a DHCP client and a DHCP server, the DHCP server allocates different network segments and VPN addresses based on Option 60 carried in user packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp server base-option60 enable**](cmdqueryname=dhcp+server+base-option60+enable)
   
   
   
   # A network-side DHCP server is enabled to allocate IP addresses based on Option 60.
3. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* **server**
   
   
   
   An address pool is created, and the address pool view is displayed.
4. Run [**client-option60**](cmdqueryname=client-option60) *option60-text*
   
   
   
   Option 60 carried in user packets of a specified address pool are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After the command is run, IP addresses can be allocated by the address pool only when the specified *option60âvalue* matches Option 60 carried in user packets.
   * The command can only be configured in the address pool on the DHCP server.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.