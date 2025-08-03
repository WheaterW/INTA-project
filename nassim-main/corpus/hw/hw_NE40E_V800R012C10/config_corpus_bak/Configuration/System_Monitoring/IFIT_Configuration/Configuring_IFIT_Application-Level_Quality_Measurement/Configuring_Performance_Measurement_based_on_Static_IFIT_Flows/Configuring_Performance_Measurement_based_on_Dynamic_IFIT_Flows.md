Configuring Performance Measurement based on Dynamic IFIT Flows
===============================================================

IFIT measurement based on dynamic flows can be triggered by packets with the IFIT header or by automatic flow learning.

#### Context

IFIT supports automatic learning of dynamic flows on the ingress by using the mask or exact match of the source or destination address. In addition, IFIT can flexibly monitor service quality in real time by configuring a learning whitelist. The generation of dynamic flows on transit and egress nodes is triggered by packets with the IFIT header.

#### Pre-configuration Tasks

Before configuring performance measurement based on dynamic IFIT flows, complete the following tasks:

* Configure a dynamic routing protocol or static routes so that devices are reachable at the network layer.
* Configure the network time protocol or G.8275.1 to implement clock synchronization for all devices that have clocks on the network.

#### Procedure

In a non-inter-AS Option A scenario, perform the following steps to configure performance measurement based on dynamic IFIT flows:

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**ifit**](cmdqueryname=ifit)
   
   IFIT is enabled globally, and its view is displayed.
3. Run [**node-id**](cmdqueryname=node-id) *node-id*
   
   A node ID is configured.
   
   Only steps 1 to 3 need to be performed on the transit node and egress to implement dynamic flow-based measurement.
4. Run [**encapsulation nexthop**](cmdqueryname=encapsulation+nexthop) *ip-address*
   
   The device is enabled to encapsulate the IFIT header into packets destined for a specified next hop IP address.
   
   This step is required only on an MPLS network.
5. Perform the following steps to configure IFIT automatic flow learning on the ingress to implement flexible performance measurement based on dynamic IFIT flows:
   1. (Optional) Run the [**whitelist-group**](cmdqueryname=whitelist-group) *whitelist-group-name* command to configure an IFIT whitelist group and enter its view.
   2. (Optional) Run either of the following commands to configure a whitelist rule:
      * In an IPv4 scenario, run the [**rule**](cmdqueryname=rule) *rule-name* **ipv4** { **source** { *src-ip-address* [ *src-mask-length* | **any** *src-mask-length* ] } | **destination** { *dest-ip-address* [ *dest-mask-length* ] | **any** *dest-mask-length* } | **protocol** { { **tcp** | **udp** | **sctp** | *protocol-number4* | *protocol-number5* | *protocol-number6* } [ **source-port** *src-port-number* ] [ **destination-port** *dest-port-number* ] | { *protocol-number* | *protocol-number3* | *protocol-number7* | *protocol-number8* } } } \* command.
      * In an IPv6 scenario, run the [**rule**](cmdqueryname=rule) *rule-name* **ipv6** { **source-ipv6** { *src-ipv6-address* [ *src6-mask-length* | **any** *src6-mask-length* ] } | **destination-ipv6** { *dest-ipv6-address* [ *dest6-mask-length* ] | **any** *dest6-mask-length* } | **protocol** { { **tcp** | **udp** | **sctp** | *protocol-number4* | *protocol-number5* | *protocol-number6* } [ **source-port** *src-port-number* ] [ **destination-port** *dest-port-number* ] | { *protocol-number* | *protocol-number3* | *protocol-number7* | *protocol-number8* } } } \* command.
   3. Run the [**flow-learning vpn-instance**](cmdqueryname=flow-learning+vpn-instance) *vpn-name* command to configure an IFIT VPN instance and enter its view.
   4. (Optional) Run the [**learning-mode**](cmdqueryname=learning-mode) { **sip-mask-dip-exact** | **sip-mask-dip-mask** | **sip-exact-dip-exact** | **sip-exact-dip-mask** } command to configure an IFIT flow learning mode.
   5. Run the [**flow-learning**](cmdqueryname=flow-learning) { **bidirectional** | **unidirectional** } command to configure an IFIT flow learning direction.
   6. Run the [**measure-mode**](cmdqueryname=measure-mode) { **e2e** | **trace** } command to set the IFIT flow learning measurement mode to end-to-end or hop-by-hop.
      
      By default, end-to-end measurement is used.
   7. (Optional) Run the [**interval**](cmdqueryname=interval) *interval-value* command to configure a measurement interval for IFIT flow learning.
   8. Run the [**flow-learning interface**](cmdqueryname=flow-learning+interface) { **all** | { *ifType* *ifNum* | *ifName* } } [ **whitelist-group** *whitelist-group-name* ] command to bind the learned IFIT flows to a specified interface.
   9. Run the [**quit**](cmdqueryname=quit) command to return to the IFIT view.
