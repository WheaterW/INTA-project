(Optional) Configuring a Rate Limit Mode for Services in a Domain
=================================================================

(Optional) Configuring a Rate Limit Mode for Services in a Domain

#### Context

You can configure different rate limit modes for upstream and downstream EDSG service traffic of users who go online from an AAA domain. To locate information about EDSG services and users whose traffic is discarded due to rate limiting, enable the function of reporting dropped EDSG service traffic.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**aaa**](cmdqueryname=aaa) command to enter the AAA view.
3. Run the [**domain**](cmdqueryname=domain) *domain-name* command to enter the domain view.
4. Run the [**service rate-limit-mode**](cmdqueryname=service+rate-limit-mode) { **car** | **user-queue** } { **inbound** | **outbound** } command to configure a rate limit mode for upstream and downstream EDSG service traffic of online users.
5. (Optional) Run the [**quit**](cmdqueryname=quit) command to return to the AAA view.
6. (Optional) Run the [**quit**](cmdqueryname=quit) command to return to the system view.
7. (Optional) Run the **[**value-added-service edsg report-car-dropped-flow enable**](cmdqueryname=value-added-service+edsg+report-car-dropped-flow+enable)** command to enable the function of reporting CAR-dropped EDSG service traffic.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.