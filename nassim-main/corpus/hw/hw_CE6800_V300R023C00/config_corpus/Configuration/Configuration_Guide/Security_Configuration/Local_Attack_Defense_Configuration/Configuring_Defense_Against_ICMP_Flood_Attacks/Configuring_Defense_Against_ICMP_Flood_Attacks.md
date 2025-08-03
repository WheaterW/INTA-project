Configuring Defense Against ICMP Flood Attacks
==============================================

Configuring Defense Against ICMP Flood Attacks

#### Context

With defense against ICMP flood attacks enabled, the device rate-limits the received ICMP messages, discarding any that exceeds the limit.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable defense against ICMP flood attacks.
   
   
   ```
   [anti-attack icmp-flood enable](cmdqueryname=anti-attack+icmp-flood+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can also run the [**anti-attack enable**](cmdqueryname=anti-attack+enable) command in the system view to enable attack defense against all attack packets, including ICMP flood attack packets.
3. Configure the rate limit for ICMP flood attack packets.
   
   
   ```
   [anti-attack icmp-flood car](cmdqueryname=anti-attack+icmp-flood+car) [cir](cmdqueryname=cir) cir-num
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display anti-attack statistics**](cmdqueryname=display+anti-attack+statistics) [**icmp-flood**](cmdqueryname=icmp-flood) command to check statistics relating to defense against ICMP flood attacks.