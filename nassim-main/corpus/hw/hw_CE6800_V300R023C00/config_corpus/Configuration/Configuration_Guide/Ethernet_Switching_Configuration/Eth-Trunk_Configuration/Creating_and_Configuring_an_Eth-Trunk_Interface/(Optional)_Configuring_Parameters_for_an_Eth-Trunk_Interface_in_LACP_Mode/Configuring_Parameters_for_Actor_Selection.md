Configuring Parameters for Actor Selection
==========================================

Configuring Parameters for Actor Selection

#### Context

LACP system priorities determine the sequence in which devices at two ends of an Eth-Trunk select active interfaces to join the Eth-Trunk. The device with a higher LACP system priority acts as the Actor. When the LACP system priorities of the two ends of an Eth-Trunk are the same, you can configure an LACP system ID to determine the Actor.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the LACP system priority.
   
   
   ```
   [lacp priority](cmdqueryname=lacp+priority) priority
   ```
   
   A smaller value indicates a higher the priority.
3. Enter the view of an Eth-Trunk interface.
   
   
   ```
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
4. Configure an LACP system ID for the Eth-Trunk interface.
   
   
   ```
   [lacp system-id](cmdqueryname=lacp+system-id) mac-address
   ```
   
   
   
   By default, the LACP system ID of an Eth-Trunk is the system bridge MAC address. You can run the [**display bridge mac-address**](cmdqueryname=display+bridge+mac-address) command to view the system bridge MAC address.
   
   A smaller LACP system ID indicates a higher priority.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```