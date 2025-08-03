Configuring Load Balancing in a Smart Link Group
================================================

Configuring Load Balancing in a Smart Link Group

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MST region view.
   
   
   ```
   [stp region-configuration](cmdqueryname=stp+region-configuration)
   ```
3. Map VLANs to an instance.
   
   
   ```
   [instance](cmdqueryname=instance) instance-id [vlan](cmdqueryname=vlan) { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] }&<1-10>
   ```
   
   A region supports up to 60 instances, among which instance 0 is the default instance and does not need to be created.
   
   All VLANs are mapped to instance 0 by default.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the Smart Link group view.
   
   
   ```
   [smart-link group](cmdqueryname=smart-link+group) group-id
   ```
6. Configure the slave interface to send packets from the VLANs bound to the instance to implement load balancing.
   
   
   ```
   [load-balance instance](cmdqueryname=load-balance+instance) { instance-id1 [ to instance-id2 ] } &<1-10> [slave](cmdqueryname=slave)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
8. Check the status of the Smart Link group.
   
   
   ```
   [display smart-link group](cmdqueryname=display+smart-link+group) { all | group-id }
   ```