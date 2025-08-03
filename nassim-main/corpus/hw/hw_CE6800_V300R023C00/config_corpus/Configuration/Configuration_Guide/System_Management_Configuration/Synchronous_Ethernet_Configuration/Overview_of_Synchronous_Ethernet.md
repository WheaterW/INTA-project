Overview of Synchronous Ethernet
================================

Overview of Synchronous Ethernet

#### Definition

Synchronous Ethernet (SyncE) enables a device to input clock signals from an external clock source or extract clock signals from Ethernet bit streams. It also enables clock signals to be transmitted to downstream devices through Ethernet. This ensures clock synchronization between upstream and downstream devices.


#### Purpose

On a communications network, clock synchronization is implemented to limit the frequency or phase difference between network elements (NEs) within an allowable range. Pulse code modulation (PCM) is used to encode information into digital pulse signals before transmission. If two digital switching devices have different clock frequencies, or if interference corrupts the digital bit streams during transmission, phase drift or jitter occurs. Consequently, data loss or duplication may occur in the buffer of the involved digital switching device, resulting in incorrect transmission of bit streams. In addition, if the clock frequency or phase difference exceeds an allowable range, bit errors or jitter may occur, degrading the network transmission performance.

Traditionally, the sites on a communications network need to obtain accurate clock signals from the Global Positioning System (GPS) to achieve clock synchronization for telecommunication services. However, this involves high construction and security costs.

SyncE enables a device to select the optimal clock source for synchronization over Ethernet lines. This ensures that the transmit and receive clocks of both communication parties are synchronized.


#### Benefits

SyncE allows sites to obtain clock signals over Ethernet lines rather than using GPS antennas. This reduces construction and maintenance costs.