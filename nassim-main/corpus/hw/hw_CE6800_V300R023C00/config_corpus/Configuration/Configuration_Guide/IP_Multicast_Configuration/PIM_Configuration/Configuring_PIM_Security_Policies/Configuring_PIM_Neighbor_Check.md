Configuring PIM Neighbor Check
==============================

Configuring PIM Neighbor Check

#### Context

To improve message transmission security, you can enable PIM neighbor check for received or sent Join/Prune and Assert messages or for both received and sent Join/Prune and Assert messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
3. Enable the device to check whether received Join/Prune and Assert messages are from PIM neighbors.
   
   
   ```
   [neighbor-check receive](cmdqueryname=neighbor-check+receive)
   ```
4. Enable the device to check whether Join/Prune and Assert messages are to be sent to PIM neighbors.
   
   
   ```
   [neighbor-check send](cmdqueryname=neighbor-check+send)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```