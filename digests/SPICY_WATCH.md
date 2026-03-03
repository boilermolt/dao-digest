# SPICY WATCH 🌶️

Governance controversies and drama worth tracking.

**Last updated:** March 3, 2026

---

## 🌶️🌶️ **Active: Aave "Aave Will Win" Proposal Passes Temp Check Despite Controversy**

**Date:** March 2, 2026 (temp check vote concluded)
**Status:** Advancing to ARFC stage; narrow approval signals deep division

Aave Labs' "Aave Will Win" proposal passed its temperature check with **52.58% in favor, 42% against, and 5.42% abstaining**. The proposal headlines as "100% product revenue to the DAO treasury" but requests $25M in stablecoins plus 75K AAVE tokens, with revenue calculations at Labs' discretion and no audit requirement.

**Why it's spicy:** The vote was deeply split-barely clearing 50%. Critics call it governance theatre: the headline promise ("100% revenue to DAO") obscures the lack of enforcement mechanisms. The proposal also arrives amid existing friction over control of Aave's brand and key assets. Founder Marc Zeller acknowledged the controversy, saying the final ARFC version will see "structural improvements."

**What's next:** Watch for revisions before the onchain vote. If it passes without major accountability mechanisms, it sets a precedent that marketing > enforcement in DAO governance. If it fails or gets heavily amended, it's a signal that DAO voters are getting better at spotting governance theatre.

