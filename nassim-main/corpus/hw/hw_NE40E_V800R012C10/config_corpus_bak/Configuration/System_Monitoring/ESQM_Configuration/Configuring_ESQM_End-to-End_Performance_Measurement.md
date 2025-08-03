Configuring ESQM End-to-End Performance Measurement
===================================================

After the end-to-end performance measurement function is configured, you can collect information, such as the packet type, timestamp, and packet statistics, for packet forwarding path restoration, traffic restoration, and fault detection.

#### Context

Traditional communication networks are unable to "perceive" services, preventing customers' ever-changing service requirements from being responded to in real time. To solve this problem, ESQM has been developed to help devices monitor the quality of services on networks. This technology integrates network deployment with service requirements and provides the data that is the foundation for automatic and intelligent network lifecycle management.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**esqm**](cmdqueryname=esqm)
   
   The ESQM view is displayed.
3. (Optional) Run [**esqm session aging-time**](cmdqueryname=esqm+session+aging-time) **sctp** *tmval*An aging time is set for SCTP flow tables.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configured aging time takes effect only for subsequently created SCTP flow tables.
4. (Optional) Run [**esqm protocol tcp enable**](cmdqueryname=esqm+protocol+tcp+enable)
   
   The device is enabled to create flow tables for sampled TCP protocol packets.
5. (Optional) Run [**esqm protocol**](cmdqueryname=esqm+protocol) { **sctp** | **gtp** } **disable**
   
   The device is disabled from creating flow tables for sampled SCTP, or GTP protocol packets.
6. (Optional) Run [**esqm filter**](cmdqueryname=esqm+filter) **permit** **ip** *ip-addr* **mask** *masklen*
   
   The function of filtering sampled packets is enabled.
7. Run any of the following commands:
   * To perform ESQM for inbound or outbound packets on all the interfaces to which a VPN instance is bound, run the [**esqm service-stream**](cmdqueryname=esqm+service-stream) { **inbound** | **outbound** } **vpn-instance** *vpn-instance-name* command in the ESQM view.
   * To perform ESQM for inbound or outbound packets on all the interfaces to which no VPN instance is bound, run the [**esqm service-stream**](cmdqueryname=esqm+service-stream) { **inbound** | **outbound** } command in the ESQM view.
   * To perform ESQM for inbound or outbound packets on an interface, run the following commands:
     1. Run [**quit**](cmdqueryname=quit)
        
        Exit from the ESQM view.
     2. Run [**interface**](cmdqueryname=interface) *interface-type interface-num*
        
        The interface view is displayed.
     3. Run [**esqm service-stream**](cmdqueryname=esqm+service-stream) { **inbound** | **outbound** }
        
        A packet sampling direction is configured for ESQM on the interface.
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
8. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.