(Optional) Configuring Adaptive Adjustment of the Default CPCAR Value for Protocol Packets
==========================================================================================

(Optional) Configuring Adaptive Adjustment of the Default CPCAR Value for Protocol Packets

#### Context

If a fixed default CPCAR value for protocol packets does not meet rate requirements, configure adaptive adjustment of the default CPCAR value. You can run the [**display cpu-defend dynamic-adjust history-record**](cmdqueryname=display+cpu-defend+dynamic-adjust+history-record) command to view the records of adaptive CPCAR adjustments.

The following table lists the types of protocol packets that support adaptive CPCAR adjustment and the maximum CPCAR value after adjustment.

| Protocol Packet Type | Protocol Packet Description | Maximum CPCAR Value After Adjustment |
| --- | --- | --- |
| arp-reply | ARP reply | Twice the default value |
| arp-request | ARP request | Twice the default value |
| arp-request-uc | Unicast ARP request | Twice the default value |
| dhcp-reply | DHCP reply | 1.5 times the default value |
| dhcp-request | DHCP request | 1.5 times the default value |
| dhcp-discovery NOTE:  This parameter is supported only by the following: CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K. | DHCP discovery | 1.5 times the default value |
| nd  NOTE:  The CE6885-LL in low latency mode does not support this parameter. | IPv6 ND | Twice the default value |



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable adaptive adjustment of the default CPCAR value for protocol packets. 
   
   
   ```
   [cpu-defend dynamic-adjust](cmdqueryname=cpu-defend+dynamic-adjust) [ packet-type { arp-reply | arp-request | arp-request-uc | dhcp-reply | dhcp-request | nd| dhcp-discovery   } ] enable
   ```
   
   The **dhcp-discovery** parameter is supported only by the following: CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.
   
   If you do not specify the **packet-type** parameter, adaptive adjustment of the default CPCAR value is enabled for all types of protocol packets that support this function.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```