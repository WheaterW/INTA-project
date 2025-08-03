Configuring Eth-Trunk Load Balancing
====================================

Configuring Eth-Trunk Load Balancing

#### Configuring Load Balancing for an Eth-Trunk Interface

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *number*
   
   The Eth-Trunk interface view is displayed.
3. Run [**mode**](cmdqueryname=mode) { **lacp-static** | **manual load-balance** }
   
   The working mode of the Eth-Trunk interface is set.
   
   * **lacp-static**: indicates the static LACP mode. In this mode, both load balancing and redundancy backup can be implemented.
   * **manual load-balance**: indicates the manual load balancing mode. By default, an Eth-Trunk interface works in manual load balancing mode.
4. (Optional) Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   The Eth-Trunk member interface view is displayed.
5. (Optional) Run [**distribute-weight**](cmdqueryname=distribute-weight) *weight-value*
   
   The weight of the member interface is set.
   
   By default, the weight of an Eth-Trunk member interface is 1.
   
   The higher the weight of a member interface, the heavier the load over the member link.
   
   A maximum of 64 member interfaces in an Eth-Trunk interface can carry out load balancing. The total weights of all member interfaces in an Eth-Trunk interface cannot be greater than 64.
   
   When multicast traffic is transmitted over an Eth-Trunk interface, if the [**distribute-weight**](cmdqueryname=distribute-weight) command is used to change the weight of a member interface, you need to run the [**shutdown**](cmdqueryname=shutdown) and then [**undo shutdown**](cmdqueryname=undo+shutdown) commands to restart the member interface for the configuration to take effect.
6. Run [**commit**](cmdqueryname=commit).
   
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