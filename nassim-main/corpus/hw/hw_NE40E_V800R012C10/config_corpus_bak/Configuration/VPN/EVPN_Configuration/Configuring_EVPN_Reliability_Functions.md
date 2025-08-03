Configuring EVPN Reliability Functions
======================================

This section describes how to configure EVPN reliability.

#### Usage Scenario

| Reliability Function Configuration | Usage Scenario |
| --- | --- |
| [Configure a PE to monitor the BGP EVPN peer status.](#EN-US_TASK_0172370504__step_01) | On an EVPN where a CE is dual-homed to PEs, after a PE restarts due to a fault or other reasons, traffic may be lost. As shown in [Figure 1](#EN-US_TASK_0172370504__fig_dc_vrp_evpn_cfg_001601), CE1 is dual-homed to PE1 and PE2, and PE1 is elected as the primary designated forwarder (DF). Once PE1 fails, PE2 changes to be the primary DF and takes over the broadcast, unknown unicast, and multicast (BUM) traffic. After PE1 recovers, if PE1 establishes a BGP peer relationship with PE2 before with PE3, PE1 and PE2 send Ethernet segment routes to each other. At this time, PE1 becomes the primary DF, and PE2 becomes the backup DF again. In this case, if PE3 still forwards traffic to PE2, the traffic will be discarded. However, if PE1 establishes a BGP peer relationship with PE3 before with PE2, PE1 and PE2 both become the primary DFs. In this case, PE3 forwards traffic to both PE1 and PE2, causing CE1 to receive duplicate copies of traffic.  To resolve this issue, configure PE1's interface connected to CE1 to monitor the BGP EVPN peer status.  This configuration allows PE1 to trigger a timer for delaying Ethernet segment route advertisement once PE1 recovers and the PE1 interface connecting to CE1 goes up. After the delay timer is triggered, PE1 monitors the status of its BGP peers PE2 and PE3. If the BGP peer relationships both go up before the delay timer expires, PE1 sends Ethernet segment routes to both PE2 and PE3. After the timer expires, PE1 sends Ethernet segment routes only to the peer with whom its BGP peer relationship is in the up state. After originating and sending Ethernet segment routes upon delay timer expiration, PE1 performs DF election based on all received Ethernet segment routes.  NOTE:  The delay timer for sending Ethernet segment routes must be set based on the BGP peer relationship status. If no peer relationship is established after the timer expires, two primary or backup DFs exist. If two primary DFs exist, duplicate copies of traffic are sent. If two backup DFs exist, the traffic is discarded.  **Figure 1** CE dual-homing networking |
| [Set a delay after which Ethernet segment routes are advertised.](#EN-US_TASK_0172370504__step_02) | If the PE functioning as the primary DF recovers from a fault, the traffic on the network side may be dropped due to slow connection recovery on the access side. As shown in [Figure 2](#EN-US_TASK_0172370504__fig_timer_es-recovery), at least one of PE1 and PE2 is configured to work in the single-active mode. If PE1 fails, the connection between CE1 and PE1 is interrupted, and the Ethernet segment identifier (ESI) configured for the connection to CE1 becomes invalid. As a result, PE1 becomes the backup DF, and PE2 becomes the primary DF. Traffic is switch from the path CE2 â PE3 â PE1 â CE1 to the path CE2 â PE3 â PE2 â CE1. After PE1 recovers, PE1's ESI becomes valid again, and PE1 generates Ethernet segment routes immediately for DF election so that PE1 switches to be the primary DF rapidly. However, PE1 still fails to establish the connection to CE1. CE2 has to keep sending traffic to PE2, causing traffic loss.  To resolve this issue, on PE1's interface connected to CE1, set a delay after which Ethernet segment routes are advertised. This configuration allows PE1 to generate Ethernet segment routes only after restoring the communication with the access-side network. **Figure 2** CE dual-homing networking |
| [Enable the function that AC interface status influences DF election on a PE.](#EN-US_TASK_0172370504__step_03) | In CE dual-homing networking, access-side sub-interfaces are bound to an EVPN instance. If an ESI is set on the interface and one of the sub-interfaces goes down due to a fault or some other reason, the ESI remains valid because the other sub-interfaces bound to the EVPN instance remain up. As a result, the PE does not re-originate Ethernet segment routes to trigger DF election, which may prevent the BUM traffic from being forwarded.  To resolve this issue, enable the function that allows AC interface status to influence DF election. This configuration helps check whether the PE has received the auto discovery (A-D) routes from all PEs during DF election to determine whether these PEs are qualified for DF election. If a PE has not received the A-D routes from a peer PE, the peer PE cannot participate in DF election. |
| [Configure a hold time after which a device responds to the up event of public network outbound interfaces.](#EN-US_TASK_0172370504__step_05) | In a scenario where a VLL accesses an EVPN in active-active mode, when the standby PE restarts, BUM traffic can still be forwarded due to the unstable status. As a result, extra packets are sent. To resolve this issue, configure a hold time after which the standby PE responds to the up event of all public network outbound interfaces of the VLL. Setting a 5-minute hold time is recommended. |
| [Configure local-remote FRR for MAC routes.](#EN-US_TASK_0172370504__cmd197153181401) | In an EVPN dual-homing active-active or dual-homing single-active scenario, a CE is dual-homed to two PEs. After local-remote FRR is enabled for MAC routes on dual-homing PEs, traffic destined for a CE can be rapidly switched to the link connected to the other PE if the link between the CE and one PE fails, ensuring traffic continuity.  NOTE:  The configuration described in this section applies to common EVPN and BD EVPN scenarios. For details about how to configure FRR in an EVPN VPWS scenario, see [Configuring EVPN VPWS over MPLS](dc_vrp_evpn_cfg_0020.html). |



#### Pre-configuration Tasks

Before configuring EVPN reliability, configure [EVPN VPLS over MPLS (common EVPN instance)](dc_vrp_evpn_cfg_0003.html).


#### Procedure

* Configure a PE to monitor the BGP EVPN peer status.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id*
     
     
     
     The Eth-Trunk interface view is displayed.
  3. Run [**es track evpn-peer**](cmdqueryname=es+track+evpn-peer) *peer-address*
     
     
     
     The device is configured to monitor the BGP EVPN peer status.
     
     To monitor the status of multiple BGP EVPN peers, repeat this step.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a delay for generating Ethernet segment routes on the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id*
     
     
     
     The Eth-Trunk interface view is displayed.
  3. Run [**timer es-recovery**](cmdqueryname=timer+es-recovery) *interval*
     
     
     
     A delay for generating Ethernet segment routes is configured.
     
     The recommended value is 30 seconds.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable the function that AC interface status influences DF election on the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn**](cmdqueryname=evpn)
     
     
     
     The EVPN global configuration view is displayed.
  3. Run [**df-election ac-influence enable**](cmdqueryname=df-election+ac-influence+enable)
     
     
     
     The function that allows AC interface status to influence DF election is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a hold time after which the device responds to the up event of a public network outbound interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**carrier up-hold-time**](cmdqueryname=carrier+up-hold-time) *interval*
     
     
     
     A hold time is configured, after which the device responds to an interface up event.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure local-remote FRR for MAC routes. 
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn**](cmdqueryname=evpn)
     
     
     
     The EVPN global configuration view is displayed.
  3. You can use either of the following methods to enable the redirection function. Configure VLAN extension redirection or MAC redirection as required.
     
     
     + Enable VLAN extension redirection.
       1. Run the [**vlan-extend private enable**](cmdqueryname=vlan-extend+private+enable) command to enable the device to add the new VLAN extended community attribute to local routes before advertising them to peers.
       2. Run the [**vlan-extend redirect enable**](cmdqueryname=vlan-extend+redirect+enable) command to enable the device to redirect received routes carrying the newly added VLAN extended community attribute.
     + Enable MAC redirection using either of the following methods:
       - Global configuration: Run the [**mac-redirect-compatible enable**](cmdqueryname=mac-redirect-compatible+enable) command in the EVPN global configuration view.
       - EVPN instance-specific configuration: Run the [**mac-redirect-compatible enable**](cmdqueryname=mac-redirect-compatible+enable) command in the BD EVPN instance view.
       
       By default, an EVPN instance inherits the MAC redirection configuration in the EVPN global configuration view. If MAC redirection is configured in the EVPN instance view, the configuration in this view takes precedence over that in the global view.
  4. Enable local-remote FRR for MAC routes using either of the following methods:
     
     
     + Global configuration: Run the [**local-remote frr enable**](cmdqueryname=local-remote+frr+enable) command in the EVPN global configuration view.
     + EVPN instance-specific configuration: Run the [**local-remote frr enable**](cmdqueryname=local-remote+frr+enable) command in the EVPN instance or BD EVPN instance view.
     
     By default, the configuration of local-remote FRR for MAC routes in an EVPN instance is the same as that in the EVPN global configuration view. After local-remote FRR for MAC routes is configured in the EVPN instance view, the configuration in the EVPN instance takes effect.

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether the EVPN reliability function is successfully configured.