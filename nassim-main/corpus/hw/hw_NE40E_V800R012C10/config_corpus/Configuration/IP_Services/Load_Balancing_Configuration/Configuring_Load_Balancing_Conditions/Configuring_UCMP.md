Configuring UCMP
================

UCMP can be configured using the following methods:

#### Enabling UCMP Globally

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**load-balance unequal-cost enable**](cmdqueryname=load-balance+unequal-cost+enable)
   
   UCMP is enabled globally.
3. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Enabling UCMP Based on the Configuration Bandwidth Globally

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   The interface view is displayed.
3. Run [**bandwidth**](cmdqueryname=bandwidth) *bandwidth*
   
   The configuration bandwidth is set for the interface.
4. Run [**quit**](cmdqueryname=quit)
   
   Return to the system view.
5. Run [**load-balance unequal-cost bandwidth-config enable**](cmdqueryname=load-balance+unequal-cost+bandwidth-config+enable)
   
   UCMP based on the configuration bandwidth is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Enabling UCMP on an Interface

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   The interface view is displayed.
   
   UCMP can be separately enabled only on physical interfaces.
3. Run [**load-balance unequal-cost enable**](cmdqueryname=load-balance+unequal-cost+enable)
   
   UCMP is enabled on the interface.
4. Run [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown)
   
   The interface is restarted for the UCMP configuration to take effect.
   
   Enabling/Disabling UCMP on a physical interface through commands does not immediately trigger routes and FIB entries to be updated. You must restart the interface.
5. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Enabling UCMP on the P Node of an MPLS LSP/Tunnel

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**load-balance mpls unequal-cost enable**](cmdqueryname=load-balance+mpls+unequal-cost+enable)
   
   UCMP is enabled on the MPLS P node (excluding the P node on a BGP LSP).
   
   If UCMP is enabled and the MPLS P node (excluding the P node on the BGP LSP) has multiple outbound interfaces, UCMP is performed among the outbound interfaces based on bandwidth weights. If UCMP is disabled and the MPLS P node has multiple outbound interfaces, ECMP is performed among the outbound interfaces.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command does not support sub-interfaces.

#### Enabling UCMP for MPLS TE Tunnels

MPLS TE tunnels include static MPLS TE and P2P RSVP-TE tunnels. When multiple MPLS TE tunnels are destined for a downstream device, you can configure UCMP weights or CT bandwidths to load-balance traffic among the MPLS TE tunnels in UCMP mode.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If UCMP is globally enabled for static MPLS TE and P2P RSVP-TE tunnels and UCMP weights are configured for all the tunnels, UCMP is preferentially performed based on the weights. If no load balancing weight is configured for some tunnels but UCMP is globally enabled and CT bandwidths are configured for all tunnels, UCMP is performed based on the CT bandwidths. If neither weights nor CT bandwidths are configured for tunnels, equal-cost load balancing is performed by default.

When UCMP is performed based on weights, the actual weight of a tunnel is calculated using the following formula: Actual weight of this tunnel = 100 x (Weight of this tunnel/Sum of weights of all tunnels).

The volume of traffic carried by a single tunnel in load balancing mode (known as load balancing traffic volume of the tunnel, for short) is calculated using the following formula: Load balancing traffic volume of a tunnel = Total traffic volume x (Actual weight of the tunnel/Sum of weights of all tunnels). Because the sum of load balancing weights of all TE tunnels may not be exactly divided by the weight of a single TE tunnel, the actual load balancing traffic volume of a TE tunnel may be slightly different from the calculated value.

1. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   The MPLS TE tunnel interface view is displayed.
2. Run [**load-balance unequal-cost enable**](cmdqueryname=load-balance+unequal-cost+enable)
   
   UCMP is enabled globally.
3. Configure UCMP for MPLS TE tunnels. For details, see [Table 1](#EN-US_CONCEPT_0172365024__table7246163215374).
   
   You can perform one or more steps in [Table 1](#EN-US_CONCEPT_0172365024__table7246163215374).
   
   **Table 1** Configuring UCMP for MPLS TE tunnels
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a UCMP weight for each MPLS TE tunnel. | [**load-balance unequal-cost weight**](cmdqueryname=load-balance+unequal-cost+weight) *weight* | This function takes effect only when UCMP weights are configured for all tunnels. |
   | Configure a bandwidth for each MPLS TE tunnel. | **[**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth)** *ctType* **ctValue** | This function takes effect only when bandwidths are configured for all tunnels. |
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Enabling UCMP for SR-MPLS

To implement UCMP for a transit P node of a tunnel (such as an SR-MPLS BE or SR-MPLS TE tunnel), run the [**load-balance mpls unequal-cost enable**](cmdqueryname=load-balance+mpls+unequal-cost+enable) command.

UCMP on the ingress of an SR-MPLS TE Policy is performed among multiple segment lists in the SR-MPLS TE Policy. You only need to configure weights for the segment lists. For configuration details, see [Configuring an SR-MPLS TE Policy](../vrp/dc_vrp_sr_all_cfg_0062.html) and [Example for Configuring EVPN L3VPN over Static SR-MPLS TE Policy and UCMP](../vrp/dc_vrp_sr_all_cfg_0409.html).

To implement UCMP for a transit P node of an SR-MPLS TE Policy, run the [**load-balance mpls unequal-cost enable**](cmdqueryname=load-balance+mpls+unequal-cost+enable) command.


#### Enabling UCMP for SRv6

In an SRv6 BE scenario, the [**load-balance unequal-cost enable**](cmdqueryname=load-balance+unequal-cost+enable) command needs to be run to globally enable UCMP on the ingress and transit nodes.

UCMP on the ingress of an SRv6 TE Policy is performed among multiple segment lists in the SRv6 TE Policy. You only need to configure weights for the segment lists. For configuration details, see [Configuring an SRv6 TE Policy](../vrp/dc_vrp_srv6_cfg_all_0112.html) and [Example for Configuring EVPN L3VPNv4 over SRv6 TE Policy (Manual Configuration + UCMP Scenario)](../vrp/dc_vrp_srv6_cfg_all_0140.html).

For the transit P node of an SRv6 TE Policy, UCMP is not supported in an End.X SID scenario. To globally enable UCMP in an End SID scenario, run the [**load-balance unequal-cost enable**](cmdqueryname=load-balance+unequal-cost+enable) command.


#### Follow-up Procedure

Run the [**save**](cmdqueryname=save) command to save the current configuration to the configuration file when a set of configuration is finished and the expected functions have been achieved.