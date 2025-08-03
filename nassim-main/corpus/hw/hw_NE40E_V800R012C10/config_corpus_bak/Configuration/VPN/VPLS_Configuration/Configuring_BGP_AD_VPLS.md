Configuring BGP AD VPLS
=======================

BGP AD VPLS uses BGP packets for VSI member discovery and LDP FEC 129 signaling for PW establishment negotiation, enabling automatic VPLS PW establishment.

#### Usage Scenario

As VPLS technologies are used more widely and VPLS networks grow in scale, VPLS configurations on networks increase accordingly. BGP AD VPLS is introduced to simplify network configurations, enable automatic service deployment, and reduce OPEX.

BGP AD VPLS combines the advantages of BGP VPLS and LDP VPLS. It uses extended BGP messages for automatic discovery of VSI members and LDP FEC 129 for PW establishment negotiation, enabling automatic VPLS PW deployment.

BGP AD VPLS also has the following features compared with other VPLS configuration modes:

* As described in [Table 1](#EN-US_TASK_0172370185__tab-01), BGP AD VPLS saves local label resources but involves complex PW establishment and depends on LDP signaling.
  
  **Table 1** Comparison between BGP AD VPLS and BGP VPLS
  | VPLS Mode | Advantage | Disadvantage |
  | --- | --- | --- |
  | BGP VPLS | + BGP VPLS-enabled devices exchange BGP Update messages that carry label block information and compute and compare received label block information with the local label block information before establishing a PW with each other. + BGP VPLS is simpler than BGP AD VPLS in implementation. | + Labels are wasted. + Site ID management is needed. + There is no standard mechanism of clearing MAC address entries. |
  | BGP AD VPLS | + Label resources are saved. + BGP AD VPLS-enabled devices can communicate with PWE3-enabled devices by using LDP FEC 128. | + To establish a PW with each other, BGP AD VPLS-enabled devices need to use LDP signaling messages to exchange label information after VPLS member discovery. + BGP AD VPLS depends on BGP capabilities and is complex in implementation. |
* As described in [Table 2](#EN-US_TASK_0172370185__tab-02), BGP AD VPLS uses existing BGP sessions to discover members in a VPLS domain when new nodes are added to the VPLS domain or new VPLS domains are deployed. A PW can be set up between devices without explicit member configuration. This simplifies PW configurations in VSIs.
  
  **Table 2** Comparison of VPLS configurations in BGP AD VPLS mode and LDP VPLS mode when existing BGP sessions are used for VPLS member discovery after new nodes are added for VSIs
  | VPLS Mode | VSI Configurations on New Nodes | Additional Configurations on Existing Nodes |
  | --- | --- | --- |
  | LDP VPLS | ``` vsi-id company1  pwsignal ldp   vsi-id 2   peer x.x.x.x   ... ``` | ``` vsi-id company1  pwsignal ldp   vsi-id 2   peer y.y.y.y   ... ``` |
  | BGP AD VPLS | ``` vsi-id company1  bgp-ad   vpls-id 10   ...  l2vpn-ad-family   peer x.x.x.x enable  ``` | No additional configurations need to be performed.  BGP AD VPLS-enabled devices use extended BGP Update messages carrying VSI member information to automatically discover VSI members and LDP FEC 129 signaling to negotiate and establish VSI PWs. In this way, VSI members in the VPLS domain are automatically discovered, and VSI PWs are automatically established. Therefore, existing VSIs do not need additional configurations. |

With automatic VPLS member discovery and automatic PW deployment, BGP AD VPLS reduces the VPLS network configuration workload, implements automatic service deployment, and reduces customers' OPEX.

On the network shown in [Figure 1](#EN-US_TASK_0172370185__fig_dc_vrp_vpls_cfg_505701), BGP sessions are established between PE1, PE2, and PE3, and BGP AD VPLS is configured on PE1 and PE2, which reside in the same VPLS domain. PE3 needs to be added to the VPLS domain for network expansion. To achieve this goal, it is necessary to configure the same VPLS domain ID for the VSI on PE3. VPLS configurations do not need to be modified on BGP AD VPLS-enabled PE1 and PE2. After PE3 joins the VPLS domain, PWs can be automatically established using BGP AD between PE1 and PE3 and between PE2 and PE3, simplifying VPLS configuration.

**Figure 1** Full-mesh BGP AD VPLS networking  
![](images/fig_dc_vrp_vpls_cfg_505701.png)

BGP AD also supports HVPLS. The [**pw spoke-mode**](cmdqueryname=pw+spoke-mode) command can be run to configure the PWs of BGP AD VSIs as spoke PWs. After the command is run, remote peers are used as user-side devices on the HVPLS network.

#### Pre-configuration Tasks

Before configuring BGP AD VPLS, complete the following tasks:

* Configure IP addresses and routes on PEs and Ps to ensure network layer connectivity.
* Configure LSR IDs and enable basic MPLS functions on PEs and Ps.
* Establish tunnels between PEs to carry L2VPN services.
* Enable MPLS L2VPN on PEs.


[Enabling BGP Peers to Exchange VPLS Member Information](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5058.html)

BGP peers need to be enabled to exchange VPLS member information in the L2VPN-AD address family view.

[Creating a VSI and Configuring BGP AD Signaling](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5059.html)

When configuring BGP AD VPLS, you need to create a VSI and configure BGP AD signaling.

[Binding an AC Interface to a VSI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5005-03.html)

The view in which an AC interface is bound to a VSI depends on the type of link between the PE and CE.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_5061.html)

After configuring BGP AD VPLS, check local and remote VSI and VPLS connection information.