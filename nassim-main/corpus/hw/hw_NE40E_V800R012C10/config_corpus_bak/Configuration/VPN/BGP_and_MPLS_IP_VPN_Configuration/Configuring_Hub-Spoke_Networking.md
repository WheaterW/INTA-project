Configuring Hub-Spoke Networking
================================

On a VPN with hub-spoke networking, all users communicate with each other through a central access control device.

#### Usage Scenario

If it is required that an access control device be specified on the VPN and all users communicate through this access control device, you can deploy hub-spoke networking, so that all the data exchanged between spoke sites pass through the hub site.

Currently, the following hub-spoke networking schemes are supported:

* Hub-PE and Hub-CE dual-link access: On the network shown in [Figure 1](dc_vrp_mpls-l3vpn-v4_cfg_0021.html#EN-US_TASK_0172369267__fig_dc_vrp_mpls-l3vpn-v4_cfg_002101), site 1 and site 2 of VPN1 communicate through site 3. The Hub-CE connects to the Hub-PE over dual links. The Hub-PE has two VPN instances configured, **vpn\_in** and **vpn\_out**, which are bound to the corresponding access links. **vpn-in** receives and maintains all the VPNv4 routes advertised by all the Spoke-PEs. **vpn-out** maintains the routes of all hub and spoke sites and advertises those routes to all the Spoke-PEs.**Figure 1** Hub-CE accessing Hub-PE over dual links  
  ![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_002101.png)
* The Hub-CE accesses the Hub-PE through a single link. On the network shown in [Figure 2](dc_vrp_mpls-l3vpn-v4_cfg_0021.html#EN-US_TASK_0172369267__fig_dc_vrp_mpls-l3vpn-v4_cfg_002103), traffic between site 1 and site 2 of VPN1 needs to pass through site 3. The Hub-PE and Hub-CE are connected over a single link. The Hub-PE has only one VPN instance (**vpnhub**) configured, which is bound to the AC interface connected to the Hub-CE. Additionally, the [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go) command needs to be run in the VPN instance view to configure the Hub-PE to directly search the label mapping table for the outbound interface to forward data packets received from the Spoke-PEs.
  
  **Figure 2** Hub-CE accessing Hub-PE over a single link  
  ![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_002103.png)


#### Pre-configuration Tasks

Before configuring hub-spoke networking, complete the following tasks:

* Configure IGP on the MPLS backbone network to ensure IP connectivity on the backbone network.
* Configure MPLS both globally and per interface on each node of the backbone network and establish an LDP LSP between PEs.
* Configure an IP address for the interface connecting a CE to a PE.


[Configuring a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0022.html)

A VPN instance can be configured on a PE to manage VPN routes.

[Binding an Interface to a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0024.html)

By binding an interface to a VPN instance, you can change the interface to be a VPN interface. Then, packets entering this interface are forwarded according to the forwarding information of the VPN instance.

[Configuring Route Exchange Between a Hub-PE and a Spoke-PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0025.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between PEs.

[Configuring Route Exchange Between a PE and a CE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0026.html)

The routing protocol running between a PE and a CE can be BGP or an IGP. A static route (including the default route) can also run between them. You can choose any of them as required.

[Verifying the Hub and Spoke Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0027.html)

After configuring hub & spoke, check VPN routing information on the PE or CE.