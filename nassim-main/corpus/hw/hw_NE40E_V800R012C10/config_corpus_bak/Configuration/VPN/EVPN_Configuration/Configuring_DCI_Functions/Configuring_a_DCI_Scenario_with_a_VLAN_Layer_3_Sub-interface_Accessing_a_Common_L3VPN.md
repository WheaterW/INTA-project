Configuring a DCI Scenario with a VLAN Layer 3 Sub-interface Accessing a Common L3VPN
=====================================================================================

The DCI Scenario with a VLAN Layer 3 Sub-interface Accessing a Common L3VPN uses different cloud management platforms, and a Layer 3 Ethernet sub-interface is associated with a VLAN to access an L3VPN.

#### Context

VLAN Layer 3 sub-interface accessing common L3VPN applies to scenarios where traditional data centers communicate through the DCI network.

Gateways and DCI-PEs are deployed individually. The DCI-PEs consider connected DC GWs as CEs, receive VM IP routes from the data center through a VPN Layer 3 routing protocol, and save and maintain the received routes.

If VXLAN is deployed in the data center, the solution of Underlay VLAN Layer 3 access to DCI can be used. On the network shown in [Figure 1](#EN-US_TASK_0172363947__fig_dc_vrp_dci_cfg_000401), VXLAN tunnels are established within each data center to allow communication between VMs in the local data center. A BGP/MPLS IP VPN is deployed on the DCI backbone network. Layer 3 Ethernet sub-interfaces are deployed on DCI-PEs, associated with VLANs, and connected to the BGP/MPLS IP VPN, enabling VMs in different data centers to communicate with each other.

**Figure 1** Configuring a DCI Scenario with a VLAN Layer 3 Sub-interface Accessing a Common L3VPN  
![](images/fig_dc_vrp_dci_cfg_000401.png)

#### Procedure

1. Configure basic L3VPN functions on the DCI backbone network. For configuration details, see [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).
2. Configure a dot1q VLAN tag termination sub-interface and bind the sub-interface to a VPN instance.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*.*subinterface-number*
      
      
      
      An Ethernet sub-interface is created, and its view is displayed.
   2. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
      
      
      
      A VLAN is bound to the sub-interface, and a VLAN encapsulation mode is specified.
   3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      The sub-interface is bound to a VPN instance.
   4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the sub-interface.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.