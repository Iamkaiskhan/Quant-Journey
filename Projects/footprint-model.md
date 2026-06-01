# The Footprint Model

### A Discretionary SMC / ICT Trading Model

**Setup tag:** `B-P-D-C` → **B**ias → **P**OI → **D**isplacement → **C**onfirmation

> **Core idea:** A Point of Interest (POI) is the *footprint of the dealers* — their sentiment, their intent, and how they are moving recent price. We trade **with** the higher-timeframe bias, entering on a retracement into the imbalance that price leaves behind when it displaces away from a POI.

---

## 0. Timeframes

| Purpose | Timeframe |
|---|---|
| Bias / direction | HTF — **[ TO CONFIRM: 4H / 1H anchor ]** |
| Setup & execution | 15m → 5m |
| Imbalance refinement | 1m |

---

## 1. The Model — Step by Step

1. **Bias.** Define HTF direction using liquidity buildup, imbalance, and COT report.
2. **POI.** Mark the dealers' footprint — the zone where price should react in the bias direction.
3. **Reach.** Wait for price to trade into the POI.
4. **Displacement.** Expect a strong, one-directional move (a clean imbalance) off the POI in the bias direction. This is the first sign of a high-probability setup.
5. **Imbalance entry zone.** Mark the imbalance (FVG) the displacement left behind. Refine on 5m, then 1m for the *real* imbalance.
6. **Discount/premium.** Plot from the swing low of the imbalance area to the swing high it came from. Entry must sit in **discount** (for longs) / **premium** (for shorts).
7. **Liquidity sweep.** Price must sweep liquidity **first**, inside the discount zone, before the entry.
8. **Candle confirmation.** A confirming candle is required at the zone.
9. **MSS check & grade.** A+ if structure has already shifted; A if not (see §3).
10. **Execute.** If every condition is satisfied → take the trade.

---

## 2. The Two POIs (keep them separate)

- **Bias POI** — the *origin* of the move; where conviction comes from.
- **Entry POI** — the *imbalance* left by the displacement; where the trade actually triggers.

---

## 3. Grading: A+ vs A

| | **A+ — MSS Model** | **A — Non-MSS Model** |
|---|---|---|
| Sequence | Sweep → **MSS confirmed** → retrace into Entry POI → enter | Sweep → retrace into Entry POI → enter (**MSS expected *after***) |
| Confirmation | Structure has already shifted | Sweep + candle reaction only; structure not yet shifted |
| Nature | **Confirmed** | **Anticipatory** |
| Risk | 0.5% | 0.5% — **same for now**, revisit with data |

> **MSS = a strong breakout, NOT a wick sweep.**
> **Note:** The A-grade is an entry placed *before* the structural proof arrives. Tag A+ vs A separately in the journal — only the data will show whether anticipating the MSS pays as well as waiting for it.

---

## 4. Risk Rules

- **Risk per trade:** 0.5%
- **Max daily loss:** 1% → a hard ceiling of ~2 full-risk trades per day. This *is* the patience filter.
- **Weekly circuit breaker:** 4 losing setups in one week → **stop trading for the week. Review and improve only.**

---

## 5. Stop Loss & Take Profit

**Stop Loss**
- At the swing low below the imbalance, **or** the low formed during the retracement into the imbalance.
- Prefer the level below the **swept liquidity**, so a routine wick can't stop you out.

**Take Profit**
- Target the **next offloading zone of the dealers** (opposing liquidity / POI).
- **Minimum 3RR** — if the nearest valid target is below 3RR, **skip the trade.**
- Use **2 TP levels**, scaling toward **4RR**.

---

## 6. Sessions (Kill Zones)

Enter only inside:
- **London open**
- **New York open**
- **London close**

---

## 7. PRE-TRADE CHECKLIST — tick before EVERY entry

**Bias & context**
- [ ] HTF bias defined (direction + reason: liquidity buildup / imbalance / COT)
- [ ] Bias POI marked
- [ ] Inside a valid session (London open / NY open / London close)

**Setup**
- [ ] Price reached the POI
- [ ] Strong displacement (clean imbalance) off the POI in the bias direction
- [ ] Entry POI / imbalance zone marked (15m → 5m, refined on 1m)
- [ ] Discount/premium plotted — entry sits in discount (long) / premium (short)

**Trigger**
- [ ] Liquidity sweep occurred in the discount zone **first**
- [ ] Price retraced into the imbalance zone
- [ ] Candle confirmation present
- [ ] Graded: **A+** (MSS before entry) or **A** (no MSS yet)

**Risk**
- [ ] Risk set to 0.5%
- [ ] SL placed below swept liquidity (swing low / retracement low)
- [ ] TP1 + TP2 set, **minimum 3RR confirmed** (else SKIP)
- [ ] Daily loss not yet at 1% (not already 2 trades down)
- [ ] Not at 4 weekly losses

**Execute**
- [ ] **All boxes ticked → enter. Any box unchecked → NO TRADE.**

---

## 8. Post-Trade Journal

- [ ] Logged grade (A+ / A)
- [ ] Screenshot + entry reasoning saved
- [ ] R outcome recorded
- [ ] Rule followed? (Y/N — note any deviation)

---

## Open Items to Confirm

1. **Bias timeframe anchor** — set your HTF (4H / 1H) so the top-down chain is complete.
2. **A-grade risk** — currently equal to A+ (0.5%). Re-evaluate after ~30–40 logged trades of each grade.

---

*The Footprint Model — discipline over prediction. The checklist is the boss.*
