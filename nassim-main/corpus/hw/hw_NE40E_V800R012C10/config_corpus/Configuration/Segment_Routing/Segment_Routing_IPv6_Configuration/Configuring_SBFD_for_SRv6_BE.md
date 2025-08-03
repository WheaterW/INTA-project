Configuring SBFD for SRv6 BE
============================

This section describes how to configure SBFD for SRv6 BE to detect SRv6 BE faults.

#### Prerequisites

Before configuring SBFD for SRv6 BE, complete the following tasks:

* Configure SRv6 BE. For details, see [Configuring SRv6 BE (IS-IS)](dc_vrp_srv6_cfg_all_0002.html).
* Run the [**te ipv6-router-id**](cmdqueryname=te+ipv6-router-id)*ipv6Addr* command to configure a global TE IPv6 router ID.

#### Context

SBFD for SRv6 BE triggers a rapid FRR switchover if the primary path fails, thereby minimizing the impact on services.

SBFD for SRv6 BE typically applies to SBFD for BGP public network IPv4/IPv6 over SRv6 BE, L3VPNv4/L3VPNv6 over SRv6 BE, EVPN L3VPNv4/EVPN L3VPNv6 over SRv6 BE, and EVPN L2VPN over SRv6 BE scenarios.

**Figure 1** SBFD for SRv6 BE networking  
![](figure/en-us_image_0000001216301459.png "Click to enlarge")

Assume that data is forwarded from CE1 to CE2. In this example, SBFD for SRv6 BE is implemented as follows:


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
     
     
     
     SBFD is enabled globally, and the SBFD view is displayed.
  5. Run [**reflector discriminator**](cmdqueryname=reflector+discriminator) { *unsigned-integer-value* | *ip-address-value* }
     
     
     
     A discriminator is configured for the SBFD reflector.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     BGP is enabled, the local AS number is specified, and the BGP view is displayed.
  8. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
     
     
     
     The BGP-IPv4 unicast address family view is displayed.
     
     
     
     This example uses the SBFD for public network IPv4 over SRv6 BE scenario, in which the BGP-IPv4 unicast address family view needs to be used. Determine which BGP address family view to use according to your scenario.
  9. Run [**segment-routing ipv6 advertise sbfd-discriminator**](cmdqueryname=segment-routing+ipv6+advertise+sbfd-discriminator)
     
     
     
     The device is enabled to advertise the SBFD discriminator to an IPv6 peer.
     
     
     
     In an [EVPN L3VPN over SRv6 BE](dc_vrp_srv6_cfg_all_0252.html) scenario, you need to run the **segment-routing ipv6 advertise sbfd-discriminator evpn** command in the BGP-VPN instance view.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Public network IP over SRv6 BE scenario
       
       After the [**segment-routing ipv6 locator end-dt46**](cmdqueryname=segment-routing+ipv6+locator+end-dt46) command is run in the BGP view, public network IPv4 and IPv6 unicast routes carry the same SID. You can run the **segment-routing ipv6 advertise sbfd-discriminator end-dt46** command in the BGP view to enable the device to advertise the SBFD discriminator to a public network BGP peer through a BGP route.
     + L3VPN over SRv6 BE scenario
       
       After the [**segment-routing ipv6 locator end-dt46**](cmdqueryname=segment-routing+ipv6+locator+end-dt46) command is run in the BGP-VPN instance view, VPN IPv4 and IPv6 unicast routes carry the same SID. You can run the [**segment-routing ipv6 advertise sbfd-discriminator end-dt46**](cmdqueryname=segment-routing+ipv6+advertise+sbfd-discriminator+end-dt46) command in the BGP-VPN instance view to enable the device to advertise the SBFD discriminator to a BGP VPN peer through a BGP route.
  10. Run [**peer**](cmdqueryname=peer) *ipv6-address* **prefix-sid** **advertise-srv6-locator**
      
      
      
      The device is enabled to exchange prefix SIDs with the specified peer.
      
      
      
      In the BGP-VPNv4 address family view, run the [**peer**](cmdqueryname=peer+prefix-sid+%28BGP-IPv4+unicast+address+family+view%29+%28IPv6%29) *ipv6-address* **prefix-sid** **sid-type5** **advertise-srv6-locator** command to enable the device to carry SRv6 SIDs through the SRv6 Services TLV (TLV Type 5).
      
      In a scenario where BFD is used to check locator reachability and the P nodes between local and remote PEs summarize locator routes, specify the **advertise-srv6-locator** parameter to enable PE-advertised BGP routes to carry locator length information. In this way, when the peer IPv6 address bound to the BFD session matches the locator's IPv6 address, locator reachability can be checked using BFD to complete auto FRR path switching.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
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
     
     
     
     SRv6 is enabled, and the SRv6 view is displayed.
  8. Run **locator-bfd seamless enable** [ **filter-policy** **ipv6-prefix** *ipv6-prefix-name* ]
     
     
     
     SBFD for SRv6 BE is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     SBFD must be enabled globally before you run this command. Otherwise, SBFD for SRv6 BE cannot take effect.
  9. (Optional) Run **locator-bfd** { **min-tx-interval** *transmit-interval* | **min-rx-interval** *receive-interval* | **detect-multiplier** *multiplier-value* }\*
     
     
     
     SRv6 locator-specific SBFD parameters are configured.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring SBFD for SRv6 BE, verify the configuration, such as the BFD session status.

* Run the [**display bfd session all**](cmdqueryname=display+bfd+session+all) command to check the configurations of all BFD sessions.
* Run the **[**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table)** *ipv6-address*[ *mask* | *mask-length* ] **bfd-discriminator** command to check SBFD discriminator information.