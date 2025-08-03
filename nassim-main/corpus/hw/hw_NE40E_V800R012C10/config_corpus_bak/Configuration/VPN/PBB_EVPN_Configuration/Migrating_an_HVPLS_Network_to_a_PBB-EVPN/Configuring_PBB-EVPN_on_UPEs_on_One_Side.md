Configuring PBB-EVPN on UPEs on One Side
========================================

Configuring provider backbone bridge Ethernet VPN (PBB-EVPN) on user-end provider edges (UPEs) is the prerequisite for migrating a hierarchical virtual private LAN service (HVPLS) network to a PBB-EVPN.

#### Context

Configuring PBB-EVPN on a UPE includes configuring a B-EVPN instance and an I-EVPN instance, binding an interface to the I-EVPN instance, configuring an Ethernet segment identifier (ESI), configuring a PBB-EVPN source address, and configuring B-MAC addresses. B-MAC addresses can be configured in one or more of the following views:

* B-EVPN instance view
* I-EVPN instance view
* View of a PE interface connecting to a CE

B-MAC addresses configured in these views must be different. PBB preferentially uses the B-MAC addresses configured in the interface view for packet encapsulation. If no B-MAC addresses are configured in the interface view, PBB uses B-MAC addresses configured in the I-EVPN instance view instead. If no B-MAC addresses are configured in the I-EVPN instance view either, PBB uses B-MAC addresses configured in the B-EVPN instance view.

#### Procedure

* Configure a B-EVPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **b-evpn**
     
     
     
     A B-EVPN instance is created, and its view is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     A description is configured for the B-EVPN instance.
     
     Similar to a hostname or an interface description, a B-EVPN instance description helps you memorize the B-EVPN instance.
  4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     A route distinguisher (RD) is configured for the B-EVPN instance.
     
     
     
     A B-EVPN instance takes effect only after the RD is configured. The RDs of different EVPN instances on a UPE must be different.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After being configured, an RD cannot be modified, but can be deleted. After you delete the RD of a B-EVPN instance, the VPN targets of the B-EVPN instance will also be deleted.
  5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     VPN targets are configured for the B-EVPN instance.
     
     
     
     A VPN target is a BGP extended community attribute used to control the receiving and advertisement of EVPN routes. A maximum of eight VPN targets can be configured using a [**vpn-target**](cmdqueryname=vpn-target) command. To configure more VPN targets for an EVPN instance address family, run the [**vpn-target**](cmdqueryname=vpn-target) command several times.
  6. (Optional) Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *mac-address*
     
     
     
     A B-MAC address is configured in the B-EVPN instance view.
  7. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
     
     
     
     The B-EVPN instance is associated with a tunnel policy.
     
     
     
     This configuration enables UPEs to use TE tunnels to transmit data packets.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an I-EVPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **i-evpn**
     
     
     
     An I-EVPN instance is created, and its view is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     A description is configured for the I-EVPN instance.
     
     
     
     Similar to a hostname or an interface description, an I-EVPN instance description helps you memorize the I-EVPN instance.
  4. Run [**pbb i-tag**](cmdqueryname=pbb+i-tag) *i-tag*
     
     
     
     An I-SID is configured for the I-EVPN instance.
  5. Run [**pbb binding b-evpn**](cmdqueryname=pbb+binding+b-evpn) *vpn-instance-name*
     
     
     
     The I-EVPN instance is bound to the B-EVPN instance.
  6. (Optional) Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *mac-address*
     
     
     
     A B-MAC address is configured in the I-EVPN instance view.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind an interface to an I-EVPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the UPE interface connecting to a CE is displayed.
  3. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
     
     
     
     The interface is bound to the I-EVPN instance.
  4. (Optional) Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *mac-address*
     
     
     
     A B-MAC address is configured in the interface view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a PBB-EVPN source address.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn source-address**](cmdqueryname=evpn+source-address) *ip-address*
     
     
     
     A PBB-EVPN source address is configured.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an ESI.
  
  
  
  For configuration details, see [Configuring an ESI](dc_vrp_pbb-evpn_cfg_0006.html).