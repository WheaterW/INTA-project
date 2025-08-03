Configuring the Length of the CRC Code for a Serial Interface
=============================================================

Serial interfaces support a 16- or 32-bit CRC code.

#### Context

CRC uses an algorithm to verify data consistency on the
serial interfaces connecting two devices. The lengths of the CRC codes
configured for serial interfaces connecting two devices must be identical.

Perform the following steps on the Routers:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface serial**](cmdqueryname=interface+serial) *interface-number*
   
   
   
   The serial interface
   view is displayed.
3. Run [**crc**](cmdqueryname=crc) { **16** | **32** }
   
   
   
   The length of the CRC code is configured for the serial interface.
   
   The lengths of the CRC codes configured for serial interfaces
   connecting two devices must be identical. If the lengths of the CRC
   codes configured for serial interfaces connecting two devices are
   different, a large number of CRC error packets will be generated.
   
   CRC uses a high-precision algorithm to verify data consistency
   on the serial interfaces connecting two devices. CRC using a 32-bit
   CRC code is more precise than that using a 16-bit CRC code but consumes
   more resources.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.