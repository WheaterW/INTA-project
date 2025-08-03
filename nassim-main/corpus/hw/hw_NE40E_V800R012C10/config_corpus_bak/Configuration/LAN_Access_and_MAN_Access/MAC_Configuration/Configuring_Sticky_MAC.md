Configuring Sticky MAC
======================

Configuring_Sticky_MAC

#### Context

On an EVPN and VPLS network, MAC spoofing attacks may occur. In a BD, sticky flags are set for all dynamic MAC address entries (MAC addresses with sticky flags are sticky MAC addresses). This prevents an interface from learning MAC addresses same as a sticky MAC address from other interfaces in the BD, thereby protecting the interface against attack packets sent from forged MAC addresses.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
3. Run either of the following commands:
   
   
   * To bind the interface to an EVPN instance, run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* command.
   * To bind the interface to a VSI, run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command.
4. Run [**sticky-mac enable**](cmdqueryname=sticky-mac+enable)
   
   
   
   Sticky MAC is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display mac-address sticky**](cmdqueryname=display+mac-address+sticky) [ **conflict** ] [ **bridge-domain** *bdId* ] [ **verbose** ] command to check whether sticky MAC is configured successfully.


#### Follow-up Procedure

* To configure an interface to discard packets sent from MAC addresses the same as sticky MAC addresses, run the [**mac-address source-check discard**](cmdqueryname=mac-address+source-check+discard) command.
* To change the sticky MAC address range, run the [**mac-address sticky-whitelist**](cmdqueryname=mac-address+sticky-whitelist) *mac-address* [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command.