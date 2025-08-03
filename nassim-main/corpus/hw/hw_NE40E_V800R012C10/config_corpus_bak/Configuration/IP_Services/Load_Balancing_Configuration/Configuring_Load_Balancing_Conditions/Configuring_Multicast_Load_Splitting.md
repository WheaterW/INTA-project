Configuring Multicast Load Splitting
====================================

Configuring_Multicast_Load_Splitting

#### Configuring a Multicast Load Splitting Mode

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. (Optional) Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   The VPN instance view is displayed.
   
   If multicast routes belong to a public network, skip this step.
3. Run [**multicast load-splitting**](cmdqueryname=multicast+load-splitting) { **balance-ucmp** | **stable-preferred** | **source** | **group** | **source-group** }
   
   A multicast load splitting mode is configured.
   
   By default, no multicast load splitting mode is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Enabling Trunk Load Balancing for Layer 2 Multicast

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   The VLAN view is displayed.
   
   Or run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **auto** | **static** ]
   
   The VSI view is displayed.
3. Run [**trunk multicast load-balance enable**](cmdqueryname=trunk+multicast+load-balance+enable)
   
   Trunk load balancing is enabled for Layer 2 multicast.
   
   By default, trunk load balancing is not enabled for Layer 2 multicast.
   
   Trunk load balancing for Layer 2 multicast conflicts with IGMP snooping and MLD snooping in the same VLAN or VSI.
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Follow-up Procedure

Run the **save** command to save the current configuration to the configuration file when a set of configuration is finished and the expected functions have been achieved.