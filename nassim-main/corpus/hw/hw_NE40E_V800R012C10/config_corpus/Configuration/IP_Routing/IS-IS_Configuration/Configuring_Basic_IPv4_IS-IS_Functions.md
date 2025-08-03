Configuring Basic IPv4 IS-IS Functions
======================================

This section describes how to configure basic IPv4 IS-IS functions.

#### Usage Scenario

To deploy IS-IS on an IPv4 network, configure basic IS-IS functions for communication between different nodes on the network.

Other IS-IS functions can be configured only after basic IS-IS functions are configured.

Configuring basic IPv4 IS-IS functions includes the following operations:

1. Create IPv4 IS-IS processes.
2. Configure IPv4 IS-IS interfaces.


#### Pre-configuration Tasks

Before configuring basic IPv4 IS-IS functions, complete the following tasks:

* Configure a link layer protocol.
* Assign an IP address to each interface to ensure IP connectivity.


[Creating an IPv4 IS-IS Process](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1001.html)

To configure basic IPv4 IS-IS functions, first create an IPv4 IS-IS process and enable IPv4 IS-IS interfaces.

[Configuring an IPv4 IS-IS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1002.html)

IS-IS can send Hello packets through an interface to establish neighbor relationships and flood LSPs only after IS-IS is enabled on the interface.

[(Optional) Configuring a Cost for IS-IS Interfaces (IPv4)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1003.html)

Configuring IS-IS interface costs can control IS-IS route selection. Set interface costs based on network planning.

[(Optional) Configuring IPv4 IS-IS Attributes on Networks of Different Types](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1004.html)

Different IS-IS attributes can be configured for different types of network interfaces.

[(Optional) Configuring IS-IS to Adjust the Flooding Rate (IPv4)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1215.html)



[(Optional) Enabling LSP Fragment Extension on an IS-IS Device (IPv4)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_2013.html)

If the LSP capacity is insufficient, newly imported routes and new TLVs fail to be added to LSP fragments. In this case, you can use LSP fragment extension to increase the LSP capacity, restoring the LSP space. When the LSP capacity is restored, the system automatically attempts to re-add these routes and TLVs to LSP fragments.

[(Optional) Enabling a Device to Encapsulate Only One Interface IP Address in IS-IS LSPs (IPv4)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_2015.html)

To implement interworking between Huawei and non-Huawei devices, you need to enable the type-132 TLV in LSPs to carry the IP address of only one IS-IS interface on the Huawei device.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1005.html)

After configuring basic IPv4 IS-IS functions, check information about IS-IS neighbors, interfaces, and routes.