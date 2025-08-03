Verifying the Configuration
===========================

After you configure VPN services on the VLAN tag termination sub-interface, verify the configuration.

#### Prerequisites

The configurations of the VLAN tag termination sub-interface to transmit VPN services are complete.


#### Procedure

* Run the [**display dot1q information termination**](cmdqueryname=display+dot1q+information+termination) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check configured dot1q VLAN tag termination information.
* Run the [**display qinq information termination**](cmdqueryname=display+qinq+information+termination) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check configured QinQ VLAN tag termination information.
* View the configuration of the L2VPN in CCC mode.
  
  
  + Run the [**display vll ccc**](cmdqueryname=display+vll+ccc) [ *ccc-name* | **type** { **local** | **remote** } ] command to check information about the CCC connection.
  + Run the [**display l2vpn ccc-interface vc-type ccc**](cmdqueryname=display+l2vpn+ccc-interface+vc-type+ccc) [ **up** | **down** ] command to check information about the interface in the Up or Down state.
* Check the configuration of the L2VPN in LDP mode.
  
  
  + Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **interface** *interface-type* *interface-number* ] command to check the local LDP VLL connection information on the PE.
  + Run the [**display mpls l2vc remote-info**](cmdqueryname=display+mpls+l2vc+remote-info) [ *vc-id* ] command to check the remote LDP VLL connection information on the PE.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** [ *vpn-instance-name* ] command to check VPN instance information.
* Run the [**display bgp**](cmdqueryname=display+bgp) [ **vpnv4 vpn-instance** *vpn-instance-name* ] **peer** command to check information about BGP peers.