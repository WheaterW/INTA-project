Configuring RIPng to Advertise Default Routes
=============================================

Configuring RIPng to Advertise Default Routes

#### Context

You can configure a RIPng device to advertise RIPng default routes by specifying the **only** or **originate** parameter as required. Alternatively, you can specify the cost of the default routes to be advertised.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface mode.
4. Configure RIPng to advertise default routes.
   
   
   ```
   [ripng default-route](cmdqueryname=ripng+default-route) { only | originate } [ cost cost-value | tag tag-value ]* 
   ```
   
   
   
   Configure RIPng to advertise default routes according to networking conditions:
   
   * **only**: The RIPng device is configured to advertise only IPv6 default routes (::/0), suppressing the advertisement of other routes.
   * **originate**: The RIPng device is configured to advertise IPv6 default routes (::/0) without affecting the advertisement of other routes.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The RIPng device advertises generated RIPng default routes using Update messages through a specified interface, regardless of whether these routes exist in the local IPv6 routing table.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```