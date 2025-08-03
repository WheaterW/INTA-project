Configuring RIPng to Advertise the Default Routes
=================================================

There are two methods of advertising RIPng default routes. You can configure a router to advertise RIPng default routes as required. Alternatively, you can specify the cost of the default routes to be advertised.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ripng default-route**](cmdqueryname=ripng+default-route) { **only** | **originate** } [ **cost** *cost* | **tag** *tag* ] \*
   
   
   
   RIPng is configured to advertise default routes.
   
   Specify either of the following parameters as required:
   
   * **only**: advertises only IPv6 default routes (::/0) and suppress the advertisement of other routes.
   * **originate**: advertises IPv6 default routes (::/0) without affecting the advertisement of other routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is submitted.

#### Follow-up Procedure

RIPng default routes are advertised in Update packets through the specified interface, regardless of whether these routes exist in the IPv6 routing table.