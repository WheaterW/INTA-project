Clearing Local Attack Defense Statistics
========================================

Before collecting new attack defense statistics, you need to clear the existing attack defense statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Cleared attack defense statistics cannot be restored. Exercise caution when performing this operation.



#### Procedure

1. To clear attack defense statistics, run the [**reset cpu-defend**](cmdqueryname=reset+cpu-defend+all+application-apperceive+tcpip-defend) { **all** | **application-apperceive** | **tcpip-defend** | **tcpip-defend-v6** | **total-packet** | **urpf** } **statistics** [ **slot** *slot-id* ] command in the user view.
   
   
   
   In VS mode, this command is supported only by the admin VS.
2. To clear attack source tracing information saved in the memory of the specified or all interface boards, run the [**reset attack-source-trace**](cmdqueryname=reset+attack-source-trace) **slot** { *slot-id* | **all** } command in the user view.
   
   
   
   In VS mode, this command is supported only by the admin VS.
3. To clear statistics about packets of a specified protocol group or all protocol groups, run the [**reset cpu-defend protocol-group**](cmdqueryname=reset+cpu-defend+protocol-group+whitelist+user-defined-flow) { **whitelist** | **user-defined-flow** | **management** | **route-protocol** | **multicast** | **arp** | **mpls** | **access-user** | **link-layer** | **network-layer** | **system-message** | **blacklist** | **check-failed** | **fwddata-to-cp** | **all** } **statistics** **slot** *slot-id* command in the user view.
4. To clear statistics about ND invalid packet attack defense, run the [**reset nd packet filter statistics**](cmdqueryname=reset+nd+packet+filter+statistics) [ **slot** *slot-id* ] command in the user view.
5. To clear ND attack statistics, run the [**reset ipv6 nd**](cmdqueryname=reset+ipv6+nd+na+ns-multicast+ns-unicast+attack+interface) { **na** | **ns-multicast** | **ns-unicast** } **attack interface** { *interface-type* *interface-num* | *interface-name* } or [**reset ipv6 nd**](cmdqueryname=reset+ipv6+nd+na+ns-multicast+ns-unicast+attack+slot+all) { **na** | **ns-multicast** | **ns-unicast** } **attack slot** { *slotid* | **all** } command in the user view.