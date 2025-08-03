(Optional) Adjusting MSDP Peer Connection Parameters
====================================================

(Optional) Adjusting MSDP Peer Connection Parameters

#### Context

You can adjust the retry interval for establishing an MSDP peer relationship and KeepAlive parameters as required.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MSDP view.
   
   
   ```
   [msdp](cmdqueryname=msdp) [ vpn-instance vpn-instance-name ]
   ```
3. (Optional) Set the interval at which MSDP peers retry a connection setup with each other.
   
   
   ```
   [timer retry](cmdqueryname=timer+retry) timeRetryInterval
   ```
   
   By default, the interval for retrying MSDP peer connection setup is 30 seconds.
   
   A TCP connection needs to be immediately set up between MSDP peers when a new MSDP peer relationship is created, an ended MSDP peer connection is restarted, or a faulty MSDP peer attempts to re-set up a connection. You can run this command to flexibly adjust the interval at which MSDP peers retry a connection setup.
4. (Optional) Set a holdtime period for MSDP peer entries.
   
   
   ```
   [peer](cmdqueryname=peer) peer-address [hold-time-interval](cmdqueryname=hold-time-interval) holdtime-value
   ```
   
   By default, the holdtime period of MSDP peer entries is 90s.
   
   After an MSDP peer relationship is established, the devices at both ends generate MSDP peer entries, record MSDP peer information, and start the hold timer for the entries. The hold timer is reset each time a KeepAlive message is received from the MSDP peer and deleted when the connection is disabled.
5. (Optional) Set the interval for sending KeepAlive messages to the MSDP peer.
   
   
   ```
   [peer](cmdqueryname=peer) peer-address [keepalive-interval](cmdqueryname=keepalive-interval) keepalive-time-value
   ```
   
   By default, the interval for sending KeepAlive messages to the MSDP peer is 60 seconds.
   
   After an MSDP peer relationship is established, devices at both ends of the connection send KeepAlive messages and start the KeepAlive timer to control the interval for sending such messages. The local end sends a KeepAlive message to the peer and resets the KeepAlive timer whenever a KeepAlive period ends and deletes the timer when the connection is disabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The interval at which KeepAlive messages are sent must be shorter than the holdtime period of MSDP peer entries configured using the **[**peer**](cmdqueryname=peer)** *peer-address* **[**hold-time-interval**](cmdqueryname=hold-time-interval)** *holdtime-value* command on the peer.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```