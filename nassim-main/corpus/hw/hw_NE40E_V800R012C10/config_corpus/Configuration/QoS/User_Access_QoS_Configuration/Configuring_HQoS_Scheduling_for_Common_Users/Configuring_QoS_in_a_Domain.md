Configuring QoS in a Domain
===========================

You can configure a rate limiting mode for common users and configure the service traffic of users in a domain not to participate in QoS scheduling for family users as required.

#### Context

After a rate limiting mode is configured for users, the system uses CAR or SQ parameters in the corresponding QoS profile for scheduling. If the service traffic of users in a specified domain does not participate in family-based traffic scheduling, the system performs service-specific bandwidth management.

In VS mode, this configuration is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   An AAA domain is created and its view is displayed.
   
   
   
   Here, *domain-name* specifies the domain to which the service needs to be mapped.
4. Run [**qos rate-limit-mode**](cmdqueryname=qos+rate-limit-mode) { **car** | **user-queue** } { **inbound** | **outbound** }
   
   
   
   A rate limiting mode is configured for common users.
   
   
   
   If a QoS profile with both [**car**](cmdqueryname=car) and [**user-queue**](cmdqueryname=user-queue) configured is applied to an AAA domain, the system checks whether the [**qos rate-limit-mode**](cmdqueryname=qos+rate-limit-mode) command is configured in the domain. If the **qos rate-limit-mode car** command is configured, the system uses CAR parameters in the QoS profile for scheduling. If the **qos rate-limit-mode user-queue** command is configured in the domain, the system uses SQ parameters in the QoS profile for scheduling. If the **qos rate-limit-mode** command is not configured, CAR and SQ parameters in the QoS profile are applied to upstream and downstream traffic respectively by default.
5. (Optional) Run **[**qos user-queue granularity**](cmdqueryname=qos+user-queue+granularity)** **granularity-value**
   
   
   
   The user-queue bandwidth granularity is configured for users who go online from the specified domain.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the AAA view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
10. (Optional) Run [**access-user user-queue recovery**](cmdqueryname=access-user+user-queue+recovery) **disable**
    
    
    
    The automatic switchback function is disabled when user-queue resources fail to be applied for.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.