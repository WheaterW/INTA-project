(Optional) Configuring a Constant Index for an IPv4 Address Pool
================================================================

By default, IPv4 address pools do not support constant indexes. Instead, their indexes change after a device restart. After a device restart, the NMS loses all IPv4 address pool statistics and can no longer monitor these address pools. This problem can be solved by configuring constant indexes for the address pools.

#### Context

After the [**ip-pool constant-index enable**](cmdqueryname=ip-pool+constant-index+enable) command is run, the index of an IPv4 address pool remains unchanged after the device restarts. The **constant-index** *index* command is automatically generated in the corresponding IPv4 address pool view for all IPv4 address pools that have been configured on the device. However, you cannot run the [**constant-index**](cmdqueryname=constant-index) command to change the automatically generated constant index of an IPv4 address pool.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip-pool constant-index enable**](cmdqueryname=ip-pool+constant-index+enable)
   
   
   
   The constant index function is enabled for IPv4 address pools.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.