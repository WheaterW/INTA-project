Verifying the Configuration
===========================

After configuring a BGP peer group, check information about BGP peers and BGP peer groups.

#### Prerequisites

A BGP peer group has been configured.
#### Procedure

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ *ipv4-address* ] **verbose** command to check detailed peer information.
* Run the [**display bgp group**](cmdqueryname=display+bgp+group) [ *group-name* ] command to check information about peer groups.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  This command can be used to view information about a BGP peer group only on the device where the peer group is created.
  
  If a peer group is specified in this command, detailed information about this peer group will be displayed. If no peer group is specified in this command, information about all BGP peer groups is displayed.