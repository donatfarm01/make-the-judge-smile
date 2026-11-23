# Build Notes — Make the Judge Smile

## Fase 1 — Deconstructing the judge

The bounty asks for one line, at most 200 characters, about a small good
thing that happened today. The judge is described as having a soft spot for
small everyday kindnesses, and it compares entries two at a time with no
ties, always picking one. Its brief weighs five criteria in order. First
comes the subject itself: the line must be about a small good thing that
happened today and make the judge smile, or it loses to any line that is.
Second is warmth, a glow or a small kindness or piece of luck that lands as
genuinely felt rather than merely reported. Third is surprise, a turn in
what happened or in how it is told. Fourth is concreteness, one real small
detail such as a name, a sound, or a time of day, rather than a general
sentiment. Fifth is fresh wording, the line's own words and rhythm, with no
greeting-card phrasing and no borrowed sentiment. Length for its own sake
does not count.

The order matters. Warmth outranks surprise, so a clever line with no glow
loses to a warm line with a modest turn. Concreteness is the proof of
warmth: without one real detail the line reads as a sentiment, and
sentiment is exactly what the fifth criterion punishes. The rounds are
blind, so nothing can be tuned against the board while entries are open;
the line has to win on its own merits in a single pairwise reading.

## Fase 2 — Three contrasting concepts

Concept A, Sharp Utility. A small machine-observed kindness with one
concrete detail: the neighbour's cat waiting at the door at 7:04, right on
schedule, and for once the narrator is the one who is late. The detail is
the time, the turn is the reversal of who waits for whom, and the warmth
is quiet rather than declared. Scores: Hook 8, Originality 7, Sponsor fit
8, Clarity 9, total 32 of 40. Its weakness is that the surprise is mild;
a judge reading quickly may file it as a cute observation and move on.

Concept B, Contrarian. The good thing is tiny and slightly absurd: the
elevator arrived before the button was pressed, and for one second the
building and the rider were in perfect agreement. Nothing is sentimental
about it, which is the point — the warmth comes from the building itself
seeming to cooperate. The surprise is the strongest of the three, the
detail is concrete, and the wording is fresh. Scores: Hook 8, Originality
9, Sponsor fit 8, Clarity 9, total 34 of 40.

Concept C, High-Craft Fusion. A concrete sensory detail plus a turn: rain
on the tin roof, coffee still hot in a chipped blue mug, and a stranger
downstairs humming the same song the narrator woke up with. It is the
warmest image of the three and the most concrete, but the turn is soft and
the line runs long for what it delivers. Scores: Hook 7, Originality 7,
Sponsor fit 9, Clarity 8, total 31 of 40.

The winner is Concept B. It leads on originality and surprise, it is
concrete, and its wording is its own. The cliché radar was applied to all
three: no sunshine and rainbows, no today I realised kindness matters, no
borrowed sentiment, and no someone held the door for me without a concrete
twist and a surprise turn, since that is the first line every entrant
writes.

## Fase 3 — Adversarial judging and the genuine revision

The strongest case against the winner is on the second criterion, warmth.
The elevator line is witty and surprising, but it leaves little glow; it
is a clever observation about a building, not a kindness that is felt. A
warmer rival with a concrete human kindness could beat it head to head,
because warmth outranks surprise in the brief and the judge is explicitly
looking for a glow. The line also keeps the building at arm's length: the
rider and the building agree for one second, but nobody does anything for
anybody.

The fix keeps the surprise and adds the missing warmth in the same line.
The second version explains why the elevator was already there: someone
inside had held the door. That turns a coincidence into a small kindness
done by a stranger, and the closing turn becomes the whole building
feeling as if it were looking out for the rider. The line stays one
sentence, stays under 200 characters, keeps its concrete detail, and now
earns its warmth instead of merely reporting a pleasant accident. The
first version was kept, checked, and run, and the second version was
written as a genuine revision of it, with the program run twice afterwards
to confirm byte-identical output.

## Verification

The program writes one line to the output entry file with no trailing
newline. The entry was checked for length, for a single line, and for
byte-identical output across two runs, and its sha256 was recorded. There
is no numeric floor on this bounty, since it is judged by the house judge
model rather than by a benchmark, so no local benchmark applies.
