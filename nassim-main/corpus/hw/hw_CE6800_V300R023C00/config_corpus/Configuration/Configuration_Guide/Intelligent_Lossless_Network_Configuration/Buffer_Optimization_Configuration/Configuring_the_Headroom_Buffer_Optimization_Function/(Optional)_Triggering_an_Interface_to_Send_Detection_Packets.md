(Optional) Triggering an Interface to Send Detection Packets
============================================================

(Optional) Triggering an Interface to Send Detection Packets

#### Context

After the distance-based headroom buffer check function is enabled on an interface, the detection may fail if the link is faulty or congested. In this case, you can manually trigger the interface to send detection packets for distance-based headroom buffer check when the link recovers. If the distance-based headroom buffer check function is not enabled on the remote interface, the local interface is unable to automatically complete detection even if it has the distance-based headroom buffer check function enabled. Therefore, you are advised to manually trigger an interface to send detection packets after operations that may cause link status changes, such as interface initialization, interface rate switching, and interface split/aggregation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Trigger the interface to send a detection packet for distance-based headroom buffer check.
   
   
   ```
   [start long-distance detect](cmdqueryname=start+long-distance+detect)
   ```
4. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```