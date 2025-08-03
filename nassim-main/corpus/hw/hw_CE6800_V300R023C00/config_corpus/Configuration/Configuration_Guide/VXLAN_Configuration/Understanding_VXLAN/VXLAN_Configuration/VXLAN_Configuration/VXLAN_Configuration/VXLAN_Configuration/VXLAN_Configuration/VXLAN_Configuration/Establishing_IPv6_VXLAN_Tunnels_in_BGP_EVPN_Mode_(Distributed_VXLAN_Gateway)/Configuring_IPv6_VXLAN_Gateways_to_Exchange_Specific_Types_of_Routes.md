Configuring IPv6 VXLAN Gateways to Exchange Specific Types of Routes
====================================================================

Configuring IPv6 VXLAN Gateways to Exchange Specific Types of Routes

#### Context

By default, IPv6 VXLAN gateways can exchange MAC routes. The gateways must be configured to exchange IRB or IP prefix routes if hosts need to communicate across network segments. If an RR is deployed on the network, IRB or IP prefix routes must be exchanged only between the gateways and RR.

![](../public_sys-resources/note_3.0-en-us.png) 

Host routes can be advertised through IRB routes (recommended), IP prefix routes, or both. In contrast, network segment routes of hosts can be advertised through IP prefix routes only.



#### Procedure

* Configure IRB route advertisement.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view or BGP multi-instance view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number [ instance instance-name ]
     ```
  3. Enter the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
     
     
     ```
     [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
     ```
  4. Run one of the following commands based on the overlay network type to configure IRB route advertisement:
     
     
     
     For an IPv4 overlay network, run the following command:
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } advertise irb
     ```
     
     For an IPv6 overlay network, run the following command:
     
     ```
     [peer](cmdqueryname=peer) { ipv6-address | group-name } advertise irbv6
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure IP prefix route advertisement. 
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Perform one of the following steps based on the overlay network type to import IP routes to the BGP-VPN instance IPv4 or IPv6 address family:
     
     
     
     For an IPv4 overlay network, run the following command:
     
     ```
     [bgp](cmdqueryname=bgp) as-number [ instance instance-name ]
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     [import-route](cmdqueryname=import-route) { direct | isis process-id | ospf process-id | rip process-id | static } [ med med | route-policy route-policy-name ] *
     ```
     
     For an IPv6 overlay network, run the following command:
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
     [import-route](cmdqueryname=import-route) { direct | isis process-id | ospfv3 process-id | ripng process-id | static } [ med med | route-policy route-policy-name ] *
     ```
     
     To advertise host IP routes, configure import of direct routes. To advertise the route of a network segment where hosts reside, configure a dynamic routing protocol (such as OSPF or OSPFv3) and then run one of the preceding commands based on the overlay network type to import the route into the dynamic routing protocol.
  3. Configure IP prefix route advertisement. 
     
     
     ```
     [advertise l2vpn evpn](cmdqueryname=advertise+l2vpn+evpn) [ valid-routes | best-route ]
     ```
     
     IP prefix routes are Type 5 BGP EVPN routes that carry host IP addresses or network segment addresses as well as L3VNIs. Such routes are used to advertise host IP routes as well as network segment routes to which the host IP routes belong. If many specific host routes exist, you can reduce the number of routes that a gateway needs to save by configuring it to advertise IP prefix routes and importing the routes to the target BGP VPN instance address family.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + A gateway can advertise network segment routes only if the attached network segments are unique across the entire network.
     + After configuring IP prefix route advertisement, run the [**arp direct-route enable**](cmdqueryname=arp+direct-route+enable) or [**ipv6 nd direct-route enable**](cmdqueryname=ipv6+nd+direct-route+enable) command to allow the device to generate direct routes to host IP addresses. This will affect host migration.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```