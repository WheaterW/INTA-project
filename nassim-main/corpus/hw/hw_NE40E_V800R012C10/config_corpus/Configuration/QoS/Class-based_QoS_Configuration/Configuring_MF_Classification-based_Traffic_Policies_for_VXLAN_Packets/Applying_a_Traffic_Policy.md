Applying a Traffic Policy
=========================

A class-based traffic policy takes effect only after being applied to a BD/VPN.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform the following operations based on the type of the instance to which a traffic policy applies.
   
   
   * To apply a traffic policy to a BD, perform the following operations:
     1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
     2. Run the **traffic-policy** *policy-name* { **inbound** [ **link-layer** ] | **outbound** } **vxlan-mode** command to apply a traffic policy to the BD.
   * To apply a traffic policy to a VPN, perform the following operations:
     1. Run the [**ip**](cmdqueryname=ip) [ **dcn** ] **vpn-instance** *vpn-instance-name* command to enter the VPN view.
     2. Run the **traffic-policy** *policy-name* { **inbound** [ **link-layer** ] | **outbound** } **vxlan-mode** command to apply a traffic policy to the VPN.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.