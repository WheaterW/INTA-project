Configuring the EVC Model to Carry L2VPN Services
=================================================

This section describes how to use the EVC model to carry L2VPN services to reduce enterprise costs.

#### Usage Scenario

The traditional service model supported by the NE40E uses either VPLS or VPWS to access a carrier network. If VPLS is used, common sub-interfaces (VLAN type), dot1q VLAN tag termination sub-interfaces, or QinQ VLAN tag termination sub-interfaces must be created on the user-side interfaces of PEs and bound to different VSIs. If Layer 2 devices use different access modes on a network, network planning and management are complex and difficult. To resolve this issue and reduce enterprise costs, configure the EVC model to carry Layer 2 services.

#### Pre-configuration Tasks

Before configuring the EVC model to carry L2VPN services, complete the following tasks:

1. Configure a routing protocol to ensure Layer 3 connectivity.
2. Configure basic Multiprotocol Label Switching (MPLS) functions, enable MPLS Label Distribution Protocol (LDP), and establish LDP Label Switched Paths (LSPs).
3. Enable MPLS L2VPN, and enable L2VPN globally.
4. Establish the EVC model. For details, see [Establishing the EVC Model](dc_vrp_evc_cfg_0003.html).


[Configuring the EVC Model to Carry VPLS Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0031.html)

This section describes how to use the EVC model to carry virtual private LAN service (VPLS) services to reduce enterprise costs.

[Configuring the EVC Model to Carry VPWS Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0032.html)

This section describes how to use the EVC model to carry VPWS services. This implementation can facilitate network planning and management, thereby cutting down enterprise costs.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0033.html)

After configuring the EVC model to carry L2VPN services, verify the configuration.