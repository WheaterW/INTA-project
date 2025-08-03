Configuring a Policy for Dynamically Establishing a BGP BFD Session
===================================================================

BGP BFD sessions can be dynamically established based on either host addresses or an IP address prefix list.

#### Context

The policies for dynamically establishing BGP BFD sessions are as follows:

* Host address-based policy: used when all host addresses are available to trigger the creation of BGP BFD sessions.
* IP address prefix list-based policy: used when only some host addresses can be used to establish BFD sessions.

Perform the following steps on the ingress of an E2E BGP tunnel:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**ip ip-prefix**](cmdqueryname=ip+ip-prefix+index+permit+deny+match-network+greater-equal) *ip-prefix-name* [ **index** *index-number* ] { **permit** | **deny** } *ipv4-address* *mask-length* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]
   
   
   
   An IPv4 address prefix list is configured, and list entries are configured.
   
   You can perform this step when you want to use an IP address prefix list to dynamically establish BGP BFD sessions. For configuration details about how to configure an IP address prefix list, see [Configuring an IPv4 Address Prefix List](dc_vrp_route-policy_cfg_0004.html).
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
4. Run [**mpls bgp bfd-trigger-tunnel**](cmdqueryname=mpls+bgp+bfd-trigger-tunnel+host+ip-prefix) { **host** | **ip-prefix** *ip-prefix-name* }
   
   
   
   A policy for dynamically establishing a BGP BFD session is configured.
   
   After a policy is configured, the device starts to dynamically establish a BFD session.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.