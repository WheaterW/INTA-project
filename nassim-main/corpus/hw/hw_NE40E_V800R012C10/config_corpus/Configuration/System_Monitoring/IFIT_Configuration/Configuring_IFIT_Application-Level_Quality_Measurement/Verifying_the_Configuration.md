Verifying the Configuration
===========================

You can check IFIT measurement configurations.

#### Prerequisites

IFIT has been configured.


#### Procedure

1. Run the [**display ifit**](cmdqueryname=display+ifit) command to check information about IFIT flows.
2. Run the [**display ifit**](cmdqueryname=display+ifit) { **source** *src-ip-address* [ **destination** *dest-ip-address* ] | **destination** *dest-ip-address* } command to check IFIT flow information based on specified IPv4 addresses.
3. Run the [**display ifit**](cmdqueryname=display+ifit) { **source-ipv6** *src-ipv6-address* [ **destination-ipv6** *dest-ipv6-address* ] | **destination-ipv6** *dest-ipv6-address* } command to check IFIT flow information based on specified IPv6 addresses.
4. Run the [**display ifit**](cmdqueryname=display+ifit) **static** [ **instance** *instance-name* | **flow-id** *flow-id* ] command to check information about static IFIT flows.
5. Run the [**display ifit**](cmdqueryname=display+ifit) **static** **instance-ht16** *instance-name* command to check information about static IFIT flows bound to an IFIT instance with Header Type being 16.
6. Run the [**display ifit**](cmdqueryname=display+ifit) **dynamic** [ **flow-id** *flow-id* ] command to check information about dynamic IFIT flows on the ingress.
7. Run the [**display ifit**](cmdqueryname=display+ifit) **dynamic-hop** [ **flow-id** *flow-id* ] command to check information about dynamic IFIT flows on transit and egress nodes.
8. Run the [**display ifit**](cmdqueryname=display+ifit) { **peer-ip** *peer-ip-address* | **peer-locator** *locator-ipv6-prefix* } command to check IFIT flow information by specifying the next hop of the target flow.
9. Run the [**display ifit**](cmdqueryname=display+ifit)**apn-id-ipv6**[ **apn-instance***apn-instance-name* ] command to check IFIT flow information based on an APN6 instance name.
10. Run the [**display ifit multicast**](cmdqueryname=display+ifit+multicast) { { ****source**** *source-address* [ **group***group-address* ] | **group***group-address* } | { ****source-ipv6**** *source-ipv6-address* [ **group-ipv6***group-ipv6-address* ] | **group-ipv6***group-ipv6-address* } } command to check IFIT flow information based on a specified multicast source and group address.
11. Run the [**display license resource usage ifit all**](cmdqueryname=display+license+resource+usage+ifit+all) command to check the usage of IFIT license resources.
12. Run the [**display ifit resource**](cmdqueryname=display+ifit+resource) [ **per-packet-delay** ] command to check the resource usage of IFIT flows.
13. In the system view, run the [**display ifit timesource**](cmdqueryname=display+ifit+timesource) [ **slot** *slot-id* ] command to check the clock synchronization status of each board.