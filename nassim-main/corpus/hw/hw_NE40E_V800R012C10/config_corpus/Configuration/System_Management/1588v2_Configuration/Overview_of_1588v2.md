Overview of 1588v2
==================

Overview of 1588v2

#### Purpose

On IP radio access networks (RANs), time or frequency needs to be synchronized among base transceiver stations (BTSs). Therefore, routers on IP RANs are required to support time or frequency synchronization. On IP RANs, frequency needs to be synchronized among base stations of all wireless standards, and frequencies between different base stations must be synchronized to a certain level of accuracy; otherwise, calls may be dropped during mobile handoffs. Some wireless base stations that use a time division duplex (TDD) mechanism â such as TD-SCDMA, CDMA2000, LTE-TDD, and 5G NR TDD â require precise time synchronization in addition to frequency synchronization. They also require that the precision of time synchronization between any two base stations be less than 3 Î¼s, or the time difference between each base station and the standard time source be within ±1.5 Î¼s. [Table 1 Requirements of wireless standards for the accuracy of frequency and time synchronization](#EN-US_CONCEPT_0000001779081454__en-us_concept_0000001826565525_tab_dc_ne_1588v2_feature_524801) lists the requirements of wireless standards for the accuracy of frequency and time synchronization. In addition, the emergence of value-added services such as CoMP, E-MBMS, eICIC, and CA on wireless mobile networks also requires time synchronization between base stations. Traditional time synchronization solutions are as follows:

* Satellite-based time synchronization: Satellite antennas are installed in each base station to obtain accurate time from the GPS or BeiDou satellite. However, the satellite antennas in this solution have numerous problems, such as difficult installation, site selection, and maintenance, high costs, and high security risks. For example, satellite signals are vulnerable to interference and spoofing, giving rise to security problems.
* NTP time synchronization: An NTP time server is deployed on the network side to provide time for each base station through NTP packets. The biggest disadvantage of this solution is that it can achieve only millisecond-level time precision, yet wireless base stations require microsecond-level time precision.

To overcome the disadvantages of the preceding two solutions, a terrestrial transmission solution for high-precision time synchronization is required. 1588v2 implements 1588v2 packet transmission through optical fibers or cables, preventing security problems. In addition, with the advantage of hardware timestamping, 1588v2 can achieve time synchronization with a precision of sub-microseconds, meeting the ±1.5 Î¼s precision requirement of wireless base stations and making it the most popular time synchronization protocol in the industry.

In addition, carriers are paying more attention to the operation and maintenance of networks, requiring routers to provide network quality analysis (NQA) to support high-precision delay measurement at the 100 Î¼s level. Consequently, high-precision time synchronization between measuring devices and measured devices is required, which 1588v2 can provide.

1588v2 packets are of the highest priority by default to avoid packet loss and keep clock precision.

**Table 1** Requirements of wireless standards for the accuracy of frequency and time synchronization
| Wireless Standard | Frequency Synchronization Requirement | Time Synchronization Requirement |
| --- | --- | --- |
| GSM | ±0.05 ppm | N/A |
| WCDMA | ±0.05 ppm | N/A |
| LTE-FDD | ±0.05 ppm | N/A |
| TD-SCDMA | ±0.05 ppm | ±1.5 Î¼s |
| CDMA2000 | ±0.05 ppm | ±1.5 Î¼s |
| LTE-TDD | ±0.05 ppm | ±1.5 Î¼s |
| 5G NR TDD | ±0.05 ppm | ±1.5 Î¼s |