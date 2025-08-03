(Optional) Configuring the Prepaid Function
===========================================

The prepaid function allows the RADIUS server to deliver an EDSG service with a specified time or traffic volume quota in advance. After the quota is exhausted, the BRAS reapplies for an EDSG service quota from the RADIUS server. When the RADIUS server returns a zero quota, the BRAS executes a deactivation or redirection policy. If a carrier wants users to pay in advance and reserve the time or volume quota, the carrier can configure the prepaid function. This section describes how to configure the prepaid function.

#### Context

An authentication scheme, an accounting scheme, and a RADIUS server group have been configured for the prepaid function of EDSG services (for details, see [AAA Configuration](dc_ne_aaa_cfg_0515.html)).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a prepaid profile.
   1. Run [**prepaid-profile**](cmdqueryname=prepaid-profile) *prepaid-profile-name*
      
      
      
      A prepaid profile is created, and the prepaid profile view is displayed.
   2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
      
      
      
      A RADIUS server group is bound to the prepaid profile.
   3. Run [**authentication-scheme**](cmdqueryname=authentication-scheme) *authentication-scheme-name*
      
      
      
      An authentication scheme is configured for the prepaid profile.
   4. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *string-value*
      
      
      
      An accounting scheme is configured for the prepaid profile.
      
      
      
      The BRAS provides two fixed accounting schemes: **default0** and **default1**. The two accounting schemes cannot be deleted but can be modified.
   5. Run [**password**](cmdqueryname=password) **cipher** *cipher-password*
      
      
      
      A password used for the BRAS to apply for an EDSG service quota from the RADIUS server group is configured.
   6. (Optional) Run [**threshold**](cmdqueryname=threshold) **time** *time-threshold* **seconds**
      
      
      
      A time threshold is configured for the BRAS to reapply for a time quota for EDSG services from the RADIUS server.
      
      
      
      When the remaining time quota of a user's EDSG service reaches a configured time threshold, the BRAS reapplies for a time quota for the EDSG service from the RADIUS server. When the RADIUS server returns a zero time quota, the BRAS executes a deactivation or redirection policy.
   7. (Optional) Run [**threshold**](cmdqueryname=threshold) **volume** *volume-threshold* { **kbytes** | **mbytes** | **bytes** }
      
      
      
      A traffic volume threshold is configured for the BRAS to reapply for a traffic volume quota for EDSG services from the RADIUS server.
      
      
      
      When the remaining traffic volume quota of a user's EDSG service reaches a configured traffic volume threshold, the BRAS reapplies for a traffic volume quota for the EDSG service from the RADIUS server. When the RADIUS server returns a zero traffic volume quota, the BRAS executes a deactivation or redirection policy.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) You can configure both the time and traffic volume thresholds for the BRAS to reapply for EDSG service quotas from the RADIUS server. Once the remaining time or traffic volume quota of a user's EDSG service reaches the corresponding configured threshold, the BRAS reapplies for an EDSG service quota from the RADIUS server. For example, if the time and traffic volume thresholds are respectively set to 60s and 5 Mbytes for a user:
      * When the remaining traffic volume quota of the user's EDSG service is 5 Mbytes but the remaining time quota of the EDSG service is greater than 60s, the BRAS reapplies for a traffic volume quota for the EDSG service from the RADIUS server.
      * When the remaining time quota of the user's EDSG service is 60s but the remaining traffic volume quota of the EDSG service is greater than 5 Mbytes, the BRAS reapplies for a time quota for the EDSG service from the RADIUS server.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. (Optional) Configure a policy used when the quota is exhausted as required.
   1. Configure a deactivation policy. When the quota of a user's EDSG service is exhausted, the BRAS deletes the EDSG service.
      
      
      1. Run the [**quota-out**](cmdqueryname=quota-out) **service deactivate** command to configure a deactivation policy.
      2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
      3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   2. Configure a redirection policy. When the quota of a user's EDSG service is exhausted, the user is redirected to a specified web page.
      
      
      1. Run the [**http-redirect-profile**](cmdqueryname=http-redirect-profile) *redirect-profile-name* command to create an HTTP redirection profile and enter the HTTP redirection profile view.
      2. Run the [**web-server**](cmdqueryname=web-server) **url** *redirect-url* command to configure a redirection web page.
      3. (Optional) Run the [**web-server**](cmdqueryname=web-server) **mode** { **get** | **post** } command to configure an HTTP access mode for the web server.
      4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
      5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
      6. Run the [**prepaid-profile**](cmdqueryname=prepaid-profile) *prepaid-profile-name* command to enter the prepaid profile view.
      7. Run the [**quota-out**](cmdqueryname=quota-out) **redirect** *redirect-profile-name* command to configure a redirection policy and specify an HTTP redirection profile.
      8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
      9. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. Apply the prepaid profile in the EDSG service policy view.
   1. Run [**service-policy**](cmdqueryname=service-policy) **name** *policy-name* **edsg**
      
      
      
      The EDSG service policy view is displayed.
      
      
      
      An EDSG service policy must have been configured. For details about how to configure an EDSG service policy, see [Configuring an EDSG Service Policy](dc_ne_edsg_cfg_0007.html).
   2. Run [**prepaid-profile**](cmdqueryname=prepaid-profile) *prepaid-profile-name*
      
      
      
      A prepaid profile is configured for the EDSG service policy.
5. (Optional) Run [**service volume-quota apply**](cmdqueryname=service+volume-quota+apply) { **inbound** | **outbound** }
   
   
   
   The traffic direction to which the EDSG service quota applies is configured.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.