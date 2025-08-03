Overview of Clock Synchronization
=================================

Overview_of_Clock_Synchronization

#### Definition

Synchronization is classified into the following types:

* Clock Synchronization
  
  Clock synchronization maintains a strict relationship between signal frequencies or between signal phases. Signals are transmitted at the same average rate within the valid time. In this manner, all devices on a network run at the same rate.
  
  On a digital communication network, a sender places a pulse signal in a specific timeslot for transmission. A receiver needs to extract this pulse signal from this specific timeslot to ensure that the sender and receiver communicate properly. A prerequisite of successful communication between the sender and receiver is clock synchronization between them. Clock synchronization enables the clocks on the sender and receiver to be synchronized.
* Time Synchronization
  
  Generally, the word "time" indicates either a moment or a time interval. A moment is a transient in a period, whereas a time interval is the interval between two transients. Time synchronization is achieved by adjusting the internal clocks and moments of devices based on received time signals. The working principle of time synchronization is similar to that of clock synchronization. When a time is adjusted, both the frequency and phase of a clock are adjusted. The phase of this clock is represented by a moment in the form of year, month, day, hour, minute, second, millisecond, microsecond, and nanosecond. Time synchronization enables devices to receive discontinuous time reference information and to adjust their times to synchronize times. Clock synchronization enables devices to trace a clock source to synchronize frequencies.

![](images/fig_dc_ne_clock_cfg_500301.png "Click to enlarge")

The figure shows the difference between time synchronization and clock synchronization. In time synchronization (also known as phase synchronization), watches A and B always keep the same time. In clock synchronization, watches A and B keep different times, but the time difference between the two watches is a constant value, for example, 6 hours.


#### Purpose

On a digital communication network, clock synchronization is implemented to limit the frequency or phase difference between network elements (NEs) within an allowable range. Information is encoded into digital pulse signals using pulse code modulation (PCM) and transmitted on a digital communication network. If two digital switching devices have different clock frequencies, or if interference corrupts the digital bit streams during transmission, phase drift or jitter occurs. Consequently, code-element loss or duplication may occur in the buffer of the involved digital switching device, resulting in slip of transmitted bit streams. In addition, if the clock frequency or phase difference exceeds an allowable range, bit errors or jitter may occur, degrading the network transmission performance.