Configuring Defense Against Fragmentation Attacks
=================================================

Configuring Defense Against Fragmentation Attacks

#### Context

With defense against fragmentation attacks enabled, the device rate-limits the received fragmented packets, discarding any that exceeds the limit.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable defense against fragmentation attacks.
   
   
   ```
   [anti-attack fragment enable](cmdqueryname=anti-attack+fragment+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can also run the [**anti-attack enable**](cmdqueryname=anti-attack+enable) command in the system view to enable attack defense against all attack packets, including fragmented packets.
3. Configure the rate limit for fragmented packets.
   
   
   ```
   [anti-attack fragment car](cmdqueryname=anti-attack+fragment+car) [cir](cmdqueryname=cir) cir-num
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display anti-attack statistics**](cmdqueryname=display+anti-attack+statistics) [**fragment**](cmdqueryname=fragment) command to check statistics relating to defense against fragmentation attacks on the device.