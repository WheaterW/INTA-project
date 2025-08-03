Configuring BFD Session Check for an IPv6 IS-IS Process
=======================================================

Configuring BFD Session Check for an IPv6 IS-IS Process

#### Context

If the Layer 2 network is normal but the Layer 3 network is faulty, IS-IS neighbor relationships can be established and routes can be delivered, but Layer 3 traffic may be lost. To solve this problem, enable the BFD session check function so that IS-IS neighbor relationships can be established only after a BFD session is established on the corresponding interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) process-id
   ```
3. Configure BFD session check for the current IS-IS process.
   
   
   ```
   [bfd session-up check](cmdqueryname=bfd+session-up+check)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To reduce the impact of traffic loss on services, you are advised to enable the BFD session check function for the IPv6 IS-IS process.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```