Setting the Maximum Length of RIP packets
=========================================

You can increase the maximum length of RIP packets to enable
them to carry more routes, which improves bandwidth utilization.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

You can run the [**rip max-packet-length**](cmdqueryname=rip+max-packet-length) command to set a length greater than 512 bits for RIP packets
only when the remote end can accept RIP packets longer than 512 bits.

After the maximum length of RIP packets is increased, Huawei devices
may fail to communicate with non-Huawei devices. Therefore, exercise
caution when running this command.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**rip max-packet-length**](cmdqueryname=rip+max-packet-length) { *value* | **mtu** }
   
   
   
   The maximum length of RIP packets is set.
   
   **mtu** specifies the maximum length of a RIP packet that
   can be accepted.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.