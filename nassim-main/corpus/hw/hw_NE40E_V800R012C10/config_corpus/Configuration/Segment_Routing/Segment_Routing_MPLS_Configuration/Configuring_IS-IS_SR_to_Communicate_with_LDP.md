Configuring IS-IS SR to Communicate with LDP
============================================

This section describes how to configure IS-IS SR to communicate with LDP.

#### Usage Scenario

The SR and LDP interworking technique allows both segment routing and LDP to work within the same network. This technique connects an SR network to an LDP network to implement MPLS forwarding.

On the network shown in [Figure 1](#EN-US_TASK_0172368826__fig_dc_vrp_sr_all_cfg_001801), an SR domain is created between PE1 that functions as a mapping client and the P device that functions as a mapping server. Mappings between prefixes and SIDs need to be configured on the P device and advertised to PE1, which receives the mappings. An LDP domain lies between the P device and PE2, which supports only LDP. To enable PE1 and PE2 to communicate with each other, you need to establish an SR LSP and an LDP LSP, and establish the mapping between the SR LSP and LDP LSP on the P device.

**Figure 1** Communication between SR and LDP  
![](images/fig_dc_vrp_sr_all_cfg_001801.png)  


#### Pre-configuration Tasks

Before you configure IS-IS SR to communicate with LDP, complete the following tasks:

* Configure an SR LSP from PE1 to the P. See [Configuring an IS-IS SR-MPLS BE Tunnel](dc_vrp_sr-be_cfg_0008.html).
* Configure an LDP LSP from the P to PE2. See [Configuring an LDP LSP](dc_vrp_ldp-p2p_cfg_0015.html).

#### Procedure

* Configure the mapping server.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     Segment routing is globally enabled, and the Segment Routing view is displayed.
  3. Run [**mapping-server prefix-sid-mapping**](cmdqueryname=mapping-server+prefix-sid-mapping) *ip-address* *mask-length* *begin-value* [ **range** *range-value* ] [ **attached** ]
     
     
     
     Mapping between the prefix and SID is configured.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exist the SR view.
  5. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  6. Run [**segment-routing mapping-server**](cmdqueryname=segment-routing+mapping-server) **send**
     
     
     
     The local node is enabled to advertise the local SID label mapping.
  7. (Optional) Run [**segment-routing mapping-server**](cmdqueryname=segment-routing+mapping-server) **receive**
     
     
     
     The local node is enabled to receive SID label mapping messages.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the mapping client.
  
  
  
  A device that is not configured as a mapping server functions as a mapping client by default.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**segment-routing mapping-server**](cmdqueryname=segment-routing+mapping-server) **receive**
     
     
     
     The local node is enabled to receive SID label mapping messages.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device connecting the LDP domain and the SR domain.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**lsp-trigger segment-routing-interworking best-effort host**](cmdqueryname=lsp-trigger+segment-routing-interworking+best-effort+host)
     
     
     
     A policy for triggering backup LDP LSP establishment is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Checking the Configurations

After completing the configurations, run the [**display segment-routing prefix mpls forwarding**](cmdqueryname=display+segment-routing+prefix+mpls+forwarding) command to check the label forwarding information base of Segment Routing.