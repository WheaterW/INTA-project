Configuring PBB-EVPN B-MAC Addresses
====================================

Provider backbone bridge (PBB) precedes customer MAC (C-MAC) addresses with backbone MAC (B-MAC) addresses in packets to completely separate the user network from the carrier network.

#### Context

PBB is a technique defined in IEEE 802.1ah. By preceding C-MAC addresses with B-MAC addresses to separate the user network from the carrier network, PBB enhances network stability and minimizes the number of MAC address entries required on PEs. B-MAC addresses can be configured in one or more of the following views:

* B-EVPN instance view
* I-EVPN instance view
* View of a PE interface connecting to a CE

B-MAC addresses configured in these views must be different. PBB preferentially uses the B-MAC addresses configured in the interface view for packet encapsulation. If no B-MAC addresses are configured in the interface view, PBB uses B-MAC addresses configured in the I-EVPN instance view instead. If no B-MAC addresses are configured in the I-EVPN instance view either, PBB uses B-MAC addresses configured in the B-EVPN instance view.

If multiple PEs connect to the same CE, the PE interfaces connecting to this CE must use the same B-MAC addresses.


#### Procedure

* Configure a B-MAC address in the I-EVPN instance view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **i-evpn**
     
     
     
     The I-EVPN instance view is displayed.
  3. Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *mac-address*
     
     
     
     A B-MAC address is configured in the I-EVPN instance view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a B-MAC address in the B-EVPN instance view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **b-evpn**
     
     
     
     The B-EVPN instance view is displayed.
  3. Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *mac-address*
     
     
     
     A B-MAC address is configured in the B-EVPN instance view.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a B-MAC address in the interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the PE interface connecting to a CE is displayed.
  3. Run [**pbb backbone-source-mac**](cmdqueryname=pbb+backbone-source-mac) *mac-address*
     
     
     
     A B-MAC address is configured in the interface view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If this interface is an Eth-Trunk interface configured with the LACP mode, the system automatically generates a B-MAC address.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.