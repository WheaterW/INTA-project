Applying a Tunnel Policy to a VPN
=================================

After configuring a tunnel policy, you need to apply it to a VPN service. The mode in which a tunnel policy is applied to VPN services varies according to the VPN type.

#### Context

A device can select proper tunnels for VPN data transmission based on the configured tunnel policy only after the policy is applied to VPN services.

The mode in which a tunnel policy is applied to VPN services varies according to the VPN type. Select one of the following modes as needed:

* [Apply a tunnel policy to a BGP/MPLS IP VPN.](#EN-US_TASK_0172369022__step_dc_vrp_tnlm_cfg_003801)
* [Apply a tunnel policy to a BGP/MPLS IPv6 VPN.](#EN-US_TASK_0172369022__step_dc_vrp_tnlm_cfg_003802)
* [Apply a tunnel policy to SVC VPWS.](#EN-US_TASK_0172369022__step_dc_vrp_tnlm_cfg_003803)
* [Apply a tunnel policy to LDP VPWS.](#EN-US_TASK_0172369022__step_dc_vrp_tnlm_cfg_003804)
* [Apply a tunnel policy to LDP VPLS.](#EN-US_TASK_0172369022__step_dc_vrp_tnlm_cfg_003806)
* [Apply a tunnel policy to an EVPN.](#EN-US_TASK_0172369022__step_dc_vrp_tnlm_cfg_003807)

#### Procedure

* Apply a tunnel policy to a BGP/MPLS IP VPN. 
  
  
  
  For details about how to configure BGP/MPLS IP VPN, see [Configuring Basic BGP/MPLS IP VPN Functions](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  4. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
     
     
     
     A tunnel policy is applied to the VPN instance IPv4 address family.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a tunnel policy to a BGP/MPLS IPv6 VPN. 
  
  
  
  For details about how to configure a BGP/MPLS IPv6 VPN, see [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  4. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
     
     
     
     A tunnel policy is applied to the VPN instance IPv6 address family.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a tunnel policy to SVC VPWS.
  
  
  
  For details about how to configure SVC VPWS, see [Configuring SVC VPWS.](dc_vrp_vpws_cfg_6000.html)  Perform the following steps on the PEs with VCs configured:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The AC interface view is displayed.
  3. Run [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** ] ] \*
     
     
     
     A tunnel policy is applied to the VC of the SVC VPWS.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a tunnel policy to LDP VPWS.
  
  
  
  For details about how to configure LDP VPWS, see [Configuring LDP VPWS](dc_vrp_vpws_cfg_3004.html) . Perform the following steps on the PEs with VCs configured:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The AC interface view is displayed.
  3. Run [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *pw-template-name* } \* *vc-id* **tunnel-policy** *policy-name*
     
     
     
     A tunnel policy is applied to a specified VC of LDP VPWS.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a tunnel policy to LDP VPLS.
  
  
  
  For details about how to configure LDP VPLS, see [Configuring LDP VPLS](dc_vrp_vpls_cfg_5003.html). Perform the following steps on each endpoint PE of a PW:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **auto** | **static** ]
     
     
     
     A VSI is created.
  3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
     
     
     
     LDP is configured as a PW signaling protocol, and the VSI-LDP view is displayed.
  4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
     
     
     
     A VSI ID is set.
  5. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ]
     
     
     
     A VSI peer is configured, and a tunnel policy is applied to the VSI peer.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a tunnel policy to an EVPN.
  
  
  
  For details about how to configure EVPN, see [Configuring EVPN](dc_vrp_evpn_cfg_0000.html). Perform the following steps on PEs:
  
  + Apply a tunnel policy to Layer 2 services.
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* [ **vpws** ] or [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
       
       The EVPN instance view is displayed.
    3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
       
       A tunnel policy is applied to the EVPN instance.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Apply a tunnel policy to Layer 3 services.
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
       
       The VPN instance view is displayed.
    3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
       
       The VPN instance IPv4 address family view is displayed.
    4. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
       
       The EVPN routes that can be imported into the VPN instance IPv4 address family are associated with a tunnel policy.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  
  If an EVPN carries both Layer 2 and Layer 3 services, the preceding configurations for Layer 2 and Layer 3 services must be performed on each PE.