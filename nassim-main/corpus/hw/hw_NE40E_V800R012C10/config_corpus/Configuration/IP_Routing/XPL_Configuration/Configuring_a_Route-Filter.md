Configuring a Route-Filter
==========================

A route-filter can use its condition clause to filter routes and use its action clause to set or modify route attributes of the routes that match the condition clause. This section describes how to configure route-filters.

#### Usage Scenario

Route-filters include various matching rules and can flexibly apply to a variety of scenarios. Route-filters consist of condition clauses and action clauses, use condition clauses to filter routes based on sets or a single element, and use action clauses to modify route attributes of the routes that meet matching rules.

* Condition clause: A condition clause is defined based on a set or single element, beginning with an introductory condition clause in most cases. The action specified in the action clause is applied only to the routes that match the conditions specified in the condition clause.
* Action clause: An action clause specifies an action to be applied to the routes that match the conditions specified in the condition clause. An action clause determines whether the routes match the route-filter or modifies their route attributes.


#### Pre-configuration Tasks

Before configuring route-filters, complete the following tasks:

* Determine whether to configure [route attribute sets](dc_vrp_xpl_cfg_0003.html).
* Configure a global variable set if some values need to be frequently used.


#### Procedure

* Configure a route-filter using the paragraph-by-paragraph editing mode.
  1. Run the [**edit xpl route-filter**](cmdqueryname=edit+xpl+route-filter) *route-filter-name* command to enter the route-filter paragraph-by-paragraph editing view.
  2. Press **i** to enter the text editing mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Sets or route-filters can be configured only in the text editing mode. If you exit from the text editing mode, you can perform shortcut key operations only.
  3. Configure a start clause in the format of [**xpl route-filter**](cmdqueryname=xpl+route-filter) *route-filter-name*($*var1*,$*var2*,...) for a route-filter in the route-filter paragraph-by-paragraph editing view. The parameters are optional and can be used in condition or action clauses.
  4. Configure a matching condition in the format of **if**+condition clause+**then** and connect the conditions with the Boolean operator **NOT**, **AND**, or **OR**. The keyword **then** is followed by an action clause. For details about condition clauses, see [Condition Clauses](dc_vrp_xpl_cfg_0016.html).
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Route-filters can have only action clauses and can also be empty (configured with only a start clause and an end clause). In this case, the default action **refuse** is used. If an empty route-filter is specified in another route-filter using a **call** clause, the empty route-filter does not take effect.
  5. Configure an action clause. For details about action clauses, see [Action Clauses](dc_vrp_xpl_cfg_0017.html).
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Multiple action clauses can be configured if they do not conflict with each other.
     + Action clauses (excluding **approve**, **refuse**, **finish**, **break**, and **call route-filter** *route-filter-name*) must follow **apply**.
  6. (Optional) Configure **elseif**+condition clause+**then** to filter the routes that fail to match the conditions specified in the **if** clause and specify an action clause for the **elseif** clause. You can configure multiple **elseif** clauses to filter the routes that fail to meet the previous matching rule or configure an **else** clause to match the routes that fail to meet all the previous matching rules. Each **if**, **elseif**, or **else** clause must be followed by an action clause.
  7. Configure a conclusive condition clause (**endif**).
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Steps 2 to 5 describe how to configure an **if** condition branch. One route-filter can have multiple **if** condition branches, and the **if** condition branches can be configured as follows:
     
     + One **if** condition branch is followed by another.
     + The **if**+condition clause+**then** or **elseif**+condition clause+**then** is followed by another **if** condition branch. Such a configuration further filters routes that match **if**+condition clause+**then** or **elseif**+condition clause+**then** against the second **if** condition branch.
     
     Regardless of the configuration mode, route filtering continues until **finish**, **break**, **refuse,** or the last **if** condition branch.
  8. Configure a conclusive clause (**end-filter**) for the route-filter.
  9. Press **Esc** to exit from the text editing mode.
  10. Press **:wq** and **Enter** to save the configurations and exit from the global variable set paragraph-by-paragraph editing view.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      A message is displayed for you to confirm whether to commit the configurations when you attempt to exit from the global variable set paragraph-by-paragraph editing view. To commit the configurations, press **Y**.
      
      To exit from the global variable set paragraph-by-paragraph editing view without saving the configurations, press **:q!** and **Enter**.
