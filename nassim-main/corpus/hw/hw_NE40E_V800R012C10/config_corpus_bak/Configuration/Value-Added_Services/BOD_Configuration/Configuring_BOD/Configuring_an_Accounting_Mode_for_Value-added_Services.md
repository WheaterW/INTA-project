Configuring an Accounting Mode for Value-added Services
=======================================================

Operators can configure differentiated services and tariff policies for users.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *scheme-name*
   
   
   
   An accounting scheme is created.
4. Run [**accounting interim interval**](cmdqueryname=accounting+interim+interval) *interval* [ **second** ] [ **traffic** ][ **hash** ]
   
   
   
   A real-time accounting interval is configured. The **traffic** and **hash** parameters can be configured to prevent the server performance from deteriorating when the server receives a large number of real-time accounting packets.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the AAA view.
6. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
7. Run [**value-added-service account-type**](cmdqueryname=value-added-service+account-type) { **none** | **radius** *radius-server* | **default** }
   
   
   
   An accounting mode is configured for value-added services. The accounting mode can be none, RADIUS accounting, or default accounting.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.