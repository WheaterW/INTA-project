Configuring Huawei-NACM Authorization
=====================================

You can configure Huawei-NACM authorization to authorize specific users to perform NETCONF operations or access NETCONF resources. This ensures device security.

#### Context

After a NETCONF connection is established using SSH, all SSH users can use NETCONF to manage devices, imposing security risks. To resolve this problem, you can configure NETCONF authorization rules to authorize specific users to perform NETCONF operations or access NETCONF resources.


#### Procedure

1. Configure NETCONF authorization in the task group view and add a task to the task group.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**task-group**](cmdqueryname=task-group) *task-group-name*
      
      
      
      A task group is created, and the task group view is displayed.
   4. Run [**netconf authorization-rule**](cmdqueryname=netconf+authorization-rule) *rule-name* { { **deny** { **rpc-operation** *rpc-oper-name* | **schema-path** *data-node-path* } } | { **permit** { **rpc-operation** *rpc-oper-name* | **schema-path** *data-node-path* **access-operation** { **read** | **write** | **execute** }\* } } } [ **description** *description-text* ]
      
      
      
      A NETCONF authorization rule for operations and data nodes is configured, and the task is added to the task group.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the AAA view.
2. Add the task group to a user group.
   1. Run [**user-group**](cmdqueryname=user-group) *user-group-name*
      
      
      
      A user group is created, and the user group view is displayed.
   2. Run [**task-group**](cmdqueryname=task-group) *task-group-name*
      
      
      
      The specific task group is added to the user group.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the AAA view.
3. Run [**local-user**](cmdqueryname=local-user) *user-name* **user-group** *user-group-name*
   
   
   
   A local user is added to the user group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.