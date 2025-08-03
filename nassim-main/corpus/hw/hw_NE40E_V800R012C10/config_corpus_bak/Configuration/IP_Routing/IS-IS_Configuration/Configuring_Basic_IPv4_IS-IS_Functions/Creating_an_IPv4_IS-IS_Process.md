Creating an IPv4 IS-IS Process
==============================

To configure basic IPv4 IS-IS functions, first create an IPv4 IS-IS process and enable IPv4 IS-IS interfaces.

#### Context

To configure an IS-IS process, perform the following operations:

1. [Create an IS-IS process and configure a NET for the device.](#EN-US_TASK_0172365973__step9669734112517)
2. (Optional) Perform the following operations as required:
   * [Set a level for the device.](#EN-US_TASK_0172365973__p698218914410)
     
     Configure a device level based on the network planning. If no device level is configured, IS-IS establishes both Level-1 and Level-2 neighbor relationships and maintains two identical LSDBs, consuming excessive system resources.
   * [Configure IS-IS host name mapping.](#EN-US_TASK_0172365973__choice9689337192912)
     
     After IS-IS host name mapping is configured, a host name rather than the system ID of a device is displayed when you query IS-IS information. This improves the maintainability on an IS-IS network.
   * [Enable IS-IS neighbor strict-check.](#EN-US_TASK_0172365973__choice369318143219)
     
     If both IPv4 and IPv6 run on a network, and the IPv6 topology type of this network is **standard** or **compatible**, enable IS-IS neighbor strict-check to ensure that an IS-IS neighbor relationship is established only when both IPv4 and IPv6 are up. IS-IS neighbor strict-check improves network reliability and prevents traffic loss.
   * [Enable the LSDB capacity threshold alarm function.](#EN-US_TASK_0172365973__choice2730133910327)
     
     On an IS-IS network, incorrect configurations may cause a large number of external routes to be imported. Similarly, an IS-IS device may advertise a large number of LSPs after receiving attack packets. Both instances would lead to a network fault. To prevent this problem, you can configure the LSDB capacity threshold alarm function, which generates an alarm if the number of LSPs reaches the configured threshold, facilitating troubleshooting by the administrator.
   * [Configure IS-IS to add the POI TLV to purge LSPs.](#EN-US_TASK_0172365973__choice6551143263314)
     
     This function helps locate the source of error packets when a fault occurs on the network.
   * [Configure automatic IS-IS system ID recovery in case of conflicts.](#EN-US_TASK_0172365973__choice11117171203619)
     
     Two devices on an IS-IS network cannot have the same system ID. Otherwise, network flapping may occur.

#### Procedure

1. Create an IS-IS process and configure a NET for the device.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to create an IS-IS process and enter its view.
      
      
      
      *process-id* specifies an IS-IS process ID. If the *process-id* parameter is not specified, the system creates process 1 by default. To associate an IS-IS process with a VPN instance, run the [**isis**](cmdqueryname=isis) *process-id* **vpn-instance** *vpn-instance-name* command.
   3. Run the [**network-entity**](cmdqueryname=network-entity) *net-addr* command to configure a NET.
      
      An IS-IS NET consists of the following three parts:
      * Area ID, which is variable (1 to 13 bytes).
      * System ID (6 bytes) of this device.
      * SEL, which is 1 byte and its value must be 00.For example, the NET of an IS-IS device can be configured as 10.1234.6e9f.0001.00.
      ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
      * An area ID uniquely identifies an area in a routing domain. All devices in a Level-1 area must have the same area ID. Devices in a Level-2 area can have different area IDs.
      * The system ID must be unique in the whole area and backbone area.
      * Multiple NETs can be configured, but they must have the same system ID.
      
      In conclusion, it is recommended that you convert the loopback interface address into a NET to ensure that the NET is unique on the network. If NETs are not unique on the network, route flapping may occur. Therefore, you need to plan the network properly. To convert the IP address of a loopback interface into a system ID, extend each octet of the IP address to three digits by adding 0s at the beginning if necessary, and then divide the extended IP address into three parts, with each part consisting of four digits.
   4. (Optional) Run the [**description**](cmdqueryname=description) *description* command to configure a description for the IS-IS process.
      
      
      
      A network administrator can configure a description to facilitate subsequent maintenance and management. The description, however, is not advertised in LSPs.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. (Optional) Perform the following steps as required:
   * Set a level for the device.
     1. Run the [**is-level**](cmdqueryname=is-level) { **level-1** | **level-1-2** | **level-2** } command to configure a level for the device.
     2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Configure IS-IS host name mapping.
     1. Perform the following operations as required:
        + Run the [**is-name**](cmdqueryname=is-name) *symbolic-name* command to configure IS-IS dynamic host name mapping and configure a host name for the local device.
          
          This configuration is dynamic. That is, the configured *symbolic-name* is advertised to other IS-IS devices in the area through LSPs.
          
          The configured host name (*symbolic-name*), rather than the system ID of the local device, is displayed on the IS-IS neighbors when IS-IS information is checked on these neighbors.
        + Run the [**is-name map**](cmdqueryname=is-name+map) *system-id* *symbolic-name* command to configure IS-IS static host name mapping and configure a host name for the remote IS-IS device.
          
          This configuration is static and takes effect only on the local device. The configured *symbolic-name* is not sent through LSPs.
          
          Therefore, if dynamic host name mapping is configured on an IS-IS device and static host name mapping is configured (for the previous device) on the local device, the dynamic host name overrides the static one on the local device.
     2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Enable IS-IS neighbor strict-check.
     1. Run the [**adjacency-strict-check enable**](cmdqueryname=adjacency-strict-check+enable) command to enable IS-IS neighbor strict-check.
     2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Enable the LSDB capacity threshold alarm function.
     1. Run the [**lsdb limit**](cmdqueryname=lsdb+limit) *limit-number* **threshold-alarm** **upper-limit** *upper-limit-value* **lower-limit** *lower-limit-value* command to enable the LSDB capacity threshold alarm function.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        *upper-limit-value* must be greater than or equal to *lower-limit-value*.
     2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Configure IS-IS to add the POI TLV to purge LSPs.
     1. Run the [**purge-originator-identification enable**](cmdqueryname=purge-originator-identification+enable) [ **always** ] command to configure IS-IS to add the POI TLV (as well as the host name TLV if the dynamic host name function is enabled) to purge LSPs.
        + If the [**purge-originator-identification enable**](cmdqueryname=purge-originator-identification+enable) command is run and the **send-only** parameter is specified when configuring authentication, generated purge LSPs do not carry the POI TLV or host name TLV.
        + If the [**purge-originator-identification enable**](cmdqueryname=purge-originator-identification+enable) command is run and HMAC-MD5 authentication is configured, generated purge LSPs do not carry the POI TLV or host name TLV. If the command is run and authentication of another type is configured or no authentication is configured, generated purge LSPs carry the POI TLV and host name TLV. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          HMAC-SHA256 rather than HMAC-MD5 is recommended for the sake of security.
        + If the [**purge-originator-identification enable always**](cmdqueryname=purge-originator-identification+enable+always) command is run, generated purge LSPs carry the POI TLV and host name TLV, regardless of whether authentication is configured or whether the **send-only** parameter is specified when configuring authentication.
     2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Disable automatic IS-IS system ID recovery in case of conflicts.
     1. Run the [**quit**](cmdqueryname=quit) command to exit the IS-IS view and return to the system view.
     2. Run the [**isis system-id auto-recover disable**](cmdqueryname=isis+system-id+auto-recover+disable) command to disable automatic IS-IS system ID recovery in case of conflicts.
     3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.