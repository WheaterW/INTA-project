Configuring Dynamic BFD to Monitor a BGP Tunnel
===============================================

BFD for BGP tunnel rapidly detects faults in E2E BGP tunnels.

#### Usage Scenario

On an IP/MPLS network transmitting VPN services, PEs establish a multi-segment MPLS tunnel between each other. Therefore VPN services are sent to multiple PEs. In this case, VPN service provision on PEs becomes complex, and the VPN service scalability decreases. As PEs establish BGP peer relationships, a routing policy can be used to assign MPLS labels for BGP routes so that an End-to-end (E2E) BGP tunnel can be established. The BGP tunnel consists of a primary BGP LSP and a backup BGP LSP. VPN services can travel along the E2E BGP tunnel, which simplifies service provision and improves VPN service scalability.

To rapidly detect faults in an E2E BGP tunnel, BFD for BGP tunnel is used. BFD for BGP tunnel establishes a dynamic BFD session, also called a BGP BFD session, which is bound to both the primary and backup BGP LSPs. If both BGP LSPs fail, the BGP BFD session detects the faults and triggers VPN FRR switching.


#### Pre-configuration Tasks

Before configuring dynamic BFD to monitor a BGP tunnel, configure basic MPLS functions.


[Enabling an MPLS Device to Dynamically Establish a BGP BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0038.html)

Before a dynamic BGP BFD session is established, the capability to dynamically establish BGP BFD sessions must be enabled on each MPLS device.

[Configuring a Policy for Dynamically Establishing a BGP BFD Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0039.html)

BGP BFD sessions can be dynamically established based on either host addresses or an IP address prefix list.

[(Optional) Adjusting BGP BFD Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0040.html)

You can adjust BGP BFD parameters, including the minimum interval at which BGP BFD packets are sent, the minimum interval at which BGP BFD packets are received, and the BGP BFD detection multiplier.

[Verifying the Configuration of Dynamic BFD to Monitor a BGP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0041.html)

After configuring a dynamic BFD session to monitor a BGP tunnel, you can view BGP BFD session information on the ingress of the BGP tunnel.