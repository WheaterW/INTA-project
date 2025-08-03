Configuring the Hard Pipe Function for a VPLS PW
================================================

Configuring the hard pipe function for an LDP VPLS PW allows P2MP services to be carried over the hard-pipe static PW, enhancing private line services for high-value customers.

#### Context

VPLS enables carriers to provide L2VPN services over different media through the same IP hard pipe network. By providing P2MP services over the hard pipe, this implementation enhances private line services for high-value customers.


#### Procedure

1. Configure MPLS L2VPN.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to configure MPLS L2VPN.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
2. Create a tunnel policy.
   1. Run the [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name* command to create a tunnel policy and enter its view.
   2. Run the [**tunnel binding**](cmdqueryname=tunnel+binding) **destination** *dest-ip-address* **te** { *tunnel-name* | *tunnel-type**tunnel-number* } & <1-32> [ **ignore-destination-check** ] [ **down-switch** | **include-ldp** ] command to specify the TE tunnel for binding in the tunnel policy.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Configure the hard pipe function for VPLS.
   
   
   
   In VPLS, the hard pipe function can be configured only for static LDP VPLS PWs.
   
   
   
   1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to create a VSI and enter its view.
   2. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to configure LDP as the VSI signaling protocol and enter the VSI-LDP view.
   3. Run the [**hard-pipe enable**](cmdqueryname=hard-pipe+enable) command to enable the hard pipe function in the VSI-LDP view.
   4. Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *pwIdValue* ] [ **encapsulation** { **ethernet** | **vlan** } ] [ **tnl-policy** *policy-name* ] { **static-npe** | **static-upe** } **trans** *transmit-label* **recv** *receive-label* [ **hard-pipe** **bandwidth** *bandwidth* [ **burst-time** *burst-time* ] ] command to configure a hard-pipe static PW.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.