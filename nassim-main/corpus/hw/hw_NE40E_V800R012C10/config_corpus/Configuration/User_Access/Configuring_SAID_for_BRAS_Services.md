Configuring SAID for BRAS Services
==================================

Manual fault diagnosis is time-consuming and locating failure points is difficult on networks that have various types of users and large numbers of access users and peripheral interworking devices. The System of Active Immunization and Diagnosis (SAID) can therefore be used to implement self-diagnosis and self-recovery of service nodes for user access.

#### Context

The SAID can identify typical faults and automatically diagnose and rectify the faults. If a large number of users fail to go online, the SAID automatically performs comprehensive fault diagnosis and collects diagnostic data (including user login/logout failure causes and the number of users by board). If self-healing conditions are met, the SAID initiates an active/standby switchover or restart the faulty board to rectify the fault. In addition, the SAID can collect statistics about the number of users and traffic based on interfaces. It automatically performs fault diagnosis at a specified detection interval. If fault diagnosis conditions are met, the SAID records log information for fault tracing, facilitating fault diagnosis and prevention and helping locate service faults.

#### Pre-configuration Tasks

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run **undo set said-node all disable**
   
   
   
   All SAID nodes are enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   SAID nodes are enabled by default. To check whether a SAID node is enabled, run the [**display said-node status brief**](cmdqueryname=display+said-node+status+brief) command. (If the value of **OPERATE** is *Enable*, the SAID node is enabled. If the value of **OPERATE** is *Disable*, the SAID node is disabled.)
4. Run [**aaa-said check-rule rule1**](cmdqueryname=aaa-said+check-rule+rule1) **online-fail-num increase** *increase-num*
   
   
   
   The increment of the number of login failures detected by SAID nodes based on rule 1 is set.
5. Run [**aaa-said check-rule online-fail-reason**](cmdqueryname=aaa-said+check-rule+online-fail-reason) **exclude fail-code** *fail-code*
   
   
   
   Login failures with a specified cause code are excluded from being detected or diagnosed by SAID nodes.
6. Run [**aaa-said diag-rule**](cmdqueryname=aaa-said+diag-rule) **online-fail-num** **increase** *increase-num* **user-num reduce** *user-num* **online-success-ratio below** *succ-rate*
   
   
   
   The user login failure increment within 10 minutes, number of online users reduced, and login success rate reduced that can trigger fault diagnosis on SAID nodes are set.
7. Run [**aaa-said recover**](cmdqueryname=aaa-said+recover) **interval** *interval-time*
   
   
   
   An interval between two same SAID recovery operations is set.
8. Run [**aaa-said enable**](cmdqueryname=aaa-said+enable)
   
   
   
   SAID diagnosis based on the number of users and traffic statistics on an interface is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To check whether the SAID function is enabled, run the [**display aaa configuration**](cmdqueryname=display+aaa+configuration) command. (If the value of **Said switch** is **enable**, the SAID function is enabled. If the value of **Said switch** is **disable**, the SAID function is disabled.)
   
   If the KPI function has been enabled for sub-interfaces using the [**set aaa sub-interface kpi enable**](cmdqueryname=set+aaa+sub-interface+kpi+enable) command, running the [**aaa-said disable**](cmdqueryname=aaa-said+disable) command does not disable SAID diagnosis based on the number of users or traffic statistics on an interface.
9. Run [**aaa-said check-rule user-number**](cmdqueryname=aaa-said+check-rule+user-number) **reduce-ratio** *reduce-ratio*
   
   
   
   A SAID rule based on the user reduction rate is configured. The SAID condition is met only when the user deduction rate reaches a specified value, and diagnosis and recovery are then triggered.
10. Run [**aaa-said check-rule flow-speed**](cmdqueryname=aaa-said+check-rule+flow-speed) **reduce-ratio** *reduce-ratio*
    
    
    
    A SAID rule based on the traffic reduction rate is configured. The SAID condition is met only when the traffic reduction rate reaches a specified value, and diagnosis and recovery are then triggered.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

Run the [**display aaa configuration**](cmdqueryname=display+aaa+configuration) command to check the SAID configuration.