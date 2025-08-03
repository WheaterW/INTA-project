(Optional) Configuring Intra-AS MSDP Peers
==========================================

If multiple PIM-SM domains exist in an AS or multiple Rendezvous Points (RPs) serving different multicast groups exist in a PIM-SM domain, configure MSDP peer relationships between RPs (including static RPs and C-RPs).

#### Context

If a CE is configured as an RP, the MSDP peer should be configured on the CE and the PE that connects to the CE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** *interface-type* *interface-number*
   
   
   
   An MSDP peer connection is set up.
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * *interface-type* *interface-number*: specifies the local interface connected with the remote MSDP peer.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.