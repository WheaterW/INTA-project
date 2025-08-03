(Optional) Creating a Validity Period for an ACL6 Rule
======================================================

You can create a validity period for an ACL6 rule to control network traffic in a specified period.

#### Context

To control certain types of traffic in a specified period, you can configure the validity period of an ACL6 rule to determine the time traffic passes through. For example, to ensure reliable transmission of video traffic at prime time at night, you need to limit the volume of traffic for common online users.

After this configuration task is performed, a time range is created. Then, you can specify the time range as the validity period when creating an ACL6 rule.

The validity period of an ACL6 rule can be either of the following types:

* Absolute time range: The validity period is fixed.
* Relative time range: The validity period is a periodic period, for example, each Monday.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**time-range**](cmdqueryname=time-range+to+from+to) *time-name* { *start-time* **to** *end-time days* &<1-7> | **from** *time1 date1* [ **to** *time2 date2* ] }
   
   
   
   A validity period is created.
   
   
   
   * You can configure up to 256 time ranges.
   * Up to 32 relative time ranges (periodic time ranges) and 12 absolute time ranges can share one time range name.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.