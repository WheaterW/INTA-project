(Optional) Enabling the Captive Portal Function Based on EDSG Services
======================================================================

After an HTTP redirection profile is bound to a service policy, the captive portal function based on EDSG services is enabled. When users visit HTTP web pages matching service traffic, the service traffic is redirected to a specified page.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a redirection profile.
   1. Run [**http-redirect-profile**](cmdqueryname=http-redirect-profile) *profile-name*
      
      
      
      An HTTP redirection profile is created.
   2. Run [**web-server url**](cmdqueryname=web-server+url) *redirect-url*
      
      
      
      The destination link for user HTTP redirection is configured.
   3. (Optional) Run [**web-server redirect-limit**](cmdqueryname=web-server+redirect-limit) *limit-value* [ *limit-value* | **infinite** ]
      
      
      
      The number of times advertisements are forcibly pushed for an HTTP redirection profile is configured.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
3. Apply the redirection profile in the service policy view.
   1. Run [**service-policy name policy-name edsg**](cmdqueryname=service-policy+name+policy-name+edsg)
      
      
      
      An EDSG service policy profile is created and the EDSG service policy profile view is displayed.
   2. (Optional) Run [**web-server redirect-key user-ip-address user-ip-key**](cmdqueryname=web-server+redirect-key+user-ip-address+user-ip-key)
      
      
      
      The user IP address and name carried in the URL to which EDSG users are redirected in mandatory web authentication are configured.
   3. Run either of the following command to bind the redirection profile to the service policy view.
      
      
      * If users are required to be redirected to a specified page while visiting HTTP web pages matching service traffic, run the [**http-redirect-profile**](cmdqueryname=http-redirect-profile) *profile-name* command to bind the redirection profile to the service policy view
      * If the traffic matching the service needs to be redirected instantly after the service is activated, run the [**service force redirect**](cmdqueryname=service+force+redirect) *redirect-profile-name* command to bind the redirection profile to the service policy view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.