(Optional) Configuring a Constant Index for an IPv6 Address Pool
================================================================

(Optional)_Configuring_a_Constant_Index_for_an_IPv6_Address_Pool

#### Context

After the [**ip-pool constant-index enable**](cmdqueryname=ip-pool+constant-index+enable) command is run, the indexes of IPv4 address pools, IPv6 prefix pools, and IPv6 address pools remain unchanged after the device restarts. The [**constant-index**](cmdqueryname=constant-index) *index* command is automatically generated in the views of all the IPv4 address pools, IPv6 prefix pools, and IPv6 address pools configured on the device for users to check the constant indexes. However, you cannot run the [**constant-index**](cmdqueryname=constant-index) command to change the automatically generated constant index of an IPv6 address pool or IPv6 prefix pool.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip-pool constant-index enable**](cmdqueryname=ip-pool+constant-index+enable) command to enable the constant index function for IPv4 address pools, IPv6 prefix pools, and IPv6 address pools.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.