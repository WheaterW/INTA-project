Checking a Smart Link Group's Links
===================================

Checking a Smart Link Group's Links

#### Context

If you need to check a Smart Link group's links without impacting normal services, you can configure a data flow forwarding policy for the Smart Link group to forcibly lock data flows to the secondary or primary link. After the check is complete, data traffic is switched back.

![](public_sys-resources/note_3.0-en-us.png) 

If data flows are locked to an interface, they cannot be automatically switched to another if the original interface fails. This can lead to traffic interruptions.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Smart Link group view.
   
   
   ```
   [smart-link group](cmdqueryname=smart-link+group) group-id
   ```
3. Lock data flows as required.
   
   
   * Lock data flows on the master interface.
     
     ```
     [smart-link](cmdqueryname=smart-link) [lock](cmdqueryname=lock)
     ```
   * Lock data flows on the slave interface.
     
     ```
     [smart-link](cmdqueryname=smart-link) [force](cmdqueryname=force)
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The **lock** and **force** keywords are mutually exclusive, and only one can be configured at a time. The **lock** keyword takes precedence over the **force** keyword. If you configure **force** and then **lock**, the **lock** keyword takes effect. You cannot configure **force** if **lock** has been configured.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```