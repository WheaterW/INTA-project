Configuring Isolated LSP Computation
====================================

To improve label switched path (LSP) reliability on a network that has the constraint-based routed label switched path (CR-LSP) hot standby feature, you can configure the isolated LSP computation feature so that the device uses both the disjoint algorithm and the constrained shortest path first (CSPF) algorithm to compute isolated primary and hot-standby LSPs.

#### Context

Most IP radio access networks (IP RANs) that use Multiprotocol Label Switching (MPLS) TE have high reliability requirements for LSPs. However, the existing CSPF algorithm simplifies the LSP path according to the principle of minimizing the link cost, and cannot automatically calculate the completely separate primary and secondary LSP paths.

Specifying explicit paths prevents the preceding issue. However, a loose explicit path may not be the optimal path, and a strict explicit path does not adapt to topology changes.

To resolve these problems, you can configure isolated LSP computation. After this feature is enabled, the disjoint and CSPF algorithms work together to compute primary and hot-standby LSPs at the same time and cut off crossover paths of the two LSPs. Then, the device gets the isolated primary and hot-standby LSPs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Isolated LSP computation is a best-effort technique. If the disjoint and CSPF algorithms cannot get isolated primary and hot-standby LSPs or two isolated LSPs do not exist, the device uses the primary and hot-standby LSPs computed by CSPF.
* After you enable the disjoint algorithm, the shared risk link group (SRLG), if configured, becomes ineffective.


#### Pre-configuration Tasks

Before configuring isolated LSP computation, complete the following tasks:

* [Configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0003.html).
* [Configure CR-LSP backup](dc_vrp_te-p2p_cfg_0057.html) and establish a hot-standby CR-LSP.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* CSPF must be enabled on ingress node of the RSVP-TE tunnel.
* Isolated LSP computation requires the collaboration of the CR-LSP hot standby feature and requires the hot-standby LSP to have the same reserved bandwidth as the primary LSP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The TE tunnel interface view is displayed.
3. Run [**mpls te cspf disjoint**](cmdqueryname=mpls+te+cspf+disjoint)
   
   
   
   The disjoint algorithm is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

* Run the [**display mpls te cspf destination**](cmdqueryname=display+mpls+te+cspf+destination) *ip-address* **computation-mode** **disjoint** command to check the computed primary and hot-standby LSPs after the disjoint algorithm is enabled.
* Run the [**display mpls te tunnel path**](cmdqueryname=display+mpls+te+tunnel+path) *tunnel-name* command to check information about the actual primary and hot-standby LSPs.