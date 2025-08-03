(Optional) Configuring the Egress Protection Function
=====================================================

The egress protection function reduces E2E BFD sessions to be established, bandwidth resources to be consumed, and the burden on devices.

#### Context

In seamless MPLS scenarios, when an egress MASG fails, E2E BFD for BGP tunnel is used to instruct a CSG to perform VPN FRR switching. In this protection solution, both BGP LSPs and BFD sessions are in great numbers, which consumes a lot of bandwidth resources and burdens the device. To optimize the solution, the egress protection function can be configured on the master and backup MASGs. With this function enabled, both the master and backup MASGs assign the same private network label value to a core ASBR. If the master MASG fails, BFD for LDP LSP or BFD for TE can instruct a core ASBR to perform BGP FRR protection switching. After traffic is switched to the backup MASG, the MASG removes the BGP public network label and uses the private network label the same as that on the faulty master MASG to search for a matching VPN instance. Traffic can then be properly forwarded.

The egress protection function is configured on both the master and backup MASGs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the egress protection function is configured on egress MASGs between which a tunnel exists and a route imported by BGP on one of the MASGs recurses to the tunnel, this MASG then recurses the route to another tunnel of a different type. In this case, traffic is directed to the other MASG, which slows down traffic switchover. As a result, the egress protection function does not take effect. To address this problem, specify **non-relay-tunnel** when running the [**import-route**](cmdqueryname=import-route) or [**network**](cmdqueryname=network) command to prevent the routes imported by BGP from recursing to tunnels.



#### Prerequisites

Before configuring the egress protection function, complete the following tasks:

* Configure a loopback interface on each of the master and backup MASGs. The IP address of each loopback interface on an MASG is used to establish a remote BGP peer relationship with a remote device.
* Host routes to the loopback interfaces are imported into the BGP routing table, and both the master and backup MASGs assigns BGP labeled routes to a core ASBR. Therefore, the core ASBR has two BGP labeled routes destined for the same loopback interface. A routing policy is configured to enable the core ASBR to select one route to implement BGP FRR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The VPN instance IPv4 address family view is displayed.
4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the VPN instance IPv4 address family.
5. Run [**apply-label per-instance static**](cmdqueryname=apply-label+per-instance+static) *static-label-value*
   
   
   
   A device is enabled to assign the same static label to all routes destined for a remote PE in a VPN instance IPv4 address family.
   
   The same static label value must be set on both the master and backup MASGs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A change in the label allocation mode leads to re-advertising of IPv4 address family routes in a VPN instance. This step causes a temporary service interruption. Exercise caution when using this command.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.