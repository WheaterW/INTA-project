Configuring a Number for a FlexE Group
======================================

To ensure normal communication between interconnected devices, you need to configure the same group number for the FlexE groups to which the FlexE physical interfaces on both devices are added.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flexe group**](cmdqueryname=flexe+group) *group-index*
   
   
   
   A FlexE group is created, or the view of a specified FlexE group is displayed.
3. Run [**flexe-groupnum**](cmdqueryname=flexe-groupnum) *groupNum*
   
   
   
   A group number is configured for the FlexE group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.