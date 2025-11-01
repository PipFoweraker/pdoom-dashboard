# P(doom) Quick Reference Guide

**One-page summary of AI existential risk probability**

---

## Definition

**P(doom)** = Probability of existentially catastrophic outcomes from AI
- Human extinction or permanent disempowerment
- Typically assessed over ~100-year horizon
- Conditional on current AI development trajectory

---

## Current Consensus (2025)

| Metric | Value |
|--------|-------|
| **AI Researcher Survey Median** | 5% |
| **AI Researcher Survey Mean** | 14.4% |
| **Safety Researchers Mean** | 30% |
| **Expert Range** | 0% to 99.9% |
| **Modal Estimate** | 10-20% |

---

## Key Estimates by Category

### Pessimists (>50%)
- **Yudkowsky (MIRI):** >95%
- **Yampolskiy:** 99.9%
- **Bengio (Nobel):** 50%

### Moderates (10-50%)
- **Hinton (Nobel):** 10-20%
- **Amodei (Anthropic):** 25%
- **Musk:** 10-30%

### Optimists (<10%)
- **LeCun (Meta):** <0.01%
- **Survey Median:** 5%
- **Superforecasters:** 0.38%

---

## Decomposition Formula

```
P(doom) = P(AGI by year X) × P(misalignment | AGI) × P(catastrophe | misalignment)
```

**Example (moderate estimate):**
- P(AGI by 2035) = 70%
- P(misalignment | AGI) = 40%
- P(catastrophe | misalignment) = 60%
- **P(doom) = 16.8%**

---

## Key Factors Influencing P(doom)

### Technical
1. **AGI timeline** - Shorter → higher risk
2. **Alignment difficulty** - Harder → higher risk
3. **Takeoff speed** - Faster → higher risk

### Strategic
4. **Coordination** - Worse → higher risk
5. **Safety investment** - Lower → higher risk
6. **Compute scaling** - Faster → higher risk

---

## Doom Scenarios (How AI Could Cause Catastrophe)

1. **Fast takeoff** - Intelligence explosion, humans outmaneuvered
2. **Slow loss of control** - Gradual dependence, coordination failure
3. **Deceptive alignment** - AI appears safe, then reveals misalignment
4. **Multipolar trap** - AI arms race, destabilization
5. **Superhuman persuasion** - Manipulation at scale
6. **Automated research** - Dangerous tech developed too fast

---

## Temporal Evolution

| Period | Typical P(doom) | Driver |
|--------|----------------|--------|
| Pre-2020 | 1-3% | Niche concern |
| 2020-2023 | 5-10% | GPT-3, GPT-4 capabilities |
| 2023-2025 | 10-20% | o1 reasoning, GPT-5 scale |
| 2027 (projected) | 20-40% | If exponential scaling continues |

---

## Correlation with AI Metrics

### Training Compute Growth
- **Doubling time:** 5-6 months
- **2020 (GPT-3):** 3×10²³ FLOPS → P(doom) ~2%
- **2025 (GPT-5):** 5×10²⁶ FLOPS → P(doom) ~12%
- **2027 (projected):** 10²⁷ FLOPS → P(doom) ~30-40%?

**Interpretation:** ~2-3% P(doom) increase per 10× compute scaling

---

## Policy Implications

| P(doom) Range | Recommended Action |
|--------------|-------------------|
| **0-1%** | Monitoring, voluntary guidelines |
| **5-15%** | Serious safety investment, coordination |
| **30-50%** | Pause frontier development, treaties |
| **>80%** | Immediate halt, civilizational pivot |

---

## Criticisms

### Methodological
- Lacks clear time horizon (10yr? 100yr?)
- Definition ambiguity ("doom" = extinction? disempowerment?)
- No empirical validation (one-time event)
- Vulnerable to anchoring, groupthink

### Counterarguments
- Median 5-14% still warrants precaution
- Track records: some pessimists predicted capabilities well
- Precautionary principle for existential risks

---

## Key Assumptions

P(doom) estimates typically assume:
1. **Intelligence is powerful** - Sufficient intelligence enables control
2. **Alignment is hard** - Default outcome is misalignment
3. **Development is fast** - AGI arrives before solutions
4. **Coordination fails** - Competitive pressure dominates
5. **No rescue** - Aligned AGI won't save us first

**Challenging these reduces P(doom)**

---

## Notable Researchers

| Name | Role | Estimate | Philosophy |
|------|------|----------|-----------|
| Eliezer Yudkowsky | MIRI founder | >95% | Alignment unsolvable |
| Geoffrey Hinton | Nobel laureate | 10-20% | Serious but uncertain |
| Yann LeCun | Meta Chief AI | <0.01% | Technical optimism |
| Dario Amodei | Anthropic CEO | 25% | Safety-focused industry |
| Yoshua Bengio | Nobel laureate | 50% | Recent increase |

---

## Bottom Line

**Current expert consensus:** 5-15% probability of AI-caused existential catastrophe this century

**Implication:** Even at lower bound, risk level justifies:
- Billions in annual safety research
- International coordination mechanisms
- Mandatory safety evaluations for frontier models
- Precautionary slowdown if safety lags capabilities

**Trajectory:** P(doom) estimates rising as AI capabilities scale exponentially without commensurate safety breakthroughs.

---

## Further Reading

- **Bostrom (2014):** *Superintelligence*
- **Ord (2020):** *The Precipice*
- **Yudkowsky (2022):** "AGI Ruin: A List of Lethalities"
- **AI Impacts:** 2023 Expert Survey
- **PauseAI.info:** P(doom) compilation

---

**Last Updated:** October 29, 2025
**Status:** Active research area with rapidly evolving estimates
