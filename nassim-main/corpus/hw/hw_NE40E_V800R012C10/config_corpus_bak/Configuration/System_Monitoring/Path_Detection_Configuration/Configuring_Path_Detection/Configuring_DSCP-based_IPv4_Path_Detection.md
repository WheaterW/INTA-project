Configuring DSCP-based IPv4 Path Detection
==========================================

Configuring DSCP-based IPv4 path detection includes enabling path detection and constructing and forwarding an IPv4 path detection packet.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip path detection enable**](cmdqueryname=ip+path+detection+enable)**dscp** *dscp-value*
   
   
   
   DSCP-based IPv4 path detection is enabled.
3. Run [**ip path detection send-packet**](cmdqueryname=ip+path+detection+send-packet)**src-mac***src-mac-address***dst-mac***dst-mac-address* [ **pe-vlan***pe-vlan-id* [ **8021p** *8021p-value* ] [ **ce-vlan***ce-vlan-id* ] ] **src-ip***src-ip-addr***dst-ip***dst-ip-address***protocol** { **icmp** | { **tcp** | **udp** [ **gtp-u** **gtp-teid** *teid-value* ] | **sctp** } **src-port** *src-port-value* **dst-port** *dst-port-value* } **dscp** *dscp-value* [ **vpn-instance** *vpn-name* ] **interface** { *ifType* *ifNum* | *ifName* } **testid** *test-id*
   
   
   
   The ingress is enabled to construct and forward an IPv4 path detection packet.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is required only on the ingress for path detection.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.