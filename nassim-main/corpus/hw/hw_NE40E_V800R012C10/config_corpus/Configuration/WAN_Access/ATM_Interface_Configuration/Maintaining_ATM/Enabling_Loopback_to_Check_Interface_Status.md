Enabling Loopback to Check Interface Status
===========================================

Loopback can be enabled to check whether links work properly.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Running the [**loopback**](cmdqueryname=loopback) command on the Router to enable loopback may cause interfaces or links to be unable to work properly. Exercise caution when enabling loopback to check the interface or link status. After checking the interface or link status, run the [**undo loopback**](cmdqueryname=undo+loopback) command to disable loopback in time.

Perform the following steps on the Router to be checked:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface atm**](cmdqueryname=interface+atm) *interface-number* command to enter the view of an ATM interface to be checked.
3. Run the following command as required:
   
   
   * To check an ATM OC-3/STM-1 or ATM OC-12/STM-4 interface, run the [**loopback**](cmdqueryname=loopback) { **local** | **remote** } command.
   * To check an ATM E1 interface, run the [**loopback**](cmdqueryname=loopback) { **local** | **remote** } command.
   * To check an ATM E3 interface, run the [**loopback**](cmdqueryname=loopback) { **local** | **remote** } command.
   * To check whether the local service component works properly, configure **local**.
   * To check whether the peer works properly, configure **remote**.