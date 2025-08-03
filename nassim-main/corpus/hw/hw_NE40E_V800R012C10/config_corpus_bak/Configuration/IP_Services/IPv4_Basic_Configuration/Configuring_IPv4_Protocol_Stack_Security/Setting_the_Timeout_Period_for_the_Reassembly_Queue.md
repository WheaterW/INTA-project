Setting the Timeout Period for the Reassembly Queue
===================================================

To improve the router performance and prevent against network attacks, configure a proper reassembly timeout period so that reassembly queues that have waited for all fragments to be reassembled for a long period can be aged in time.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv4 reassembling timeout**](cmdqueryname=ipv4+reassembling+timeout) *time*
   
   
   
   The timeout period of IPv4 fragment reassembly is set.
   
   *time* ranges from 5 to 120, in seconds. Using the default value 30 seconds is recommended.
3. (Optional) Run [**reset ip reassembly**](cmdqueryname=reset+ip+reassembly)
   
   
   
   The fragment and assembly data are initialized.