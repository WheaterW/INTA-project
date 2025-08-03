Configuring Rail Group
======================

Configuring Rail Group

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a Rail Group port group and enter the view of the Rail Group port group.
   
   
   ```
   [rail-group](cmdqueryname=rail-group) group-name
   ```
3. Configure the interface index allocation mode for Rail Group.
   
   
   ```
   [rail-group mode](cmdqueryname=rail-group+mode) { auto | manual }
   ```
   
   By default, the interface index allocation mode for Rail Group is **auto**.
4. Add interfaces to the Rail Group port group.
   
   
   * If the interface index allocation mode is auto, you cannot manually specify the index of an interface in a Rail Group port group when adding the interface to the Rail Group port group.
     ```
     [group-member interface](cmdqueryname=group-member+interface) { { interface-name | interface-type interface-number } [ to { interface-name | interface-type interface-number } ] } &<1-32>
     ```
   * If the interface index allocation mode is manual, you need to manually specify the index of an interface in a Rail Group port group when adding the interface to the Rail Group port group.
     ```
     [group-member interface](cmdqueryname=group-member+interface) { interface-name | interface-type interface-number } index index-value
     ```![](public_sys-resources/note_3.0-en-us.png) 
   * Only physical interfaces can be added to a Rail Group port group.
   * A physical interface that has been added to an Eth-Trunk interface cannot be added to a Rail Group port group.
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Enable the Rail Group function.
   
   
   ```
   [load-balance ecmp rail-group enable](cmdqueryname=load-balance+ecmp+rail-group+enable)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **[**display rail-group status**](cmdqueryname=display+rail-group+status)** [ **group-name** *group-name* ] command to check the Rail Group configuration and status.