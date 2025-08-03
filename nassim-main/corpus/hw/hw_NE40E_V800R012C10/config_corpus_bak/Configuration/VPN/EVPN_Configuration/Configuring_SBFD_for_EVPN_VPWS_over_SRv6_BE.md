Configuring SBFD for EVPN VPWS over SRv6 BE
===========================================

This section describes how to configure SBFD for EVPN VPWS over SRv6 BE to detect EVPN VPWS over SRv6 BE faults.

#### Prerequisites

Before configuring SBFD for SRv6 BE, complete the following tasks:

* Configure EVPN VPWS over IS-IS SRv6 BE or EVPN VPWS over OSPFv3 SRv6 BE. For details, see [Configuring EVPN VPWS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0021_copy.html) or [Configuring EVPN VPWS over OSPFv3 SRv6 BE](dc_vrp_srv6_cfg_all_1004.html).
* Run the [**te ipv6-router-id**](cmdqueryname=te+ipv6-router-id)*ipv6Addr* command to configure a global TE IPv6 router ID.

#### Context

SBFD for EVPN VPWS over SRv6 BE can trigger a rapid traffic switchover when the primary path fails, minimizing the impact on services.


#### Procedure

* Configure an SBFD reflector.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
     
     
     
     BFD-related configuration can be performed only after BFD is enabled globally using the [**bfd**](cmdqueryname=bfd) command.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**sbfd**](cmdqueryname=sbfd)
     
     
     
     SBFD is enabled globally, and its view is displayed.
  5. Run [**reflector discriminator**](cmdqueryname=reflector+discriminator) { *unsigned-integer-value* | *ip-address-value* } 
     
     
     
     A discriminator is configured for the SBFD reflector.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
     
     
     
     The view of the VPWS EVPN instance is displayed.
  8. Run [**segment-routing ipv6 advertise sbfd-discriminator**](cmdqueryname=segment-routing+ipv6+advertise+sbfd-discriminator)
     
     
     
     The function to advertise the SBFD discriminator attribute to the EVPN IPv6 peer is enabled.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an SBFD initiator.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
     
     
     
     BFD-related configuration can be performed only after BFD is enabled globally using the [**bfd**](cmdqueryname=bfd) command.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**sbfd**](cmdqueryname=sbfd)
     
     
     
     SBFD is enabled globally.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  7. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
     
     
     
     SRv6 is enabled, and its view is displayed.
  8. Run **locator-bfd seamless enable**
     
     
     
     SBFD for SRv6 BE is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     SBFD must be enabled globally prior to this step. Otherwise, SBFD for SRv6 BE cannot take effect.
  9. (Optional) Run **locator-bfd** { **min-tx-interval** *tx-value* | **min-rx-interval** *rx-value* | **detect-multiplier** *detectmulti-value* }\*
     
     
     
     SBFD parameters are configured for the SRv6 locator.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring SBFD for EVPN VPWS over SRv6 BE, verify the configuration, such as the BFD session status.

* Run the [**display bfd session all**](cmdqueryname=display+bfd+session+all) command to check the configurations of all BFD sessions.
* Run the **display bgp evpn all routing-table** { **ad-route** | **inclusive-route** | **mac-route** } *prefix* **bfd-discriminator** command to check SBFD discriminator information.