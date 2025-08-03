Configuring the Function to Locally Generate and Store User Bills
=================================================================

If RADIUS is used to implement accounting, configure the function to locally generate and store user bills, so that user accounting information is still correct if an interworking RADIUS server fails to respond upon user login or logout.

#### Context

If a RADIUS server is configured to implement accounting for access users, the Router can be enabled to generate local bills in the following scenarios:

* The RADIUS server fails to respond to an accounting stop request: The Router generates a local bill to record the accounting information and considers that the user is offline.
* User login is allowed even if accounting fails to start for the user (this function is configured using the [**accounting start-fail**](cmdqueryname=accounting+start-fail) **online** command): The Router generates a local bill when the user goes offline to record the accounting information.

Local bills can be transferred to a bill server for account reconciliation on the RADIUS server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**local-aaa-server**](cmdqueryname=local-aaa-server)
   
   
   
   The local AAA server view is displayed.
3. Run [**local-bill-pool enable**](cmdqueryname=local-bill-pool+enable)
   
   
   
   A local bill pool is created.
4. Run [**bill-server**](cmdqueryname=bill-server) *ip-address* **filename** *file-name* [ **user-name** *user-name* **password** **cipher** *cipher-password* *port* ]
   
   
   
   A bill server is specified.
   
   
   
   User bills stored in the local bill pool or CF card can be transferred to the specified bill server to release the local space.
5. Configure a bill transfer mode and transfer trigger conditions.
   
   
   * Configure a transfer mode for bills stored in the local bill pool or CF card.
     1. To configure the automatic bill transfer mode for bills in the local bill pool, run the [**local-bill**](cmdqueryname=local-bill) **cache** **backup-mode** { **cfcard** | **none** | **tftp** | **sftp** } command.
        
        If **none** is specified, bills in the local bill pool are not transferred. If you want bill transfer to be performed before the automatic bill transfer condition is met, run the [**local-bill**](cmdqueryname=local-bill) **cache** **backup** command to manually transfer local bills to the CF card or bill server.
     2. To configure the automatic bill transfer mode for bills in the CF card, run the [**local-bill**](cmdqueryname=local-bill) **cfcard** **backup-mode** { **tftp** | **sftp** } command.
        
        The Router also supports manual bill transfer from the CF card to the bill server using the [**local-bill**](cmdqueryname=local-bill) **cfcard** **backup** command.
   * Configure the transfer trigger conditions for local bill transfer from the local bill pool or CF card to the bill server.
     1. To configure an automatic transfer interval as the trigger condition, run the [**local-bill**](cmdqueryname=local-bill) { **cache** | **cfcard** } **backup-interval** *interval* command.
        
        After a transfer interval is specified, bills in the local bill pool or CF card are automatically transferred to the bill server at the specified interval.
     2. To configure a transfer alarm threshold as the trigger condition, run the [**local-bill**](cmdqueryname=local-bill) { **cache** | **cfcard** } **alarm-threshold** *threshold* command.
        
        After a transfer alarm threshold is specified, if automatic bill transfer is enabled, bills in the local bill pool or CF card are automatically transferred to the bill server when the alarm threshold is reached. If automatic bill transfer is disabled, an alarm is reported when the threshold is reached, informing you to clear unneeded local bills in time.
6. (Optional) Run [**local-bill**](cmdqueryname=local-bill) **cfcard** **reset**
   
   
   
   Bills in the CF card are cleared.
   
   
   
   When the CF card storage space is insufficient and the bill server is faulty, run the preceding command to clear local bills. Otherwise, new bills will be dropped.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Bills cannot be restored after they are deleted from the CF card. Exercise caution when running this command.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

After configuring the function to locally generate and store user bills, perform the following checks:

* Run the [**display local-bill configuration**](cmdqueryname=display+local-bill+configuration) command to check the configuration of the local bill transfer function.
* Run the [**display local-bill information**](cmdqueryname=display+local-bill+information) command to check the usage of the CF card or local bill pool.
* Run the [**display local-bill cache**](cmdqueryname=display+local-bill+cache) *start-num* *count* command to check the information about specified bills in the local bill pool.