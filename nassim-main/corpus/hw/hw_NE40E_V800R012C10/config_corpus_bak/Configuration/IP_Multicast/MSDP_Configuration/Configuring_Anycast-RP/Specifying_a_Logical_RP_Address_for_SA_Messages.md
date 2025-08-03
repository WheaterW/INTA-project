Specifying a Logical RP Address for SA Messages
===============================================

An MSDP peer performs the Reverse Path Forwarding (RPF) check on received Source Active (SA) messages. If the remote Rendezvous Point (RP) address carried in the SA message is the same as the local RP address, the MSDP peer discards the SA message. Therefore, you need to specify a logical RP address for the SA messages on the Router on which Anycast-RP is to be configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**originating-rp**](cmdqueryname=originating-rp) *interface-type* *interface-number*
   
   
   
   A logical RP interface is configured. The logical RP interface cannot be the same as an actual RP interface. Configuring an MSDP peer interface as a logical interface is recommended.
   
   
   
   After the [**originating-rp**](cmdqueryname=originating-rp) command is run, SA messages sent by the Router will carry the logical RP address. The logical RP address then replaces the RP address in the IP header of the SA messages. As a result, the SA messages can pass the RPF check on the remote Router.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.