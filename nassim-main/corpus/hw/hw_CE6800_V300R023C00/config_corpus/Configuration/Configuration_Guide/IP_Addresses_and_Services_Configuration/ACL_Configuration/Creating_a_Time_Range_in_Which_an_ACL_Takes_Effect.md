Creating a Time Range in Which an ACL Takes Effect
==================================================

Creating a Time Range in Which an ACL Takes Effect

#### Context

A time range defines when ACL rules are in effect, for example, during a specific time range or a fixed time range of each week. This allows network administrators to configure different policies during different time ranges for network optimization.

Time ranges associated with ACL rules are classified as follows:

* Absolute time range: defined by a period of time, in the format of from YYYY/MM/DD HH:MM to YYYY/MM/DD HH:MM. That is, ACL rules take effect only during this period.
* Periodic time range: defined by week. That is, ACL rules can take effect at an interval of one week. For example, if the time range of ACL rules is 08:00 to 12:00 on Monday, the ACL rules take effect during this time at each week.

A time name can be specified for multiple time ranges, which take effect based on the following principles:

* If only periodic time ranges are configured, all the periodic time ranges take effect.
* If only absolute time ranges are configured, all the absolute time ranges take effect.
* If both periodic and absolute time ranges are configured, only those that exist in both the periodic and absolute time ranges take effect.

![](public_sys-resources/caution_3.0-en-us.png) 

* To associate a time range with an ACL rule, ensure that the system time of the device is the same as that of other devices on the network; otherwise, the rule may not take effect. A time name must have been configured for the time range; otherwise, the time range cannot be associated with the rule.
* Before deleting a time range, you must delete the ACL rules associated with the time range or delete the ACL to which the ACL rules belong. Deleting the time range of an ACL may cause some ACL rules to become invalid. Exercise caution when performing this operation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a time range.
   
   
   ```
   [time-range](cmdqueryname=time-range+to+from+to) time-name [ { time1 to time2 { days } &<1-7> | from time1 date1 [ to time2 date2 ] } ]
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display time-range**](cmdqueryname=display+time-range) *time-name* command to check the configuration in a specified time range.


#### Follow-up Procedure

After a time range is created, you need to create an ACL and configure the ACL rules to be associated with the time range.