Configuring an IPv4 IS-IS Interface
===================================

IS-IS can send Hello packets through an interface to establish neighbor relationships and flood LSPs only after IS-IS is enabled on the interface.

#### Context

The IS-IS device level and interface level determine the level of neighbor relationships. By default, Level-1 and Level-2 neighbor relationships are established between Level-1-2 devices. If only one level (Level-1 or Level-2) of neighbor relationships is required, you can configure the level of an interface to prevent the establishment of neighbor relationships of the other level.

After IS-IS is enabled on an interface, the interface will automatically send Hello packets, attempting to establish neighbor relationships. If a peer device is not an IS-IS device or if an interface is not expected to send Hello packets, suppress the interface. After the IS-IS interface is suppressed, the routes of the network segment where the interface resides can still be advertised but Hello packets are not sent. This reduces link bandwidth consumption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**isis interface limit disable**](cmdqueryname=isis+interface+limit+disable)
   
   
   
   The limit on the number of IS-IS interfaces that can be configured on the device is removed.
   
   
   
   After this command is run, the limit on the number of IS-IS interfaces that can be configured on the device is removed. To restore the limit, run the [**undo isis interface limit disable**](cmdqueryname=undo+isis+interface+limit+disable) command. After the limit is restored and the number of IS-IS interfaces on the device is greater than or equal to the limit, no more IS-IS interfaces can be added on the device.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
   
   
   
   IS-IS is enabled on the interface.
   
   
   
   After this command is run, the IS-IS device uses this interface to send Hello packets and flood LSPs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Loopback interfaces do not need to establish neighbor relationships. If IS-IS is enabled on a loopback interface, the routes of the network segment where the loopback interface resides will be advertised through other IS-IS interfaces.
5. (Optional) Run [**isis circuit-level**](cmdqueryname=isis+circuit-level) [ **level-1** | **level-1-2** | **level-2** ]
   
   
   
   A level is set for the interface.
6. (Optional) Run [**isis silent**](cmdqueryname=isis+silent) [ **advertise-zero-cost** ]
   
   
   
   The IS-IS interface is suppressed.
   
   
   
   When an IS-IS interface is suppressed, the interface no longer accepts or sends IS-IS packets. The routes of the network segment where the interface resides, however, can still be advertised to other IS-IS devices in the same area.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.