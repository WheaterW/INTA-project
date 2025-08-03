Configuring a Mode in Which BGP4+ Path Attributes Are Processed
===============================================================

To enhance reliability, you can configure a special mode in which BGP4+ path attributes are processed.

#### Prerequisites

Before configuring a mode in which BGP4+ path attributes are processed, you have completed the following task:

* [Configuring Basic BGP4+ Functions](vrp_bgp6_cfg_0006.html)

#### Context

BGP4+ Update messages contain various path attributes. If the local device receives any Update message with an incorrect format, BGP4+ session flapping may occur. To enhance reliability, you can perform this task to configure a mode for the device to process specified BGP4+ path attributes.

![](public_sys-resources/note_3.0-en-us.png) 

This function takes effect immediately for the routes received after the [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) command is run. However, this function does not take effect immediately for the routes received before the [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) command is run. To allow this function to take effect immediately in this case, run the [**refresh bgp**](cmdqueryname=refresh+bgp) command.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a processing mode for incorrect path attributes.
   
   
   ```
   [bgp path-attribute](cmdqueryname=bgp+path-attribute+originator-id+attr-set+accept-zero-value) { originator-id | attr-set } accept-zero-value
   ```
   ```
   [bgp path-attribute](cmdqueryname=bgp+path-attribute+community+ext-community+ipv6-ext-community) { community | ext-community | ipv6-ext-community | large-community | attr-set | wide-community | cluster-list } accept-zero-length
   ```
   
   The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) **accept-zero-value** command allows the path attributes with the value of 0 to be accepted. The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) **accept-zero-length** command allows the path attributes with the length of 0 to be accepted.
   
   After the [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) [**attr-set accept-zero-value**](cmdqueryname=attr-set+accept-zero-value) command is run, if the Originator\_ID in the Attr\_Set attribute is 0, the corresponding route is accepted. After the [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) [**attr-set accept-zero-length**](cmdqueryname=attr-set+accept-zero-length) command is run, if the length of the Community, Ext-community, IPv6 ext-community, Large-community, Wide-community, or Cluster\_List attribute in the Attr\_Set attribute is 0, the corresponding route is accepted.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) command takes effect for all address families. To configure the device to perform special processing on path attributes in a specific address family, perform the following steps.
   
   The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) **accept-zero-value** command takes effect for all address families. To configure the device to perform special processing on path attributes in a specific address family, run the [**peer**](cmdqueryname=peer) *peerIpv4Addr* **treat-with-error** **attribute-id** *id* **accept-zero-value** command. Currently, the **attribute-id** *id* supports only the Originator\_ID attribute.
   
   The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) [**wide-community accept-zero-length**](cmdqueryname=wide-community+accept-zero-length) command does not take effect in the BGP RPD address family. After a device receives an RPD route with the Wide-Community attribute whose length is 0, the device still withdraws the route even if this command is run.
3. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
4. Enter the BGP-IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
5. Configure a processing mode for specified attributes.
   
   
   ```
   [peer](cmdqueryname=peer+path-attribute-treat+attribute-id+to+discard+withdraw) { peerIpv4Addr | peerIpv6Addr  } path-attribute-treat attribute-id { id [ to id2 ] } &<1-255> { discard | withdraw | treat-as-unknown }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Running this command may cause path attribute discarding and route withdrawal. Therefore, exercise caution when running this command.
   
   If both the [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) and [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) **attribute-id** commands are configured, the device executes the [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) **attribute-id** command.
   
   The [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) parameter specifies a path attribute processing mode, which can be any of the following ones:
   * Discarding specified attributes
   * Withdrawing the routes with specified attributes
   * Processing specified attributes as unknown attributes
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```