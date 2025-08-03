Configuring IETF-NACM Authorization
===================================

You can configure IETF-NACM authorization to authorize specific users to perform NETCONF operations or access NETCONF resources. This ensures device security.

#### Context

NACM authorization is an IETF-defined, more flexible authorization mode. It allows you to define NACM authorization rules to control specific users' permissions for performing NETCONF operations and accessing NETCONF resources.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**netconf**](cmdqueryname=netconf)
   
   
   
   The NETCONF user interface view is displayed.
3. Run [**nacm**](cmdqueryname=nacm)
   
   
   
   The NACM view is displayed.
4. Run [**nacm enable**](cmdqueryname=nacm+enable)
   
   
   
   The NACM function is enabled.
5. (Optional) Run [**read-default permit**](cmdqueryname=read-default+permit)
   
   
   
   Users are enabled to perform query operations.
6. (Optional) Run [**write-default permit**](cmdqueryname=write-default+permit)
   
   
   
   Users are enabled to perform configuration operations.
7. (Optional) Run [**execute-default permit**](cmdqueryname=execute-default+permit)
   
   
   
   Users are enabled to have the default execution permission for RPC operations.
8. Run [**group-name**](cmdqueryname=group-name) *group-name*
   
   
   
   An NACM user group is created, and the NACM user group view is displayed.
9. Run [**user-name**](cmdqueryname=user-name) *user-name*
   
   
   
   A user is specified for the NACM user group.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the NACM user group view.
11. Run [**rule-list-name**](cmdqueryname=rule-list-name) *list-name*
    
    
    
    An NACM rule list is created, and the NACM rule list view is displayed.
12. Run [**group**](cmdqueryname=group) *group-name*
    
    
    
    The NACM user group is associated with the NACM authorization rule list.
13. Run [**rule-name**](cmdqueryname=rule-name) *rule-name* **action** { **permit** | **deny** }
    
    
    
    A name is set for an NACM authorization rule in the NACM authorization rule list view.
14. (Optional) Run [**description**](cmdqueryname=description) *description*
    
    
    
    A description is configured for the NACM authorization rule.
15. Run [**module-name**](cmdqueryname=module-name) *module-name*
    
    
    
    The name of a feature module is specified in the NACM authorization rule.
16. Run [**rule-type**](cmdqueryname=rule-type) { **rpc-name** *rpc-name* | **notification-name** *notification-name* | **path** *path* }
    
    
    
    A type is specified for the NACM authorization rule.
17. Run [**access-operation**](cmdqueryname=access-operation) { { **create** | **read** | **update** | **delete** | **exec** } \* | \* }
    
    
    
    Access operations are configured.
18. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.