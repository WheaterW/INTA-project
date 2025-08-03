Checking the Destination IP Addresses of ARP Packets
====================================================

This section describes how to check the destination addresses of ARP packets, therefore discarding packets with incorrect destination addresses and enhancing CPU protection.

#### Context

Perform the following steps on the Router whose ARP entries are to be prevented from being attacked.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**arp check-destination-ip enable**](cmdqueryname=arp+check-destination-ip+enable)
   
   
   
   The check of the destination IP address of ARP packets is enabled.
   
   The [**arp check-destination-ip enable**](cmdqueryname=arp+check-destination-ip+enable) command is used to protect the CPU. After the command is run, the system checks whether the destination IP addresses of the packets on the interface are correct. If the IP addresses are correct, packets are sent to the CPU; otherwise, packets are discarded.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.