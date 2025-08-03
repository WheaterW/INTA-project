Configuring the Maximum Length of RIP Messages
==============================================

Configuring the Maximum Length of RIP Messages

#### Context

You can increase the maximum length of RIP messages that can be sent to improve bandwidth utilization.

![](public_sys-resources/notice_3.0-en-us.png) 

You can run the [**rip max-packet-length**](cmdqueryname=rip+max-packet-length) command to set the maximum length of RIP messages to be greater than 512 bytes only when the remote end is capable of accepting RIP messages of such a length.

Huawei devices may fail to communicate with non-Huawei devices after the RIP message length is increased. Therefore, exercise caution when executing this command.

By default, a RIP message can contain a maximum of 25 routes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure the maximum length of RIP messages.
   
   
   ```
   [rip max-packet-length](cmdqueryname=rip+max-packet-length) { value | mtu }
   ```
   
   
   
   By default, the maximum length of RIP messages is 512 bytes. **mtu** indicates the maximum allowable length of RIP messages.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```