Configuring OSPF Multi-Area Adjacency
=====================================

OSPF multi-area adjacency allows one link to be shared by multiple OSPF areas.

#### Usage Scenario

According to OSPF, intra-area paths take precedence over inter-area paths. If a link in an area is a high-speed link, routes in other areas cannot use the high-speed link for transmission at the same time. Instead, they can use only low-speed links. To solve this problem, run the [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) command to enable OSPF on the multi-area adjacency interface so that a path can be shared by multiple areas.

Among the OSPF features supported by an OSPF multi-area adjacency interface, some can be inherited from the main interface, whereas others need to be configured independently. For details, see [Table 1](#EN-US_TASK_0172365632__tab_dc_vrp_ospf_cfg_205801).

**Table 1** OSPF features supported by OSPF multi-area adjacency interfaces
| OSPF Feature | Description | Related Configuration Links |
| --- | --- | --- |
| BFD for OSPF | BFD for OSPF can be inherited from main interfaces, except for the configuration that disables BFD from an interface. This configuration needs to be configured independently. | [Disabling an OSPF Multi-Area Adjacency Interface from Creating BFD Sessions](dc_vrp_ospf_cfg_2066.html) |
| OSPF fast convergence | OSPF multi-area adjacency interfaces support OSPF fast convergence which needs to be configured independently for these interfaces and cannot be inherited from their main interfaces. | [Configuring Fast Convergence for a Multi-Area Adjacency Interface](dc_vrp_ospf_cfg_2062.html) |
| IGP-LDP synchronization | Multi-area adjacency interfaces support IGP-LDP synchronization, which needs to be configured independently for these interfaces. | [Configuring LDP-IGP Synchronization](dc_vrp_ldp-p2p_cfg_0046.html) |
| OSPF IP FRR | OSPF multi-area adjacency interfaces support OSPF IP FRR. OSPF IP FRR can be inherited from main interfaces, except for the configuration that disables FRR from a specified OSPF interface. This configuration needs to be configured independently for OSPF multi-area adjacency interfaces. | [Disabling OSPF IP FRR on an OSPF Multi-Area Adjacency Interface](dc_vrp_ospf_cfg_2067.html) |
| OSPF neighbor relationship flapping suppression | Multi-area adjacency interfaces support neighbor relationship flapping suppression, which needs to be configured independently for these interfaces. | [Configuring Neighbor Relationship Flapping Suppression on an OSPF Multi-Area Adjacency Interface](dc_vrp_ospf_cfg_2065.html) |
| OSPF flush LSA source tracing | OSPF multi-area adjacency interfaces support OSPF flush LSA source tracing which can be inherited from their main interfaces. | [Configuring OSPF Flush Source Tracing](dc_vrp_ospf_cfg_2070.html) |
| OSPF TE | Multi-area adjacency interfaces inherit TE information from their main interfaces. | [Configuring IGP TE (OSPF or IS-IS)](dc_vrp_te-p2p_cfg_0005.html) |



#### Pre-configuration Tasks

Before configuring OSPF multi-area adjacency, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).


[Enabling OSPF on a Multi-Area Adjacency Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2059.html)

Enabling OSPF on a multi-area adjacency interface is the prerequisite for configuring basic multi-area adjacency functions.

[Configuring a Cost for a Multi-Area Adjacency Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2060.html)

Configuring a cost for a multi-area adjacency interface can control route selection.

[Configuring an Authentication Mode for a Multi-Area Adjacency Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2061.html)

Configuring an authentication mode for a multi-area adjacency interface improves OSPF network security.

[Configuring Fast Convergence for a Multi-Area Adjacency Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2062.html)

Configuring fast convergence for a multi-area adjacency interface improves network performance.

[Configuring Neighbor Relationship Flapping Suppression on an OSPF Multi-Area Adjacency Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2065.html)

Neighbor relationship flapping suppression can be configured on an OSPF multi-area adjacency interface to delay OSPF neighbor relationship reestablishment or set the link cost to the maximum value in case of neighbor relationship flapping.

[Disabling an OSPF Multi-Area Adjacency Interface from Creating BFD Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2066.html)

After BFD for OSPF is configured, all interfaces on which neighbor relationships are in Full state in the OSPF process create BFD sessions. You can disable an interface from creating BFD sessions as required.

[Disabling OSPF IP FRR on an OSPF Multi-Area Adjacency Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2067.html)

If an interface runs key services, ensure that the backup path does not pass through this interface so that services will not be affected after FRR calculation.

[Configuring a Fallback Cost for an Eth-Trunk Multi-Area Adjacency Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2068.html)

Configuring a fallback cost for an Eth-Trunk multi-area adjacency interface helps control route selection.

[Maintaining OSPF on a Multi-Area Adjacency Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2069.html)



[Verifying the Configuration of OSPF Multi-Area Adjacency](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2063.html)

After configuring OSPF multi-area adjacency, verify the configuration.