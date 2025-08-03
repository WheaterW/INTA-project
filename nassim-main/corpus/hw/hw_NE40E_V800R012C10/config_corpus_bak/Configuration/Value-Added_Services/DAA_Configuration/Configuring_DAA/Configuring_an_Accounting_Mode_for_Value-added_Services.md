Configuring an Accounting Mode for Value-added Services
=======================================================

Carriers can configure differentiated services and tariff policies for different users.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *acct-scheme-name*
   
   
   
   An accounting scheme is created.
4. Run [**accounting interim interval**](cmdqueryname=accounting+interim+interval) *interval* [ **second** ] [ **traffic** ] [ **hash** ]
   
   
   
   An interval for real-time accounting and conditions for sending real-time accounting packets are configured, and real-time accounting packets are hashed for the accounting scheme.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the AAA view.
6. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
7. Run [**value-added-service account-type**](cmdqueryname=value-added-service+account-type) { **none** | **radius** *radius-server* | **default** }
   
   
   
   An accounting mode is configured for value-added services.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The accounting mode can be default accounting, non-accounting, or RADIUS accounting.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.