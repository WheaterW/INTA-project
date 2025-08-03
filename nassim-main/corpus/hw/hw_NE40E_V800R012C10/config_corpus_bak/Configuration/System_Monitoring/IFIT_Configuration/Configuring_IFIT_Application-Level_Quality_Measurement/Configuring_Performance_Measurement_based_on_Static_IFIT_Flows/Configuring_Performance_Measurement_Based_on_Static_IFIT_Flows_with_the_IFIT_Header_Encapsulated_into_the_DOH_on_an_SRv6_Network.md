Configuring Performance Measurement Based on Static IFIT Flows with the IFIT Header Encapsulated into the DOH on an SRv6 Network
================================================================================================================================

This section describes how to configure performance measurement based on static IFIT flows with the IFIT header encapsulated into the DOH on an SRv6 network.

#### Prerequisites

When an IFIT instance with Header Type being 16 is configured, each SRv6 SID node (including SRv6 BE ingress and egress) must be able to identify the DOH and SRH in packets. Otherwise, traffic will be interrupted (for example, some nodes do not support IFIT instances with Header Type being 16). To use new functions related to IFIT instances with Header Type being 16, upgrade SRv6 SID nodes on the network to versions that support this type of instance in an end-to-end manner.


#### Context

Static IFIT flows with the IFIT header encapsulated into the DOH can be generated in many modes, including those generated based on 5-tuple, peer, and multicast information. After creating a static IFIT flow, you can select end-to-end or hop-by-hop measurement as required. [Figure 1](#EN-US_TASK_0000001232913654__fig339555465014) shows the typical networking of performance measurement based on a static IFIT flow. The target flow enters the transit network through DeviceA, traverses DeviceB, and leaves the transit network through DeviceC.

* End-to-end measurement: To monitor transit network performance in real time or diagnose faults, configure IFIT end-to-end measurement on both DeviceA and DeviceC.
* Hop-by-hop measurement: To measure the packet loss and delay hop by hop for fault locating when a performance fault occurs on the transit network, configure hop-by-hop measurement on DeviceA, DeviceB, and DeviceC.

**Figure 1** Performance measurement based on static IFIT flows  
![](figure/en-us_image_0000001386386516.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ifit**](cmdqueryname=ifit)
   
   
   
   IFIT is enabled globally, and its view is displayed.
3. Run [**node-id**](cmdqueryname=node-id) *node-id*
   
   
   
   A node ID is configured.
   
   
   
   Only steps 1 to 3 need to be configured on DeviceB and DeviceC that function as the transit node and egress, respectively.
4. (Optional) Run [**measure disable**](cmdqueryname=measure+disable)
   
   
   
   Global IFIT measurement is disabled.
5. (Optional) Run [**decapsulation peer-locator**](cmdqueryname=decapsulation+peer-locator) *locator-ipv6-prefix* *locator-prefix-length*
   
   
   
   The device is enabled to remove the IFIT header from packets destined for a specified next-hop locator.
   
   
   
   In SRv6 HoVPN-based interworking scenarios, to ensure that the IFIT header is not carried in packets across domains in an E2E manner, you can perform this step on inter-domain devices to terminate IFIT packets within a domain. This allows the NMS to display statistics in a unified manner.
6. (Optional) Run [**clock-source**](cmdqueryname=clock-source) { **ntp** | **auto** }
   
   
   
   The clock source for IFIT measurement is set to NTP or is automatically selected.
   
   
   
   By default, the clock source is automatically selected. In this mode, the high-precision clock source is preferentially selected. This step allows you to manually select a clock type in order to cope with measurement failures caused by asynchronous clocks in cross-domain interconnection scenarios where multiple clock protocols are deployed. In addition, you can run the [**period-clock-mode**](cmdqueryname=period-clock-mode) { **ptp** **current-leap** *current-leap-value* [ { **leap59** | **leap61** } **date** *utc-date* ] } command to configure a timing mode for the IFIT measurement interval and timestamp sampling.
7. Run [**instance-ht16**](cmdqueryname=instance-ht16)*instance-id*
   
   
   
   An IFIT instance with Header Type being 16 is created, and its view is displayed.
8. Run [**measure-mode**](cmdqueryname=measure-mode) { **e2e** | **trace** }
   
   
   
   The IFIT measurement mode is set to end-to-end or hop-by-hop.
   
   
   
   By default, end-to-end measurement is used. In multicast flow measurement scenarios, only end-to-end measurement is supported.
9. (Optional) Run [**interval**](cmdqueryname=interval) *interval-value*
   
   
   
   A measurement interval is set for the IFIT instance.
10. Run different commands to create static IFIT flows based on service scenarios, as described in [Table 1](#EN-US_TASK_0000001232913654__table1026131313513).
    
    
    
    **Table 1** Creating static IFIT flows in different service scenarios
    | Service Scenario | Command | Description |
    | --- | --- | --- |
    | L3VPNv4/EVPN L3VPNv4 (HVPN) | [**flow**](cmdqueryname=flow) **unidirectional** **source** { *source-ip* [ *source-mask* ] | **any** } **destination** { *destination-ip* [ *destination-mask* ] | **any** } [ **protocol** { { **tcp** | **udp** | **sctp** | *protocol-number4* | *protocol-number5* | *protocol-number6* } [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] | { *protocol-number* | *protocol-number7* | *protocol-number8* | *protocol-number3* } } ] [ **dscp** *dscp-value* ] [ **vpn-instance** *vpn-instance-name* ] | Create a static IFIT flow based on 5-tuple information. |
    | L3VPNv6/EVPN L3VPNv6 (HVPN) | [**flow**](cmdqueryname=flow) **unidirectional** **source-ipv6** { *src-ipv6-address* [ *src6-mask-length* ] | **any** } **destination-ipv6** { *dest-ipv6-address* [ *dest6-mask-length* ] | **any** } [ **protocol** { { **tcp** | **udp** | **sctp** | *protocol-number4* | *protocol-number5* | *protocol-number6* } [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] | { *protocol-number* | *protocol-number7* | *protocol-number8* | *protocol-number3* } } ] [ **dscp** *dscp-value* ] [ **vpn-instance** *vpn-instance-name* ] | Create a static IFIT flow based on 5-tuple information. |
    | IPv4 public network | [**flow**](cmdqueryname=flow) **unidirectional** **source** { *source-ip* [ *source-mask* ] | **any** } **destination** { *destination-ip* [ *destination-mask* ] | **any** } [ **protocol** { { **tcp** | **udp** | **sctp** | *protocol-number4* | *protocol-number5* | *protocol-number6* } [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] | { *protocol-number* | *protocol-number7* | *protocol-number8* | *protocol-number3* } } ] [ **dscp** *dscp-value* ] | Create a static IFIT flow based on 5-tuple information. |
    | IPv6 public network | [**flow**](cmdqueryname=flow) **unidirectional** **source-ipv6** { *src-ipv6-address* [ *src6-mask-length* ] | **any** } **destination-ipv6** { *dest-ipv6-address* [ *dest6-mask-length* ] | **any** } [ **protocol** { { **tcp** | **udp** | **sctp** | *protocol-number4* | *protocol-number5* | *protocol-number6* } [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] | { *protocol-number* | *protocol-number7* | *protocol-number8* | *protocol-number3* } } ] [ **dscp** *dscp-value* ] | Create a static IFIT flow based on 5-tuple information. |
    | MVPNv4/GTMv4 | [**flow**](cmdqueryname=flow) **unidirectional** ****source**** *source-address***group***group-address* [ **vpn-instance***vpn-name* ] | Create a static IFIT flow based on the multicast source and multicast group. |
    | MVPNv6/GTMv6 | [**flow**](cmdqueryname=flow) **unidirectional** ****source-ipv6**** *source-ipv6-address***group-ipv6***group-ipv6-address* [ **vpn-instance***vpn-name* ] | Create a static IFIT flow based on the multicast source and multicast group. |
    | EVPN VPWS | [**flow**](cmdqueryname=flow) **unidirectional** **evpl-instance** *evpl-instance-value* **peer-locator** *locator-ipv6-prefix* *locator-prefix-length* | Create a static IFIT flow based on the peer locator. |
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    * Static IFIT flows based on DOH encapsulation support only SRv6 tunnels. Because tunnel types cannot be distinguished based on the configured 5-tuple, IFIT does not take effect for unsupported tunnel types.
    * In multicast flow measurement scenarios, the **vpn-instance***vpn-name* keyword applies only to MVPN scenarios, not to GTM scenarios.
11. Run [**binding interface**](cmdqueryname=binding+interface){ *interface-type**interface-number* | *interface-name* }
    
    
    
    The IFIT flow is bound to an interface.
    
    
    
    Different IFIT instances can be configured with the same flow characteristics, but cannot be bound to the same interface.
12. (Optional) Run [**measure disable**](cmdqueryname=measure+disable)
    
    
    
    Measurement is disabled for an IFIT instance.
13. (Optional) Run [**delay-measure enable**](cmdqueryname=delay-measure+enable)
    
    
    
    Delay measurement is enabled.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.