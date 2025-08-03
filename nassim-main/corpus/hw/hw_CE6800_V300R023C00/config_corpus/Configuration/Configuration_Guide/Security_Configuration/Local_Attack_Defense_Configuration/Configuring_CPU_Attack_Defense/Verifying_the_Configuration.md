Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the **[**display cpu-defend policy**](cmdqueryname=display+cpu-defend+policy)** [ *policy-name* ] command to check the attack defense policy configuration.
* Run the [**display cpu-defend configuration**](cmdqueryname=display+cpu-defend+configuration) [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* } command to check the rate configuration for protocol packets sent to the CPU.
* Run the [**display cpu-defend dynamic-adjust history-record**](cmdqueryname=display+cpu-defend+dynamic-adjust+history-record) [ **packet-type** { **arp-reply** | **arp-request** | **arp-request-uc** | **dhcp-request** | **dhcp-reply** | **nd** | ****dhcp-discovery**** } ] { **all** | **slot** *slot-id* } command to check the records of adaptive CPCAR adjustments for protocol packets.
* Run the [**display cpu-defend linkup statistics**](cmdqueryname=display+cpu-defend+linkup+statistics) [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* } command to check statistics on application layer association.
* Run the [**display cpu-defend linkup configuration**](cmdqueryname=display+cpu-defend+linkup+configuration) [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* } command to check the configuration of application layer association.
* Run the **[**display cpu-defend local-host anti-attack**](cmdqueryname=display+cpu-defend+local-host+anti-attack)** [ **slot** *slot-id* ] command to check statistics on the packets matching hardware-based ACLs after host attack defense is enabled as well as the numbers and status of the ACLs bound to protocols.
* Run the **[**display cpu-defend rate**](cmdqueryname=display+cpu-defend+rate)** [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* } command to check the CPCAR value configured for protocol packets.
* Run the [**display cpu-defend statistics**](cmdqueryname=display+cpu-defend+statistics) [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* } command to check statistics on the packets sent to the CPU.
  
  
  
  When the ICMP fast reply function is enabled, statistics on ICMPv4 and ICMPv6 packets are not differentiated. The total number of ICMPv4 and ICMPv6 packets is recorded in the **icmp** field.
* Run the **[**display cpu-defend filter statistics**](cmdqueryname=display+cpu-defend+filter+statistics)** [ **slot** *slot-id* ] command to check statistics on the packets discarded based on filters.
  
  
  
  For loopback packets, only the number of discarded packets is counted, and the number of discarded bytes is not.