Configuring the Frame Format for a POS Interface
================================================

The frame format of a POS interface determines the application
mode of the interface. POS interfaces support two frame formats: SDH
and SONET.

#### Context

A POS interface supports the following types of frame
formats:

* SDH
* SONET

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
   
   
   
   The POS interface
   view is displayed.
3. Run [**frame-format**](cmdqueryname=frame-format) { **sdh** | **sonet** }
   
   
   
   A frame format is configured for the POS interface.
   
   SDH and
   SONET are two optical transmission standards defined by different
   organizations. These two standards do not have obvious differences
   in contents and specifications. The selection of SDH or SONET is determined
   by carriers in different geographical locations and by different device
   manufacturers. The frame format configured on the POS interface must
   be the same as that on transmission devices.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.