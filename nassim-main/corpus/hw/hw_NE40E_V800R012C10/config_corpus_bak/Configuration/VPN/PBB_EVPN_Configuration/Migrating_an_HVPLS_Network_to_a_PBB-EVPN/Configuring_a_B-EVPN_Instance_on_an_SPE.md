Configuring a B-EVPN Instance on an SPE
=======================================

A backbone Ethernet VPN (B-EVPN) instance is essential for a superstratum provider edge (SPE) in connecting to hierarchical virtual private LAN service (HVPLS) and provider backbone bridge Ethernet VPN (PBB-EVPN) networks.

#### Context

During migration from an HVPLS network to a PBB-EVPN, HVPLS and PBB-EVPN will coexist for some time. To transmit traffic between HVPLS and PBB-EVPN networks, SPEs must have B-EVPN instances configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn source-address**](cmdqueryname=evpn+source-address) *ip-address*
   
   
   
   A PBB-EVPN source address is configured.
3. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **b-evpn**
   
   
   
   A B-EVPN instance is created, and its view is displayed.
4. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   A description is configured for the B-EVPN instance.
   
   Similar to a hostname or an interface description, a B-EVPN instance description helps you memorize the B-EVPN instance.
5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   A route distinguisher (RD) is configured for the EVPN instance.
   
   
   
   A B-EVPN instance takes effect only after the RD is configured. The RDs of different EVPN instances on an SPE must be different.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After being configured, an RD cannot be modified, but can be deleted. After you delete the RD of an EVPN instance, the VPN targets of the EVPN instance will also be deleted.
6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   VPN targets are configured for the B-EVPN instance.
   
   
   
   A VPN target is a BGP extended community attribute used to control the receiving and advertisement of EVPN routes. A maximum of eight VPN targets can be configured using a [**vpn-target**](cmdqueryname=vpn-target) command. To configure more VPN targets for an EVPN instance address family, run the [**vpn-target**](cmdqueryname=vpn-target) command several times.
7. Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *mac-address*
   
   
   
   A B-MAC address is configured in the B-EVPN instance view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.