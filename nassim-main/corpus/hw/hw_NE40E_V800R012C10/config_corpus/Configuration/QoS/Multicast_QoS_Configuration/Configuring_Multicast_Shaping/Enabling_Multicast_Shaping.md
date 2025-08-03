Enabling Multicast Shaping
==========================

When a multicast source is busy, excessive jitter may occur. In this case, you can configure multicast shaping to limit the jitter of the multicast source to an acceptable range.

#### Context

Multicast shaping can be enabled globally or on an interface. When multicast shaping is enabled globally on the Router, this function is enabled on all interfaces.


#### Procedure

* Enable multicast shaping globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast shaping enable**](cmdqueryname=multicast+shaping+enable)
     
     
     
     Multicast shaping is enabled.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable multicast shaping on an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**multicast shaping enable**](cmdqueryname=multicast+shaping+enable)
     
     
     
     Multicast shaping is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.