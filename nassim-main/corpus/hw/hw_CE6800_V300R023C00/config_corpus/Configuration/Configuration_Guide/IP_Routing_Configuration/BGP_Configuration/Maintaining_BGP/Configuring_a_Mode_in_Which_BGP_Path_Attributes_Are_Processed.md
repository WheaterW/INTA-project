Configuring a Mode in Which BGP Path Attributes Are Processed
=============================================================

To enhance reliability, you can configure a special mode in which BGP path attributes are processed.

#### Prerequisites

Before configuring a mode in which BGP path attributes are processed, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

BGP Update messages contain various path attributes. If the local device receives any Update message with an incorrect format, BGP session flapping may occur. To enhance reliability, you can perform this task to configure a mode for the device to process specified BGP path attributes.

![](public_sys-resources/note_3.0-en-us.png) 

This function takes effect immediately for the routes received after the [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) command is run. However, this function does not take effect immediately for the routes received before the [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) command is run. To allow this function to take effect immediately in this case, run the [**refresh bgp**](cmdqueryname=refresh+bgp) command.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. You can also configure a processing mode for incorrect path attributes.
   
   
   ```
   [bgp](cmdqueryname=bgp+path-attribute+originator-id+attr-set+accept-zero-value) path-attribute { originator-id | attr-set } accept-zero-value
   ```
   ```
   [bgp](cmdqueryname=bgp+path-attribute+community+ext-community+ipv6-ext-community) path-attribute { community | ext-community | ipv6-ext-community | large-community | attr-set | wide-community | cluster-list } accept-zero-length
   ```
   
   The [**bgp**](cmdqueryname=bgp) **path-attribute** **accept-zero-value** command allows the path attributes with the value of 0 to be accepted. The [**bgp**](cmdqueryname=bgp) **path-attribute** **accept-zero-length** command allows the path attributes with the length of 0 to be accepted.
   
   If the [**bgp path-attribute attr-set accept-zero-value**](cmdqueryname=bgp+path-attribute+attr-set+accept-zero-value) command is run and the Originator\_ID in the Attr\_Set attribute is 0, the route corresponding to the Attr\_Set attribute is accepted. After the [**bgp path-attribute attr-set accept-zero-length**](cmdqueryname=bgp+path-attribute+attr-set+accept-zero-length) command is run, if the length of the Community, Ext-community, IPv6 ext-community, Large-community, Wide-community, or Cluster\_List attribute in the Attr\_Set attribute is 0, the routes corresponding to the Attr\_Set attribute are accepted.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**bgp**](cmdqueryname=bgp) **path-attribute** command takes effect for all address families. To configure the device to perform special processing on path attributes in a specific address family, perform the following steps.
   
   The [**bgp path-attribute accept-zero-value**](cmdqueryname=bgp+path-attribute+accept-zero-value) command takes effect for all address families. To configure the device to perform special processing on path attributes in a specific address family, run the [**peer**](cmdqueryname=peer) *peerIpv4Addr* **treat-with-error** **attribute-id** *id* **accept-zero-value** command in this address family view. Currently, the **attribute-id** *id* supports only the Originator\_ID attribute.
   
   The [**bgp path-attribute wide-community accept-zero-length**](cmdqueryname=bgp+path-attribute+wide-community+accept-zero-length) command does not take effect in the BGP RPD address family. After a device receives an RPD route with the Wide-Community attribute whose length is 0, the device still withdraws the route even if this command is run.
3. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
4. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
5. Configure a processing mode for a specified attribute.
   
   
   ```
   [peer](cmdqueryname=peer+path-attribute-treat+attribute-id+to+discard+withdraw) peerIpv4Addr path-attribute-treat attribute-id { id [ to id2 ] } &<1-255> { discard | withdraw | treat-as-unknown }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Running this command may cause path attribute discarding and route withdrawal. Therefore, exercise caution when running this command.
   
   If both the [**bgp**](cmdqueryname=bgp) **path-attribute** and [**peer**](cmdqueryname=peer) **path-attribute-treat** **attribute-id** commands are configured, the device follows the [**peer**](cmdqueryname=peer) **path-attribute-treat** **attribute-id** command.
   
   The **path-attribute-treat** parameter specifies a path attribute processing mode, which can be any of the following ones:
   * Discarding specified attributes
   * Withdrawing the routes with specified attributes
   * Processing specified attributes as unknown attributes
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```