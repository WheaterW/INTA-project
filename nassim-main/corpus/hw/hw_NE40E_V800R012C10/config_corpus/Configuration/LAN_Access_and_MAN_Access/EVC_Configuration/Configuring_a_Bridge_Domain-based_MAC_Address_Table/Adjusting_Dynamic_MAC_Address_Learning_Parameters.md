Adjusting Dynamic MAC Address Learning Parameters
=================================================

Dynamic MAC address learning parameters can be adjusted to improve device security.

#### Context

[Table 1](#EN-US_TASK_0172363375__tab_1)

**Table 1** Parameters of dynamic MAC address learning
| **Parameters of Dynamic MAC Address Learning** | **Description** | **Usage Scenario** |
| --- | --- | --- |
| Aging time of dynamic MAC address entries | Dynamic address entries age after an aging timer expires.  The shorter the aging time, the more adaptive a device becomes to the changing network topology. | As the network topology changes, devices keep learning MAC addresses. To prevent a MAC address table overflow, an aging time can be set for dynamic MAC address entries. These entries will be deleted after the aging time elapses. |
| Limit on MAC address learning | - | On insecure networks, devices are prone to attacks using forged MAC addresses. Because the capacity of a MAC address table on a device is limited, a hacker can forge a great number of source MAC addresses to a device. Upon receipt, the device adds the MAC addresses to the dynamic MAC address table, resulting in a dynamic MAC address table overflow. As a result, the device cannot learn more source MAC addresses carried in valid packets.  The maximum number of MAC addresses a device can learn can be set, which helps control the number of access users. If the number of learned MAC addresses reaches the upper limit, the device can be configured to discards packets carrying new MAC addresses, which prevents MAC address attacks and improves network security. |

Steps 3 and 4 can be performed in a random order. Perform one or more steps as required.

Before you correctly set the maximum number of MAC addresses that a device can learn, run the [**reset mac-address**](cmdqueryname=reset+mac-address) [ *mac-address* ] **bridge-domain** *bd-id* command to delete all learned MAC addresses.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The bridge domain view is displayed.
3. Run [**mac-address aging-time**](cmdqueryname=mac-address+aging-time) *time-value*
   
   
   
   The aging time of dynamic MAC addresses is set.
4. Configure a MAC address learning limit rule.
   
   
   1. Run the [**mac-limit**](cmdqueryname=mac-limit) { **action** { **discard** | **forward** } | **alarm** { **disable** | **enable** } | **maximum** *maxValue* [ **rate** *interval* ] } \* command to configure a limit rule for dynamic MAC address learning.
   2. (Optional) Run [**mac-limit**](cmdqueryname=mac-limit) **up-threshold** *up-threshold* **down-threshold** *down-threshold*
      
      The threshold (%) for generating and clearing alarms on the number of MAC addresses is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.