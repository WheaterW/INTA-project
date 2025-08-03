Configuring VTY User Interfaces to Support SSH
==============================================

STelnet is based on SSH2. When the client and the server set up a secure connection after negotiation, the client can log in to the server in the same way as using Telnet.

#### Context

Perform the following steps on the device that functions as an SSH server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ]
   
   
   
   One or more VTY user interface views are displayed.
3. Run [**authentication-mode**](cmdqueryname=authentication-mode) **aaa**
   
   
   
   The authentication mode is set to AAA authentication.
4. Run [**protocol inbound**](cmdqueryname=protocol+inbound) { **ssh** | **all** }
   
   
   
   The VTY user interfaces are configured to support SSH.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring VTY user interfaces to support SSH, you must set the authentication mode to AAA authentication for the user interfaces. If you do not set the authentication mode to AAA authentication, the [**protocol inbound**](cmdqueryname=protocol+inbound) { **ssh** | **all** } command does not take effect.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.