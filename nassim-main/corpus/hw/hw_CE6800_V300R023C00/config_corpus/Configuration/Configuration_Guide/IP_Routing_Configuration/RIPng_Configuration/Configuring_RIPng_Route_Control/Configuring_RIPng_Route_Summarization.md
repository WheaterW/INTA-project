Configuring RIPng Route Summarization
=====================================

Configuring RIPng Route Summarization

#### Context

On a medium or large RIPng network, a device's RIPng routing table contains many routes. Storing, transmitting, and processing these routes consume a significant amount of memory and network resources. To address this issue, configure RIPng route summarization.

Route summarization is the process of summarizing routes that share the same next hop but are destined for different subnets of a network segment into one summary route, and then advertising this route to other network segments. Route summarization reduces both the routing table size and system resource consumption. In addition, if a specific link within the summarized IP address range frequently alternates between up and down, the link status changes will not be advertised to devices that are located beyond the summary route network segment, preventing route flapping and improving network stability.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface mode.
4. Configure RIPng route summarization.
   
   
   ```
   [ripng summary-address](cmdqueryname=ripng+summary-address) ipv6-address prefix-length [ avoid-feedback ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The routing table of the local RIPng device remains unchanged and still contains the routes before RIPng route summarization is configured, while the routing tables of neighbors contain only the summary route.
   
   The metric of the summary route is the minimum metric among all the original routes.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```