Maintaining APN6
================

During APN6 network maintenance, you can perform a ping operation to check network connectivity, and a tracert operation to determine a fault source.

#### Procedure

* Run the [**ping ipv6**](cmdqueryname=ping+ipv6) { **-apn-id-ipv6****instance***instName* [ **-a** *source-ipv6-address* | **-c** *echo-number* | { **-s** *byte-number* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | { **-tc** *traffic-class-value* | **-dscp** *dscp* } | **vpn-instance** *vpn-instance-name* | **-m** *wait-time* | **-name** | **-si** { *source-interface-name* | *source-interface-type**source-interface-number* | **-h** *hoplimit* } | { **-brief** | [ **-system-time** | **-ri** | **-detail** ] \* } | **-p** *pattern* ] \* *destination-ipv6-address* } command to check whether the network connection is normal.
* Run the **[**tracert ipv6**](cmdqueryname=tracert+ipv6)** **-apn-id-ipv6****instance***instName* [ **-f** *first-hop-limit* | **-m** *max-hop-limit* | **-p** *port-number* | **-fixedPort** | **-q** *probes* | **-w** *timeout* | **vpn-instance** *vpn-instance-name* | **-s** *size* | **-name** | **-a** *source-ipv6-address* | **-v** | **-si** { *source-interface-name* | *source-interface-type**source-interface-number* } | { **-tc** *tc* | **-dscp** *dscp* } ] \* *host-name* command to determine a fault source.