Configuring U-BFD Echo
======================

Configuring U-BFD Echo

#### Procedure

1. Enable BFD globally.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enable BFD globally and enter the global BFD view.
      
      
      ```
      [bfd](cmdqueryname=bfd)
      ```
      
      You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable BFD globally.
2. Create a U-BFD Echo session.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Create a U-BFD Echo session and enter the BFD session view.
      
      
      
      On an IPv4 network:
      
      
      
      ```
      [bfd](cmdqueryname=bfd) sessname-value bind peer-ip ip-address [ vpn-instance vpn-name ] interface { interface-name | interface-type interface-number } [ source-ip ip-address ] one-arm-echo [ destination-ip ip-address ]
      ```
      
      On an IPv6 network:
      
      ```
      [bfd](cmdqueryname=bfd) sessname-value bind peer-ipv6 ipv6-address [ vpn-instance vpn-name ] interface { interface-name | interface-type interface-number } [ source-ipv6 source-ipv6 ] one-arm-echo [ destination-ipv6 destination-ipv6-value ]
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      The CE6885-LL in low-latency mode does not support IPv6 functions.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   U-BFD Echo sessions apply only to single-hop BFD detection.
3. Configure a local discriminator for the BFD session.
   
   
   ```
   [discriminator](cmdqueryname=discriminator) local discr-value
   ```
   
   
   
   You only need to configure the local discriminator because the U-BFD Echo function is configured only on the device supporting BFD.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **discriminator** *discr-value* | **dynamic** | **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] | **static** } [ **verbose** ] command to check BFD session information.
* Run the [**display bfd statistics**](cmdqueryname=display+bfd+statistics) command to check global BFD statistics.
* Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) { **all** | **static** | **dynamic** | **discriminator** *discr-value* | **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] } command to check BFD session statistics.