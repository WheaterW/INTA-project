(Optional) Changing the MAC Address Update Speed on an HVPLS Network
====================================================================

(Optional)_Changing_the_MAC_Address_Update_Speed_on_an_HVPLS_Network

#### Context

By default, a network provider edge (NPE) does not forward the LDP MAC Withdraw messages received from other NPEs to UPEs, received from UPEs to other NPEs, or received from a UPE to other UPEs.

To speed up network convergence, enable NPEs to send LDP MAC Withdraw messages to accelerate MAC address updates on a VPLS network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   The VSI view is displayed.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   LDP is configured as the PW signaling protocol, and the VSI-LDP view is displayed.
4. Run any of the following commands:
   * To enable an NPE to forward LDP MAC Withdraw messages received from other NPEs to UPEs, run the [**npe-upe mac-withdraw enable**](cmdqueryname=npe-upe+mac-withdraw+enable) command.
     
     An NPE is a network-end peer of the local VSI in hierarchical virtual private LAN service (HVPLS). A UPE is a user-end peer of the local VSI in HVPLS.
     
     In good network conditions, running this command speeds up network convergence. In bad network conditions, running this command generates a large number of exchange messages, and therefore is not recommended.
   * To enable an NPE to forward LDP MAC Withdraw messages received from UPEs to other NPEs, run the [**upe-npe mac-withdraw enable**](cmdqueryname=upe-npe+mac-withdraw+enable) command.
   * To enable an NPE to forward LDP MAC Withdraw messages received from a UPE to other UPEs, run the [**upe-upe mac-withdraw enable**](cmdqueryname=upe-upe+mac-withdraw+enable) command.
5. (Optional) Enable MAC Withdraw loop detection.
   1. Run the [**quit**](cmdqueryname=quit) command to return to the VSI view.
   2. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   3. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to enter the L2VPN view.
   4. Run the [**vpls mac-withdraw loop-detect enable**](cmdqueryname=vpls+mac-withdraw+loop-detect+enable) command to enable MAC Withdraw loop detection.
      
      
      
      After you configure MAC Withdraw loop detection on a PE, the PE adds the Path TLV field to a MAC Withdraw message before forwarding the message. If you do not configure MAC Withdraw loop detection on a PE but the PE receives a MAC Withdraw message, the PE directly forwards the message.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.