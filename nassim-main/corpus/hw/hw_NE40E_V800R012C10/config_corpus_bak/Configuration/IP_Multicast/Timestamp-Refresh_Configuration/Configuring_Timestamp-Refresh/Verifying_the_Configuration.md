Verifying the Configuration
===========================

After timestamp-refresh is configured successfully, you can view the local and global timestamp-refresh offset values and the configurations of timestamp-refresh instances.

#### Procedure

* Run the [**display multicast timestamp-refresh**](cmdqueryname=display+multicast+timestamp-refresh) [ **instance** *instance-name* ] command to check the local and global timestamp-refresh offset values.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration**[ *multicast-tsrefresh-instance* ] command to check the configurations of timestamp-refresh instances.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration**[ *behavior* ] command to check the configuration result of binding a traffic behavior to a timestamp-refresh instance.