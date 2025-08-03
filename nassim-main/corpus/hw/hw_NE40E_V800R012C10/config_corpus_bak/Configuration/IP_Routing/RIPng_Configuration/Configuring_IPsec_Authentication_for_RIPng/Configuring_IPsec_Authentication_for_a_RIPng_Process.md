Configuring IPsec Authentication for a RIPng Process
====================================================

Configuring IP security (IPsec) authentication in the RIPng
view is one of the methods used to configure IPsec authentication
for RIPng.

#### Context

After IPsec authentication is configured in the RIPng
view, all interfaces in this RIPng process perform IPsec authentication
on RIPng packets received and to be sent.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ]
   
   
   
   The RIPng view is displayed.
3. Run [**ipsec sa**](cmdqueryname=ipsec+sa) *sa-name*
   
   
   
   IPsec authentication is enabled, and
   the name of a security association (SA) is specified.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The
   configuration is committed.