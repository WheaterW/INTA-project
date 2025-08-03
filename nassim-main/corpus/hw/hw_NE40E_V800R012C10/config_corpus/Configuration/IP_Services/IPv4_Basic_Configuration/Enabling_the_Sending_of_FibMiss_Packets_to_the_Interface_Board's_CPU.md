Enabling the Sending of FibMiss Packets to the Interface Board's CPU
====================================================================

Enabling the Sending of FibMiss Packets to the Interface Board's CPU

#### Usage Scenario

[Figure 1](#EN-US_TASK_0172364928__fig_1001) shows the process in which the NE40E processes an IP packet that has the destination address not being the local device address and does not match any entry in the FIB table.

**Figure 1** Processing an IP packet that does not match any FIB entry  
![](images/fib-miss-report_enable.png)  

If the destination IP address of a packet received by an interface board on a device from a peer device is not the local device address and does not match any FIB entry on the local device and no CAR operation is performed, the interface board determines whether to send a FibMiss packet to the CPU.

After receiving a FibMiss packet, the CPU parses the source IP address of the packet and determines whether to generate an ICMP network unreachable packet and send it to the peer device.

The preceding operations consume resources. To save resources, you can run the following commands to disable the function of sending ICMP network unreachable packets.

1. Run the [**undo fib-miss-report enable**](cmdqueryname=undo+fib-miss-report+enable) command to disable the device from sending FibMiss packets to the interface board's CPU.
2. Run the [**undo icmp name net-unreachable send**](cmdqueryname=undo+icmp+name+net-unreachable+send) command to disable the device to send ICMP network unreachable packets.

As shown in the preceding figure, the local device replies with an ICMP network unreachable packet only when the [**fib-miss-report enable**](cmdqueryname=fib-miss-report+enable) and [**icmp name net-unreachable send**](cmdqueryname=icmp+name+net-unreachable+send) commands are run.
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**fib-miss-report enable**](cmdqueryname=fib-miss-report+enable)
   
   
   
   The device is enabled to send FibMiss packets to the interface board's CPU.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.