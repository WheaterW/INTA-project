Configuring the 16-Bit Compressed Dynamic SID Function for EVPN
===============================================================

Configuring_the_16-Bit_Compressed_Dynamic_SID_Function_for_EVPN

#### Usage Scenario

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before configuring this function, load the license for the 16-bit compressed SID function. Otherwise, the commands fail to be delivered.

Segment Routing Header (SRH) is a key extension for SRv6 implementation. In encapsulation mode, an SRv6 ingress encapsulates an outer IPv6 header and an SRH into a packet before forwarding the packet. This can increase header overhead. If there are a large number of SRv6 SIDs, the SRH length increases further. The 16-bit compressed SID function for EVPN further improves SRv6 payload efficiency and saves network bandwidth and costs.


#### Pre-configuration Tasks

Before configuring the 16-bit compressed dynamic SID function for EVPN, complete the following tasks:

* EVPN VPLS scenario: [Configuring EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html)
* EVPN VPWS scenario: [Configuring EVPN VPWS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpws_over_srv6-te_policy_copy.html)


#### Procedure

* Configure the 16-bit compressed dynamic SID function in an EVPN VPLS over SRv6 TE Policy scenario.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enter the SRv6 view.
  3. Run the [**compress-16**](cmdqueryname=compress-16) [ **next-mode** ] **enable** command to configure the 16-bit compression mode.
  4. Run the [**locator**](cmdqueryname=locator) *locator-name* **compress-16 ipv6-prefix** *ipv6-address* *mask-length* [ [ **compress-static** *compress-length* ] | [ **static** *static-length* ] | [ **args** *args-length* ] | [ **flex-algo** *flexAlgoId* ] ]\* command to configure the 16-bit compressed SRv6 locator function and enter the SRv6 locator view.
  5. Run the [**quit**](cmdqueryname=quit) command to return to the SRv6 view.
  6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  7. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to enter the BD EVPN instance view.
  8. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **compress** command to enable the device to add the compressed SID attribute to EVPN routes to be sent.
  9. (Optional) Run the [**segment-routing ipv6 apply-sid compress**](cmdqueryname=segment-routing+ipv6+apply-sid+compress) { **coc-next** | **next** } command to configure flavor adjustment for SIDs to be dynamically allocated to EVPN VPN routes.
  10. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the 16-bit compressed dynamic SID function in an EVPN VPWS over SRv6 TE Policy scenario.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enter the SRv6 view.
  3. Run the [**compress-16**](cmdqueryname=compress-16) [ **next-mode** ] **enable** command to configure the 16-bit compression mode.
  4. Run the [**locator**](cmdqueryname=locator) *locator-name* **compress-16 ipv6-prefix** *ipv6-address* *mask-length* [ [ **compress-static** *compress-length* ] | [ **static** *static-length* ] | [ **args** *args-length* ] | [ **flex-algo** *flexAlgoId* ] ]\* command to configure the 16-bit compressed SRv6 locator function and enter the SRv6 locator view.
  5. Run the [**quit**](cmdqueryname=quit) command to return to the SRv6 view.
  6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  7. Run the [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id* command to enter the EVPL instance view.
     
     
     
     A VPWS EVPN instance must be bound to an EVPL instance in the EVPL view.
  8. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* **compress** command to enable the device to add the compressed SID attribute to EVPN routes to be sent.
  9. (Optional) Run the [**segment-routing ipv6 apply-sid compress**](cmdqueryname=segment-routing+ipv6+apply-sid+compress) { **coc-next** | **next** } command to configure flavor adjustment for SIDs to be dynamically allocated to EVPN VPN routes.
  10. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **vpn-instance** *vpn-instance-name* **routing-table** [ { **ad-route** | **inclusive-route** | **mac-route** } *prefix* ] command to check the Endpoint Behavior field in BGP EVPN routes.