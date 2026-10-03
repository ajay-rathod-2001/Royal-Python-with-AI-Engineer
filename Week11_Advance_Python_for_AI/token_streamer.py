import time

HISTORY_OF_CHHATRAPATI_SHIVAJI_MAHARAJ= """## History of Chhatrapati Shivaji Maharaj:


Chhatrapati Shivaji Maharaj was born in **1630 at Shivneri Fort** in present-day Maharashtra. His father was **Shahaji Bhosale**, and his mother was **Jijabai**.

### Early life

Shivaji Maharaj grew up during a period when the Deccan was divided among several powerful states, including the **Bijapur Sultanate**, the **Mughal Empire**, and various local powers.

Under the influence of Jijabai and his advisers, he developed the idea of establishing **Swarajya (self-rule)**.

### Beginning of Swarajya

In his teenage years, Shivaji Maharaj began acquiring forts in the Pune region. **Torna Fort** is traditionally regarded as his first major fort captured, around **1645**.

He subsequently expanded his control by capturing or building several strategically important forts, including:

* Torna
* Rajgad
* Purandar
* Pratapgad
* Raigad
* Panhala
* Sindhudurg

### Conflict with Bijapur

The growing Maratha power brought Shivaji Maharaj into conflict with the **Bijapur Sultanate**.

In **1659**, Bijapur commander **Afzal Khan** marched against Shivaji Maharaj. Their famous meeting took place near **Pratapgad**, followed by a battle in which Shivaji's forces defeated the Bijapur army.

### Conflict with the Mughals

Shivaji Maharaj later came into direct conflict with the Mughal Empire.

In **1664**, his forces attacked **Surat**, an important commercial center.

In **1665**, the **Treaty of Purandar** was concluded with the Mughal commander Jai Singh.

In **1666**, Shivaji Maharaj travelled to **Agra** to meet Emperor Aurangzeb. He was placed under confinement but escaped and eventually returned to the Deccan.

### Expansion of the Maratha state

After returning, Shivaji Maharaj reorganized his forces and recovered territories lost under the Treaty of Purandar.

His state expanded across parts of present-day **Maharashtra and neighboring regions**.

He also developed a naval force to protect the Konkan coast and constructed or strengthened coastal forts such as **Sindhudurg**.

### Coronation at Raigad

On **6 June 1674**, Shivaji Maharaj was formally crowned at **Raigad Fort**.

He adopted the title **Chhatrapati**, and the coronation represented the formal establishment of his sovereign kingdom.

### Administration

Shivaji Maharaj established an organized administrative system. His important ministers were traditionally known as the **Ashta Pradhan**.

His administration dealt with:

* Revenue collection
* Justice
* Military organization
* Fort management
* Foreign relations
* Intelligence
* Civil administration

### Death

Shivaji Maharaj died on **3 April 1680 at Raigad Fort**.

His son **Sambhaji Maharaj** succeeded him.

### Historical legacy

The historical importance of Shivaji Maharaj is closely connected with the development of an independent **Maratha state**, his fort and military strategy, administration, naval organization, and the political idea of **Swarajya**.

**Timeline:**
**1630** — Birth → **1645** — Torna and early expansion → **1659** — Pratapgad/Afzal Khan episode → **1664** — Surat campaign → **1666** — Agra episode → **1674** — Coronation at Raigad → **1680** — Death.
"""


def stream_response(text):
    for word in text.split():
        time.sleep(0.1)
        yield word

gen_streamer = stream_response(HISTORY_OF_CHHATRAPATI_SHIVAJI_MAHARAJ)

for word in gen_streamer:
    print(word, end = " ", flush = True)