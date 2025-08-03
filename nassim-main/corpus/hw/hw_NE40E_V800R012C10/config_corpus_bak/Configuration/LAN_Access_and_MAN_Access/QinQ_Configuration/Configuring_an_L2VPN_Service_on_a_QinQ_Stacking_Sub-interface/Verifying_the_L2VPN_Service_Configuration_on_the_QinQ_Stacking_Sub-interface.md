Verifying the L2VPN Service Configuration on the QinQ Stacking Sub-interface
============================================================================

After you configure an L2VPN service on a QinQ stacking sub-interface, verify the configuration

#### Prerequisites

The configurations of the sub-interface for QinQ stacking to provide L2VPN access are complete.


#### Procedure

* Run the [**display qinq information stacking**](cmdqueryname=display+qinq+information+stacking) [ **interface** *interface-type interface-number* [ .*subinterface-number* ] ] command to check QinQ stacking information.
* View the configuration of the L2VPN in CCC mode.
  
  
  + Run the [**display vll ccc**](cmdqueryname=display+vll+ccc) [ *ccc-name* | **type** { **local** | **remote** } ] command to check information about the CCC connection.
  + Run the [**display l2vpn ccc-interface vc-type ccc**](cmdqueryname=display+l2vpn+ccc-interface+vc-type+ccc) [ **up** | **down** ] command to check information about the interface in the Up or Down state.
* Check the configuration of the L2VPN in LDP mode.
  
  
  + Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **interface** *interface-type* *interface-number* ] command to check the local LDP VLL connection information on the PE.
  + Run the [**display mpls l2vc remote-info**](cmdqueryname=display+mpls+l2vc+remote-info) [ *vc-id* ] command to check the remote LDP VLL connection information on the PE.