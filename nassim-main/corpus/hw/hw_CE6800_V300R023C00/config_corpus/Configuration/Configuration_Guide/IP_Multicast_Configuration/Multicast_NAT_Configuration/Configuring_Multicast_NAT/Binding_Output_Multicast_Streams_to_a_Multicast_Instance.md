Binding Output Multicast Streams to a Multicast Instance
========================================================

Binding Output Multicast Streams to a Multicast Instance

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the multicast NAT binding view.
   
   
   ```
   [multicast-nat bind-list](cmdqueryname=multicast-nat+bind-list)
   ```
3. Bind output multicast streams to a multicast instance.
   
   
   ```
   [multicast-nat outbound](cmdqueryname=multicast-nat+outbound) id outbound-id [ name outbound-name ] bind instance id instance-id [ name instance-name ]
   ```
4. Exit the multicast NAT binding view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```