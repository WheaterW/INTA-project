Enabling the Payload Scramble Function on a Serial Interface
============================================================

To prevent communication failures caused by consecutive
0s or 1s on a link, enable the payload scramble function on a serial
interface.

#### Context

On a datacom network, the data link layer transmits distributed
data frames to a specified interface at the physical layer. Upon receipt,
the interface decapsulates these frames into data bits, encodes the
bits based on the coding mode, and transmits them to a remote interface
through high and low levels on a link. Upon receipt of the levels,
the remote interface decodes them and restores them to data bits.
In this way, the local device can communicate with the remote device.

If the payload of a data frame contains consecutive 0s, the link
will stay at the zero level for a long time. After failing to detect
signals for a prolonged period of time, the remoter interface mistakenly
thinks that all bits have been received or the link is faulty, leading
to a communication failure.

To resolve this problem, enable
the payload scramble function on a synchronous serial interface or trunk-serial interface. Using this function,
the interface adds interference to the payload to prevent consecutive
0s or 1s in the payload, avoiding communication failures.

Configurations
of the payload scramble function on the local and remote interfaces
must be consistent.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the specified serial interface or trunk-serial interface is displayed.
3. Run [**link-protocol**](cmdqueryname=link-protocol) **atm**
   
   
   
   ATM is configured as the link layer protocol.
4. Run [**scramble**](cmdqueryname=scramble)
   
   
   
   The payload scramble function
   is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.