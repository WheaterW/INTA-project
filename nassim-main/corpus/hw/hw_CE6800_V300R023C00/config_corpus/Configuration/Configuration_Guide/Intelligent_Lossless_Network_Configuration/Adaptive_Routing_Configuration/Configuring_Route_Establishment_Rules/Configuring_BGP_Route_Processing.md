Configuring BGP Route Processing
================================

Configuring BGP Route Processing

#### Context

The adaptive routing function can be used on a device only after specific BGP routes and the corresponding routing policies are correctly configured.

* Configure the device to import direct routes in the Mix VPN instance to the public network routing table.
* Configure route advertisement and reception for the public network instance.
* Configure route import, advertisement, and reception for the Non-min VPN instance.
* Configure route import for the Mix VPN instance.
* Configure load balancing.

For details about how to configure BGP routes, see the operations of configuring BGP route processing in [Example for Configuring Adaptive Routing](galaxy_adaptive_routing_cfg_0016.html).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to import direct routes in the Mix VPN instance to the public network routing table.
   
   
   ```
   [ip import-rib vpn-instance](cmdqueryname=ip+import-rib+vpn-instance) vpn-instance-name protocol direct
   ```
3. Configure route advertisement and reception for the public network instance.
   
   
   1. Start a BGP process.
      1. Enable BGP (with a specified local AS number) and enter the BGP view.
         ```
         [bgp](cmdqueryname=bgp) as-number
         ```
         
         Devices in the same group must belong to the same AS, meaning they must have the same AS number. Devices in different groups must belong to different ASs, meaning they must have different AS numbers.
         
         When global adaptive routing is enabled on a device, the AS number of the device ranges from 4200000000 to 4200000210. If a BGP AS number not in this range is configured, the configuration fails to be delivered.
      2. Configure a router ID for BGP.
         ```
         [router-id](cmdqueryname=router-id) ipv4-address
         ```
   2. Configure a BGP peer.
      1. Create a BGP peer group.
         ```
         [group](cmdqueryname=group) group-name { internal | external }
         ```
      2. Configure an IP address for the peer and the number of the AS where the peer resides.
         ```
         [peer](cmdqueryname=peer) { ipv4-address | group-name } as-number as-number
         ```
      3. Add the peer to the peer group.
         ```
         [peer](cmdqueryname=peer) ipv4-address group group-name
         ```
   3. Configure BGP to import routes.
      1. Enter the BGP-IPv4 unicast address family view.
         ```
         [ipv4-family unicast](cmdqueryname=ipv4-family+unicast)
         ```
      2. Configure BGP to import local routes.
         ```
         [network](cmdqueryname=network) ipv4-address [ mask | mask-length ]
         ```
         
         Ensure that only the routes of the compute nodes in the Mix VPN instance are imported. The routes of the public network instance cannot be imported to BGP routes.
   4. Set the maximum number of BGP equal-cost routes that can participate in load balancing globally.
      ```
      [maximum load-balancing](cmdqueryname=maximum+load-balancing) number
      ```
   5. Configure a BGP route reflector (RR).
      1. Set a cluster ID for the RR.
         ```
         [reflector cluster-id](cmdqueryname=reflector+cluster-id) { cluster-id-value | cluster-id-ipv4 }
         ```
         
         All devices on the network must be configured as RRs, and devices in the same group must have different RR cluster IDs.
      2. Enable the RR to modify the path attributes of BGP routes using an export policy.
         ```
         [reflect change-path-attribute](cmdqueryname=reflect+change-path-attribute)
         ```
      3. Configure an RR and its clients.
         ```
         [peer](cmdqueryname=peer) { ipv4-address | group-name } reflect-client
         ```
   6. Configure the device to filter the routes to be advertised to a specified peer or peer group.
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name } route-policy route-policy-name export
      ```
   7. Configure the device to filter the routes to be received from a specified peer or peer group.
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name } route-policy route-policy-name import
      ```
   8. Enable BGP Auto FRR for unicast routes.
      ```
      [auto-frr](cmdqueryname=auto-frr)
      ```
   9. Exit the BGP-IPv4 unicast address family view.
      ```
      [quit](cmdqueryname=quit)
      ```
   10. Commit the configuration.
       ```
       [commit](cmdqueryname=commit)
       ```