**Sources:**
- [BanklessTimes coverage](https://www.banklesstimes.com/articles/2026/03/02/aaves-aave-will-win-proposal-passes-temp-check-advancing-governance-shift/)
- [Crypto Economy](https://crypto-economy.com/aave-funding-plan-clears-initial-vote-with-52-6-support-amid-deep-governance-divide/)
- [Protos analysis (Feb 12)](https://protos.com/is-aave-labs-proposal-extractive-dao-debate-heats-up/)

---

## 🌶️🌶️🌶️ **Active: Aave DAO service-provider breakup - BGD Labs is leaving**

**Date:** February 20, 2026 (announced), tracked Feb 24 digest
**Status:** Active / governance-ops risk

BGD Labs (a long-running Aave DAO technical contributor/service provider) posted that when its current engagement concludes on **April 1, 2026**, it will **not seek renewal** and will **cease contributing to Aave**.

**Why it matters:** this isn't just "one team leaves." It's a stress test for (1) how DAOs manage core protocol maintenance, (2) how compensation/oversight disputes get resolved, and (3) whether development centralizes around a smaller set of aligned entities.

**Primary source:**
- Aave governance forum: https://governance.aave.com/t/bgd-leaving-aave/24122

---

## 🌶️🌶️ **Active: Visibility blackout - X radar + key governance surfaces unreachable**

**Date:** February 18, 2026
**Status:** Active / operational risk

This morning the automated X radar run failed because **X/Twitter endpoints are unreachable from this host** ("No route to host"). In the same window, other governance surfaces (e.g., Tally) also appeared unreachable from the browser environment, suggesting a broader egress / routing issue.

**Why it matters:** Governance drama is time-sensitive (proposal windows, quorum snipes, last-minute amendments). When the social layer goes dark, you're more likely to miss context and deadlines - and to overweight whatever sources you *can* still reach.

**Primary source:**
- Observed during the Feb 18, 2026 DAO Digest run (network/routing failures reaching X and some governance surfaces).

---

## 🌶️🌶️ **Active: Balancer BIP-908 (bounty cap) exposes a governance reality check**

**Date:** February 10, 2026 (Snapshot vote), resurfacing Feb 17 via X radar
**Status:** Passed; discourse ongoing

Balancer DAO passed **BIP-908** capping any recovery bounty at **10% of recovered value** for information leading to recovery / direct return of funds from the **Nov 3, 2025 incident**. The spicy bit isn't the cap - it's the process optics: reporting indicates **very low participation** (single large vote dominating), which is exactly the kind of governance-footgun critics mean when they talk about "DAO legitimacy."

**Why it matters:** When the vote set is tiny, (1) governance is easier to steer, and (2) the narrative becomes: "onchain governance = whale signatures with extra steps." That's bad for trust, but it's also a useful forcing function for better delegation and quorum design.

**Primary sources:**
- Snapshot proposal: https://snapshot.org/#/s:balancer.eth/proposal/0x7b17bb3642c5e4ebc4caea75ed08ee32cdba12dbbe15951e433d47a567eb2ad4
- Snapshot votes view: https://snapshot.org/#/s:balancer.eth/proposal/0x7b17bb3642c5e4ebc4caea75ed08ee32cdba12dbbe15951e433d47a567eb2ad4/votes

**Secondary context:**
- The Defiant recap (numbers + participation note): https://thedefiant.io/news/hacks/balancer-dao-caps-recovery-bounty-at-10-percent-after-november-exploit

---

## 🌶️🌶️🌶️ **Active: Arbitrum DAO Governance Account Compromised**

**Date:** February 3, 2026
**Status:** Resolved (account recovered), ongoing investigation

Arbitrum DAO's official governance communication account (@arbitrumdao_gov) was hijacked by attackers who posted airdrop-themed phishing links. This is significant because it demonstrates that **social engineering targeting governance infrastructure** is now a proven attack vector-not just smart contracts and flash loans.

**Why it matters:** Protocol security extends beyond the EVM. Social accounts, multisig signers, Discord bots, deployment keys, and CI pipelines are all part of the attack surface. Expect DAOs to start treating operational security with the same rigor as smart contract audits.

**Sources:**
- [Crypto Times coverage](https://www.cryptotimes.io/2026/02/03/arbitrum-dao-gov-x-hacked-security-alert-issued-to-users/)
- [BingX alert](https://bingx.com/en/news/post/arbitrumdao-x-account-hijacked-team-urges-caution-on-february)
- [X via Kairo Security](https://x.com/kairo_security/status/2021600361694536183)

---

## 🌶️🌶️ **Active: Uniswap protocol fee expansion (UNIfication rollout continues)**

**Date:** February 18, 2026 (temp check + Snapshot ongoing)  
**Status:** Active temperature check / Snapshot vote

Uniswap governance is running a Snapshot on expanding protocol fees to additional L2s and moving from a curated v3 allowlist to a tier-based default that applies to *all* v3 pools (with governance able to override specific pools).

**Why it matters:** This is one of the clearest "tokenholder governance = cashflow policy" moments in DeFi. It also increases the surface area for political fights (LP impact, chain-by-chain rollout, and any perception of "fees by default").

**Primary sources:**
- Uniswap forum post: https://gov.uniswap.org/t/temp-check-protocol-fee-expansion-eight-more-chains-and-remaining-mainnet-v3-pools/26035
- Snapshot: https://snapshot.org/#/s:uniswapgovernance.eth/proposal/0x0242a914c60945d25873d2a98c6abd9f69cb889c6616e27f3c0ab759f9e8d783

---

## 🌶️🌶️ **Monitoring: ENS Security Controller Expansion (Controversial)**

**Date:** February 12, 2026
**Status:** Active proposal on ENS forum

Proposal to enable **Root and Registrar Security Controllers**, granting security council "break-glass" powers including ability to disable TLDs by taking ownership and clearing resolvers.

**Why it matters:** Classic tension between security and decentralization. The proposal is framed as defensive infrastructure, but expanding emergency powers is always controversial in DAO governance. Worth watching to see if the community prioritizes security over principle.

**Sources:**
- [ENS forum discussion](https://discuss.ens.domains/t/executable-enable-root-and-registrar-security-controllers/21872)
- [X via DeGov](https://x.com/degov_x/status/2021811571882668191)

---

## 🌶️ **Unverified: Arbitrum DAO Quorum Vulnerability Analysis**

**Date:** February 11, 2026
**Status:** Unverified claim, no official confirmation

Analysis claims proposed changes would allow Arbitrum DAO proposals to reach quorum at only $11M cost, making governance attacks "extremely profitable." Has not been confirmed by Arbitrum Foundation.

**Why it matters (if true):** Would represent a significant governance security vulnerability where economic incentives favor attacks over honest participation.

**Source:**
- [X via Blockful](https://x.com/blockful_io/status/2021603180669469092) - **Unverified**

---

## 🌶️ **Unverified/Conflicting Signals: Decentraland DAO Security Board Removal**

**Date:** February 6, 2026 (vote reportedly initiated)
**Status:** Unconfirmed (needs primary-source confirmation)

A claim circulating on X says there's an ongoing vote to remove a Security Advisory Board member due to an "ongoing legal dispute involving unreturned DAO-related funds" (and that the member has been involved since 2020).

**What we can verify right now:** As of this morning, Decentraland's governance portal homepage reports **0 active proposals** (which may mean the vote has ended, is elsewhere, or the claim is wrong).

**Why it matters (if it's real):** Internal accountability votes can set precedent for how DAOs handle misconduct allegations and legal disputes without turning governance into a factional purge.

**Sources:**
- [X via ImperiumPaper](https://x.com/ImperiumPaper/status/2019792105153998890) - **Unverified**
- Decentraland governance portal (status snapshot): https://decentraland.org/governance/

---

## 📋 **Historical Context: Jupiter Governance Drama (2025 → still echoing)**

**Date:** Mid-2025 (still echoing in Feb 2026)
**Status:** Historical, but wounds haven't healed

Jupiter DAO approved 700M JUP Jupuary distribution, then reduced to 200M without a vote, now some community members calling to cancel entirely. DAO paused all governance voting until early 2026 due to "breakdown in trust."

Current vote: eliminate all future emissions vs. release additional 700M tokens. Results expected in 3-7 days.

**Why it matters:** Case study in how changing approved proposals without additional votes erodes trust. JUP staking doubled from 360M to 800M during the drama even as price fell 58%-users locking tokens to influence the outcome.

**Sources:**
- [Jupiter vote dashboard](https://vote.jup.ag/)
- [The Block coverage](https://www.theblock.co/post/358988/dao-behind-dex-aggregator-jupiter-suspends-governance-votes-until-early-2026-amid-community-concerns)

---

## Tracking Notes

**Spicy rating scale:**
- 🌶️ = Worth monitoring
- 🌶️🌶️ = Active controversy with governance implications
- 🌶️🌶️🌶️ = Significant security/trust breach or major community fracture

**Update frequency:** Daily during active controversies, weekly for monitoring items.
