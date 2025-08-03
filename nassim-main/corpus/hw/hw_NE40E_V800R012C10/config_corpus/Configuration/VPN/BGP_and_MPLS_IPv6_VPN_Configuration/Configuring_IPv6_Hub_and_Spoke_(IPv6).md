Configuring IPv6 Hub and Spoke (IPv6)
=====================================

In the hub-spoke networking, an access control device is specified in the VPN, and users communicate with each other through the access control device.

#### Usage Scenario

If it is required that an access control device be specified in the VPN and all the users access the VPN through this access control device, you can deploy the hub-spoke networking so that all the data exchanged between Spoke sites flow through the Hub site.

On the network shown in [Figure 1](dc_vrp_mpls-l3vpn-v6_cfg_2063.html#EN-US_TASK_0172369611__fig_dc_vrp_mpls-l3vpn-v6_cfg_206301), Site 1 and Site 2 in VPN1 communicate with each other through Site 3. In such a scenario, you can deploy an access control device at Site 3 to monitor the communication between Site 1 and Site 2.

**Figure 1** Diagram of the hub-spoke networking
  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_206301.png)

#### Pre-configuration Tasks

Before configuring Hub and Spoke, complete the following tasks:

* Configure an IGP on the MPLS backbone network to implement IP interworking.
* Configure the basic MPLS capability and establish an LDP LSP between PEs.
* Configure an IP address for the interface connecting the CE to the PE.


[Configuring a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2064.html)

A VPN instance can be configured on a PE to manage VPN routes.

[Configuring Routing Attributes for a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2065.html)

In the networking of Hub and Spoke, you can configure VPN targets on the Hub-PE and Spoke PEs to control the advertisement of VPN routes. The import VPN target configured on the Hub-PE must contain the export VPN targets configured on all the Spoke-PEs. The export VPN target list configured on the Hub-PE must contain the import VPN targets configured on all the Spoke-PEs.

[Binding an Interface to a VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2066.html)

By binding an interface to a VPN instance, you can change the interface to a VPN interface. Then, packets entering this interface are forwarded according to the forwarding information of the VPN instance.

[Configuring Route Exchange Between a Hub-PE and a Spoke-PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2067.html)

By importing extended community attributes to BGP, MP-IBGP can advertise VPNv6 routes between PEs.

[Configuring Route Exchange Between a PE and a CE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2068.html)

The routing protocol running between a PE and a CE can be BGP or IGP. A static route (including the default route) can also run between them. You can choose any of them as required.

[Verifying the Configuration of Hub and Spoke (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2069.html)

After configuring hub & spoke, check VPN routing information on the PE or CE.