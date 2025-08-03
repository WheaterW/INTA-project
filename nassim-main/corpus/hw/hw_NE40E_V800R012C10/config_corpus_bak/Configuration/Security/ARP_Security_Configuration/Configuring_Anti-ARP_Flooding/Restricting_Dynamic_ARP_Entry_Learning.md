Restricting Dynamic ARP Entry Learning
======================================

When a large number of ARP entries are generated on a specified
interface, you can prevent the interface to dynamically learn ARP
entries.

#### Background Information

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

* If dynamic ARP entry learning is disabled on an interface,
  traffic forwarding may fail on this interface.
* After dynamic ARP entry learning is disabled on an interface,
  the system will not automatically delete the ARP entries that were
  learnt previously on this interface. You can delete or retain these
  dynamic ARP entries as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface
   view is displayed.
3. Run [**arp learning disable**](cmdqueryname=arp+learning+disable)
   
   
   
   Dynamic ARP entry learning is disabled on the
   interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.