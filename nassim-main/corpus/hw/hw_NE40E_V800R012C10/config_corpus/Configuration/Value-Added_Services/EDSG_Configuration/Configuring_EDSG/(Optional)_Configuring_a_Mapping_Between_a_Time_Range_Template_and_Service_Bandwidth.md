(Optional) Configuring a Mapping Between a Time Range Template and Service Bandwidth
====================================================================================

This section describes how to configure a mapping between a time range template and EDSG service bandwidth. After the configuration is complete, the EDSG service bandwidth is adjusted when the time range changes.

#### Context

User service traffic has different requirements on service bandwidth in different time ranges. For example, the service traffic volume used by a user in a time range during daylight hours is usually greater than that in the early morning. Therefore, a larger service bandwidth must be set for the time range during daylight hours. To properly distribute service traffic, configure the service bandwidth to be flexibly adjusted when the time range changes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**time-range**](cmdqueryname=time-range) *time-name* [ *start-time* **to** *end-time* *days* &<1-7> | **from** *time1* *date1* [ **to** *time2* *date2* ] ]
   
   
   
   A time range is defined.
3. Run [**service-policy**](cmdqueryname=service-policy) **name** *policy-name* **edsg**
   
   
   
   The EDSG service policy view is displayed.
4. Run [**time-range**](cmdqueryname=time-range) *time-range-name* **rate-limit** **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **inbound** | **outbound** ]
   
   
   
   A mapping is configured between the time range template and EDSG service bandwidth.