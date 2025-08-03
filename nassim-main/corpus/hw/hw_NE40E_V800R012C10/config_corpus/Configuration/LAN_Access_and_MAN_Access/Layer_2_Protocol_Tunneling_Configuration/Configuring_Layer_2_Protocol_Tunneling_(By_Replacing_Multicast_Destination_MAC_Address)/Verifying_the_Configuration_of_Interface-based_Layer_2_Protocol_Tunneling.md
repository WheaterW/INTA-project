Verifying the Configuration of Interface-based Layer 2 Protocol Tunneling
=========================================================================

After configuring interface-based Layer 2 protocol tunneling, check Layer 2 protocol tunneling information, such as the tunneled Layer 2 protocol names, protocol types, multicast destination MAC addresses, and specified multicast MAC addresses (group MAC addresses).

#### Context

Interface-based Layer 2 protocol tunneling has been configured.


#### Procedure

* Run the [**display l2protocol-tunnel
  group-mac**](cmdqueryname=display+l2protocol-tunnel+group-mac) { **all** | *protocol* } command to check Layer 2 protocol tunneling information.
  
  
  
  Run the [**display stp**](cmdqueryname=display+stp) [ **brief** ] command to check the spanning tree information for tunneled STP, Rapid Spanning Tree Protocol (RSTP), or Multiple Spanning Tree Protocol (MSTP).