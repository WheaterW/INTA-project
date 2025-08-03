Creating a VSI and Configuring LDP Signaling
============================================

Configuring VSI IDs and peer IP addresses is mandatory for LDP VPLS services. VSI IDs are used to identify VSIs in PW signaling negotiation. Perform the following steps on the endpoint PEs of a PW.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ]
   
   
   
   A VSI is created, and its view is displayed.
   
   
   
   VSIs on the same device cannot use the same name.
3. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the VSI.
4. (Optional) Run [**encapsulation**](cmdqueryname=encapsulation) { **ethernet** | **vlan** }
   
   
   
   An encapsulation mode is set for the VSI.
   
   
   
   * VSIs have two encapsulation modes: Ethernet and VLAN. On the public network, packets encapsulated in Ethernet mode do not carry any VLAN tags, but packets encapsulated in VLAN mode do.
   * The two ends of a PW must use the same VSI encapsulation mode.
5. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
   
   
   
   A public network tunnel policy is applied to the VSI.
   
   
   
   If you do not want to use the **tnl-policy** *policy-name* command to specify a tunnel policy during VSI peer configuration in Step 12, run this command to apply a public network tunnel policy to the VSI.
   
   A tunnel policy specified during VSI peer configuration takes precedence over one specified in the VSI view. If tunnel policies are specified using both methods, only the tunnel policy specified during VSI peer configuration takes effect.
6. (Optional) Run [**mtu**](cmdqueryname=mtu) *mtu*
   
   
   
   The MTU of the VSI is configured for VPLS negotiation.
   
   
   
   If the MTUs of the same VSI on two PEs are different, the two PEs may fail to establish a connection.
7. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   LDP is configured as the signaling protocol for the VSI, and the VSI-LDP view is displayed.
8. (Optional) Run [**control-word enable**](cmdqueryname=control-word+enable)
   
   
   
   The control word function is enabled for the VSI.
9. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   
   
   A VSI ID is configured.
   
   
   
   * The VSI IDs at the two ends of a PW must be the same, or the VSI cannot be created. If the VSI IDs at the two ends of a PW are different, specify **negotiation-vc-id** *vc-id* for PW negotiation when running the [**peer**](cmdqueryname=peer) command.
   * VSIs can exist only on PEs. A PE can be configured with multiple VSIs, but the ID of each VSI must be unique on the PE.
10. (Optional) Run [**admin-vsi**](cmdqueryname=admin-vsi)
    
    
    
    The current VSI is configured as the mVSI.
11. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] [ [ **endpoint** *endpoint4-address* ] **color** *color-value* ] [ **secondary** ] [ **ignore-standby-state** ]
    
    
    
    A VSI peer is configured.
    
    
    
    * *peer-address* specifies the peer IP address, which is usually the peer LSR ID.
    * Generally, the VSI IDs on both ends of a VSI must be the same. If they are different, configure **negotiation-vc-id** *vc-id* to re-specify the VC ID used for PW negotiation.
    * If a tunnel policy is configured, you can use **tnl-policy** *policy-name* to reference the tunnel policy when configuring a peer.
    * On the network where PW redundancy is configured, if the primary PW fails, traffic is switched to the secondary PW. If the secondary PW is in the standby state, service traffic cannot be forwarded, resulting in packet loss. However, if the **ignore-standby-state** parameter is configured on the two PEs to which a CE is dual-homed, the secondary PW ignores the standby state sent from the remote end and stays in the forwarding state, preventing packet loss caused by the primary/secondary PW switchover.
12. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name*
    
    
    
    A VSI peer is configured.
13. (Optional) Run [**control-word enable**](cmdqueryname=control-word+enable)
    
    
    
    The control word function is enabled for the PW.
14. (Optional) Run [**undo interface-parameter-type vccv**](cmdqueryname=undo+interface-parameter-type+vccv)
    
    
    
    The VCCV byte (interface parameter) is deleted from the Label Mapping message.
    
    
    
    If LDP VPLS is configured for devices running V800R005 or later to communicate with devices running VRP V300R001 or branch versions, configure this command.
15. (Optional) Run [**ignore-stp-loopcheck**](cmdqueryname=ignore-stp-loopcheck)
    
    
    
    STP loop detection is disabled for the PW.
16. (Optional) Run [**status-code-change flush-mac disable**](cmdqueryname=status-code-change+flush-mac+disable)
    
    
    
    The device is configured not to clear local MAC addresses when it receives a remote status code of 20.
17. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Follow-up Procedure

If the specified VSI is an mVSI, you must run the [**track admin-vsi**](cmdqueryname=track+admin-vsi) *vsi-name* command in the service VSI view to bind the service VSI to the mVSI.