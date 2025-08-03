Creating a Loopback Interface and Configuring an IP Address for It
==================================================================

IP addresses need to be configured for loopback interfaces that are always up so that these interfaces can be used to communicate with other devices.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
   
   
   
   A loopback interface is created.
   
   
   
   You can create or delete loopback interfaces as required. Once a loopback interface is created, it remains up all the time unless it monitors an interface monitoring group and may go down.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   The IP address of the loopback interface is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.