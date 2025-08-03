Configuring Defense Against UDP Flood Attacks
=============================================

Configuring Defense Against UDP Flood Attacks

#### Context

With defense against UDP flood attacks enabled, the device discards the packets received from ports 7, 13, and 19.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable defense against UDP flood attacks.
   
   
   ```
   [anti-attack udp-flood enable](cmdqueryname=anti-attack+udp-flood+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can also run the [**anti-attack enable**](cmdqueryname=anti-attack+enable) command in the system view to enable attack defense against all attack packets, including UDP flood attack packets.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display anti-attack statistics**](cmdqueryname=display+anti-attack+statistics) [**udp-flood**](cmdqueryname=udp-flood) command to check statistics relating to defense against UDP flood attacks.