Configuring an OSPF Sham Link
=============================

This section describes how to configure an OSPF sham link so that traffic between sites of the same VPN in the same OSPF area is forwarded through the OSPF intra-area route over the MPLS VPN backbone network.

#### Usage Scenario

Generally, BGP peers use BGP extended community attributes to carry routing information over the BGP/MPLS IP VPN backbone network. PEs can use the routing information to exchange inter-area routes between PEs and CEs through OSPF. OSPF sham links are unnumbered P2P links between two PEs over an MPLS VPN backbone network. The source and destination IP addresses of each sham link are IP addresses with a 32-bit mask of loopback interfaces. The loopback interfaces must be bound to a VPN instance, and routes of the two IP addresses are advertised through BGP.

On the BGP/MPLS IP VPN backbone network, if an intra-area OSPF link exists between the network segment where the local CE resides and the network segment where the remote CE resides, the route over this intra-area OSPF link is an intra-area route and has a higher priority than the inter-area route over the BGP/MPLS IP VPN backbone network. In this case, VPN traffic is always forwarded through this intra-area route. To prevent this problem, you can set up an OSPF sham link between the PEs so that the route over the MPLS IP VPN backbone network becomes an OSPF intra-area route and ensure that this route is preferentially selected.


#### Pre-configuration Tasks

Before configuring an OSPF sham link, complete the following tasks:

* [Configure basic BGP/MPLS IP VPN functions](dc_vrp_mpls-l3vpn-v4_cfg_0154.html) and configure OSPF between each PE and its corresponding CE.
* Configure OSPF in the LAN of each CE.

#### Procedure

1. Configure endpoint IP addresses for a sham link. 
   
   
   
   Perform the following steps on PEs at both ends of the sham link:
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
      
      
      
      A loopback interface is created, and its view is displayed.
      
      Each VPN instance must have an endpoint IP address of a sham link, and the IP address is a loopback interface IP address with a 32-bit mask in the VPN address space of a PE. Sham links of the same OSPF process can share the same endpoint IP address. The endpoint IP addresses of sham links of different OSPF processes must be different.
   3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is bound to the loopback interface.
   4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the loopback interface.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The mask of the configured IP address must be 32 bits (255.255.255.255).
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Advertise routes of the sham link's endpoint IP addresses.
   
   
   
   Perform the following steps on PEs at both ends of the sham link:
   
   
   
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4 address family view is displayed.
   3. Run [**import-route**](cmdqueryname=import-route) **direct**
      
      
      
      Configure the device to import direct routes (routes of the sham link's endpoint IP addresses in this case) to BGP.
      
      Routes of the sham link's endpoint IP addresses are advertised as VPN IPv4 routes by BGP.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Ensure that routes of the sham link's endpoint IP addresses are not advertised to the remote PE through the VPN OSPF process.
      
      If routes of the sham link's endpoint IP addresses are advertised to the remote PE through the VPN OSPF process, the remote PE has two routes to the endpoint of the sham link. One of the routes is learned through the VPN OSPF process, and the other is learned through the MP-BGP connection. Because the OSPF route has a higher priority than the BGP route, the OSPF route is selected, causing a sham link establishment failure.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Create an OSPF sham link.
   
   
   
   Perform the following steps on PEs at both ends of the sham link:
   
   
   
   1. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ] [ **router-id** *router-id* | **vpn-instance** *vpn-instance-name* ] \*
      
      
      
      The OSPF multi-instance view is displayed.
   2. Run [**area**](cmdqueryname=area) *area-id*
      
      
      
      The OSPF area view is displayed.
   3. Run **[**sham-link**](cmdqueryname=sham-link)** *source-ip-address**destination-ip-address* [ **smart-discover** | **cost***cost-interval* | **dead***dead-interval* | **hello***hello-interval* | **retransmit***retransmit-interval* | **trans-delay***trans-delay-interval* | [ **simple** [ **plain***SPlainText* | **cipher***SCipherText* | *SCipherText* ] | { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain***MPlainText* | **cipher***MCipherText* | *MCipherText* } ] | **authentication-null** | **keychain***keychain-name* ] ] \*
      
      
      
      A sham link is configured.
      
      
      
      The authentication modes at both ends of the sham link must be the same. If packet authentication is configured, only the OSPF packets that pass the authentication are accepted; if the authentication fails, the OSPF neighbor relationship cannot be established.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      To ensure that VPN traffic is forwarded over the MPLS backbone network, ensure that the cost of the sham link is smaller than that of the OSPF route used to forward the traffic over the user network when configuring the sham link using the [**sham-link**](cmdqueryname=sham-link) command. In most cases, you need to change the cost of the interfaces on the user network to ensure that the cost of the OSPF route used to forward the traffic over the user network is greater than that of the sham link.
      
      It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

#### Verifying the Configuration

After configuring the OSPF sham link, run the following commands to check the configurations.

* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the VPN routing table on the PE.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the routing table on the CE.
* Run the [**tracert**](cmdqueryname=tracert) *host* command on the CE to check the nodes through which data is transmitted to the peer end.
* Run the [**display ospf**](cmdqueryname=display+ospf) *process-id* **sham-link** [ **area** *area-id* ] command to check the sham link status on the PE.
* Run the [**display ospf routing**](cmdqueryname=display+ospf+routing) command to check OSPF routes on the CE.