Verifying the SR-MPLS TE Policy Configuration
=============================================

After configuring SR-MPLS TE Policies, verify the configuration.

#### Prerequisites

SR-MPLS TE Policies have been configured.


#### Procedure

1. Run the [**display sr-te policy**](cmdqueryname=display+sr-te+policy) [ [**endpoint**](cmdqueryname=endpoint) *ipv4-address* **color** *color-value* | **policy-name** *name-value* ] command to check SR-MPLS TE Policy details.
2. Run the [**display sr-te policy statistics**](cmdqueryname=display+sr-te+policy+statistics) command to check SR-MPLS TE Policy statistics.
3. Run the [**display sr-te policy status**](cmdqueryname=display+sr-te+policy+status) { [**endpoint**](cmdqueryname=endpoint) *ipv4-address* **color** *color-value* | **policy-name** *name-value* } command to check SR-MPLS TE Policy status to determine the reason why a specified SR-MPLS TE Policy cannot go up.
4. Run the [**display sr-te policy last-down-reason**](cmdqueryname=display+sr-te+policy+last-down-reason) [ [**endpoint**](cmdqueryname=endpoint) *ipv4-address* **color** *color-value* | **policy-name** *name-value* ] command to check records about events where SR-MPLS TE Policies or segment lists in SR-MPLS TE Policies go down.
5. Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance)*vpn-instance-name* **tunnel-info nexthop** *nexthopIpv4Addr* command to display information about the iterations of the routes that match the nexthop under each address family in the current VPN instance.
6. Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] **tunnel-info** command to displays information about the tunnel associated with the EVPN instance.
7. Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name)*vpn-instance-name* **tunnel-info** **nexthop** *nexthopIpv4Addr* command to display information about a tunnel associated with an EVPN with a specified next-hop address.