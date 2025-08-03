(Optional) Configuring a Time Synchronization Mode for a FlexE Physical Interface
=================================================================================

The FlexE standards define two 1588v2 message transmission modes: Overhead (OH) and Client. By default, 1588v2 messages are transmitted in OH mode.

#### Context

* OH mode: Clock messages are transmitted using FlexE overhead timeslots. The configuration related to clock synchronization is the same as that on a standard Ethernet interface.
* Client mode: Clock messages are transmitted using FlexE clients. In this mode, the FlexE interface that carries clock services must be bound to a FlexE physical interface that has clock services deployed.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This function is supported only on the NE40E-M2H/NE40E-M2K/NE40E-M2K-B.



#### Pre-configuration Tasks

1588v2 has been configured, no matter which mode is used to transmit 1588v2 messages. For details, see *HUAWEI NE40E-M2 series Configuration Guide* > *System Management*.

After 1588v2 is configured on a FlexE physical interface, 1588v2 messages are transmitted in OH mode by default. To change the transmission mode of 1588v2 messages to Client, perform the following steps.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of a specified FlexE physical interface (for example, FlexE-50G 0/1/0) is displayed.
3. Run [**clock binding flexe**](cmdqueryname=clock+binding+flexe) **interface** *iftype* *ifnum*
   
   
   
   A specified FlexE interface carrying clock services is bound to the FlexE physical interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.