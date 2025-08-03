Configuring Inter-AS Static RPF Peers
=====================================

To enable PIM-SM domains in different ASs to share multicast source information, configure a static Reverse Path Forwarding (RPF) peer relationship between Rendezvous Points (RPs) in different ASs.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If [inter-AS MSDP peers have been configured for BGP peers](dc_vrp_multicast_cfg_0047.html), skip this configuration.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**msdp**](cmdqueryname=msdp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The MSDP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** *interface-type* *interface-number*
   
   
   
   An MSDP peer connection is set up.
   
   
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * *interface-type* *interface-number*: specifies the local interface connected with the remote MSDP peer.
4. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* **description** *text*
   
   
   
   A description is added for the remote MSDP peer.
   
   This configuration helps you differentiate remote MSDP peers and manage the connections with the remote MSDP peers.
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * *text*: specifies the description text. The text is a string of a maximum of 80 characters.
5. Run [**static-rpf-peer**](cmdqueryname=static-rpf-peer) *peer-address* [ **rp-policy** *ip-prefix-name* ]
   
   
   
   The remote MSDP peer is specified as a static RPF peer.
   
   
   
   * *peer-address*: specifies the IP address of a remote MSDP peer.
   * **rp-policy** *ip-prefix-name*: specifies the policy of filtering the addresses of source's RPs in the Source Active (SA) messages.
     
     If several static RPF peers are configured for one Router, obey the following configuration rules:
     
     + Specify **rp-policy** for all static RPF peers.
       
       After receiving SA messages from active static RPF peers, the local Router filters the SA messages based on the **rp-policy** configured for each static RPF peer. The local Router accepts only the SA messages that pass the filtration rule.
     + Do not specify **rp-policy** for any static RPF peers.
       
       The Router accepts all SA messages received from active static RPF peers.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.