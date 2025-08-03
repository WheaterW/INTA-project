Configuring the Aging Period for eMDI Detection
===============================================

You can configure the aging period of eMDI BIER channels in a BIER eMDI scenario.

#### Context

In a BIER eMDI scenario, if no traffic has been detected in a multicast group within a period of time, the corresponding ACL entry ages, and the traffic of the multicast group is no longer detected. The interval between when the traffic rate becomes 0 and when the ACL entry starts to age is considered as the aging period of the eMDI BIER channels. You can perform the following steps to configure the aging period.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**emdi**](cmdqueryname=emdi)
   
   
   
   The eMDI view is displayed.
3. Run [**emdi bier channel age-periods**](cmdqueryname=emdi+bier+channel+age-periods) *period-value*
   
   
   
   The aging period of eMDI BIER channels is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.