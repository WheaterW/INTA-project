(Optional) Configuring the Thresholds for Public IP Address Pool Usage in a Domain
==================================================================================

This section describes how to configure the upper and lower
thresholds for public IP address pool usage in a domain to calculate
pool usage status, which is sent to a Remote Authentication Dial-In
User Service (RADIUS) server.

#### Context

If a domain has public and private
network users, the Broadband Remote Access Server (BRAS) sends public
IP address pool status to the RADIUS server. The RADIUS server determines
whether a user is a public or private network user based on user information
and the public IP address pool status. The RADIUS server then sends
the corresponding user group name and IP address pool name or IP address
pool group name to the BRAS. The BRAS determines whether the user
is a public or private network user based on the received user group
name and assigns an IP address to the user from the received IP address
pool or IP address pool group. This section describes how to
configure the upper and lower thresholds for public IP address pool
usage in a domain to calculate public IP address pool status, which
is sent to the RADIUS server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**ip-pool usage-status threshold**](cmdqueryname=ip-pool+usage-status+threshold) **low** *low-threshold* **high** *high-threshold* [ **all** ]
   
   
   
   The upper and lower thresholds are configured for public
   IP address pool usage in an AAA domain to calculate public IP address
   pool status, which is sent to the RADIUS server.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command needs to be used with the [**ip-attribute public**](cmdqueryname=ip-attribute+public) command.
   
   In IP address pool view
   or IP address pool group view, run the [**ip-attribute public**](cmdqueryname=ip-attribute+public) command to configure the public network attribute of an IP
   address pool or an IP address pool group. After the configuration
   is complete, the IP address pool or pool group serves as a public
   IP address pool or pool group whose usage status is calculated.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.