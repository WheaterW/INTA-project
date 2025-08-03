(Optional) Configuring EDSG Service Rate Limiting and Traffic Statistics Collection Policies
============================================================================================

(Optional) Configuring EDSG Service Rate Limiting and Traffic Statistics Collection Policies

#### Context

If EDSG service traffic consumes the user traffic bandwidth, run the **edsg traffic-mode rate together statistic together** command so that rate limiting is performed on user traffic after it is performed on service traffic. For example, when the service traffic bandwidth is 2 Mbit/s and the user traffic bandwidth is 5 Mbit/s, if a user accesses services and consumes 2 Mbit/s service traffic bandwidth, the user can only use the remaining 3 Mbit/s user traffic bandwidth to access other services.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**aaa**](cmdqueryname=aaa) command to enter the AAA view.
3. Run the [**domain**](cmdqueryname=domain) *domain-name* command to enter the domain view.
4. Run the [**edsg traffic-mode rate**](cmdqueryname=edsg+traffic-mode+rate) { **separate** | **together** } **statistic together** command to configure an EDSG service rate limit policy and a traffic statistics collection policy.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.