6. Run the following commands to modify the learned dynamic IFIT flows as required:
   * In IPv4 scenarios:
     + To set dynamic flow parameters, run the [**dynamic flow**](cmdqueryname=dynamic+flow)**source**{ *src-ip-address* [ *src-mask-length* ] | **srcAny** } **destination** { *dest-ip-address* [ *dest-mask-length* ] | **dstAny** } [ **vpn-instance** *vpn-name* ] **interface** { *ifType**ifNum* | *ifName* } [ **dscp***dscp-value* ] [ **protocol** { { **tcp** | **udp** | *protocol-tcp* | *protocol-udp* | **sctp** | *protocol-sctp* } [ **source-port***src-port-number* ] [ **destination-port** *d**est-port-number* ] | { *protocol-number* | *protocol-number3* | *protocol-number4* | *protocol-number5* } } ] { **measure-mode** { **e2e** | **trace** } | **delay-measure** { **enable** | **disable** } | **interval***interval-value* | { **loss-measure-enable** | **loss-measure-disable** } | { **disorder-measure-enable** | **disorder-measure-disable** } | **per-packet-delay** { **enable** | **disable** } } \* command.
     + To clear the learned dynamic IFIT flows, run the [**reset dynamic flow**](cmdqueryname=reset+dynamic+flow) **source**{ *src-ip-address* [ *src-mask-length* ] | **srcAny** } **destination** { *dest-ip-address* [ *dest-mask-length* ] | **dstAny** } [ **vpn-instance** *vpn-name* ] **interface** { *ifType**ifNum* | *ifName* } [ **dscp***dscp-value* ] [ **protocol** { { **tcp** | **udp** | *protocol-tcp* | *protocol-udp* | **sctp** | *protocol-sctp* } [ **source-port***src-port-number* ] [ **destination-port** *d**est-port-number* ] | { *protocol-number* | *protocol-number3* | *protocol-number4* | *protocol-number5* } } ] command.
   * In IPv6 scenarios:
     + To set dynamic flow parameters, run the [**dynamic flow**](cmdqueryname=dynamic+flow) **source-ipv6**{ *src-ipv6-address* [ *src6-mask-length* ] | **srcAny** } **destination-ipv6** { *dest-ipv6-address* [ *dest6-mask-length* ] | **dstAny** } [ **vpn-instance** *vpn-name* ] **interface** { *ifType**ifNum* | *ifName* } [ **dscp***dscp-value* ] [ **protocol** { { **tcp** | **udp** | *protocol-tcp* | *protocol-udp* | **sctp** | *protocol-sctp* } [ **source-port***src-port-number* ] [ **destination-port** *d**est-port-number* ] | { *protocol-number* | *protocol-number3* | *protocol-number4* | *protocol-number5* } } ] { **measure-mode** { **e2e** | **trace** } | **delay-measure** { **enable** | **disable** } | **interval***interval-value* | { **loss-measure-enable** | **loss-measure-disable** } | { **disorder-measure-enable** | **disorder-measure-disable** } | **per-packet-delay** { **enable** | **disable** } } \* command.
     + To clear the learned dynamic IFIT flows, run the [**reset dynamic flow**](cmdqueryname=reset+dynamic+flow) **source-ipv6**{ *src-ipv6-address* [ *src6-mask-length* ] | **srcAny** } **destination-ipv6** { *dest-ipv6-address* [ *dest6-mask-length* ] | **dstAny** } [ **vpn-instance** *vpn-name* ] **interface** { *ifType**ifNum* | *ifName* } [ **dscp***dscp-value* ] [ **protocol** { { **tcp** | **udp** | *protocol-tcp* | *protocol-udp* | **sctp** | *protocol-sctp* } [ **source-port***src-port-number* ] [ **destination-port** *d**est-port-number* ] | { *protocol-number* | *protocol-number3* | *protocol-number4* | *protocol-number5* } } ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If automatic flow learning is not performed, this step can also be used to modify the learned dynamic reverse flows in scenarios where IFIT measurement is performed for bidirectional flows.
   * Per-packet delay measurement can be enabled only after packet loss measurement is enabled and is mutually exclusive with out-of-order packet measurement.
7. (Optional) Run [**flow-learning reverse-flow-mode eth-trunk**](cmdqueryname=flow-learning+reverse-flow-mode+eth-trunk)
   
   The learning mode of IFIT reverse flows is set to Eth-Trunk interface-based learning.
8. (Optional) Run [**dynamic-flow age interval-multiplier**](cmdqueryname=dynamic-flow+age+interval-multiplier) *multi-value*
   
   The aging time of dynamic IFIT flows is set.
9. (Optional) Run [**reset dynamic**](cmdqueryname=reset+dynamic) **flow** { *flowId* | **all** }
   
   All learned dynamic flows or a specific one is deleted.
10. Run [**commit**](cmdqueryname=commit)
    
    The configuration is committed.

In an inter-AS Option A scenario, in addition to the preceding configurations, you also need to perform the following steps to enable IFIT mapping on the interfaces of the devices (a pair of ASBRs) that connect different ASs:

1. In the system view, run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
   
   The interface view is displayed.
2. Run either of the following commands based on the device location to enable IFIT mapping on the interface:
   * To enable IFIT mapping in the inbound direction, run the [**ifit ingress mapping enable**](cmdqueryname=ifit+ingress+mapping+enable) command on the egress ASBR.
   * To enable IFIT mapping in the outbound direction, run the [**ifit egress mapping enable**](cmdqueryname=ifit+egress+mapping+enable) command on the ingress ASBR.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You are advised to configure IFIT mapping in the inbound direction and then in the outbound direction. Otherwise, traffic may be interrupted.
3. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.