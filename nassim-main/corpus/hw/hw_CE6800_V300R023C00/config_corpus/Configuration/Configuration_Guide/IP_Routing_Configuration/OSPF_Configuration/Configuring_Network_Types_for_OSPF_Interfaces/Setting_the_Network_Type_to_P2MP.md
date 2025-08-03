Setting the Network Type to P2MP
================================

Setting the Network Type to P2MP

#### Prerequisites

Before setting the network type to P2MP, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set the network type of the OSPF interface to P2MP.
   
   
   ```
   [ospf network-type](cmdqueryname=ospf+network-type) p2mp
   ```
   
   A P2MP network can be obtained only by changing a network type to P2MP. For an interface with the NBMA network type, if the network is not fully meshed, change the network type of the interface to P2MP. By doing this, two indirectly connected devices can communicate through a third device that can directly reach both devices. After the network type of the interface is changed to P2MP, there is no need to manually specify a neighbor.
5. (Optional) Disable OSPF from checking the network mask.
   
   
   ```
   [ospf p2mp-mask-ignore](cmdqueryname=ospf+p2mp-mask-ignore)
   ```
   
   By default, OSPF checks the network mask of Hello packets on a P2MP network. Devices with different network mask lengths cannot establish a neighbor relationship. After devices are configured not to check the network masks in Hello packets, OSPF neighbor relationships can be established.
6. (Optional) Configure the device to filter the LSAs to be sent on the P2MP network.
   1. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   2. Create an ACL and enter the ACL view.
      
      
      ```
      [acl](cmdqueryname=acl) { name basic-acl-name { basic | [ number ] basic-acl-number } | [ number ] basic-acl-number }
      ```
   3. Configure an ACL rule.
      
      
      ```
      [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment-type fragment | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
      ```
      
      When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
      
      The following table lists the strategies that can be taken when an ACL is used for filtering.
      
      **Table 1** ACL strategies
      | Condition | Result |
      | --- | --- |
      | The action in an ACL rule is **permit**. | The matched LSAs will be advertised. |
      | The action in an ACL rule is **deny**. | The matched LSAs will not be advertised. |
      | The network segment of a route is beyond the range specified in an ACL rule. | The LSA carrying the route information will not be advertised by default. |
      | The ACL does not contain rules. | Any LSAs matched against the filtering policy based on this ACL will not be advertised. |
      | If the configuration order is used as the ACL rule matching order, LSAs are matched against the ACL rules based on the configuration order by default. If the ACL rules are numbered with IDs, LSAs are matched against the ACL rules in ascending order of their IDs. | In this case, LSAs can be filtered using a blacklist or whitelist:  Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted LSAs. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to advertise the other LSAs.  Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the LSAs to be advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out unwanted LSAs. |
   4. Enter the OSPF view.
      
      
      ```
      [ospf](cmdqueryname=ospf) [ process-id ]
      ```
   5. Configure the device to filter the LSAs to be sent to a specified neighbor.
      
      
      ```
      [filter-lsa-out peer](cmdqueryname=filter-lsa-out+peer) peer-addr { all | { ase [ acl { ase-acl-num | ase-acl-name } ] | nssa [ acl { nssa-acl-num | nssa-acl-name } ] | summary [ acl { sum-acl-num | sum-acl-name } ] } * }
      ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check information about OSPF interfaces.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **peer** command to check information about OSPF neighbors.