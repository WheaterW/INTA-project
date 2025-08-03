Associating the VPWS PW Status with the VPNv6 Route Status
==========================================================

Associating the VPWS PW status with the VPNv6 route status prevents traffic loss caused by a failure to detect link failures.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0272267219__fig_dc_vrp_l2-l3_cfg_502601), a PW is established between the CSG and each AGG. PW1 is the primary PW, and PW2 is the secondary PW. A BGP VPNv6 peer relationship is established between AGG1 and RSG1, between AGG2 and RSG2, and between AGG1 and AGG2. A VE-Group consisting of one L2VE interface and one L3VE interface is configured on each AGG. The L3VE interface on an AGG is bound to the VPN instance on that AGG.

**Figure 1** Associating the VPWS PW status with the VPNv6 route status  
![](figure/en-us_image_0272271851.png)

When no fault occurs, the CSG sends traffic to RSG1 through AGG1 along PW1. If both links between AGG1 and RSG1 and between AGG1 and AGG2 fail and the CSG cannot detect the link failures, the CSG still sends traffic to AGG1, and as a result, traffic loss occurs.

To resolve this problem, configure AGG1 to associate the PW status with the VPNv6 route status. If the link between AGG1 and RSG1 and the link between AGG1 and AGG2 fail, the VPNv6 route status becomes down. AGG1 sets the corresponding VPWS PW status to down and instructs the CSG to perform a primary/secondary PW switchover. Then, the CSG switches upstream traffic to the path CSG -> AGG2 -> RSG2 -> RSG1, preventing traffic loss caused by the link failures.

#### Pre-configuration Tasks

Before associating the VPWS PW status with the VPNv6 route status, complete the following tasks:

* Configure data link layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol of each interface is up.
* Configure basic MPLS functions and public network tunnels.
* Configure PWE3. For configuration details, see [Configuring LDP VPWS](dc_vrp_vpws_cfg_3004.html).
* Configure an L2VPN to access an L3VPN. For configuration details, see [VPWS Accessing a Public Network or L3VPN](dc_vrp_l2-l3_cfg_5003.html).
* Configure BFD to detect public network link faults. For configuration details, see [Configuring BFD to Detect Public Network Link Faults](dc_vrp_vpws_cfg_6021.html).



#### Procedure

* Configure each RSG to advertise VPNv6 routes to its BGP VPNv6 peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
     
     
     
     The loopback interface view is displayed.
  3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
     
     
     
     The interface is bound to a VPN instance.
  4. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address* | *prefix-length* }
     
     
     
     An IPv6 address is configured for the interface.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  8. Run [**network**](cmdqueryname=network) *ipv6-address* *mask-length*
     
     
     
     The RSG is enabled to advertise VPNv6 routes to a corresponding AGG.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure AGG1 to associate the PW status with the VPNv6 route status.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mpls l2vpn track route**](cmdqueryname=mpls+l2vpn+track+route) *ipv6-address* { *ipv6-mask* | *ipv6-mask-length* } **vpn-instance** *vpn-instance-name*
     
     
     
     The PW status is associated with the VPNv6 route status.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display mpls l2vpn track route**](cmdqueryname=display+mpls+l2vpn+track+route) command to check information about the association between the PW status and VPNv6 route status on an AGG.