Configuring Longest Match for Multicast Route Selection
=======================================================

Configuring Longest Match for Multicast Route Selection

#### Context

By default, a device selects routes according to the route preference during an RPF check. You can change the default RPF route selection rules by configuring longest match for multicast routes. With this configuration, when a device selects an RPF route, it first compares the mask matching lengths of routes and then compares route preferences.

The rules for selecting routes based on the longest match rule are as follows:

1. The multicast device preferentially selects the route whose destination address has the longest matching mask with the source address. For example, a host with address 192.168.1.1 needs multicast data from the multicast source with address 10.1.1.1. Two reachable routes to the multicast source are found after a lookup of the multicast static routing table and unicast routing table. Their destination subnets are 10.1.0.0/16 and 10.1.1.0/24, respectively. Based on the longest match rule for route selection, the route to subnet 10.1.1.0/24 is chosen for multicast data forwarding.
2. If the mask matching lengths are the same, the route with a higher preference is selected for multicast data forwarding.
3. If the mask matching lengths and the route preferences are the same, a route is selected in the following order of preference for multicast data forwarding: multicast static route > unicast route.
4. If all the preceding conditions cannot determine a forwarding path for multicast data (multiple equal-cost routes exist), the route with the largest next-hop IP address is selected for multicast data forwarding.

#### Procedure

* Public network instance
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable the multicast function.
     
     
     ```
     [multicast routing-enable](cmdqueryname=multicast+routing-enable)
     ```
  3. Configure longest-match route selection for the public network instance.
     
     
     ```
     [multicast longest-match](cmdqueryname=multicast+longest-match)
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* VPN instance
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VPN instance view.
     
     
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
  3. Enable the IPv4 address family for the VPN instance and enter the VPN instance IPv4 address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
  4. Set an RD for the VPN instance IPv4 address family.
     
     
     ```
     [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
     ```
     
     Only after an RD is configured for this family can other configurations be performed for the VPN instance IPv4 address family.
  5. Enable the multicast function.
     
     
     ```
     [multicast routing-enable](cmdqueryname=multicast+routing-enable)
     ```
  6. Configure longest-match route selection for the VPN instance.
     
     
     ```
     [multicast longest-match](cmdqueryname=multicast+longest-match)
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     VPN instance-related configurations apply only to provider edges (PEs). To configure longest match for multicast routes in a VPN instance on a PE, you must perform the configuration in the VPN instance. For other cases, configurations need to be performed in the public network instance.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] [ **verbose** ] command to check the RPF route information of a specific multicast source.