Configuring the Management Protocol ACL Delivering Function
===========================================================

Configuring the Management Protocol ACL Delivering Function

#### Usage Scenario

When there is no need to filter out invalid management protocol packets to be sent to the CPU using hardware, run the [**management-acl disable**](cmdqueryname=management-acl+disable) command to disable the management protocol ACL delivering function. The management-acl disable command takes effect for FTP, Telnet, SSH, and SNMP. For example, if an FTP ACL is configured and the management-acl disable command is run, the FTP ACL does not take effect.

In VS mode, this feature is supported only by the admin VS.


#### Prerequisites

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**undo management-acl disable**](cmdqueryname=undo+management-acl+disable)
   
   
   
   The management protocol ACL delivering function is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After configuring interface-based CAR, check the configurations.

Run the [**display cpu-defend policy**](cmdqueryname=display+cpu-defend+policy) *policy-number* command to view information about the user-defined attack defense policy.