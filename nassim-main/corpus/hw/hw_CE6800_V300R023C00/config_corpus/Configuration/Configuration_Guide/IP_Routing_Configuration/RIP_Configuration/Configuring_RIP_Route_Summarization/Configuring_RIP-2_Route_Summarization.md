Configuring RIP-2 Route Summarization
=====================================

Configuring RIP-2 Route Summarization

#### Procedure

* Enable RIP-2 automatic route summarization.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a RIP process and enter the RIP view.
     
     
     ```
     [rip](cmdqueryname=rip) [ process-id ]
     ```
  3. Enable RIP-2 automatic route summarization.
     
     
     ```
     [summary](cmdqueryname=summary) [ always ]
     ```
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If the **always** parameter is specified, RIP-2 automatic route summarization takes effect, regardless of whether split horizon or poison reverse is configured.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure RIP-2 to advertise a summary route.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure RIP-2 to advertise a summary route (with a local IP address).
     
     
     ```
     [rip summary-address](cmdqueryname=rip+summary-address) ip-address mask [ avoid-feedback ]
     ```
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     After the **avoid-feedback** parameter is specified, the interface does not learn summary routes with the same IP address as the advertised summary route.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```