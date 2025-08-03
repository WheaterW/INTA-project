Configuring Smooth Evolution of SRv6 TE Policy from Non-compression to Compression
==================================================================================

This section describes how to configure smooth evolution of SRv6 TE Policy from non-compression to compression.

#### Context

In encapsulation mode, the SRv6 ingress encapsulates an outer IPv6 header and an SRH into each packet to be forwarded, increasing the packet header overhead. In addition, when there are a large number of SRv6 SIDs, the SRH length further increases, reducing the packet payload efficiency and hardware forwarding performance.

Against this backdrop, SRH compression is introduced, reducing the packet header overhead and also improving bandwidth utilization and forwarding efficiency. To achieve SRH compression, networks with non-compression SRv6 deployed need to be smoothly upgraded to G-SRv6. If a non-compression locator has been configured for an SRv6 TE Policy, you can configure the second locator, set compression-related parameters for this locator to become a compression locator, and then reference the compression locator in the corresponding BGP address family view to complete the evolution.

**Figure 1** Configuring smooth evolution of SRv6 TE Policy from non-compression to compression  
![](figure/en-us_image_0000001620051789.png)

#### Pre-configuration Tasks

Before configuring the evolution, complete the following tasks: (EVPN L3VPNv4 over SRv6 TE Policy is used as an example.)

* Configure both compression and non-compression SRv6 TE Policies. For details, see [Configuring an SRv6 TE Policy (Manual Configuration + IS-IS as an IGP)](dc_vrp_srv6_cfg_all_0110.html).
* Configure services based on the networking type. For details, see [Configuring EVPN L3VPNv4 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpn_over_srv6-te_policy.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) **as-number**
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) **vpn-instance-name**
   
   
   
   The BGP-VPN instance IPv4 address family view is displayed.
4. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* ****evpn****
   
   
   
   The device is enabled to add SIDs to VPN routes to be sent to EVPN.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The *locator-name* parameter needs to be set to the compression locator configured later.

#### Verifying the Configuration

* Run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) [ **endpoint** *endpoint-ip* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* ] command to check SRv6 TE Policy details.