Configuring Basic IS-IS Functions (IPv6)
========================================

This section describes how to configure basic IS-IS functions (IPv6) for communication between nodes on an IPv6 IS-IS network. The configuration procedure includes configuring the IS-IS process and IS-IS interface.

#### Usage Scenario

To deploy IS-IS on an IPv6 network, configure basic IS-IS functions to implement communication between different nodes on the network.

Other IS-IS functions can be configured only after basic IS-IS functions are configured.

Configuring basic IS-IS functions (IPv6) includes the following operations:

1. Create IPv6 IS-IS processes.
2. Configure IPv6 IS-IS interfaces.


#### Pre-configuration Tasks

Before configuring basic IS-IS functions (IPv6), complete the following tasks:

* Configure a link layer protocol.
* Assign an IPv6 address to each interface to ensure IP connectivity.
* Enable IPv6 forwarding in the system view.


[Creating an IS-IS Process (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1024.html)

Before configuring basic IPv6 IS-IS functions, create an IPv6 IS-IS process and then enable IPv6 IS-IS interfaces.

[Enabling an IS-IS Interface (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1025.html)

IS-IS can send Hello packets through an interface to establish neighbor relationships and flood LSPs only after IS-IS is enabled on the interface.

[(Optional) Configuring a Cost for IS-IS Interfaces (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1026.html)

Configuring IS-IS interface costs can control IS-IS route selection. Set interface costs based on network planning.

[(Optional) Configuring IS-IS Attributes for Interfaces of Different Network Types (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1027.html)

Different IS-IS attributes can be configured for different types of network interfaces.

[(Optional) Configuring IS-IS to Adjust the Flooding Rate (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1128.html)



[(Optional) Enabling LSP Fragment Extension on an IS-IS Device (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_2014.html)

If the LSP capacity is insufficient, newly imported routes and new TLVs fail to be added to LSP fragments. In this case, you can use LSP fragment extension to increase the LSP capacity, restoring the LSP space. When the LSP capacity is restored, the system automatically attempts to re-add these routes and TLVs to LSP fragments.

[Verifying the Basic IPv6 IS-IS Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1028.html)

After configuring basic IPv6 IS-IS features, check information about IS-IS neighbors, interfaces, and routes.