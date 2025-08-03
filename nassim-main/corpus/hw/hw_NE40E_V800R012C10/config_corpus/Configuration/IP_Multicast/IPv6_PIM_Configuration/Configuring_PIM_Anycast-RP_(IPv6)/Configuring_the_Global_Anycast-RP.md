Configuring the Global Anycast-RP
=================================

On several devices to be deployed with the Anycast-Rendezvous Point (RP) in a PIM-SM domain, configure the address of the RP elected in the PIM-SM domain as the Anycast-RP address.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Either static or dynamic RPs can be used on the network. Configuring RPs on loopback interfaces is recommended. Configure the same RP address on the Routers to be deployed with the Anycast-RP.

Perform the following steps on the Routers in a PIM-SM domain to be deployed with the Anycast-RP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The PIM-IPv6 view is displayed.
3. Run [**anycast-rp**](cmdqueryname=anycast-rp) *rp-address*
   
   
   
   The Anycast-RP is configured and the IPv6 Anycast-RP view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the Anycast-RP, several RPs need to use the same IP address. Configure the Anycast-RP address on loopback interfaces. The Anycast-RP address must be the same as that of RPs on the network.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.