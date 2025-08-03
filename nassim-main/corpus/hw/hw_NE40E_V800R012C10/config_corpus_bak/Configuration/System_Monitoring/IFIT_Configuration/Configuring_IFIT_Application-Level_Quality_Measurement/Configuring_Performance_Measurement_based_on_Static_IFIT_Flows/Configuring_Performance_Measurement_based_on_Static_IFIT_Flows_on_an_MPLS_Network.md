Configuring Performance Measurement based on Static IFIT Flows on an MPLS Network
=================================================================================

This section describes how to configure performance measurement based on static IFIT flows on an MPLS network.

#### Context

A static IFIT flow can be uniquely identified based on 5-tuple information or specified by setting the peer address. After creating a static IFIT flow, you can select end-to-end or hop-by-hop measurement as required. [Figure 1](#EN-US_TASK_0000001280981181__fig339555465014) shows the typical networking of performance measurement based on a static IFIT flow. The target flow enters the transit network through DeviceA, traverses DeviceB, and leaves the transit network through DeviceC.

* End-to-end measurement: To monitor transit network performance in real time or diagnose faults, configure IFIT end-to-end measurement on both DeviceA and DeviceC.
* Hop-by-hop measurement: To measure the packet loss and delay hop by hop for fault locating when a performance fault occurs on the transit network, configure hop-by-hop measurement on DeviceA, DeviceB, and DeviceC.

**Figure 1** Performance measurement based on static IFIT flows  
![](figure/en-us_image_0000001274688178.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this scenario, data can be reported only through telemetry of the OnChange type.



#### Procedure

In a non-inter-AS Option A scenario, perform the following steps to configure performance measurement based on static IFIT flows:

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**ifit**](cmdqueryname=ifit)
   
   IFIT is enabled globally, and its view is displayed.
3. Run [**node-id**](cmdqueryname=node-id) *node-id*
   
   A node ID is configured.
4. Run [**encapsulation nexthop**](cmdqueryname=encapsulation+nexthop) *ip-address*
   
   The device is enabled to encapsulate the IFIT header into packets destined for a specified next-hop IP address.
   
   Only steps 1 to 3 need to be configured on DeviceB and DeviceC that function as the transit node and egress, respectively. However:
   * In Segment Routing scenarios where hop-by-hop measurement is performed, this step must be run on DeviceB to specify a next hop for the flow to be measured.
   * In scenarios where bidirectional flow measurement is performed, this step must be run on DeviceC to specify a reverse next hop for the flow to be measured.
5. (Optional) Run [**measure disable**](cmdqueryname=measure+disable)
   
   Global IFIT measurement is disabled.
6. (Optional) Run [**clock-source**](cmdqueryname=clock-source) { **ntp** | **auto** }
   
   The clock source for IFIT measurement is set to NTP or is automatically selected.
   
   By default, the clock source is automatically selected. In this mode, the high-precision clock source is preferentially selected. This step allows you to manually select a clock type in order to cope with measurement failures caused by asynchronous clocks in cross-domain interconnection scenarios where multiple clock protocols are deployed. In addition, you can run the [**period-clock-mode**](cmdqueryname=period-clock-mode) { **ptp** **current-leap** *current-leap-value* [ { **leap59** | **leap61** } **date** *utc-date* ] } command to configure a timing mode for the IFIT measurement interval and timestamp sampling.
7. Run [**instance**](cmdqueryname=instance) *instance-id*
   
   An IFIT instance is created, and its view is displayed.
8. Run [**measure-mode**](cmdqueryname=measure-mode) { **e2e** | **trace** }
   
   The IFIT measurement mode is set to end-to-end or hop-by-hop.
   
   By default, end-to-end measurement is used.
9. (Optional) Run [**interval**](cmdqueryname=interval) *interval-value*
   
   A measurement interval is set for the IFIT instance.
10. Run different commands to create static IFIT flows based on service scenarios, as described in [Table 1](#EN-US_TASK_0000001280981181__table1026131313513).
    
    **Table 1** Creating static IFIT flows in different service scenarios
    | Service Scenario | Command | Description |
    | --- | --- | --- |
    | L3VPNv4/EVPN L3VPNv4 (HVPN) | [**flow**](cmdqueryname=flow) { **unidirectional** | **bidirectional** } **source** { *source-ip* [ *source-mask* ] | **any** } **destination** { *destination-ip* [ *destination-mask* ] | **any** } [ **protocol** { { **tcp** | **udp** | **sctp** | *protocol-number4* | *protocol-number5* | *protocol-number6* } [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] | { *protocol-number* | *protocol-number7* | *protocol-number8* | *protocol-number3* } } ] [ **gtp** [ **gtp-te-id** *te-id-value* ] ] [ **dscp** *dscp-value* ] [ **vpn-instance** *vpn-instance-name* ] | Create a static IFIT flow based on 5-tuple information. |
    | [**flow**](cmdqueryname=flow) **unidirectional** **source** **any** **destination** **any** { **vpn-instance** *vpn-instance-name* } **peer-ip** *peer-ip-address* | Create a static IFIT flow based on the peer IP address. |
    | L3VPNv6/EVPN L3VPNv6 (HVPN) | [**flow**](cmdqueryname=flow) { **unidirectional** | **bidirectional** } **source-ipv6** { *src-ipv6-address* [ *src6-mask-length* ] | **any** } **destination-ipv6** { *dest-ipv6-address* [ *dest6-mask-length* ] | **any** } [ **protocol** { { **tcp** | **udp** | **sctp** | *protocol-number4* | *protocol-number5* | *protocol-number6* } [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] | { *protocol-number* | *protocol-number7* | *protocol-number8* | *protocol-number3* } } ] [ **gtp** [ **gtp-te-id** *te-id-value* ] ] [ **dscp** *dscp-value* ] [ **vpn-instance** *vpn-instance-name* ] | Create a static IFIT flow based on 5-tuple information. |
    | [**flow**](cmdqueryname=flow) **unidirectional** **source-ipv6** **any** **destination-ipv6** **any** { **vpn-instance** *vpn-instance-name* } **peer-ip** *peer-ip-address* | Create a static IFIT flow based on the peer IP address. |
    | EVPN VPWS | [**flow**](cmdqueryname=flow) **unidirectional** **evpl-instance** *evpl-instance-value* **peer-ip** *peer-ip-address* | Create a static IFIT flow based on the peer IP address. |
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In VPN scenarios where a static IFIT flow is configured based on 5-tuple information, a VPN instance must be configured unless IFIT is performed for downstream traffic in HoVPN scenarios or upstream/downstream traffic in H-VPN scenarios.
11. Run [**binding interface**](cmdqueryname=binding+interface){ *interface-type**interface-number* | *interface-name* }
    
    The IFIT flow is bound to an interface.
    
    Different IFIT instances can be configured with the same flow characteristics, but cannot be bound to the same interface.
12. (Optional) Run [**disorder-measure enable**](cmdqueryname=disorder-measure+enable)
    
    Out-of-order packet measurement is enabled.
13. (Optional) Run [**gtpu-sn-measure enable**](cmdqueryname=gtpu-sn-measure+enable)
    
    Out-of-order packet measurement is enabled for GTP-U packets.
14. (Optional) Run [**delay-measure per-packet enable**](cmdqueryname=delay-measure+per-packet+enable)
    
    Per-packet delay measurement is enabled.
    
    Per-packet delay measurement can be enabled only after packet loss measurement is enabled and is mutually exclusive with out-of-order packet measurement.
15. (Optional) Run [**loss-measure disable**](cmdqueryname=loss-measure+disable)
    
    Packet loss measurement is disabled.
16. (Optional) Run [**delay-measure disable**](cmdqueryname=delay-measure+disable)
    
    Delay measurement is disabled.
17. (Optional) Run [**match-priority**](cmdqueryname=match-priority) *priority-num*
    
    A flow matching priority is configured for the IFIT instance.
18. Run [**commit**](cmdqueryname=commit)
    
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

If only a single device on the network supports IFIT, you can run the [**single-device-measure enable**](cmdqueryname=single-device-measure+enable) command in the [IFIT instance view](#EN-US_TASK_0000001280981181__li095416543186) to enable single-device measurement after you [create a static IFIT flow](#EN-US_TASK_0000001280981181__li1116517352569). However, the following restrictions exist:

* Currently, single-device IFIT measurement is supported only in public network and L3VPN/EVPN L3VPN (HVPN) scenarios, not in Layer 2 scenarios.
* In tunnel forwarding scenarios, single-device IFIT measurement is not supported on P nodes.
* In single-device IFIT measurement scenarios, only unidirectional flows with characteristics specified can be statically configured and delivered.
* If IFIT Option A mapping is configured on the outbound interface of single-device IFIT measurement, a TransitOutput statistical node instead of an Egress statistical node is generated in the outbound direction, and this node encapsulates the IFIT header into packets and forwards them.