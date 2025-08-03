Configuring an Authorization Scheme
===================================

Configuring an authorization scheme is the prerequisite for authorizing users.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**authorization-scheme**](cmdqueryname=authorization-scheme) *authorization-scheme-name*
   
   
   
   An authorization scheme is created, and its view is displayed.
4. Run [**authorization-mode**](cmdqueryname=authorization-mode) *authorization-mode1* [ *authorization-mode2* [ *authorization-mode3* [ *authorization-mode4* ] ] ]
   
   
   
   An authorization mode is configured. If multiple authorization modes are configured in an authorization scheme, the authorization modes are used in the sequence in which they are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The next configured authorization mode is used only when the current one is unresponsive (for example, the server does not respond). If the current authorization succeeds or fails, the next authorization mode is not used.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.