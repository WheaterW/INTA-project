Overview of Bit-Error-Triggered Protection Switching
====================================================

Bit-error-triggered protection switching triggers protection switching based on bit error events, meeting high network reliability requirements.

#### Definition

A bit error refers to the deviation between
a bit that is sent and the bit that is received. Cyclic redundancy
checks (CRCs) are commonly used to detect bit errors. Bit errors caused
by line faults can be corrected by rectifying the associated link
faults. Random bit errors caused by optical fiber aging or optical
signal jitter, however, are more difficult to correct. Bit-error-triggered
protection switching is a reliability mechanism that triggers protection
switching based on bit error events (bit error occurrence event or
correction event) to minimize bit error impact.


#### Purpose

The demand for network bandwidth is rapidly increasing
as mobile services evolve from narrowband voice services to integrated
broadband services, including voice and streaming media. Meeting the
demand for bandwidth with traditional bearer networks dramatically
raises carriers' operation costs. To tackle the challenges posed by
this rapid broadband-oriented development, carriers urgently need
mobile bearer networks that are flexible, low-cost, and highly efficient.
IP-based mobile bearer networks are an ideal choice. IP radio access
networks (IPRANs), a type of IP-based mobile bearer network, are being
increasingly widely used.

Traditional bearer networks use retransmission
or the mechanism that allows one end to accept only one copy of packets
from multiple copies of packets sent by the other end to minimize
bit error impact. IPRANs have higher reliability requirements than
traditional bearer networks when carrying broadband services. Traditional
fault detection mechanisms cannot trigger protection switching based
on random bit errors. As a result, bit errors may degrade or even
interrupt services on an IPRAN.

To solve this problem, configure
bit-error-triggered protection switching.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To prevent impacts on services, check whether protection links have
sufficient bandwidth resources before deploying bit-error-triggered
protection switching.



#### Benefits

Bit-error-triggered protection switching offers
the following benefits:

* Protects traffic against random bit errors, meeting high reliability
  requirements and improving service quality.
* Enables devices to record bit error events. These records help
  carriers locate the nodes or lines that have bit errors and take corrective
  measures accordingly.