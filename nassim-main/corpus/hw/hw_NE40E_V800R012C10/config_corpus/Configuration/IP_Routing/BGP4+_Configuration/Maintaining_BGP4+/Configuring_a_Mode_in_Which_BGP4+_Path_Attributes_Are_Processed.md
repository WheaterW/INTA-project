Configuring a Mode in Which BGP4+ Path Attributes Are Processed
===============================================================

To enhance reliability, you can configure a special mode in which BGP4+ path attributes are processed.

#### Usage Scenario

A BGP4+ Update message contains various path attributes. If a local device receives Update messages containing malformed path attributes, the involved BGP4+ sessions may flap. To resolve this issue and enhance reliability, configure a special mode in which a device processes specified BGP4+ path attributes in received Update messages. Special modes indicate those that are not defined in a standard protocol.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This task may cause path attribute discarding and route withdrawal. Therefore, exercise caution when performing this task.

This function takes effect immediately for the routes received after the [**bgp**](cmdqueryname=bgp+path-attribute) **path-attribute** or [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) command is run. However, this function does not take effect immediately for the routes received before the [**bgp**](cmdqueryname=bgp+path-attribute) **path-attribute** or [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) command is run. To allow this function to take effect in this case, you need to run the [**refresh bgp**](cmdqueryname=refresh+bgp) command.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a way to handle incorrect path attributes as required.
   
   
   * To allow the device to accept the path attributes with the value of 0, run the [**bgp path-attribute**](cmdqueryname=bgp+path-attribute+originator-id+attr-set+accept-zero-value) { **originator-id** | **attr-set** } **accept-zero-value** command.
   * To allow the device to accept the path attributes with the length of 0, run the [**bgp path-attribute**](cmdqueryname=bgp+path-attribute+community+ext-community+ipv6-ext-community) { **community** | **ext-community** | **ipv6-ext-community** | **large-community** | **attr-set** | **wide-community** | **clust-list** } **accept-zero-length** command.
   
   The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute+accept-zero-value) **accept-zero-value** command allows the path attributes with the value of 0 to be accepted. The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute+accept-zero-length) **accept-zero-length** command allows the path attributes with the length of 0 to be accepted.
   
   After the [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) [**attr-set accept-zero-value**](cmdqueryname=attr-set+accept-zero-value) command is run, if the Originator\_ID in the Attr\_Set attribute is 0, the corresponding route is accepted. After the [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) [**attr-set accept-zero-length**](cmdqueryname=attr-set+accept-zero-length) command is run, if the length of the Community, Ext-community, IPv6 ext-community, Large-community, Wide-community, or Cluster\_List attribute in the Attr\_Set attribute is 0, the corresponding route is accepted.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) command takes effect for all address families. To configure the device to perform special processing on path attributes in a specific address family, perform the following steps.
   
   The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute+accept-zero-value) **accept-zero-value** command takes effect for all address families. To configure the device to perform special processing on path attributes in a specific address family, run the [**peer**](cmdqueryname=peer+treat-with-error+attribute-id+accept-zero-value) *peerIpv4Addr* **treat-with-error** **attribute-id** *id* **accept-zero-value** command. Currently, the **attribute-id** *id* supports only the Originator\_ID attribute.
   
   The [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) [**wide-community accept-zero-length**](cmdqueryname=wide-community+accept-zero-length) command does not take effect in the BGP RPD address family. After a device receives an RPD route with the Wide-Community attribute whose length is 0, the device still withdraws the route even if this command is run.
3. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   BGP4+ is started (with the local AS number specified), and the BGP view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } [**as-number**](cmdqueryname=as-number) *as-number*
   
   
   
   The IP address of a peer and the number of the AS where the peer resides are specified.
5. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
   
   
   
   The BGP-IPv6 unicast address family view is displayed.
6. Run [**peer**](cmdqueryname=peer+path-attribute-treat+attribute-id+to+discard+withdraw) { *peerIpv4Addr* | *peerIpv6Addr* } **path-attribute-treat** **attribute-id** { *id* [ **to** *id2* ] } &<1-255> { **discard** | **withdraw** | **treat-as-unknown** }
   
   
   
   A mode for the device to process specified attributes is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Running this command may cause path attribute discarding and route withdrawal. Therefore, exercise caution when running this command.
   
   If both the [**bgp path-attribute**](cmdqueryname=bgp+path-attribute) and [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat+attribute-id) **attribute-id** commands are configured, the device executes the [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat+attribute-id) **attribute-id** command.
   
   The [**peer path-attribute-treat**](cmdqueryname=peer+path-attribute-treat) parameter specifies a path attribute processing mode, which can be any of the following ones:
   * Discarding specified attributes
   * Withdrawing the routes with specified attributes
   * Processing specified attributes as unknown attributes
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.