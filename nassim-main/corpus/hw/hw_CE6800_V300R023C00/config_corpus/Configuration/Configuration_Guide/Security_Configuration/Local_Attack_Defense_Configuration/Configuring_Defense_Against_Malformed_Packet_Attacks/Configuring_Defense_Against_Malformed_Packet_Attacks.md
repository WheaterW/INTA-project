Configuring Defense Against Malformed Packet Attacks
====================================================

Configuring Defense Against Malformed Packet Attacks

#### Context

With defense against malformed packet attacks enabled, the device analyzes the received packets sent to the CPU and determines whether the packets are one of the several types of malformed packets, discarding them if so.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable defense against malformed packet attacks.
   
   
   ```
   [anti-attack abnormal enable](cmdqueryname=anti-attack+abnormal+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can also run the [**anti-attack enable**](cmdqueryname=anti-attack+enable) command in the system view to enable attack defense against all attack packets, including malformed packets.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display anti-attack statistics**](cmdqueryname=display+anti-attack+statistics) [**abnormal**](cmdqueryname=abnormal) command to check statistics relating to defense against malformed packet attacks on the device.