4. Configure route import, advertisement, and reception for the Non-min VPN instance.
   
   
   1. Enter the Non-min VPN instance IPv4 address family view.
      ```
      [ipv4-family vpn-instance](cmdqueryname=ipv4-family+vpn-instance) vpn-instance-name
      ```
   2. Configure the device to import BGP routes from the routing table of the public network instance to the routing table of the Non-min VPN instance.
      ```
      [import-rib](cmdqueryname=import-rib) public [ valid-route ] [ route-policy route-policy-name ]
      ```
   3. Set the maximum number of BGP equal-cost routes that can participate in load balancing globally.
      ```
      [maximum load-balancing](cmdqueryname=maximum+load-balancing) number
      ```
   4. Create a BGP peer group.
      ```
      [group](cmdqueryname=group) group-name internal
      ```
   5. Configure an IP address for the peer and the number of the AS where the peer resides.
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name } as-number as-number
      ```
   6. Add the peer to the peer group.
      ```
      [peer](cmdqueryname=peer) ipv4-address group group-name
      ```
   7. Configure the device to filter the routes to be advertised to a specified peer or peer group.
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name } route-policy route-policy-name export
      ```
   8. Configure the device to filter the routes to be received from a specified peer or peer group.
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name } route-policy route-policy-name import
      ```
   9. Exit the Non-min VPN instance IPv4 address family view.
      ```
      [quit](cmdqueryname=quit)
      ```
   10. Commit the configuration.
       ```
       [commit](cmdqueryname=commit)
       ```
5. Configure route import for the Mix VPN instance.
   
   
   1. Enter the Mix VPN instance IPv4 address family view.
      ```
      [ipv4-family vpn-instance](cmdqueryname=ipv4-family+vpn-instance) vpn-instance-name
      ```
   2. Configure BGP load balancing.
      1. Set the maximum number of BGP equal-cost routes that can participate in load balancing globally.
         ```
         [maximum load-balancing](cmdqueryname=maximum+load-balancing) number
         ```
      2. Disable the device from comparing the AS-Path attributes of the routes for load balancing.
         ```
         [load-balancing as-path-ignore](cmdqueryname=load-balancing+as-path-ignore)
         ```
      3. Disable the device from comparing the MED values of the routes for load balancing.
         ```
         [load-balancing med-ignore](cmdqueryname=load-balancing+med-ignore)
         ```
      4. Enable load balancing among EBGP and IBGP routes.
         ```
         [load-balancing eibgp](cmdqueryname=load-balancing+eibgp)
         ```
      5. Configure BGP adaptive routing to automatically adjust traffic forwarding paths based on network topology and traffic load changes.
         ```
         [load-balancing adaptive-routing](cmdqueryname=load-balancing+adaptive-routing)
         ```
   3. Configure the device to import BGP routes from the public network routing table to the routing table of the Mix VPN instance.
      ```
      [import-rib](cmdqueryname=import-rib) public [ valid-route ] [ route-policy route-policy-name ]
      ```
   4. Configure the device to import BGP routes from the routing table of the Non-min VPN instance to the routing table of the Mix VPN instance.
      ```
      [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name [ valid-route ] [ route-policy route-policy-name ]
      ```
   5. Exit the Mix VPN instance IPv4 address family view.
      ```
      [quit](cmdqueryname=quit)
      ```
   6. Exit the BGP view.
      ```
      [quit](cmdqueryname=quit)
      ```
   7. Commit the configuration.
      ```
      [commit](cmdqueryname=commit)
      ```
6. Configure a dynamic load balancing mode for ECMP.
   
   
   1. Enter the ECMP view.
      ```
      [load-balance ecmp](cmdqueryname=load-balance+ecmp)
      ```
   2. Enable the eligible ECMP dynamic load balancing mode.
      ```
      [ecmp mode](cmdqueryname=ecmp+mode) eligible flowlet-gap-time flowlet-gap-time
      ```
      
      In eligible dynamic load balancing mode, based on the flowlet, the device selects a member link with the lightest load to forward data packets. Data packets in the same flowlet are forwarded through the same link.
   3. Commit the configuration.
      ```
      [commit](cmdqueryname=commit)
      ```