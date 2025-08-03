Controlling OSPF Routing Information
====================================

You can control the advertising and receiving of OSPF routing information and import routes of other protocols.

#### Pre-configuration Tasks

Before controlling OSPF routing information, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).


[Configuring OSPF to Import External Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2040.html)

Importing the routes discovered by other routing protocols can enrich OSPF routing information.

[Configuring OSPF to Import a Default Route](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2041.html)

The default route is widely applied on the OSPF network to reduce routing entries in the routing table and filter specific routing information.

[Configuring Route Summarization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2006.html)

When a large-scale OSPF network is deployed, you can configure route summarization to reduce routing entries.

[Configuring OSPF to Filter LSAs in an Area](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2044.html)

Filtering LSAs in an area can prevent unnecessary LSA transmission. This reduces the size of the LSDB on the neighboring Router and speeds up network convergence.

[Configuring OSPF to Filter LSAs to Be Sent](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2051.html)

Filtering the LSAs to be sent on the local router can prevent unnecessary LSA transmission. This reduces the size of the LSDB on the neighboring device and speeds up network convergence.

[Configuring OSPF to Filter Received Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0044.html)

After a filtering policy is configured for the OSPF routes that need to be delivered to the routing management module, only the routes that match the policy will be added to the routing table.

[Configuring OSPF to Filter the Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0036_copy.html)

After a filtering policy is configured for routes imported by OSPF, only the routes that match the policy can be advertised.

[(Optional) Configuring OSPF to Discard Specified LSAs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0045.html)

You can configure a device to discard specified LSAs in an OSPF process.

[Configuring the Maximum Number of External Routes Supported by the OSPF LSDB](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2056.html)

You can set the maximum number of external routes in the LDSB to keep a proper number of external routes.

[Verifying the Configuration of OSPF Routing Information Control](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0047.html)

After OSPF routing information is controlled, you can check OSPF LSDB information.