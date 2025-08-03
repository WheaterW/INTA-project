Applying the QoS Profile to a Domain
====================================

Before applying a QoS profile to a domain on an NE40E that functions as an LNS, ensure that a QoS profile has been created. L2TP user traffic can be scheduled only after the QoS profile is applied.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The view of the domain where the L2TP users reside is displayed.
4. Run [**qos-profile**](cmdqueryname=qos-profile) *profile-name* { **inbound** | **outbound** } **lns-gts**
   
   
   
   The QoS profile is applied to the domain, and the LNS scheduling mode is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.