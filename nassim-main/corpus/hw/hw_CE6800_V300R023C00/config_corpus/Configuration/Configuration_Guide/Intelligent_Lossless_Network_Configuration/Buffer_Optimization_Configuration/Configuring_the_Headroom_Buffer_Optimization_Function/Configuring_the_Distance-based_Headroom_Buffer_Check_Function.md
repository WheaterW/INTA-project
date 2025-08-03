Configuring the Distance-based Headroom Buffer Check Function
=============================================================

Configuring the Distance-based Headroom Buffer Check Function

#### Context

The distance-based headroom buffer check function calculates the theoretically required headroom buffer space based on the configured long-distance mode (that is, link distance) and interface rate. The purpose of this function is to help avoid packet loss, which may occur if the required headroom buffer space is greater than the remaining buffer space of the plane where the current interface resides. After the distance-based headroom buffer check function is enabled on the interfaces at both ends of a direct link, the interfaces can send detection packets to each other to calculate the required headroom buffer space for lossless transmission on the link.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure the long-distance mode for the interface and enable the distance-based headroom buffer check function.
   
   
   ```
   [long-distance mode](cmdqueryname=long-distance+mode) { level-1 | level-10 | level-25 | level-50 | level-100 }
   ```
   
   By default, the distance-based headroom buffer check function is disabled. After this function is enabled, the interface automatically sends a detection packet to measure the required headroom buffer space for lossless transmission on the current link.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For successful measurement of the required headroom buffer space, you must configure the same long-distance mode for the interfaces at both ends of a link and ensure that the link status of the interfaces is normal.
4. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```