* Configure a route-filter using the line editing mode.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**xpl route-filter**](cmdqueryname=xpl+route-filter) *route-filter-name* command to enter the route-filter view.
  3. Run the [**if**](cmdqueryname=if) [ **not** ] *condition-clause* [ { **and** | **or** } [ **not** ] *condition-clause* ] \* **then** command to configure matching rules for the route-filter.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Route-filters can have only action clauses and can also be empty (only configured with **xpl route-filter** and [**end-filter**](cmdqueryname=end-filter)). In this case, the default action **refuse** is used. If an empty route-filter is specified in another route-filter using a **call** clause, the empty route-filter does not take effect.
  4. Configure an action using any of the following commands for the routes that meet matching rules:
     
     
     + [**apply**](cmdqueryname=apply) *action-clause*: sets a route attribute for the routes that meet matching rules.
     + [**approve**](cmdqueryname=approve): further filters the routes that meet the matching rules of the current **if** condition branch against the next **if** condition branch.
     + [**refuse**](cmdqueryname=refuse): denies routes that meet matching rules.
     + [**finish**](cmdqueryname=finish): completes route filtering and allows the routes that meet matching rules to match the route-filter.
     + [**call route-filter**](cmdqueryname=call+route-filter) *route-filter-name*: further matches the routes that meet the matching rules of the current route-filter against the specified route-filter.
     + [**break**](cmdqueryname=break): enables the device to exit from the current route-filter. If the current route-filter is referenced by a parent route-filter, the device keeps implementing remaining condition and action clauses of the parent route-filter.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Multiple action clauses can be configured if they do not conflict with each other.
  5. Run the [**elseif**](cmdqueryname=elseif) [ **not** ] *condition-clause* [ { **and** | **or** } [ **not** ] *condition-clause* ] \* **then** command to filter the routes that fail to meet the rules specified in the [**if**](cmdqueryname=if) command and specify an action for the routes using a command in Step 4. You can run the [**elseif**](cmdqueryname=elseif) command multiple times to filter the routes that fail to meet the previous matching rules or run the [**else**](cmdqueryname=else) command to match the routes that fail to meet all the previous matching rules in the same if condition branch. You can also run a command in Step 4 to set an action for these routes.
  6. Run the [**endif**](cmdqueryname=endif) command to conclude the configuration of the current **if** condition branch.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     An **if** condition branch begins with [**if**](cmdqueryname=if) and ends with [**endif**](cmdqueryname=endif). One route-filter can have multiple **if** condition branches, and the **if** condition branches can be configured as follows:
     
     + One **if** condition branch is followed by another.
     + The [**if**](cmdqueryname=if) or [**elseif**](cmdqueryname=elseif) clause of one **if** condition branch is followed by another **if** condition branch. Such a configuration further filters routes that match [**if**](cmdqueryname=if) or [**elseif**](cmdqueryname=elseif) clause against the second **if** condition branch.
     
     Regardless of the configuration mode, route filtering continues until [**finish**](cmdqueryname=finish), [**break**](cmdqueryname=break), [**refuse**](cmdqueryname=refuse), or the last **if** condition branch.
  7. Run the [**end-filter**](cmdqueryname=end-filter) command to conclude the configuration of the route-filter.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Example

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only paragraph-by-paragraph editing is used as an example, the corresponding line editing is similar. To use the line editing mode, perform the operations described in paragraph-by-paragraph editing.

For detailed set and route-filter configuration steps, see [Configuration Procedures for Sets and Route-Filters Using the Paragraph-by-Paragraph Editing Mode](dc_vrp_xpl_cfg_0002.html#EN-US_CONCEPT_0000001793384325__section_dc_vrp_xpl_cfg_000102). For details about XPL clauses, see [XPL Paragraph Editing Clauses](dc_vrp_xpl_cfg_0014.html).

| **Objective** | Configure a route-filter to set the priorities of the BGP routes destined for 1.1.1.1 to 200. |
| --- | --- |
| **Configuration Example 1** | ``` <HUAWEI> edit xpl route-filter r1  xpl route-filter r1 if ip route-destination in { 1.1.1.1 32 } then apply preference 200 endif end-filter ```  The IPv4 prefix set used by the preceding route-filter includes only one element. In this situation, use the format of {element A, element B...} to present the IPv4 prefix set. |
| **Objective** | Create a route-filter with a pre-defined variable and configure another route-filter to reference the preceding route-filter. |
| **Configuration Example 2** | ``` <HUAWEI> edit xpl route-filter para  xpl route-filter para($var) apply med $var end-filter ``` ``` <HUAWEI> edit xpl route-filter r2  xpl route-filter r2 if ip route-destination in aaa then call route-filter para(20) elseif ip route-destination in bbb then call route-filter para(30) endif end-filter  ```  **aaa** and **bbb** specified in this route-filter are IPv4 prefix sets, and a maximum of eight parameters can be referenced by each route-filter. |
| **Objective** | Configure a route-filter to set the priorities of the BGP routes carrying destination IP address 1.1.1.1 and MPLS labels to 50. |
| **Configuration Example 3** | ``` <HUAWEI> edit xpl route-filter r3  xpl route-filter r3 if ip route-destination in { 1.1.1.1 32 } and mpls-label exist then apply preference 50 endif end-filter  ```  The conditions in a condition clause can be connected with the Boolean operator **NOT**, **AND**, or **OR**. |



#### Verifying the Configuration

After configuring route-filters, verify the configuration.

* Run the [**display xpl route-filter**](cmdqueryname=display+xpl+route-filter) [ **name** *xpl-name* { **attachpoints** | **uses** | **detail** } ] command to check the XPL route-filter configurations or the detailed information referenced by routing protocols.
* Run the [**display xpl**](cmdqueryname=display+xpl) **route-filter** **state** [ **attached** | **unattached** ] command to check information about XPL route-filter configurations and references.
* Run the [**display xpl statistics**](cmdqueryname=display+xpl+statistics) command to check statistics about XPL and route-filter configurations.
* (Optional) Run the [**reset xpl-filter**](cmdqueryname=reset+xpl-filter) *filter-name***counters** command to clear statistics about the routes matching the specified route-filter.