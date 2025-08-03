Configuring the Interval for Sending Update Messages and the Maximum Number of Messages to Be Sent
==================================================================================================

Configuring the Interval for Sending Update Messages and the Maximum Number of Messages to Be Sent

#### Context

You can optimize the RIPng network performance by configuring the interval for sending messages as well as the maximum number of RIPng messages to be sent. Perform the following steps on a RIPng device:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure the interval for sending RIPng messages and the maximum number of messages to be sent.
   
   
   ```
   [ripng pkt-transmit](cmdqueryname=ripng+pkt-transmit) { interval interval | number pkt-count }*
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```