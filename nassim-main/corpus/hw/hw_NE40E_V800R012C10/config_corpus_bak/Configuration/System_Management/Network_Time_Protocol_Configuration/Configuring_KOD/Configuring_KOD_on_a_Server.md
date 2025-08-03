Configuring KOD on a Server
===========================

Configuring_KOD_on_a_Server

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ntp-service kod-enable**](cmdqueryname=ntp-service+kod-enable)
   
   
   
   KOD is enabled.
3. Run [**ntp-service access**](cmdqueryname=ntp-service+access) { **peer** | **query** | **server** | **synchronization** | **limited** } { { *acl-number* | **acl-name** *aclname* } [ **ipv6** { *acl6-number* | **acl6-name** *acl6name* } ] | **ipv6** { *acl6-number* | **acl6-name** acl6name } [ { *acl-number* | **acl-name** *aclname* } ] }
   
   
   
   Access control authority is set.
4. Run [**ntp-service discard**](cmdqueryname=ntp-service+discard) { **min-interval** *min-interval-val* | **avg-interval** *avg-interval-val* } \*
   
   
   
   The minimum and average interval is configured for inter-packet spacing check.
5. Run [**ntp-service refclock-master**](cmdqueryname=ntp-service+refclock-master) [ *ip-address* ] [ *stratum* ]
   
   
   
   The local clock is configured to be the NTP master clock that provides the synchronizing time for other devices.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.