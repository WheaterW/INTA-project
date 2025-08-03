Assigning an IP Address to an IP-Trunk Interface
================================================

You can assign an IP address to an IP-Trunk interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface ip-trunk**](cmdqueryname=interface+ip-trunk) *trunk-id*
   
   
   
   The IP-Trunk interface view is displayed.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is assigned to the IP-Trunk
   interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.