Configuring Rules for Obtaining Packet Headers
==============================================

In case of a user access failure, you can configure rules for obtaining packet headers to locate and diagnose the fault.

#### Context

For the configuration of packet header obtaining rules, select one or more of the following steps 2 to 5 as needed.

Perform the following steps on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**capture-packet access condition**](cmdqueryname=capture-packet+access+condition) { **pppoe** | **dhcp** | **dhcpv6** | **nd** | **ip** | **arp** } **mac-address** *mac-address* **vlan-tags** *vlan-tags* [ **inbound** | **outbound** ] [ **time-out** *time-out-value* ]
   
   
   
   The device is enabled to obtain PPPoE, DHCP, DHCPv6, IP, or ARP packets based on a specified MAC address and VLAN tags.
3. Run [**capture-packet access condition**](cmdqueryname=capture-packet+access+condition) { **pppoe** | **dhcp** | **dhcpv6** | **nd** | **ip** | **arp** } { **interface** { *interface-type* *interface-num* | *interface-name* } [ **pevlan** *pevlan-id* [ **cevlan** *cevlan-id* ] ] } [ **inbound** | **outbound** ] [ **time-out** *time-out-value* ]
   
   
   
   The device is enabled to obtain PPPoE, DHCP, DHCPv6, IP, or ARP packets based on a specified interface.
4. Run [**capture-packet access condition l2tp**](cmdqueryname=capture-packet+access+condition+l2tp) **slot** *slot-id* **source-ip** *source-ip-address* **dest-ip** *dest-ip-address* [ **inbound** | **outbound** ] [ **time-out** *time-out-value* ]
   
   
   
   The device is enabled to obtain L2TP packet headers based on a specified interface board and IP addresses.
5. Run [**capture-packet access condition l2tp**](cmdqueryname=capture-packet+access+condition+l2tp) **slot** *slot-id* { **local-tunnel-id** *local-tunnel-id* | **remote-tunnel-id** *remote-tunnel-id* } \* [ **time-out** *time-out-value* ]
   
   
   
   The device is enabled to obtain L2TP packet headers based on a specified interface board and tunnel IDs.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.