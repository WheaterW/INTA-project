Binding a Policy Server to a Domain
===================================

This section describes the procedure for binding a policy server to a domain.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run either of the following commands:
   
   
   * To bind a RADIUS server group to the domain, run the [**radius-server group**](cmdqueryname=radius-server+group) *group-name* command.
   * To bind a Diameter server group to the domain, run the [**diameter-server group**](cmdqueryname=diameter-server+group) *group-name* command.
5. Run [**user-group**](cmdqueryname=user-group) *group-name*
   
   
   
   A user group is bound to the domain.
6. Run [**billing-server type**](cmdqueryname=billing-server+type) { **1** | **2** }
   
   
   
   An accounting server type is specified.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Value 1 indicates that the accounting server supports dynamic switching of value-added service policy templates. After the policy server releases a new template, users are not charged with the corresponding tariff level, and a new accounting service is generated.
   * Value 2 indicates that the accounting server supports normal switching of value-added service policy templates. After the policy server releases a new template, users can only obtain the QoS parameters in it. Real-time accounting packets are sent after original bandwidth restrictions are updated.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.