Configuring NetStream Flexible Flow Statistics Export
=====================================================

Configuring NetStream Flexible Flow Statistics Export

#### Context

Configuring NetStream flexible flow statistics export involves the following two parts:

* Configure the source address, destination address, and destination UDP number of the exported NetStream packets carrying flow statistics. If no source address is specified, NetStream packets will not be exported. If no destination address or destination UDP port number is specified, exported NetStream packets will not reach the NetStream server.
* Configure the version of exported NetStream packets, as well as the interface index length and field value format in the packets, so that the NetStream server can successfully parse NetStream packets.![](public_sys-resources/note_3.0-en-us.png) 
  
  NetStream flexible flow statistics must be exported in V9 format, which does not need to be configured.

#### Procedure

* Configure IPv4 flexible flow statistics export.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a source address of the exported packets carrying IPv4 flexible flow statistics. (The source IPv6 address of the exported packets cannot be configured on the CE6885-LL (low latency mode).)
     
     
     ```
     [netstream export ip source](cmdqueryname=netstream+export+ip+source) { ip-address | ipv6 ipv6-address }
     ```
     
     By default, no source address is configured for the exported packets carrying IPv4 flexible flow statistics. Ensure that there are reachable routes between the source address and destination address (NSC's address) of the exported packets.
     
     A maximum of two source addresses can be specified: one IPv4 address and one IPv6 address. Only one source IPv4 address can be configured on the CE6885-LL (low latency mode).
  3. Configure a destination address and a destination UDP port number of the exported packets carrying IPv4 flexible flow statistics. (The destination IPv6 address of the exported packets cannot be configured on the CE6885-LL (low latency mode).)
     
     
     ```
     [netstream export ip host](cmdqueryname=netstream+export+ip+host) { ip-address | ipv6 ipv6-address } port [ vpn-instance vpn-instance-name ] dscp dscp-value
     ```
     
     By default, no destination address or destination UDP port number is configured for the exported packets carrying IPv4 flexible flow statistics.
  4. (Optional) Set the interval at which the template for exporting IPv4 flexible flow statistics in V9 format is updated.
     
     
     ```
     [netstream export ip template timeout-rate](cmdqueryname=netstream+export+ip+template+timeout-rate) timeout-interval
     ```
     
     By default, the template is updated every minute.
  5. Configure the length of interface indexes contained in the exported packets carrying IPv4 flow statistics.
     
     
     ```
     [netstream export ip index-switch](cmdqueryname=netstream+export+ip+index-switch) { 16 | 32 }
     ```
     
     By default, 32-bit interface indexes are contained in the exported packets carrying IPv4 flow statistics.
  6. (Optional) Configure the **IN\_BYTES** field value in exported NetStream packets to include the Ethernet header and CRC length.
     
     
     ```
     [netstream export packet-len ethernet-crc](cmdqueryname=netstream+export+packet-len+ethernet-crc)
     ```
     
     
     
     By default, the **IN\_BYTES** field value in exported NetStream packets is the value of the **len** field in the IP header.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure IPv6 flexible flow statistics export.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a source address of the exported packets carrying IPv6 flexible flow statistics. (The source IPv6 address of the exported packets cannot be configured on the CE6885-LL (low latency mode).)
     
     
     ```
     [netstream export ipv6 source](cmdqueryname=netstream+export+ipv6+source) { ip-address | ipv6 ipv6-address }
     ```
     
     By default, no source address is configured for the exported packets carrying IPv6 flexible flow statistics. Ensure that there are reachable routes between the source address and destination address (NSC's address) of the exported packets.
     
     A maximum of two source addresses can be specified: one IPv4 address and one IPv6 address. Only one source IPv4 address can be configured on the CE6885-LL (low latency mode).
  3. Configure a destination address and a destination UDP port number of the exported packets carrying IPv6 flexible flow statistics. (The destination IPv6 address of the exported packets cannot be configured on the CE6885-LL (low latency mode).)
     
     
     ```
     [netstream export ipv6 host](cmdqueryname=netstream+export+ipv6+host) { ip-address | ipv6 ipv6-address } port [ vpn-instance vpn-instance-name ] dscp dscp-value
     ```
     
     By default, no destination address or destination UDP port number is configured for the exported packets carrying IPv6 flexible flow statistics.
  4. (Optional) Set the interval at which the template for exporting IPv6 flexible flow statistics in V9 format is updated.
     
     
     ```
     [netstream export ipv6 template timeout-rate](cmdqueryname=netstream+export+ipv6+template+timeout-rate) timeout-interval
     ```
     
     By default, the template is updated every minute.
  5. Configure the length of interface indexes contained in the exported packets carrying IPv6 flow statistics.
     
     
     ```
     [netstream export ipv6 index-switch](cmdqueryname=netstream+export+ipv6+index-switch) { 16 | 32 }
     ```
     
     By default, 32-bit interface indexes are contained in the exported packets carrying IPv6 flow statistics.
  6. (Optional) Configure the **IN\_BYTES** field value in exported NetStream packets to include the Ethernet header and CRC length.
     
     
     ```
     [netstream export packet-len ethernet-crc](cmdqueryname=netstream+export+packet-len+ethernet-crc)
     ```
     
     
     
     By default, the **IN\_BYTES** field value in exported NetStream packets is the value of the **len** field in the IP header.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure VXLAN flexible flow statistics export.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a source address of the exported packets carrying VXLAN flexible flow statistics. (The source IPv6 address of the exported packets cannot be configured on the CE6885-LL (low latency mode).)
     
     
     ```
     [netstream export vxlan inner-ip source](cmdqueryname=netstream+export+vxlan+inner-ip+source) { ip-address | ipv6 ipv6-address }
     ```
     
     By default, no source address is configured for the exported packets carrying VXLAN flexible flow statistics. Ensure that there are reachable routes between the source address and destination address (NSC's address) of the exported packets.
     
     A maximum of two source addresses can be specified: one IPv4 address and one IPv6 address. Only one source IPv4 address can be configured on the CE6885-LL (low latency mode).
  3. Configure a destination address and a destination UDP port number of the exported packets carrying VXLAN flexible flow statistics. (The destination IPv6 address of the exported packets cannot be configured on the CE6885-LL (low latency mode).)
     
     
     ```
     [netstream export vxlan inner-ip host](cmdqueryname=netstream+export+vxlan+inner-ip+host) { ip-address | ipv6 ipv6-address } port [ vpn-instance vpn-instance-name ] dscp dscp-value
     ```
     
     By default, no destination address or destination UDP port number is configured for the exported packets carrying VXLAN flexible flow statistics.
  4. (Optional) Set the interval at which the template for exporting VXLAN flexible flow statistics in V9 format is updated.
     
     
     ```
     [netstream export vxlan inner-ip template timeout-rate](cmdqueryname=netstream+export+vxlan+inner-ip+template+timeout-rate) timeout-interval
     ```
     
     By default, the template is updated every minute.
  5. Configure the length of interface indexes contained in the exported packets carrying VXLAN flow statistics.
     
     
     ```
     [netstream export vxlan inner-ip index-switch](cmdqueryname=netstream+export+vxlan+inner-ip+index-switch) { 16 | 32 }
     ```
     
     By default, 32-bit interface indexes are contained in the exported packets carrying VXLAN flow statistics.
  6. (Optional) Configure the **IN\_BYTES** field value in exported NetStream packets to include the Ethernet header and CRC length.
     
     
     ```
     [netstream export packet-len ethernet-crc](cmdqueryname=netstream+export+packet-len+ethernet-crc)
     ```
     
     
     
     By default, the **IN\_BYTES** field value in exported NetStream packets is the value of the **len** field in the IP header.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```