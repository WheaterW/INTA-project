(Optional) Configuring Reporting of User Access Information to the KPI System
=============================================================================

This function allows the KPI system to record the number of user login successes, the number of user login failures, and the online success rate in real time. This configuration improves network maintainability.

#### Context

The access user login information reporting KPI function collects statistics on the number of online users, number of successful logins, number of login failures, login success rate, top 5 login failure causes, and top 5 logout causes based on the device, board, domain, interface, and VLAN. The statistics can be reported through KPIs to improve network maintainability. This function is automatically enabled on boards and the device, and the statistical period is 10 minutes. This function needs to be enabled for domains, outer VLAN IDs, and sub-interfaces, and the statistical period is 15 minutes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**access user-statistic complete-kpi enable**](cmdqueryname=access+user-statistic+complete-kpi+enable)
   
   
   
   The device is enabled to report the number of user login successes, the number of user login failures, and the user login success rate to the KPI system based on domains, outer VLAN IDs, or sub-interfaces.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.