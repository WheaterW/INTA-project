Configuring an EDSG Service Policy
==================================

You can configure different EDSG service policies to implement differentiated accounting and rate limiting for user access to different networks.

#### Context

To implement differentiated accounting and rate limiting for user access to different networks, you may need to configure multiple EDSG service policies. An EDSG service policy can be configured in either of the following modes:

1. Configuration delivery to the device from the policy server.
2. Local configuration: To implement differentiated accounting and rate limiting for two EDSG services, associate the corresponding service groups with the two EDSG service policies, bind different accounting schemes to the two EDSG service policies, and set bandwidth parameters for different traffic rate limits.

This section describes how to configure an EDSG service policy locally.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**service-policy cache update interval**](cmdqueryname=service-policy+cache+update+interval) *interval-value* command to configure an interval at which the EDSG cache policy template is updated.
3. (Optional) Run the [**value-added-service update-online-edsg rate-limit service-policy**](cmdqueryname=value-added-service+update-online-edsg+rate-limit+service-policy) [ **cache** [ *cache-policy-name* ] | **configuration** [ *configuration* ] ] command to manually trigger an update of bandwidth limit parameters for online EDSG services.
4. (Optional) Run the [**radius-attribute hw-policy-name support-type edsg**](cmdqueryname=radius-attribute+hw-policy-name+support-type+edsg) command to allow the HW-Policy-Name attribute to carry an EDSG service policy name.
5. (Optional) Configure user accounting packets to carry an EDSG service policy name.
   1. Run the [**radius-server group**](cmdqueryname=radius-server+group) **group-name** command to enter the RADIUS server group view.
   2. Run the [**radius-attribute include**](cmdqueryname=radius-attribute+include) **edsg-service-name accounting-request** command to configure user accounting packets to carry an EDSG service policy name.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**radius-attribute hw-policy-name support-type edsg**](cmdqueryname=radius-attribute+hw-policy-name+support-type+edsg) command has been configured, Huawei proprietary No. 95 attribute is carried in packets. If this command has not been configured, Huawei proprietary No. 185 attribute is carried in packets.
6. Run the [**service-policy**](cmdqueryname=service-policy) **name** *policy-name* **edsg** command to create an EDSG service policy and enter its view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the policy template name is case-sensitive, you need to run the [**service-policy name-case-sensitive enable**](cmdqueryname=service-policy+name-case-sensitive+enable) command first to enable case sensitivity for the EDSG service template name.
7. (Optional) Run the [**ip-type ipv6**](cmdqueryname=ip-type+ipv6) command to set the traffic statistic type to IPv6 for EDSG services.
8. Run the [**service-group**](cmdqueryname=service-group) *service-group-name* [ **inbound** | **outbound** ] [ **priority** *priority* ] command to configure the service group to be bound to the EDSG service policy.
   
   
   
   The service group must already exist. If not, run the [**service-group**](cmdqueryname=service-group) *service-group-name* command in the system view to create a service group.
9. Run the [**radius-server group**](cmdqueryname=radius-server+group) *group-name* command to configure the RADIUS server group to be bound to the EDSG service policy.
10. Run the [**authentication-scheme**](cmdqueryname=authentication-scheme) *authentication-scheme-name* command to configure an authentication scheme for the EDSG service policy.
11. Run the [**accounting-scheme**](cmdqueryname=accounting-scheme) *accounting-scheme-name* command to configure an accounting scheme for the EDSG service policy.
    
    
    
    Currently, EDSG services support only the RADIUS accounting and non-accounting modes.
    
    The device provides two fixed accounting schemes: default0 and default1. The two accounting schemes cannot be deleted but can be modified.
12. Run the [**rate-limit**](cmdqueryname=rate-limit) **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] [ **flow-queue-pbs** *flow-queue-pbs* ] ] { **inbound** | **outbound** } command to configure the bandwidth parameters for upstream and downstream traffic rate limiting of EDSG services.
13. (Optional) Configure a Diameter monitor key for the EDSG service policy based on the format of the monitor key delivered by the Diameter server.
    
    
    * Run the [**diameter monitor-key string**](cmdqueryname=diameter+monitor-key+string) *monitor-key-string* command to configure a Diameter monitor key in string format for the EDSG service policy.
      
      Before running this command, run the [**diameter monitor-key parse-mode**](cmdqueryname=diameter+monitor-key+parse-mode) **string** command in the system view to set the parsing mode of the Diameter monitor key to string.
    * Run the [**diameter monitor-key**](cmdqueryname=diameter+monitor-key) *monitor-key* command to configure a Diameter monitor key in integer format for the EDSG service policy.
      
      Before running this command, run the [**diameter monitor-key parse-mode**](cmdqueryname=diameter+monitor-key+parse-mode) **integer** command in the system view to set the parsing mode of the Diameter monitor key to integer.
14. (Optional) Run the [**service-class**](cmdqueryname=service-class) { **cs7** | **cs6** | **ef** | **af4** | **af3** | **af2** | **af1** | **be** } { **inbound** | **outbound** } command to configure a scheduling class in the upstream or downstream direction.
15. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.