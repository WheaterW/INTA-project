Creating a Multicast NAT Instance
=================================

Creating a Multicast NAT Instance

#### Context

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. This section describes how to create a multicast NAT instance.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a multicast NAT instance and enter the multicast NAT instance view.
   
   
   ```
   [multicast-nat instance](cmdqueryname=multicast-nat+instance) id instance-id [ name instance-name ]
   ```
3. Exit the multicast NAT instance view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```