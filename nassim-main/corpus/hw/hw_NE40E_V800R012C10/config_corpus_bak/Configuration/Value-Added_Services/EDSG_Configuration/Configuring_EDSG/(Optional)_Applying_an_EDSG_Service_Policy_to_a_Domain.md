(Optional) Applying an EDSG Service Policy to a Domain
======================================================

If no EDSG service policy is delivered from the policy server, use the service policy group configured in the AAA domain.

#### Context

After configuring an EDSG service policy locally, you can bind it to the service policy group and apply it to an AAA domain. If no service policy is delivered from the policy server, the service policy group bound to the AAA domain is used. If the policy server delivers a service policy, the service policy delivered by the policy server is used.

Before configuring this function, complete the task of [Configuring an EDSG Service Policy Locally](dc_ne_edsg_cfg_0007.html).


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the **[**service-policy-group**](cmdqueryname=service-policy-group)** **group-name** command to create a service policy group and enter the service policy group view.
3. Run the **service-policy** *policy-name* command to bind an EDSG service policy to the service policy group.
4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
5. Run the [**aaa**](cmdqueryname=aaa) command to enter the AAA view.
6. Run the [**domain**](cmdqueryname=domain) *domain-name* command to enter the AAA domain view.
7. Run the **service-policy-group** *group-name* command to apply the service policy group to the AAA domain.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.