(Optional) Customizing Characteristics of a Layer 2 Protocol for Transparent Transmission
=========================================================================================

(Optional) Customizing Characteristics of a Layer 2 Protocol for Transparent Transmission

#### Context

When non-standard Layer 2 protocol packets with a specified destination multicast MAC address from a user network need to be transparently transmitted on a backbone network, you can customize characteristics of the Layer 2 protocol on the PE. The characteristics include the protocol name, Ethernet encapsulation type, destination MAC address of packets, and multicast MAC address that replaces the destination MAC address of packets.

When customizing Layer 2 protocol characteristics, do not use the following multicast MAC addresses to replace the destination MAC addresses of Layer 2 protocol packets:

* Destination MAC addresses of BPDUs: 0180-C200-0000 to 0180-C200-002F
* MAC addresses of Smart Link packets: 010F-E200-0004
* Special multicast MAC addresses: 0100-0CCC-CCCC and 0100-0CCC-CCCD
* Common multicast MAC addresses that have been used on the device


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Customize characteristics of a Layer 2 protocol for transparent transmission.
   
   
   ```
   [l2protocol-tunnel user-defined-protocol](cmdqueryname=l2protocol-tunnel+user-defined-protocol) protocol-name protocol-mac protocol-mac [ encap-type { { ethernetii protocol-type protocol-type } | { llc dsap dsap-value ssap ssap-value } | { snap protocol-type protocol-type } } ] group-mac { group-mac | default-group-mac }
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```