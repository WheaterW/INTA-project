Configuring a PBB-EVPN Instance
===============================

PEs use provider backbone bridge Ethernet VPN (PBB-EVPN) instances to interconnect private networks with the public network.

#### Context

PBB-EVPN instances interconnect private networks with the public network. A B-EVPN instance connects to the public network and manages EVPN routes received from other PEs. An I-EVPN instance connects to a private network through a PE interface connecting to a CE. After an I-EVPN instance receives a data packet from a CE, the I-EVPN instance encapsulates a PBB header into the packet.


#### Procedure

* Configure a B-EVPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **b-evpn**
     
     
     
     A B-EVPN instance is created, and its view is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     A description is configured for the B-EVPN instance.
     
     
     
     Similar to a hostname or interface description, a B-EVPN instance description helps you memorize the B-EVPN instance.
  4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is configured for the EVPN instance.
     
     
     
     A B-EVPN instance takes effect only after the RD is configured. The RDs of different EVPN instances on a PE must be different.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After being configured, an RD cannot be modified, but can be deleted. After you delete the RD of an EVPN instance, the VPN targets of the EVPN instance will also be deleted.
  5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     VPN targets are configured for the B-EVPN instance.
     
     
     
     VPN targets are BGP extended community attributes used to control the import and export of EVPN routes. A maximum of eight import VPN targets and eight export VPN targets can be configured each time the [**vpn-target**](cmdqueryname=vpn-target) command is run. To configure more VPN targets for an EVPN instance address family, run the [**vpn-target**](cmdqueryname=vpn-target) command several times.
  6. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
     
     
     
     The B-EVPN instance is associated with the specified tunnel policy.
     
     
     
     This configuration enables PEs to use TE tunnels to transmit data packets. Currently, B-EVPN instances can only be associated with tunnel binding policies.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an I-EVPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **i-evpn**
     
     
     
     An I-EVPN instance is created, and its view is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     A description is configured for the I-EVPN instance.
     
     
     
     Similar to a hostname or interface description, an I-EVPN instance description helps you memorize the I-EVPN instance.
  4. Run [**pbb i-tag**](cmdqueryname=pbb+i-tag) *i-tag*
     
     
     
     An I-SID is configured for the I-EVPN instance.
     
     
     
     After being configured, an I-SID cannot be modified, but can be deleted. After you delete the I-SID of an I-EVPN instance, the binding between this I-EVPN instance and a B-EVPN instance will also be deleted.
  5. Run [**pbb binding b-evpn**](cmdqueryname=pbb+binding+b-evpn) *vpn-instance-name*
     
     
     
     The I-EVPN instance is bound to the B-EVPN instance.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.