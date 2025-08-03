Adjusting the Detection Time of a BFD Session
=============================================

Adjusting the Detection Time of a BFD Session

#### Context

When you set up a BFD session, you can adjust the interval for sending and receiving BFD packets, as well as the local detection multiplier according to network conditions and performance requirements.

To reduce system resource consumption, the system automatically changes the local intervals for sending and receiving BFD packets to random values greater than 1000 ms after a BFD session down event is detected. When the BFD session goes up again, the configured intervals are restored.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BFD session view.
   ```
   [bfd](cmdqueryname=bfd) session-name
   ```
   
   The BFD session specified by *session-name* must have been created before you run this command.
3. Set a desired minimum interval for sending BFD packets.
   ```
   [min-tx-interval](cmdqueryname=min-tx-interval) tx-interval
   ```
   
   The default minimum interval for sending BFD packets is 1000 milliseconds.
4. Set a desired minimum interval for receiving BFD packets.
   ```
   [min-rx-interval](cmdqueryname=min-rx-interval) rx-interval
   ```
   
   The default minimum interval for receiving BFD packets is 1000 milliseconds.
5. Set a local detection multiplier after the BFD session goes up.
   ```
   [detect-multiplier](cmdqueryname=detect-multiplier) multiplier
   ```
   
   The default local detection multiplier is 3 after the BFD session goes up.
6. (Optional) Configure the local detection multiplier used for BFD session negotiation.
   ```
   [negotiation-detect-multiplier](cmdqueryname=negotiation-detect-multiplier) detect-multiplier-value
   ```
   
   By default, the detection multiplier used for BFD session negotiation is 50.
7. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

![](public_sys-resources/note_3.0-en-us.png) 

It is recommended that the default minimum intervals for sending and receiving BFD packets and local detection multiplier be used.



#### Verifying the Configuration

Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** { [ **for-ip** ] | **for-ipv6** } | **discriminator** *discr-value* | **dynamic** | **peer-ip** { *peer-ip* [ **vpn-instance** *vpn-instance-name* ] | **default-ip** } | **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-instance-name* ] | **static** { [ **for-ip** ] | **for-ipv6** } | **static-auto** } [ **verbose** ] command to check BFD session information.