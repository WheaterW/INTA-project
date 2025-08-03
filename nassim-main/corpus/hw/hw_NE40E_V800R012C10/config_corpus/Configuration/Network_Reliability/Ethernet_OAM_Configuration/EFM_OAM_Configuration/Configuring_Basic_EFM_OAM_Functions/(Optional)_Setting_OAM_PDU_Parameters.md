(Optional) Setting OAM PDU Parameters
=====================================

You can set the maximum OAM PDU size, interval at which OAM PDUs are sent, and interval at which OAM PDUs are received to effectively control OAM PDU transmission.

#### Context

EFM devices exchange OAM PDUs periodically to report the link status. You can set OAM PDU parameters to effectively manage networks.

OAM PDU parameters include the maximum OAM PDU size, interval at which OAM PDUs are sent, and interval at which OAM PDUs are received.

* After the maximum OAM PDU size is set on an interface, the interface discards packets whose sizes are greater than the maximum OAM PDU size. You can also change the maximum OAM PDU size to implement interworking between Huawei and non-Huawei devices.
* After setting up an EFM connection, two EFM devices exchange OAM PDUs at a specific interval to check whether the connection is working properly. If an EFM device does not receive any OAM PDU from its remote EFM device within the interval at which OAM PDUs are received, it considers that the link is not working properly. You can configure different intervals at which OAM PDUs are received to meet different user requirements. A short interval can be set for high-priority users or services sensitive to link quality. A long interval can be set for low-priority users or services insensitive to link quality.

Perform the following steps on the interfaces at both ends of a link.


#### Procedure

* Set the maximum OAM PDU size.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The view of the interface at one end of a link is displayed.
  3. Run [**efm packet max-size**](cmdqueryname=efm+packet+max-size) *size*
     
     The maximum OAM PDU size is set.
     
     If the maximum OAM PDU sizes set on the interfaces at both ends of a link are different, the interfaces negotiate the maximum OAM PDU size in the discovery phase. A smaller value between the maximum OAM PDU sizes at both ends is used.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Set the interval at which OAM PDUs are sent.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The view of the interface at one end of a link is displayed.
  3. Run [**efm interval**](cmdqueryname=efm+interval) *interval-value*
     
     The interval at which OAM PDUs are sent is set.
     
     You must set the same interval at which OAM PDUs are sent on the interfaces at both ends of a link. If you set different intervals at both ends, session negotiation fails or session flapping occurs.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The interval at which OAM PDUs are sent must be set for an interface only when EFM OAM has been globally enabled and EFM OAM has not been enabled on the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Set the interval at which OAM PDUs are received.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The view of the interface at one end of a link is displayed.
  3. Run [**efm timeout**](cmdqueryname=efm+timeout) *timeout-value*
     
     The interval at which OAM PDUs are received is set.
     
     You must set the same interval at which OAM PDUs are received on the interfaces at both ends of a link. If you set different intervals at both ends, session negotiation fails or session flapping occurs.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The interval at which OAM PDUs are received must be set for an interface only when EFM OAM has been globally enabled and EFM OAM has not been enabled on the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.