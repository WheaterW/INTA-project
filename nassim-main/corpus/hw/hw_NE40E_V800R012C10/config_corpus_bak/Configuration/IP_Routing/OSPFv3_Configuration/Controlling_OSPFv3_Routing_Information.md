Controlling OSPFv3 Routing Information
======================================

This section describes how to control OSPFv3 routing information.

#### Usage Scenario

Through the configuration in this section, you can control the advertising and receiving of OSPFv3 routing information and configure OSPFv3 to import external routes.

You can control the following types of routes:

* Routes outside the local OSPFv3 area
  
  This function can be configured on any Router that runs OSPFv3. For example, you can enable the Router to filter received routes and set the maximum number of equal-cost routes.
* Routes inside the local OSPFv3 area
  
  This function can be configured only on ABRs. For example, when an ABR has multiple routes to a destination in the local area, you can configure the ABR to summarize the routes and send only a summary LSA to the backbone area.

#### Pre-configuration Tasks

Before controlling OSPFv3 routing information, complete the following tasks:

* Enable IPv6.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).


[Configuring OSPFv3 to Import External Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2026.html)

Importing the routes discovered by other routing protocols can enrich OSPFv3 routing information.

[Configuring OSPFv3 to Advertise Default Routes to OSPFv3 Areas](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2027.html)

You can configure OSPFv3 to advertise default routes to OSPFv3 areas. Only the routes that meet the conditions can be converted into LSAs and advertised.

[Configuring OSPFv3 to Filter Received Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2028.html)

After receiving Link State Advertisements (LSAs), OSPFv3 determines whether to add the calculated routes to the local routing table based on a filtering policy.

[Configuring OSPFv3 to Filter the Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2029.html)

After filtering conditions are set for imported routes, only the routes that pass the filtering can be advertised.

[Configuring OSPFv3 to Filter LSAs in an Area](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2078.html)

Filtering LSAs in an area can prevent unnecessary LSA transmission. This reduces the size of the LSDB on the neighboring device and speeds up network convergence.

[(Optional) Configuring OSPFv3 to Discard Specified LSAs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_20790.html)

You can configure a device to discard specified LSAs in an OSPFv3 process.

[Configuring OSPFv3 Route Summarization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2089.html)

Routes with the same IPv6 prefix can be summarized into one route. On a large-scale OSPFv3 network, route lookup may slow down because of the large size of the routing table. To reduce the routing table size and simplify management, configure route summarization. With route summarization, if a link connected to a device within an IPv6 address range that has been summarized alternates between Up and Down, the link status change is not advertised to the devices beyond the IPv6 address range. This prevents route flapping and improves network stability.

[Verifying the Configuration of OSPFv3 Routing Information Control](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2030.html)

After controlling OSPFv3 routing information, verify the OSPFv3 LSDB.