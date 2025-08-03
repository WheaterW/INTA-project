Configuring Static ARP/IPv6 Neighbors/MAC Address Entries and Limiting MAC Address Learning
===========================================================================================

Configuring Static ARP/IPv6 Neighbors/MAC Address Entries and Limiting MAC Address Learning

#### Prerequisites

Before configuring static ARP/IPv6 neighbors/MAC address entries and limiting MAC address learning, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1039.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](dc_vrp_vxlan_cfg_1066.html)


#### Context

You can improve the VXLAN network security using the following methods:

* Manually configure and maintain static ARP entries on Layer 3 VXLAN gateways. Static ARP entries can be neither aged nor overwritten by dynamic ARP entries. If a static ARP entry is configured on a device, the device can communicate with a peer device with a specified IP address only if the peer's MAC address is the bound one. Network attackers cannot modify the mapping between the IP and MAC addresses, improving communication security between the two devices.
* If a Layer 3 gateway is not enabled to send ND protocol packets, manually configure a static IPv6 neighbor and specify the mapping between IPv6 and MAC addresses to prevent ND packet attacks.
* Configure static MAC address entries to reduce broadcast traffic and prevent unauthorized data access from bogus users. In this case, when a source NVE on a VXLAN tunnel receives a BUM packet, the local VTEP sends a copy of the BUM packet only to the VTEPs in the ingress replication list.
* Configure the maximum number of MAC addresses that a device can learn to limit the number of access users and defend against attacks on MAC address tables. If the device has learned the maximum, no more addresses can be learned. However, you can also configure the device to discard packets after learning the maximum allowed number of MAC addresses, improving network security.
* Disable MAC address learning for a BD if a Layer 3 VXLAN gateway does not need to learn MAC addresses of packets in the BD, reducing the number of MAC address entries. You can also disable MAC address learning on Layer 2 gateways after the VXLAN network topology becomes stable and MAC address learning is complete.

The following operations can be performed on a Layer 2 gateway:

* Configure static MAC address entries.
* Limit MAC address learning.
* Disable MAC address learning.

The following operations can be performed on a Layer 3 gateway:

* Configure static ARP address entries.
* Configure static IPv6 neighbors on the VXLAN tunnel side.
* Configure static IPv6 neighbors for Layer 2 sub-interfaces.
* Disable MAC address learning.

![](../public_sys-resources/note_3.0-en-us.png) 

* Static ARP entries can be configured only on IPv4 overlay networks.
* Static IPv6 neighbors can be configured only on IPv6 overlay networks.


#### Procedure

