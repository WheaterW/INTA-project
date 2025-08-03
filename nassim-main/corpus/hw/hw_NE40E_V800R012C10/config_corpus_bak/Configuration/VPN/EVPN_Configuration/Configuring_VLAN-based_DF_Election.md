Configuring VLAN-based DF Election
==================================

In CE dual-homing networking, to balance the broadcast, unknown unicast, and multicast (BUM) traffic between the CE and PEs, you can configure virtual local area network (VLAN)-based designated forwarder (DF) election.

#### Usage Scenario

In CE dual-homing networking, the following conditions must be met to balance BUM traffic:

1. An Eth-Trunk sub-interface is bound to an EVPN instance created on each PE.
2. VLAN-based DF election is configured.

For details about how to meet the first condition, see [Eth-Trunk Interface Configuration](dc_vrp_ethtrunk_cfg_0000.html). This section describes how to configure VLAN-based DF election.


#### Pre-configuration Tasks

Before configuring VLAN-based DF election, bind an Eth-Trunk sub-interface to an EVPN instance and [configure EVPN VPLS over MPLS (common EVPN instance)](dc_vrp_evpn_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn**](cmdqueryname=evpn)
   
   
   
   The global EVPN configuration view is created and displayed.
3. Run [**df-election type vlan**](cmdqueryname=df-election+type+vlan)
   
   
   
   VLAN-based DF election is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring VLAN-based DF election, run the [**display evpn**](cmdqueryname=display+evpn) **vpn-instance** **name** *vpn-instance-name* **df result** command to view the DF election result in the EVPN instance.