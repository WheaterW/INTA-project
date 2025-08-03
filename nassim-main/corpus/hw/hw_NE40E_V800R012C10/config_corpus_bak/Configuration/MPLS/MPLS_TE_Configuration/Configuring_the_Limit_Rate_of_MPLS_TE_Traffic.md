Configuring the Limit Rate of MPLS TE Traffic
=============================================

This section describes how to configure the limit rate of MPLS TE traffic to limit TE tunnel traffic within the bandwidth range that is actually configured.

#### Usage Scenario

Physical links over which a TE tunnel is established may also transmit traffic of other TE tunnels, non-CR-LSP traffic, or even IP traffic, in addition to the TE tunnel traffic. To limit the TE tunnel traffic within a bandwidth range that is actually configured, set a limit rate for TE tunnel traffic.

After the configuration of the limit rate, TE traffic is limited to a bandwidth range that is actually configured. TE traffic with the bandwidth higher than the set bandwidth is dropped.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before you configure rate limiting for MPLS TE traffic, run the [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) command on the corresponding tunnel interface. If this command is not run, rate limiting is not performed for MPLS TE traffic.



#### Pre-configuration Tasks

Before configuring rate limiting for MPLS TE traffic, complete the following tasks:

* [Configuring Static CR-LSP](dc_vrp_te-p2p_cfg_0175.html) or [Configuring an RSVP-TE Tunnel](dc_vrp_te-p2p_cfg_0003.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The tunnel interface view is displayed.
3. Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) *ctType* *ctValue*
   
   
   
   The bandwidth constraint of the MPLS TE tunnel is configured.
4. Run [**mpls te lsp-tp outbound**](cmdqueryname=mpls+te+lsp-tp+outbound)
   
   
   
   Traffic policing for the MPLS TE tunnel is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface Tunnel** *tunnel-number* command.
  
  The command output shows that the rate limiting function has been enabled.