* Configure a static ARP entry.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a static ARP entry on the VXLAN tunnel side.
     
     
     ```
     [arp static](cmdqueryname=arp+static) ip-address mac-address vni vni-id source-ip source-ip peer-ip peer-ip
     ```
     By default, no static ARP entry is configured on the VXLAN tunnel side.![](../public_sys-resources/note_3.0-en-us.png) 
     + *ip-address* must belong to the same network segment as the IP address of the Layer 3 gateway.
     + Static ARP entries can be configured on the static VXLAN tunnel side only.
  3. If a VXLAN service access point is a Layer 2 sub-interface, mapping between IP and MAC addresses can be configured on the user access side.
     
     
     
     Untagged encapsulation type:
     
     ```
     [arp static](cmdqueryname=arp+static) ip-address mac-address interface interface-type interface-number
     ```
     
     Dot1q encapsulation type:
     
     ```
     [arp static](cmdqueryname=arp+static) ip-address mac-address { vlan vlan-id [ interface interface-type interface-number ] | interface interface-type interface-number }
     ```
     
     **interface** *interface-type* *interface-number* must specify a Layer 2 sub-interface. **vlan** *vlan-id* must be the same as the value specified in [**encapsulation**](cmdqueryname=encapsulation) **dot1q** [ **vid** *vid* ].
     
     QinQ encapsulation type:
     
     ```
     [arp static](cmdqueryname=arp+static) ip-address mac-address vlan pevlan-id cevlan cevlan-id interface interface-type interface-number
     ```
     
     **interface** *interface-type* *interface-number* must specify a Layer 2 sub-interface. *pevlan-id* and *cevlan-id* must be the same as the values specified in [**encapsulation**](cmdqueryname=encapsulation) **qinq** [ **vid** *pe-vid* **ce-vid** *ce-vid* ].
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a static IPv6 neighbor on the VXLAN tunnel side.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VBDIF interface view.
     
     
     ```
     [interface vbdif](cmdqueryname=interface+vbdif) bd-id
     ```
  3. Configure a static IPv6 neighbor.
     
     
     ```
     [ipv6 neighbor](cmdqueryname=ipv6+neighbor) ipv6-address mac-address vni vni-id source-ip source-ip peer-ip peer-ip-address
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     Static IPv6 neighbor relationships can be configured on the static VXLAN tunnel side only.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a static IPv6 neighbor for a Layer 2 sub-interface.
  
  
  
  If a Layer 2 sub-interface functions as a service access point on the Layer 3 gateway, a static IPv6 neighbor can be configured for the Layer 2 sub-interface, which must be specified by *interface-type* *interface-number*.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VBDIF interface view.
     
     
     ```
     [interface vbdif](cmdqueryname=interface+vbdif) bd-id
     ```
  3. Configure a static IPv6 neighbor for the Layer 2 sub-interface. Select the configuration command depending on its encapsulation type.
     
     
     
     Untagged encapsulation type:
     
     ```
     [ipv6 neighbor](cmdqueryname=ipv6+neighbor) ipv6-address mac-address interface-type interface-number
     ```
     
     Dot1q encapsulation type:
     
     ```
     [ipv6 neighbor](cmdqueryname=ipv6+neighbor) ipv6-address mac-address vlan vlan-id interface-type interface-number
     ```
     
     **vlan** *vlan-id* must be the same as the value specified in [**encapsulation**](cmdqueryname=encapsulation) **dot1q** [ **vid** *vid* ].
     
     QinQ encapsulation type:
     
     ```
     [ipv6 neighbor](cmdqueryname=ipv6+neighbor) ipv6-address mac-address vlan vlan-id cevlan ce-vid interface-type interface-number
     ```
     
     *vlan-id* and *ce-vid* must be the same as the values specified in [**encapsulation**](cmdqueryname=encapsulation) **qinq** [ **vid** *pe-vid* **ce-vid** *ce-vid* ].
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a static MAC address entry.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a static MAC address entry.
     
     
     
     In IPv4 scenarios:
     
     
     
     ```
     [mac-address static](cmdqueryname=mac-address+static) mac-address bridge-domain bd-id source source-ip-address peer peer-ip vni vni-id
     ```
     
     In IPv6 scenarios:
     
     ```
     [mac-address static](cmdqueryname=mac-address+static) mac-address bridge-domain bd-id source-ipv6 source-ipv6-address peer-ipv6 peer-ipv6 vni vni-id
     ```
     
     By default, no static MAC address entry is configured.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Limit MAC address learning.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. MAC address learning limit rules can be configured in the following modes:
     
     
     + Set the maximum number of MAC addresses that can be learned in a BD.
       ```
       [bridge-domain](cmdqueryname=bridge-domain) bd-id
       [mac-address limit](cmdqueryname=mac-address+limit) { action { discard | forward } | maximum max | alarm { disable | enable } } *
       ```
     + Set the maximum number of MAC addresses that can be learned on a Layer 2 sub-interface.
       ```
       
       [interface](cmdqueryname=interface) interface-type interface-number.subnum mode l2
       [mac-address limit](cmdqueryname=mac-address+limit) { action { discard | forward } | maximum max | alarm { disable | enable } } *
       ```
       ![](../public_sys-resources/note_3.0-en-us.png) 
       
       Before creating a Layer 2 sub-interface, ensure that its Layer 2 main interface does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If this configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete it.
     + Set the maximum number of MAC addresses that can be learned from a remote VTEP.
       ```
       [interface](cmdqueryname=interface) nve nve-number
       [peer](cmdqueryname=peer) ip-address mac-address limit { action { discard | forward } | maximum max | alarm { disable | enable } } *
       ```
       
       If the source VTEP address of a VXLAN tunnel is configured in a BD instance, set the maximum number of MAC addresses that can be learned from the remote VTEP as follows:
       
       ```
       [interface](cmdqueryname=interface) nve nve-number
       [source](cmdqueryname=source) ip-address [peer](cmdqueryname=peer) ip-address mac-address limit { action { discard | forward } | maximum max | alarm { disable | enable } } *
       ```
       
       After this step is performed, the device limits the maximum number of MAC addresses that can be learned from the specified remote VTEP of a VXLAN tunnel, protecting the device against MAC address attacks and limiting the number of access users. When the maximum number is reached, the device can discard subsequent packets and report an alarm if the alarming function is configured.
       
       ![](../public_sys-resources/note_3.0-en-us.png) 
       
       This configuration can be performed only for remote VTEPs of static VXLAN tunnels.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Disable MAC address learning.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BD view.
     
     
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     ```
  3. Disable MAC address learning.
     
     
     ```
     [mac-address learning disable](cmdqueryname=mac-address+learning+disable)
     ```
     
     By default, MAC address learning is enabled for a BD.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display arp**](cmdqueryname=display+arp) [ **network** *network-address* [ *network-mask* | *mask-length* ] ] **static** command to check static ARP entries.
* Run the [**display ipv6 neighbors brief**](cmdqueryname=display+ipv6+neighbors+brief) command to check static IPv6 neighbor information.
* Run the [**display mac-address**](cmdqueryname=display+mac-address) **static** **bridge-domain** *bd-id* command to check static MAC address entries in a BD.
* Run the [**display mac-address limit bridge-domain**](cmdqueryname=display+mac-address+limit+bridge-domain) *bd-id* command to check dynamic MAC address learning limiting configurations of a BD.
* Run the [**display mac-address limit**](cmdqueryname=display+mac-address+limit) **nve** *nve-number* [**peer**](cmdqueryname=peer) *ip-address* command to check the MAC address learning limit rule configured on an NVE interface for a specified remote VTEP.