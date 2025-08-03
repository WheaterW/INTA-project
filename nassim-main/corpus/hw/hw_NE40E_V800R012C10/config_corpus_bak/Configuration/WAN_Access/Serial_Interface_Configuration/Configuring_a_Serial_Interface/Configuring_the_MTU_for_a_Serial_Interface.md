Configuring the MTU for a Serial Interface
==========================================

During MTU configuration for a serial interface, ensure that the MTUs of interfaces on directly connected devices are the same. Otherwise, services may be interrupted.

#### Context

The MTUs of interfaces on directly connected devices must be the same. If you run the [**mtu**](cmdqueryname=mtu) command to change the MTU of an interface on the local device, you also need to change the MTUs of interfaces on the devices directly connected to the local device to ensure that the local and remote MTUs are the same. Otherwise, services may be interrupted.

If an interface with a small MTU receives large packets, too many packet fragments may be generated. Consequently, some packets may be discarded due to the insufficient length of a QoS queue. To avoid this issue, increase the MTU. By default, an interface uses the first in first out (FIFO) mechanism for queue scheduling.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface serial**](cmdqueryname=interface+serial) *interface-number*
   
   
   
   The view of the serial interface whose MTU needs to be changed is displayed.
3. Run [**link-protocol ppp**](cmdqueryname=link-protocol+ppp)
   
   
   
   The link layer protocol of the serial interface is set to PPP.
4. Run [**mtu**](cmdqueryname=mtu) *mtu*
   
   
   
   An MTU is configured for the serial interface.
   
   
   
   The default MTU is 1500 bytes. It is recommended that you do not change the MTU unless necessary.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.