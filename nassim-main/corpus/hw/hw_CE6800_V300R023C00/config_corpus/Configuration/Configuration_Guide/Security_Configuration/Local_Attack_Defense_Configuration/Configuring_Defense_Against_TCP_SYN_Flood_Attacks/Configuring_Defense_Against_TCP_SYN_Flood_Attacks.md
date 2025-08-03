Configuring Defense Against TCP SYN Flood Attacks
=================================================

Configuring Defense Against TCP SYN Flood Attacks

#### Context

With defense against TCP SYN flood attacks enabled, the device rate-limits the received TCP SYN packets, discarding any that exceeds the limit.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable defense against TCP SYN flood attacks.
   
   
   ```
   [anti-attack tcp-syn enable](cmdqueryname=anti-attack+tcp-syn+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can also run the [**anti-attack enable**](cmdqueryname=anti-attack+enable) command in the system view to enable attack defense against all attack packets, including TCP SYN flood attack packets.
3. Configure the limit rate for TCP SYN packets.
   
   
   ```
   [anti-attack tcp-syn car](cmdqueryname=anti-attack+tcp-syn+car) [cir](cmdqueryname=cir) cir-num
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display anti-attack statistics**](cmdqueryname=display+anti-attack+statistics) [**tcp-syn**](cmdqueryname=tcp-syn) command to check statistics relating to defense against TCP SYN flood attacks.