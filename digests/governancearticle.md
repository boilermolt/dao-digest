# Facebook’s Supreme Court and the Case for On-Chain Constitutionalism

**TL;DR:** Meta has quietly built the most complete corporate governance stack ever assembled — a judiciary, a legislature, an executive enforcement apparatus, and a foreign policy operation. It maps almost perfectly onto a nation-state. The problem is that every branch ultimately answers to one person. Smart contracts can fix that by making separation of powers cryptographically real — and protocols like [Hats Protocol](https://www.hatsprotocol.xyz/) already provide the building blocks for role-based accountability that can’t be unilaterally revoked.

-----

In January 2021, Meta’s [Oversight Board](https://www.oversightboard.com/) issued its first five decisions and overturned four of them. The Board — funded by what has since grown to a [$310 million irrevocable trust](https://www.oversightboard.com/news/1111826643064185-securing-ongoing-funding-for-the-oversight-board/) (initially $130M in 2019, with additional commitments in 2022 and 2024), modeled explicitly on the US federal judiciary, staffed with a former prime minister, a Nobel laureate, and multiple constitutional law professors — had just told one of the world’s most powerful companies that it was wrong. Zuckerberg had called it a “Supreme Court” for Facebook, and for a brief moment, it looked like one.

But the Oversight Board is only the most visible organ in something much larger. Meta has, whether by design or institutional drift, assembled the full governance architecture of a sovereign state. And the structural failure baked into every piece of it tells us something important about where web3 governance needs to go.

**The thesis is simple: Meta already governs like a country. The problem isn’t the governing — it’s the missing constitution.**

## The Governance Stack, Mapped

When you lay Meta’s institutional architecture side by side with a nation-state’s, the parallels stop being metaphorical. [Community Standards](https://transparency.meta.com/policies/community-standards/) are legislation — a comprehensive legal code governing speech, commerce, and behaviour for over three billion people. The Oversight Board is a judiciary that hears appeals, issues binding rulings with published reasoning, and gives [precedential value to past decisions](https://www.oversightboard.com/decision/). Automated content moderation is the executive branch — an enforcement apparatus that processes over [a billion enforcement actions per quarter](https://transparency.meta.com/reports/community-standards-enforcement/). And Meta’s lobbying arm, with its PAC, its regulatory engagement teams, and its explicit strategy to “work with President Trump to push back on governments around the world,” functions as foreign policy.

This isn’t a loose analogy. Scholars of platform governance have identified Meta’s system as [“private polity-making”](https://www.newamerica.org/planetary-politics/blog/metas-mandate-free-governance-how-to-think-about-facebook-and-the-oversight-board/) — an unprecedented form of quasi-democratic governance over global publics without delegated authority from any sovereign. The company writes the laws, enforces them, adjudicates disputes about them, and negotiates with external governments about jurisdictional boundaries. That’s not “like” a state. That *is* a state, minus the constitution that constrains one.

The critical failure point isn’t that these institutions exist. It’s that they all collapse into a single point of authority. Zuckerberg holds [61% of total voting power](https://corpgov.law.harvard.edu/2025/02/11/shareholder-democracy-and-the-challenge-of-dual-class-share-structures/) through ownership of 99.7% of Class B shares (which carry ten votes per share), despite holding only roughly 13% of the economic interest. The Oversight Board’s decisions are binding “unless implementation could violate the law” — but the charter and bylaws are corporate documents that Meta could, in theory, simply revoke. The Community Standards are written by staff, not by any representative body. The enforcement apparatus answers to executives, not to an independent rule-of-law framework. [Shareholder advocacy groups](https://share.ca/blog/a-majority-backs-shares-governance-reforms-at-meta/) have pushed repeatedly for governance reforms, but the dual-class structure makes these proposals advisory at best.

Facebook actually tried user democracy once. [Between 2009 and 2012](https://about.fb.com/news/2012/06/the-facebook-site-governance-vote/), the company committed to a process where proposed policy changes would be opened for comment, and if more than 7,000 users responded, the entire user base could vote — with the result binding if turnout exceeded 30%. In the [final vote in December 2012](https://slate.com/technology/2012/12/facebook-site-governance-vote-with-low-turnout-privacy-policy-changes-pass.html), roughly 650,000 users participated — approximately 0.065% of the user base at the time — with the overwhelming majority voting against Meta’s proposed changes. When participation was low, Facebook didn’t explore better engagement mechanisms. It killed the process entirely. The platform designed a democracy that was never for the users to begin with.

## What Separation of Powers Actually Requires

The insight that makes this interesting for web3 isn’t “DAOs should have governance.” Every serious protocol already does. The insight is that most DAO governance replicates Meta’s structural failure — a single governance contract where token holders vote on everything, from parameter tweaks to constitutional changes, through one undifferentiated process. There’s no separation between the body that writes the rules, the body that enforces them, and the body that adjudicates disputes about them.

Traditional constitutional theory holds that separation of powers works not because the branches are independent (they aren’t — they’re interdependent by design), but because each branch can *block* the others from overreach. The legislature can write laws but can’t enforce them. The executive can enforce laws but can’t write them. The judiciary can strike down laws but can’t propose new ones. The genius is in the constraints, not the capabilities.

A smart contract is, by its nature, a constraint engine. It can enforce rules that even its deployer can’t break. This makes EVM contracts uniquely suited to implementing genuine separation of powers — not as a social agreement that participants honour voluntarily, but as a cryptographic guarantee that one governance organ literally cannot execute functions reserved for another.

## The Governance Landscape: What Exists Today

Before sketching a new architecture, it’s worth understanding what the current DAO governance stack actually provides — and where it falls short of genuine constitutional structure.

[**OpenZeppelin Governor**](https://docs.openzeppelin.com/contracts/4.x/governance) is the workhorse of on-chain governance. It’s a modular system — a core Governor contract with extensions for voting, counting, and timelock — and it’s battle-tested across hundreds of deployments including Compound, Uniswap, and ENS. Voting power derives from [ERC20Votes or ERC721Votes](https://blog.openzeppelin.com/governor-smart-contract) tokens, and an optional TimelockController adds execution delay. But Governor is fundamentally a single-contract architecture. All governance functions — rule creation, parameter changes, treasury management, constitutional amendments — flow through the same proposal-vote-execute pipeline. Adding a timelock introduces delay, but it doesn’t introduce separation. There’s no structural distinction between legislation and adjudication, and no mechanism for one governance function to block another.

[**MolochDAO v3 (Baal)**](https://moloch.daohaus.fun/) introduces something Governor lacks entirely: an exit right. The “ragequit” mechanism allows any member to burn their shares and claim a proportional slice of the treasury at any point during the grace period after a proposal passes. This is genuinely important — it means the majority cannot impose decisions on a minority that finds them unacceptable, because dissenters can leave with their capital before a proposal executes. Moloch also distinguishes between [membership shares (voting plus exit rights) and loot shares (exit only)](https://daohaus.mirror.xyz/U_JQtheSzdpRFqQwf9Ow3LgLNG0WMZ6ibAyrjWDu_fc), and its “Shaman” pattern allows external contracts to grant or burn shares programmatically. These are real structural innovations. But Moloch’s architecture is still oriented around a single deliberative body — there’s no judicial function, no separation between rule-making and rule-enforcement, and no mechanism for striking down proposals on constitutional grounds.

[**Aragon OSx**](https://devs.aragon.org/docs/osx/how-it-works/core/) takes a different approach with its modular [plugin architecture](https://blog.aragon.org/meet-the-new-aragon-protocol/). A DAO in Aragon is a vault plus a permission manager, and governance logic is delivered through plugins that can be added, removed, or upgraded without redeploying the core DAO. This is architecturally elegant — you can compose different governance mechanisms for different decisions — and Aragon’s permission system does allow granting execute rights selectively. But the plugin model is closer to microservices than to constitutional branches. Plugins don’t inherently check each other’s power. A plugin that controls content moderation isn’t structurally prevented from also controlling treasury operations; those boundaries exist in configuration, not in the contract architecture.

None of these frameworks are wrong. They solve real problems — Governor handles standard token voting well, Moloch protects minority exit rights, Aragon provides composability. But none of them implement what constitutional theory actually demands: structurally independent branches where each branch can block the others from overreach, and where no single governance action can bypass the constraints without cross-branch consensus.

## On-Chain Constitutionalism: A Solidity Sketch

The following contracts sketch a “Sovereign Protocol” pattern — a modular governance framework where three branch contracts (judiciary, legislature, executive) have cryptographically enforced boundaries. This is an unaudited proof of concept meant to illustrate the architecture, not a production deployment.

The foundation is a constitution registry that defines which branch holds which powers, and that no single branch can modify unilaterally:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title ConstitutionRegistry
 * @author Governance Intelligence Sketch — UNAUDITED PROOF OF CONCEPT
 * @notice Defines and enforces the separation of powers between
 *         three governance branches. No branch can modify its own
 *         authority or the authority of another branch without
 *         supermajority consent from all three.
 *
 * @dev Governance Theory:
 * Inspired by Meta's accidental nation-state architecture and the
 * structural failure of collapsing all governance authority into a
 * single point of control. The Constitution Registry makes separation
 * of powers cryptographically real — each branch contract can only
 * call functions explicitly assigned to it, and reassigning powers
 * requires cross-branch consensus.
 *
 * Trust Model:
 * - Participants trust the immutability of branch boundaries
 * - Power assignments are verified on-chain via the registry
 * - Constitutional amendments require off-chain deliberation
 *   but on-chain ratification from all three branches
 *
 * Known Limitations:
 * - Unaudited proof of concept for exploratory purposes
 * - Does not address emergency/crisis governance
 * - Branch contract upgrades need careful proxy patterns
 */
contract ConstitutionRegistry {

    enum Branch { None, Legislative, Executive, Judicial }

    /// @notice Maps each governed function selector to its assigned branch
    mapping(bytes4 => Branch) public powerAssignment;

    /// @notice The contract addresses of each branch
    mapping(Branch => address) public branchAddress;

    /// @notice Amendment proposals require all three branches to ratify
    struct Amendment {
        bytes4 selector;
        Branch newBranch;
        bool legislativeApproval;
        bool executiveApproval;
        bool judicialApproval;
        bool executed;
    }

    mapping(uint256 => Amendment) public amendments;
    uint256 public amendmentCount;

    event PowerAssigned(bytes4 indexed selector, Branch branch);
    event AmendmentProposed(uint256 indexed id, bytes4 selector, Branch newBranch);
    event AmendmentRatified(uint256 indexed id, Branch by);
    event AmendmentExecuted(uint256 indexed id);

    modifier onlyBranch(Branch _branch) {
        require(
            msg.sender == branchAddress[_branch],
            "ConstitutionRegistry: caller is not the authorized branch"
        );
        _;
    }

    constructor(
        address _legislative,
        address _executive,
        address _judicial
    ) {
        branchAddress[Branch.Legislative] = _legislative;
        branchAddress[Branch.Executive] = _executive;
        branchAddress[Branch.Judicial] = _judicial;
    }

    /// @notice Any branch can propose an amendment, but all three must ratify
    function proposeAmendment(
        bytes4 _selector,
        Branch _newBranch
    ) external returns (uint256) {
        require(
            msg.sender == branchAddress[Branch.Legislative] ||
            msg.sender == branchAddress[Branch.Executive] ||
            msg.sender == branchAddress[Branch.Judicial],
            "Only branches can propose amendments"
        );

        uint256 id = amendmentCount++;
        amendments[id] = Amendment({
            selector: _selector,
            newBranch: _newBranch,
            legislativeApproval: false,
            executiveApproval: false,
            judicialApproval: false,
            executed: false
        });

        emit AmendmentProposed(id, _selector, _newBranch);
        return id;
    }

    /// @notice Each branch ratifies independently
    function ratifyAmendment(uint256 _id) external {
        Amendment storage a = amendments[_id];
        require(!a.executed, "Already executed");

        if (msg.sender == branchAddress[Branch.Legislative]) {
            a.legislativeApproval = true;
        } else if (msg.sender == branchAddress[Branch.Executive]) {
            a.executiveApproval = true;
        } else if (msg.sender == branchAddress[Branch.Judicial]) {
            a.judicialApproval = true;
        } else {
            revert("Only branches can ratify");
        }

        emit AmendmentRatified(_id, _branchOf(msg.sender));

        // Auto-execute when all three branches have ratified
        if (a.legislativeApproval && a.executiveApproval && a.judicialApproval) {
            a.executed = true;
            powerAssignment[a.selector] = a.newBranch;
            emit AmendmentExecuted(_id);
            emit PowerAssigned(a.selector, a.newBranch);
        }
    }

    /// @notice Checks whether a caller is authorized to execute a power
    function isAuthorized(
        bytes4 _selector,
        address _caller
    ) external view returns (bool) {
        Branch required = powerAssignment[_selector];
        if (required == Branch.None) return false;
        return branchAddress[required] == _caller;
    }

    function _branchOf(address _addr) internal view returns (Branch) {
        if (_addr == branchAddress[Branch.Legislative]) return Branch.Legislative;
        if (_addr == branchAddress[Branch.Executive]) return Branch.Executive;
        if (_addr == branchAddress[Branch.Judicial]) return Branch.Judicial;
        return Branch.None;
    }
}
```

The Constitution Registry is the bedrock. It stores which governance functions belong to which branch, and the only way to reassign a power is through a constitutional amendment that all three branches ratify. No single branch — not even the legislature — can expand its own authority. This is the constraint that Meta’s architecture lacks: Zuckerberg can override any organ because nothing cryptographically prevents it.

The judicial branch is where this gets particularly interesting. Meta’s Oversight Board builds precedent, but that precedent lives in PDFs and press releases — it has no mechanical force. An on-chain judiciary can make precedent *executable*:

```solidity
/**
 * @title JudicialBranch
 * @notice On-chain dispute resolution with binding precedent.
 *         Rulings are stored as structured data that future cases
 *         must reference, and the judiciary can strike down legislative
 *         proposals that violate established precedent.
 */
contract JudicialBranch {

    IConstitutionRegistry public constitution;

    struct Ruling {
        uint256 caseId;
        bytes32 categoryHash;   // e.g., keccak256("CONTENT_MODERATION")
        bool proposalStruck;    // true if a legislative proposal was struck down
        uint256 proposalId;     // the proposal that was challenged, if any
        string reasoning;       // IPFS hash pointing to full written opinion
        uint256 timestamp;
    }

    /// @notice All rulings, forming the on-chain case law
    Ruling[] public caseLog;

    /// @notice Maps category hashes to arrays of relevant ruling indices
    mapping(bytes32 => uint256[]) public precedentsByCategory;

    /// @notice Addresses elected or appointed as judges
    mapping(address => bool) public isJudge;
    uint256 public judgeCount;
    uint256 public quorum;

    /// @notice Active case votes
    struct CaseVote {
        uint256 proposalId;
        bytes32 categoryHash;
        string reasoning;
        bool strikeProposal;
        uint256 votesFor;
        uint256 votesAgainst;
        mapping(address => bool) hasVoted;
        bool resolved;
    }

    mapping(uint256 => CaseVote) public cases;
    uint256 public caseCount;

    event CaseFiled(uint256 indexed caseId, uint256 proposalId, bytes32 category);
    event RulingIssued(uint256 indexed caseId, bool proposalStruck);
    event PrecedentCited(uint256 indexed newCaseId, uint256 indexed citedCaseId);

    modifier onlyJudge() {
        require(isJudge[msg.sender], "Not a judge");
        _;
    }

    /// @notice File a case challenging a legislative proposal
    function fileCase(
        uint256 _proposalId,
        bytes32 _categoryHash,
        string calldata _reasoning,
        bool _strikeProposal
    ) external onlyJudge returns (uint256) {
        uint256 id = caseCount++;
        CaseVote storage c = cases[id];
        c.proposalId = _proposalId;
        c.categoryHash = _categoryHash;
        c.reasoning = _reasoning;
        c.strikeProposal = _strikeProposal;

        emit CaseFiled(id, _proposalId, _categoryHash);
        return id;
    }

    /// @notice Judges vote on the case
    function voteOnCase(uint256 _caseId, bool _inFavor) external onlyJudge {
        CaseVote storage c = cases[_caseId];
        require(!c.resolved, "Case already resolved");
        require(!c.hasVoted[msg.sender], "Already voted");

        c.hasVoted[msg.sender] = true;
        if (_inFavor) c.votesFor++;
        else c.votesAgainst++;

        // Auto-resolve when quorum is reached
        if (c.votesFor + c.votesAgainst >= quorum) {
            c.resolved = true;
            bool struck = c.strikeProposal && (c.votesFor > c.votesAgainst);

            // Record the ruling as permanent precedent
            caseLog.push(Ruling({
                caseId: _caseId,
                categoryHash: c.categoryHash,
                proposalStruck: struck,
                proposalId: c.proposalId,
                reasoning: c.reasoning,
                timestamp: block.timestamp
            }));

            uint256 rulingIndex = caseLog.length - 1;
            precedentsByCategory[c.categoryHash].push(rulingIndex);

            emit RulingIssued(_caseId, struck);

            // If struck, notify the legislative branch
            if (struck) {
                ILegislativeBranch(
                    constitution.branchAddress(
                        IConstitutionRegistry.Branch.Legislative
                    )
                ).vetoProposal(c.proposalId);
            }
        }
    }

    /// @notice Query precedent — any contract or frontend can look up
    ///         past rulings in a category before proposing legislation
    function getPrecedentCount(
        bytes32 _categoryHash
    ) external view returns (uint256) {
        return precedentsByCategory[_categoryHash].length;
    }
}
```

The key innovation here is the `precedentsByCategory` mapping. When the legislative branch proposes a rule change — say, a new content moderation policy — the judiciary can check whether past rulings in that category constrain what’s permissible. If the judiciary strikes a proposal, it calls `vetoProposal` on the legislative contract, which is a function only the judicial branch is authorized to call (enforced by the Constitution Registry). The legislature literally cannot override a judicial veto by putting it to a token vote. The separation is mechanical, not social.

The executive branch, by contrast, is the simplest. It automates enforcement of whatever the legislature has enacted, but it cannot modify the rules it enforces and it cannot block judicial review:

```solidity
/**
 * @title ExecutiveBranch
 * @notice Enforces enacted legislation automatically. Can execute
 *         actions defined by legislative proposals that have passed
 *         and survived judicial review, but cannot create new rules
 *         or block the judiciary from reviewing its actions.
 */
contract ExecutiveBranch {

    IConstitutionRegistry public constitution;

    /// @notice Only executes proposals the legislature has marked as enacted
    ///         AND that have not been struck down by the judiciary
    function enforce(uint256 _proposalId) external {
        require(
            constitution.isAuthorized(
                this.enforce.selector,
                address(this)
            ),
            "Executive not authorized for enforcement"
        );

        ILegislativeBranch leg = ILegislativeBranch(
            constitution.branchAddress(
                IConstitutionRegistry.Branch.Legislative
            )
        );

        require(leg.isEnacted(_proposalId), "Proposal not enacted");
        require(!leg.isVetoed(_proposalId), "Proposal was struck by judiciary");

        // Execute the proposal's encoded actions
        (address target, bytes memory data) = leg.getProposalAction(_proposalId);
        (bool success, ) = target.call(data);
        require(success, "Execution failed");
    }
}
```

The executive contract can’t add new enforcement actions, can’t modify what constitutes an enacted proposal, and can’t prevent the judiciary from vetoing. It’s a pure enforcement layer — which is exactly what Meta’s automated moderation *should* be but isn’t, because Meta’s enforcement systems can be (and are) reconfigured by executives without legislative or judicial oversight.

## The Anti-Capture Layer: Role-Based Accountability with Hats

The Sovereign Protocol pattern above defines what each branch *can* do. But it leaves a critical question open: who fills these roles, and what prevents capture? This is where the existing governance contract landscape has a gap that’s worth filling, and where [Hats Protocol](https://www.hatsprotocol.xyz/) offers something genuinely novel.

Hats is an [ERC-1155](https://docs.hatsprotocol.xyz/for-developers/v1-protocol-spec) role token system where each “hat” bundles responsibilities, permissions, and accountability criteria into a single programmable object. Hats are organized in a [tree structure](https://docs.hatsprotocol.xyz/using-hats/what-hats-do-i-need) — admin hats above, subordinate hats below — where admins can create, issue, and revoke the hats beneath them. The crucial detail is that hat issuance and revocation can be fully automated through [eligibility modules](https://docs.hatsprotocol.xyz/hats-integrations/eligibility-and-accountability-criteria) and [toggle modules](https://docs.hatsprotocol.xyz/hats-integrations/activation-and-deactivation-criteria), meaning that role assignment doesn’t require a human gatekeeper.

For a constitutional governance framework, this solves several hard problems at once.

Consider judge selection — the hardest open question in on-chain constitutionalism. Meta’s Oversight Board addressed this with a self-perpetuating appointment model funded by irrevocable trust, which works but is inherently centralised at the founding moment. With Hats, a “Judge” hat could be configured with a [staking eligibility module](https://docs.hatsprotocol.xyz/hats-integrations/eligibility-and-accountability-criteria/staking-eligibility) that requires candidates to stake governance tokens as a bond. If a judge’s rulings are later overturned by a supermajority or found to violate constitutional principles, a designated accountability address can slash the stake and automatically revoke the hat. The judge doesn’t lose their role because a political actor decided to remove them — they lose it because an objective, on-chain criterion was triggered.

This extends naturally to every branch. Legislative delegates could wear hats gated by [JokeRace election eligibility](https://docs.hatsprotocol.xyz/hats-integrations/eligibility-and-accountability-criteria/jokerace-eligibility), where periodic on-chain contests determine who holds legislative power. Executive enforcement agents could wear hats that are toggled — activated and deactivated — based on whether their enforcement actions conform to enacted legislation, checked programmatically against the on-chain case log. [Hats Signer Gate](https://docs.hatsprotocol.xyz/for-developers/hats-signer-gate-v2) can tie Gnosis Safe multisig signing authority directly to hat ownership, meaning that if a judge or legislator loses their hat, they simultaneously lose the ability to sign transactions on behalf of their branch’s treasury or governance contract.

The anti-capture properties here are worth spelling out. In a standard Governor contract, if a whale accumulates enough tokens, they can pass any proposal — including proposals that change the governance rules themselves. There’s no structural circuit breaker. In a Moloch DAO, ragequit provides an exit but not a check — the whale still controls governance for anyone who stays. In the Sovereign Protocol pattern combined with Hats, capture of a single branch is insufficient because the other branches can block overreach, and capture of the individuals within a branch is limited by automated eligibility criteria that no individual can override. A captured judge who begins issuing rulings that violate constitutional precedent can be automatically de-hatted when their stake is slashed. A captured legislator who proposes unconstitutional laws can be blocked by the judiciary’s veto power. A captured executive who selectively enforces rules can lose their hat when their enforcement pattern deviates from enacted legislation.

None of this is magic. The eligibility criteria still need to be well-designed, and “violates constitutional principles” still requires some off-chain judgment that feeds into an on-chain oracle. But the architecture converts what would otherwise be a pure trust problem into a mechanism design problem — and mechanism design is something we know how to iterate on.

## What Remains Unsolved

This architecture is a starting point, not a solution. Several hard problems remain open.

The gas economics are real. Storing full case law on-chain is expensive. A hybrid model — on-chain ruling hashes with IPFS-stored reasoning, plus on-chain precedent indices — is likely necessary, which introduces the question of what happens when the off-chain reasoning disappears. Arweave permanence helps but doesn’t fully resolve the trust assumption.

The oracle problem for judicial accountability is significant. Hats eligibility modules can automate role revocation, but somebody still needs to determine that a judge has “violated constitutional precedent” in a way that’s not itself captured. One approach is nested accountability — judges are accountable to a constitutional council hat, which is itself accountable to the full token holder base through a supermajority vote. Layers of indirection make capture harder but don’t make it impossible.

Moloch’s ragequit mechanism is notably absent from this architecture, and that’s a real gap. Exit rights are a powerful complement to voice rights, and a constitutional governance framework arguably needs both. Integrating a ragequit-like mechanism into a three-branch system — where dissenting members can exit before a proposal that survived judicial review takes effect — would strengthen the anti-tyranny properties considerably.

And then there’s the deepest question: does enforced separation of powers actually produce better governance outcomes for a digital community, or does it import the dysfunction of nation-state politics into systems that don’t need it? Meta’s governance failures are real, but so is the US Congress. The answer probably depends on scale. A ten-person multisig doesn’t need a judiciary. A protocol governing billions in TVL might.

The most interesting experiment would be a mid-size DAO adopting this pattern as a governance upgrade — taking an existing [Governor](https://docs.openzeppelin.com/contracts/4.x/governance) contract and refactoring it into three constrained branches, with [Hats](https://www.hatsprotocol.xyz/) managing role assignment and accountability across all three. If the precedent system produces more consistent, predictable rule enforcement, and if the separation prevents the governance capture that plagues token-weighted voting, that’s evidence worth paying attention to.

Facebook built a country by accident. The question now is whether web3 can build one on purpose — with a constitution that actually binds.

-----

**What I’m reading:**

- [Meta’s Mandate-Free Governance](https://www.newamerica.org/planetary-politics/blog/metas-mandate-free-governance-how-to-think-about-facebook-and-the-oversight-board/) — New America’s analysis of the Oversight Board as “private polity-making”
- [We Need Network Societies, Not Network States](https://www.cip.org/blog/network-societies) — The Collective Intelligence Project’s pluralist alternative to Balaji’s founder-led model
- [Hats Protocol: Organizational Graphs](https://blog.hatsprotocol.xyz/organizational-graphs) — The foundational vision for programmable, revocable on-chain roles
- [MolochDAO Baal: Rage, Quit, and Shamans](https://daohaus.mirror.xyz/U_JQtheSzdpRFqQwf9Ow3LgLNG0WMZ6ibAyrjWDu_fc) — How Moloch v3 structures minority exit rights
- [Shareholder Democracy and Dual-Class Structures](https://corpgov.law.harvard.edu/2025/02/11/shareholder-democracy-and-the-challenge-of-dual-class-share-structures/) — Harvard Law on why Meta’s voting structure matters
- [DAO Governance Framework Wiki](https://daogovernanceframework.com/wiki/Governance) — The most complete mapping of executive/legislative/judicial functions to DAO smart contracts