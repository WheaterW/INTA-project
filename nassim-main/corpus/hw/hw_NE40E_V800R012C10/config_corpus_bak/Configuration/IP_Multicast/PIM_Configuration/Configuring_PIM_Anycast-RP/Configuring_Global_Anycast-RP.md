Configuring Global Anycast-RP
=============================

If Anycast-RP is configured on some devices in a PIM-SM domain, configure the address of the Rendezvous Point (RP) elected in the PIM-SM domain as the Anycast-RP address.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Either static or dynamic RPs can be used. Configuring RPs on loopback interfaces is recommended. On the Routers that require Anycast-RP, configure the same RP address.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
3. Run [**anycast-rp**](cmdqueryname=anycast-rp) *rp-address*
   
   
   
   An Anycast-RP is configured, and the Anycast-RP view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The Anycast-RP address must be the same as that of the elected RP.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.