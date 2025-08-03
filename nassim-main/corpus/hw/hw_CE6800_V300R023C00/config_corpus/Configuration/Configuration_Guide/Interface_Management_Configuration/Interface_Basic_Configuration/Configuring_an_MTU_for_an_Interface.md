Configuring an MTU for an Interface
===================================

Configuring an MTU for an Interface

#### Context

The size of each data packet is limited at the network layer. Upon receiving an IP packet to be forwarded, the network layer checks to which local interface it needs to send the packet and obtains the maximum transmission unit (MTU) of the interface. The network layer then compares the MTU with the packet length. If the packet length is longer than the MTU, the network layer fragments the packet into chunks no longer than the MTU.

An MTU value determines the maximum number of bytes that an interface can send each time. A suitable MTU is therefore necessary for normal and efficient communication between network devices.

* If the MTU is too small and the size of packets is large, the packets may be broken into many fragments and discarded by QoS queues. This affects normal data transmission.
* If the MTU of the local interface is too large and the size of the packets sent by the interface exceeds the MTU supported by a transit node or a receiver, the transit node or receiver fragments the packets or may even discard them. This affects the network load and normal data transmission.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure an MTU for the interface.
   
   
   ```
   [mtu](cmdqueryname=mtu) mtu
   ```
   
   By default, the MTU is 1500 bytes. The default value varies according to hardware and interfaces. You can run the **display default-parameter interface** command to view the default value. To ensure that large packets are not dropped due to MTU mismatch, perform this step to forcibly fragment large packets.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface**](cmdqueryname=display+interface) { *interface-name* | *interface-type* *interface-number* } command to check the running status of an interface.