Verifying the Configuration
===========================

After configuring and applying a tunnel selector, run the following commands to check tunnel selector and tunnel policy information in the system.

#### Procedure

1. Run the [**display tunnel-selector**](cmdqueryname=display+tunnel-selector) *tunnel-selector-name* command to check detailed information about a tunnel selector.
2. Run the [**display tunnel-policy**](cmdqueryname=display+tunnel-policy) *tunnel-policy-name* command to check information about the **apply** clause of a tunnel selector.
3. Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) **all** **routing-table** *ipv4-address* [ *mask* [ **longer-prefixes** ] | *mask-length* [ **longer-prefixes** ] ] command to check information about the tunnels to which VPNv4 routes on an ASBR recurse.
4. Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) **all** **routing-table** *ipv6-address* [ *prefix-length* ] command to check information about the tunnels to which VPNv6 routes on an ASBR recurse.
5. Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] **verbose** command to check information about the tunnels to which labeled BGP-IPv4 routes on a PE recurse.
6. Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] [ **longer-match** ] **verbose** command to check information about the tunnels to which the labeled BGP-IPv6 routes on a PE recurse.
7. Run the [**display tunnel-info**](cmdqueryname=display+tunnel-info) { **tunnel-id** *tunnel-id* | **all** | **statistics** } command to check information about tunnels in the current system.